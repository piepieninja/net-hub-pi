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
import subprocess
import time
import sys

from Tkinter import *
from PIL import Image, ImageTk

def run():
    ################# SYS #################

    def getOS(): #it's probably better to just do this once
        if (debug):
            print "OS is " + platform.system();
        return platform.system();

    def tick():
        global time1
        time2 = time.strftime('%H:%M:%S')
        if time2 != time1:
            time1 = time2
            label5.config(text=time2)
        label5.after(200, tick)

    def btnClose():
        print "quiting..."
        sys.exit()

    def btnSpeedTest():
        if (debug):
            print "testing down-speed..."
        global down_speed
        label4.config(text="testing...")
        temp = downSpeed()
        down_speed = temp
        label4.config(text=temp)
        if (debug):
            print "testing up-speed..."
        global up_speed
        label3.config(text="testing...")
        temp = upSpeed()
        up_speed = temp
        label3.config(text=temp)

    def btnDevicesTest():
        if (debug):
            print "counting devices..."
        global devices
        label2.config(text="counting devices...")
        temp = grabDevices()
        devices = temp
        label2.config(text=temp)

    ################# NET #################

    #### INITS ####

    def grabIP():
        if (OS == "Linux"):
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 0))
            my_ip = s.getsockname()[0]
            if (debug):
                print "grabbed IP"
            return my_ip;
        elif (OS == "Darwin"):
            my_ip = socket.gethostbyname(socket.gethostname())
            return my_ip;
        else:
            print "ERROR does not yet support " + OS
            return "ERROR " + OS

    def onlineDevices():
        return "NOT IMPLEMENTED";

    def upSpeed():
        if (OS == "Linux"):
            bashCommand = "bash up.sh".strip('\n')
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output = process.communicate()[0]
            if (debug):
                print "grabbed UP speed"
            return output;
        else:
            print "ERROR does not yet supprt " + OS
            return "ERROR " + OS;

    def downSpeed():
        if (OS == "Linux"):
            bashCommand = "bash down.sh".strip('\n')
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output = process.communicate()[0]
            if (debug):
                print "grabbed DOWN speed"
            return output;
        else:
            print "ERROR does not yet supprt " + OS
            return "ERROR " + OS;

    def grabDevices():
        if (OS == "Linux"):
            bashCommand = "bash hosts.sh".strip('\n')
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output = process.communicate()[0]
            if (debug):
                print "grabbed Devices"
            return output;
        else:
            print "ERROR does not yet supprt " + OS
            return "ERROR " + OS;

    #### LOOPS ####

    def upTick():
        if (debug):
            print "testing up-speed..."
        global up_speed
        label3.config(text="testing...")
        temp = upSpeed()
        up_speed = temp
        label3.config(text=temp)
        label3.after(7200000, upTick) # every 2 hours

    def downTick():
        if (debug):
            print "testing down-speed..."
        global down_speed
        label4.config(text="testing...")
        temp = downSpeed()
        down_speed = temp
        label4.config(text=temp)
        label4.after(7200000, downTick) # every 2 hours

    def deviceTick():
        if (debug):
            print "counting devices..."
        global devices
        label2.config(text="counting devices...")
        temp = grabDevices()
        devices = temp
        label2.config(text=temp)
        label2.after(1800000, deviceTick) # every 30 mins

    ################# GUI #################

    root = Tkinter.Tk()

    # make it cover the entire screen
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.title("Hacker House Network")
    if (not debug):
        root.overrideredirect(1) # <-- this removes the menu items on top. commented for testing
        root.geometry("%dx%d+0+0" % (w, h))
    root.configure(background='black')
    root.focus_set() # <-- move focus to this widget
    root.bind("<Escape>", lambda e: e.widget.quit())

    # get OS
    OS = getOS();

    # frames
    topHolder = Frame(root, bg="black")
    topHolder.pack(side=TOP, fill=X)
    dataFrame = Frame(topHolder, bg="black")
    dataFrame.pack(side=LEFT)
    imgFrame = Frame(topHolder, bg="black")
    imgFrame.pack(side=RIGHT)
    navFrame = Frame(root, bg="black")
    navFrame.pack(side=BOTTOM, fill=X)

    # widgets
    my_ip = grabIP()
    label1 = Label(dataFrame, anchor=N, text = "IP: " + my_ip, font=guiFont, fg="green", bg="black")
    devices = 'loading...'
    label2 = Label(dataFrame, anchor=N, text = "Devices: " + devices, font=guiFont, fg="green", bg="black")
    up_speed = 'Upload: testing...' #upSpeed()
    label3 = Label(dataFrame, anchor=N, text = up_speed, font=guiFont, fg="green", bg="black")
    down_speed = "Download: testing..." #downSpeed()
    label4 = Label(dataFrame, anchor=N, text = down_speed, font=guiFont, fg="green", bg="black")
    time1 = ''
    label5 = Label(dataFrame, anchor=N, font=guiFont, fg="green", bg="black")

    B1 = Tkinter.Button(navFrame, text="Speed Test", font=guiFont, bg="grey", fg="blue", command=btnSpeedTest)
    B2 = Tkinter.Button(navFrame, text="Scan Devices",font=guiFont, bg="grey", fg="blue", command=btnDevicesTest)
    btnCls = Tkinter.Button(navFrame, text="Quit", font=guiFont, bg="grey", fg="red", command=btnClose)

    HAXimgtk = ImageTk.PhotoImage(Image.open("img/HAX.png"))
    HAXlabel = Label(imgFrame, image=HAXimgtk)

    # grid assignments
    label1.grid(row=0, column=0, sticky=Tkinter.W)
    label2.grid(row=1, column=0, sticky=Tkinter.W)
    label3.grid(row=2, column=0, sticky=Tkinter.W)
    label4.grid(row=3, column=0, sticky=Tkinter.W)
    label5.grid(row=4, column=0, sticky=Tkinter.W)

    HAXlabel.grid(row=0, column=0, sticky=Tkinter.E);

    B1.grid(row=5, column=0, sticky=Tkinter.E)
    B2.grid(row=5, column=1, sticky=Tkinter.E)
    btnCls.grid(row=5, column=2, sticky=Tkinter.E)

    # loops and ticks
    tick()
    root.after(testDelay, deviceTick) # delay because these take forever
    root.after(testDelay, upTick) # delay because these take forever
    root.after(testDelay, downTick) # delay because these take forever
    root.mainloop()

################# MAIN #################

#### GLOBALS ####
global OS
global time1
global guiFont
global testDelay

#### MAIN ####

OS = ""
time1 = ''
guiFont = ("verdana",12,"bold")
testDelay = 5000 # 5 seconds - in miliseconds

if (len(sys.argv) > 1 and str(sys.argv[1]) == "debug"):
    debug = True
else:
    debug = False

run()
