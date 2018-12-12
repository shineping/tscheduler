from .state import *
class Task:
    def __init__(self,script,targets,timeout=5,state=WAITNG):
        self.script = script
        self.targets = [ [agent,WAITNG,''] for agent in targets]
        self.state = state
        self.timeout = timeout