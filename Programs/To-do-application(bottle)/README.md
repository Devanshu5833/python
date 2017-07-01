**TO-DO application**

##configurations
ubuntu : 16.04
Python : 2.7
Mongodb : 3.3
pip : 9.0.1
bottle : 0.12.13
pymongo : 3.4.0

**To run application**
pip install -r requirements.txt

##Description (Follow define endpoints to get result)
1)Add task (TaskID, Desc, Due date) + (creation date, status, deleted, modified date) -> http://localhost:8090/addtask
    -> Pass adding value in header
2)Update task -> http://localhost/updatetask/<ID> 
    -> Pass update value in header
3)delete task -> http://localhost/deletetask/<ID>
4)Done tasks -> http://localhost:8090/done
5)Read All task -> http://localhost:8090/
6)Total pending tasks -> http://localhost:8090/pending
7)Today completed tasks -> http://localhost:8090/done/today
8)What's on tomorrow [list] -> http://localhost:8090/tomorrow
9)Recently updated tasks [Just return tasks ID list in descending order] -> http://localhost:8090/recenttask

**To update document
Pass data as a JSON format in request BODY and pass UUID in query string
**To done task
Pass {"status" : true} in request BODY and pass UUID in query string
**to delete task
Pass {"deleted" : true} in request BODY and pass UUID in query string