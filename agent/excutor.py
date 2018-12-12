from subprocess import Popen,PIPE
class Excutor:
    def excute_script(self,script,timeout=5):
        p = Popen(script,stdout=PIPE,shell=True)
        result=p.wait(timeout)
        output = p.stdout.read()
        return result,output