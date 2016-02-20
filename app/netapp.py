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

################# GUI #################

root = Tkinter.Tk()

# make it cover the entire screen
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#root.overrideredirect(1) # <-- this removes the menu items on top. commented for testing
root.title("Hacker House Network")
root.geometry("%dx%d+0+0" % (w, h))
root.configure(background='black')
root.focus_set() # <-- move focus to this widget
root.bind("<Escape>", lambda e: e.widget.quit())

# widgets
my_ip = grabIP()
label1 = Label(root, text = "IP: " + my_ip, fg="green", bg="black")
#label2 = Label(root, text="Hello, world!")
#label3 = Label(root, text="Hello, world!")
#label4 = Label(root, text="Hello, world!")
#label5 = Label(root, text="")

B1 = Tkinter.Button(root, text="test", bg="grey")
B2 = Tkinter.Button(root, text="test", bg="grey")
B3 = Tkinter.Button(root, text="test", bg="grey")

HAXimgtk = ImageTk.PhotoImage(Image.open("img/HAX.png"))
HAXlabel = Label(root, image=HAXimgtk)

# grid assignments
label1.grid(row=0, column=0)
#label2.grid(row=1, column=0)
#label3.grid(row=2, column=0)
#label4.grid(row=3, column=0)
#label5.grid(row=4, column=0)

HAXlabel.grid(row=0, column=3)

B1.grid(row=5, column=0)
B2.grid(row=5, column=1)
B3.grid(row=5, column=2)

root.mainloop()
