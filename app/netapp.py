#!/usr/bin/python
##
# Author: Caleb Adams
# Discription: Uses the tkinter 
#
#

import os
import platform
import Tkinter
import socket

from Tkinter import *
from PIL import Image, ImageTk

################# SYS ################# 

def getOS(): #it's probably better to just do this once
    #print ">> OS is " + platform.system()
    return platform.system();

################# NET ################# 

def grabIP():
    if (OS == "Linux"):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 0))
        my_ip = s.getsockname()[0]
        return my_ip;
    elif (OS == "Darwin"):
        my_ip = socket.gethostbyname(socket.gethostname())
        return my_ip;
    else:     
        print "ERROR does not yet support " + OS
        return "ERROR"

def onlineDevices():
    return "NOT IMPLEMENTED";

def upSpeed():
    return "NOT IMPLEMENTED";

def downSpeed():
    return "NOT IMPLEMENTED";

################# GUI #################

root = Tkinter.Tk()

# make it cover the entire screen
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#root.overrideredirect(1) # <-- this removes the menu items on top. commented for testing
root.title("Hacker House Network")
#root.geometry("%dx%d+0+0" % (w, h))
root.configure(background='black')
root.focus_set() # <-- move focus to this widget
root.bind("<Escape>", lambda e: e.widget.quit())

# get OS
OS = getOS();

# frames
topHolder = Frame(root, bg="black")
topHolder.pack(side=TOP)
dataFrame = Frame(topHolder, bg="black")
dataFrame.pack(side=LEFT)
imgFrame = Frame(topHolder, bg="black")
imgFrame.pack(side=RIGHT)
navFrame = Frame(root, bg="black")
navFrame.pack(side=BOTTOM, fill=X)

# widgets
my_ip = grabIP()
label1 = Label(dataFrame, anchor=N, text = "IP: " + my_ip, font="-weight bold", fg="green", bg="black")
devices = onlineDevices()
label2 = Label(dataFrame, anchor=N, text = "Devices: " + devices, font="-weight bold", fg="green", bg="black")
up_speed = upSpeed()
label3 = Label(dataFrame, anchor=N, text = "UP: " + up_speed, font="-weight bold", fg="green", bg="black")
down_speed = downSpeed()
label4 = Label(dataFrame, anchor=N, text = "DOWN: " + down_speed, font="-weight bold", fg="green", bg="black")

B1 = Tkinter.Button(navFrame, text="TBD", bg="grey")
B2 = Tkinter.Button(navFrame, text="TBD", bg="grey")
B3 = Tkinter.Button(navFrame, text="TBD", bg="grey")

HAXimgtk = ImageTk.PhotoImage(Image.open("img/HAX.png"))
HAXlabel = Label(imgFrame, image=HAXimgtk)

# grid assignments
label1.grid(row=0, column=0, sticky=Tkinter.W)
label2.grid(row=1, column=0, sticky=Tkinter.W)
label3.grid(row=2, column=0, sticky=Tkinter.W)
label4.grid(row=3, column=0, sticky=Tkinter.W)

HAXlabel.grid(row=0, column=0, sticky=Tkinter.E);

B1.grid(row=5, column=0, sticky=Tkinter.E)
B2.grid(row=5, column=1, sticky=Tkinter.E)
B3.grid(row=5, column=2, sticky=Tkinter.E)

root.mainloop()
