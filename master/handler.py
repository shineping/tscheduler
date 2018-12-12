from .store import Storage
from .state import  *
class Comm:
    def __init__(self):
        self.store = Storage()
    def reg_heart(self,meg):
        self.store.store_agent(meg)
        return 'ack:{}'.format(meg)
    def get_agents(self):
        return self.store.clients
    def add_task(self,mission):
       result = self.store.store_task(mission)
       print(mission)
       return  result
    def get_task(self,agent_id):
       for task_id,task in  self.store.tasks.items():
            for agent in task.targets:
                print(agent[1])
                if agent_id == agent[0] and agent[1] == WAITNG:
                    agent[1] = RUNING
                    task.state = RUNING
                    return task_id,task.script,task.timeout
    def hanld_result(self,mes:dict):
        task_id = mes['task_id']
        task = self.store.tasks[task_id]
        if mes['status'] == 0 :
            task.state = SUCCEED
        else:
            task.state = FAILED
    def get_result(self,task_id):
        print(task_id)
        print(self.store.tasks)
        task=self.store.tasks[task_id]
        return { task_id:task.state }
    send = reg_heart
