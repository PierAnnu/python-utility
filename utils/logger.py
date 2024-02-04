# coding=utf-8

#version 0.02
#--------------------------------------------------
#Updates
#0.02 - Name changend, now beautyname is name and name is path as really is
#0.01 - Initial Version
#--------------------------------------------------
#Description
#Easier File Logger and Log Interface
#--------------------------------------------------

# from colorama import init
import os
import time

class Logger:
    warning_style = "\x1b[33m"
    error_style = "\x1b[31m"
    info_style = "\x1b[32m"
    debug_style = "\x1b[34m"
    harddebug_style = "\x1b[35m"
    message_style = "\x1b[37m"

    printable_time = ""
    path = ""

    printable = True

    def __init__(self,path=r"./Log",lev=1):
        # init()
        self.warning_style = self.warning_style
        self.error_style = self.error_style
        self.info_style = self.info_style
        self.message_style = self.message_style
        self.level = lev
        self.path = path
        self.name = path.split('\\')[-1]

    def update_time(self, newest_time):
        self.printable_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(newest_time))
    
    def clear_console(self):
        os.system("cls")
        
    def compose_print(self, *message, end="\n"):
        msg = ""
        for tocs in message:
            if type(tocs) == str:
                msg += tocs+"\n"
            elif type(tocs) == dict:
                dk = tocs.keys()
                for k in dk:
                    msg+= k+":"+str(tocs.get(k))+" - "
            else:
                msg += str(tocs)+"\n"
        print(self.info_style + f"{self.name}\n" +self.message_style+ msg, end=end)
        
    def i(self,*message, end="\n"):
        self.update_time(time.time())
        if self.level >= 0:
            msg = ""
            for tocs in message:
                if type(tocs) == str:
                    msg += tocs+" "
                elif type(tocs) == dict:
                    dk = tocs.keys()
                    for k in dk:
                        msg+= k+":"+str(tocs.get(k))+" - "
                else:
                    msg += str(tocs)+" "
            self.save(self.printable_time+f"{self.name} [I]: " +msg)
            if self.printable:
                print(self.info_style + f"{self.name} [I]: " +self.message_style+ msg, end=end)

    def e(self,*message, end="\n"):
        self.update_time(time.time())
        if self.level >= 1:
            msg = ""
            for tocs in message:
                msg += str(tocs)+" "
            self.save(self.printable_time+f"{self.name} [E]: " +msg)
            if self.printable:
                print(self.error_style + f"{self.name} [E]: " +self.message_style+ msg, end=end)	
    def w(self,*message, end="\n"):
        self.update_time(time.time())
        if self.level >= 2:
            msg = ""
            for tocs in message:
                msg += str(tocs)+" "
            self.save(self.printable_time+f"{self.name} [W]: "+msg)
            if self.printable:
                print(self.warning_style + f"{self.name} [W]: " +self.message_style+ msg, end=end)

    
    def d(self,*message, end="\n"):
        self.update_time(time.time())
        if self.level >= 3:
            msg = ""
            for tocs in message:
                msg += str(tocs)+" "
            self.save(self.printable_time+f"{self.name} [D]: "+msg)
            if self.printable:
                print(self.debug_style + f"{self.name} [D]: " +self.message_style+ msg, end=end)	

    def hd(self,*message, end="\n"):
        self.update_time(time.time())
        if self.level >= 4:
            msg = ""
            for tocs in message:
                msg += str(tocs)+" "
            self.save(self.printable_time+f"{self.name} [HD]: " +msg)
            if self.printable:
                print(self.harddebug_style + f"{self.name} [HD]: " +self.message_style+ msg, end=end)	

    def save(self,*message):
        msg = ""
        for tocs in message:
            msg += str(tocs)+" "
        try:
            with open(self.path+".log","ab") as log_file:
                log_file.write(msg.encode('utf-8')+b"\n")
            log_file.close()
        except:
            self.e("ERROR SAVING LOG")
