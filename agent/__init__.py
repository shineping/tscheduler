import zerorpc
from .config import CONNURL,UUID_PATH
from .commer import Commanager
from .message import Message
import threading

class Agent:
    def __init__(self):
        self.meg = Message(UUID_PATH)
        self.comm = Commanager(self.meg)

    def start(self):
        while not threading.Event().wait(3) :
            try:
                self.comm.sendmeg()
            except Exception as e :
                self.comm.shutdown()



    def stop(self):
        pass




