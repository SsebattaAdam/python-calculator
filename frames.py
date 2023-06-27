# frames are used to hold or group items
# instead of adding the items to the window, we add them to the from

from tkinter import *

window = Tk()
frame = Frame(window, bg="yellow")
frame.pack()
Button(frame, text="Adam", width=3).pack(side=TOP)
Button(frame, text="Oscar", width=3).pack(side=LEFT)
Button(frame, text="Bell", width=3).pack(side=LEFT)
Button(frame, text="Bellar", width=3).pack(side=RIGHT)

window.mainloop()
