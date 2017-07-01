#!/usr/bin/env python

'''
FileName : validation.py
Description : function check that given data is in proper format or not
'''

#import core modules
import json
from datetime import datetime, timedelta

#check JOSN is in proper format or not
def is_json(data):
  try:
    json_object = json.loads(data.read())
  except ValueError, e:
    return True
  return json_object

#check json data is in proper format or not
def checkvalues(data):
    #master list
    master = ['description','duedate','name']
    if len(data.keys()) > 3:
        return {"error" : "More than Three value not allowded,Only description & duedate allowded"}
    try :
        if datetime.strptime(data['duedate'], '%Y-%m-%d') < (datetime.today() - timedelta(days=1)):
            return {"error" : "Duedate is less than the current date"}
    except ValueError,e:
        return {"error" : "date must be in yyyy-mm-dd format"}
    if not (data.has_key(master[0]) and data.has_key(master[1])):
        return {"error" : "Description or name or duedate is missing"}
    
    return {"success" : "success"}