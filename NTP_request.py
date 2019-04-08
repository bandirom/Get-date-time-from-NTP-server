from tkinter import *
from time import ctime, sleep
import threading, requests, ntplib, re

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Local Time")
        self.geometry("300x200+450+200")
        self.minsize(300,200)
        self.InitUI()

    def InitUI(self):
        self.group = LabelFrame(self, text="Time",font=("Arial", 13,"bold"))
        self.group.place(x = 40, y = 40, width = 200 )

        self.hour = Label(self.group, text = "0", font=("Arial", 13,"bold") )
        self.hour.grid(column =1, row =0)
        self.time1 = Label(self.group, text = ":", font=("Arial", 13,"bold"))
        self.time1.grid(column =2, row =0)
        self.minute = Label(self.group, text = "0", font=("Arial", 13,"bold"))
        self.minute.grid(column =3, row =0)
        self.time2 = Label(self.group, text = ":", font=("Arial", 13,"bold"))
        self.time2.grid(column =4, row =0)
        self.sec = Label(self.group, text = "0", font=("Arial", 13,"bold"))
        self.sec.grid(column =5, row =0)
        self.day = Label(self.group, text = "str", font=("Arial", 13,"bold") )
        self.day.grid(column =2, row =1)
        self.date = Label(self.group, text = "str", font=("Arial", 13,"bold") )
        self.date.grid(column =3, row =1)
        self.month = Label(self.group, text = "str", font=("Arial", 13,"bold") )
        self.month.grid(column =4, row =1)
        self.year = Label(self.group, text = "str", font=("Arial", 13,"bold") )
        self.year.grid(column =5, row =1)

class ServerTime(threading.Thread):
    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self) #thread.start()
        self.start()

    def run(self):
        c = ntplib.NTPClient()
        while(True):
            self.GetTime(c)
            sleep(1)

    def GetTime(self,c):
        response = c.request('pool.ntp.org')
        self.ParceTime(ctime(response.tx_time))

    def ParceTime(self, time):  
        time = re.findall(r'\w+', time)
        root.day.configure(text = time[0])
        root.month.configure(text = time[1])
        root.date.configure(text = time[2])
        root.hour.configure(text = time[3])
        root.minute.configure(text = time[4])
        root.sec.configure(text = time[5])
        root.year.configure(text = time[6])


if __name__=='__main__':
    time = ServerTime()
    root = Root()
    root.mainloop()
