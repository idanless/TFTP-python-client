import re
import subprocess

class TFTP():
    def __init__(self,IP):
        self.IP = IP
        self.shell = subprocess.Popen('tftp '+self.IP, stdin=subprocess.PIPE,stdout=subprocess.PIPE, universal_newlines=True, bufsize=0,shell=True)
        self.filename = ''

    def PUT_withoutdirectory(self,filename):
        self.filename = str(filename)
        put_cmd = 'put '+str(self.filename)+' '+str(self.filename)
        self.shell.wait()
        self.shell.stdin.write(put_cmd+'\n')

    def PUT_witdirectory(self,filename,dictionary):
        self.filename = filename
        if re.search(':',str(self.filename)):
            put_cmd = 'put ' + str(self.filename) + ' ' + str(dictionary) + '/' + str(self.filename).replace(':','_')
        else:
            put_cmd = 'put ' + str(self.filename) + ' ' + str(dictionary) + '/' + str(self.filename) 
        self.shell.stdin.write(put_cmd+'\n')

    def output(self):
        out,error = self.shell.communicate()
        return out.splitlines()

    def close_TFTP(self):
        self.shell.stdin.close()
