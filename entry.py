from tkinter import *

def submit():
   uername= entry.get()
   print ("Hello " + uername)
   entry.config(state=DISABLED)

def delete():
   entry.delete(0,END)
def backspace():
   entry.delete(len(entry.get())-1, END)

window = Tk()
entry = Entry(window,
              fg= "green",
              bg="black",
              font=('Arial',50))

entry.pack()

submit_button = Button(window,text="submit",command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,text="delete",command=delete)
delete_button.pack(side=RIGHT)
 
blackspace_button = Button(window,text="backspace",command=backspace)
blackspace_button.pack(side=RIGHT)

window.mainloop()