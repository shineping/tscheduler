import zerorpc
from .config import CONNURL
from .message import Message
import threading
from util import get_logger
from .state import *
from .excutor import Excutor

logger = get_logger(__name__,'f:/{}.log'.format(__name__))

class Commanager:
    def __init__(self,meg:Message,timeout=3):
        self.meg = meg
        self.client = zerorpc.Client()
        self.event = threading.Event()
        self.timeout = timeout
        self.state = WAITNG
        self.excutor = Excutor()
    def sendmeg(self):
        try:
            self.event.clear()
            self.client.connect(CONNURL)
            self.client.send(self.meg.reg())
            while not self.event.wait(self.timeout):
                self.client.send(self.meg.heart_beat())
                if self.state == WAITNG :
                    task_item = self.client.get_task(self.meg.uuid)
                    if task_item:
                        task_id , script, time_out = task_item
                        state, out_put = self.excutor.excute_script(script,time_out)
                        print('?????',state,out_put)
                        meg=self.meg.result(task_id,state,out_put)
                        print('____________',meg)
                        self.client.hanld_result(meg)
        except Exception as e :
            print(e)
            logger.error(e)
            raise e
    def shutdown(self):
        self.event.set()
        self.client.close()