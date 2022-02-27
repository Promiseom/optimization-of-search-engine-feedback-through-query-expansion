#@author: anendahpromise@yahoo.com

import threading
import time

class Task:
    def __init__(self, task_id):
        self.task_id = task_id
        self.result = None
        print('task', task_id, 'created')

    def setResult(self, resultValue):
        self.result = resultValue
    
    def getResult(self):
        return self.result
        
    # Method that does something, needs to be implemented
    # Please note that if this method contains a loop there should be a 
    # 200 millisecond delay before each next iteration
    def execute(self):
        pass

# A class that handles processing of tasks asynchronously
class AsyncTaskHandler(threading.Thread):
    def __init__(self, task, taskInfo=None):
        threading.Thread.__init__(self)
        self.__info = taskInfo
        self.task = task
        self.__result = None
    
    def run(self):
        self.__exc = None
        try:            
            if isinstance(self.task, Task): 
                self.__result = self.task.execute()
            elif str(type(self.task)) == "<class 'function'>" : 
                self.__result = self.task()
            else: 
                raise Exception('Can only execute tasks of type Task, please ensure your class is a subclass of Task or a lambda function')
        except Exception as e:
            self.__result = None
            self.__exc = e

    def join(self):
        threading.Thread.join(self)
        if self.__exc: raise self.__exc

    def getResult(self): return self.__result
    def getTaskInfo(self): return self.__info

# Enables proper management of multiple tasks
# Runs on the main application thread
class TaskManager:
    def __init__(self):
        self.tasks = {}

    def addAsyncTask(self, new_task):
        if isinstance(new_task, Task):
            task_id = new_task.task_id
            if task_id in self.tasks: 
                raise Exception('Task with the same id already exists in TaskManager')
        self.tasks[task_id] = AsyncTaskHandler(new_task)
        return True
    
    def removeAsyncTask(self, task_id):
        if task_id in self.tasks: 
            del[self.task_id]
            return True
        return False

    def startAsyncTask(self, task_id):
        task = self.tasks[task_id]
        if not task.is_alive():
            task.start()
            return True
        return False

    def joinAllTasks(self):
        for task_id in self.tasks:
            self.tasks[task_id].join()
    
    def startAsyncTasks(self):
        for task_id in self.tasks:
            self.startAsyncTask(task_id)

    def getResult(self, task_id):
        if task_id in self.tasks: return self.tasks[task_id].task.getResult()

    def getTask(self, task_id):
        if task_id in self.tasks: return self.tasks[task_id].task

    def getTasks(self):
        tasks = [x.task for x in self.tasks.values()]
        return tasks
