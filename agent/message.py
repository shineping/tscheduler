import netifaces
import ipaddress
import uuid
import socket
import os


def con_addr():
    addrlist = []
    for iface in netifaces.interfaces():
        if 2 in netifaces.ifaddresses(iface):
            addr=ipaddress.ip_address(netifaces.ifaddresses(iface)[2][0]['addr'])
            if addr.is_loopback or addr.is_multicast or addr.is_link_local:
                continue
            addrlist.append(str(addr))
    return addrlist

class Message:
    def __init__(self,uuid_path):
       if os.path.exists(uuid_path):
            with open(uuid_path) as f :
               self.uuid = f.readline()
       else:
            self.uuid = uuid.uuid4().hex
            with open(uuid_path,mode='w') as f :
                f.write(self.uuid)

    def reg(self):

        return {
            'type':'reg',
            'payload':{
                'id':self.uuid,
                'host':socket.gethostname(),
                'ip_addr':con_addr()
            }
        }

    def heart_beat(self):
        return {
            'type': 'heartbeat',
            'payload': {
                'id': self.uuid,
                'host': socket.gethostname(),
                'ip_addr': con_addr(),
                'state':0
            }
        }
    def result(self,task_id,status,out_put):
        return {
            'task_id':task_id,
            'status':status,
            'out_put':out_put
        }
