import uuid
from .task import Task
class Storage:
    def __init__(self):
        self.clients = {}
        self.tasks = {}
    def store_agent(self,meg):
        self.clients[meg['payload']['id']]=meg['payload']
        print(meg)
    def store_task(self,mission):
        task = Task(**mission)
        self.tasks[uuid.uuid4().hex]=task
        print(self.tasks)
        return list(self.tasks.keys())


