#!/usr/bin/python
##
# Author: Caleb Adams
# Discription: Uses the tkinter 
#
#

import Tkinter
import socket

from Tkinter import *
from PIL import Image, ImageTk

################# NET ################# 

def grabIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 0))
    my_ip = s.getsockname()[0]
    return my_ip;

def onlineDevices():
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

B1 = Tkinter.Button(navFrame, text="test", bg="grey")
B2 = Tkinter.Button(navFrame, text="test", bg="grey")
B3 = Tkinter.Button(navFrame, text="test", bg="grey")

HAXimgtk = ImageTk.PhotoImage(Image.open("img/HAX.png"))
HAXlabel = Label(imgFrame, image=HAXimgtk)

# grid assignments
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

HAXlabel.pack(anchor=E);

B1.grid(row=5, column=0)
B2.grid(row=5, column=1)
B3.grid(row=5, column=2)

root.mainloop()
