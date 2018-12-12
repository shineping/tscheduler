import zerorpc
from .config import CONNURL
from .handler import Comm
class AppServer:
    def __init__(self):
        self.server = zerorpc.Server(Comm())
        self.server.bind(CONNURL)
    def start(self):
         self.server.run()

    def stop(self):
        pass


