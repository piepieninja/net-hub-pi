#!/usr/bin/python
##
# Author: Caleb Adams
# Discription: Uses the tkinter 
#
#

import Tkinter


root = Tkinter.Tk()

# make it cover the entire screen
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#root.overrideredirect(1) # <-- this removes the menu items on top. commented for testing
root.geometry("%dx%d+0+0" % (w, h))
root.configure(background='black')
root.focus_set() # <-- move focus to this widget
root.bind("<Escape>", lambda e: e.widget.quit())

B1 = Tkinter.Button(root, text ="test", bg ="grey")
B2 = Tkinter.Button(root, text ="test", bg ="grey")

B1.grid(row=2, column=0)
B2.grid(row=2, column=1)

root.mainloop()
