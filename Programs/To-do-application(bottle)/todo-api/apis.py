#!/usr/bin/env python

'''
FileName : apis.py
Description : API's to performance with databases
'''

#import core modules
import json
import pymongo
from datetime import datetime, timedelta
from bson.json_util import dumps
from bson.objectid import ObjectId
#import pip modules
from bottle import get,post,put,request,response
#import other modules
import validation
from databaseconnection import Setconfiguration,Setdatabaseconfiguration

#set object for congiguration & database connection
config = Setconfiguration.get_config_instance()
client = Setdatabaseconfiguration.get_databaseconfig_instance()

#store database object
db = client['todolistdev']

'''
endpoint : /,/done,/pending,/donetoday,/tomorrow
Parameters : @timefilter cheks that task nedd for today or tomorrow
             @filters for done,pending tasks
Description : find data with timefilter & status filtes
'''
@get("/")
@get("/<filters>")
@get("/<filters>/<timefilter>")
def readalltask(filters = {"deleted" : False},timefilter = {}):
    try :
        if filters == "done" and timefilter == "today":
            filters = {"$and":[{"status": True},{"modifieddate": datetime.strptime(str(datetime.utcnow().strftime("%Y-%m-%d")), '%Y-%m-%d')},{"deleted" : False}]}
        elif filters == "done":
            filters = {"$and" : [{"status" : True },{"deleted" : False}]}
        elif filters == "pending":
            filters = {"$and" : [{"status" : False },{"deleted" : False}]}
        elif filters == "tomorrow":
            tomorrow = datetime.strptime(str(datetime.utcnow().strftime("%Y-%m-%d")), '%Y-%m-%d') + timedelta(days=1)
            filters = {"$and":[{"status": False },{"duedate": tomorrow },{"deleted" : False}]}
        result = json.loads(dumps(db.listcollection.find(filters)))
    except Exception,e:
        return {"error" : "Operation does not perform successfully"}
    return {"success" : result}

'''
endpoint : /addtask
Parameters : None
Description : Add a new task
Note : here all data get from request.body in a JSON format
'''
@post('/addtask')
def addtask():
    #check that json is in proper format or not
    requestdata = validation.is_json(request.body)
    if requestdata == True:
        response.status = 400
        return {"error" : "Json is not in a proper format"}
    #check request data is in proper format or not
    validationcheck = validation.checkvalues(requestdata)
    if validationcheck.has_key('error'):
        response.status = 400
        return validationcheck
    #add extra parameter to requestdata
    requestdata['duedate'] = datetime.strptime(requestdata['duedate'], '%Y-%m-%d')
    requestdata['creationdate'] = datetime.strptime(str(datetime.utcnow().strftime("%Y-%m-%d")), '%Y-%m-%d')
    requestdata['modifieddate'] = datetime.strptime(str(datetime.utcnow().strftime("%Y-%m-%d")), '%Y-%m-%d')
    requestdata['status'] = False
    requestdata['deleted'] = False
    #insert data into mongodb
    try :
        post_id = db.listcollection.insert_one(requestdata).inserted_id
    except Exception,e:
        return {"error" : "Operation does not perform successfully"}
    #send response
    response.status = 201
    return {"success" : "New task added with " + str(post_id) + " ID"}      
        
'''
endpoint : /updatetask,/deletetask
Parameters : @id UUID for document
Description : update or delete task
Note : for updation all data get from request.body in a JSON format
'''
@put("/updatetask/<id>")
@put("/deletetask/<id>")
def updatetask(id = {}):
    url = request.urlparts.path.split("/")[1]
    modifieddate  = datetime.strptime(str(datetime.utcnow().strftime("%Y-%m-%d")), '%Y-%m-%d')
    if url == "deletetask":
        setvalue = {"deleted" : True,"modifieddate" : modifieddate } 
    elif url == "updatetask":
        updatedata = validation.is_json(request.body)
        if updatedata == True:
            response.status = 400
            return {"error" : "Json is not in a proper format"}
        updatedata['modifieddate'] = datetime.strptime(str(datetime.utcnow().strftime("%Y-%m-%d")), '%Y-%m-%d')
        setvalue = updatedata 
    try :
        returnupdate = db.listcollection.update({'_id': ObjectId(id)},{"$set" : setvalue}, upsert=False)
    except Exception,e:
        return {"error" : "Operation does not perform successfully"}
    return {"success" : str(returnupdate['nModified']) + " No of Record modified "} 

'''
endpoint : /recenttask
Parameters : None
Description : get the latest updated task
'''
@get("/recenttask")
def recenttask():
    try :
        result = list(json.loads(dumps(db.listcollection.find({}).sort('modifieddate',pymongo.DESCENDING))))
    except Exception,e:
        return {"error" : "Operation does not perform successfully"}
    return {"success" : result}