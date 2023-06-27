from tkinter import *


def submit():
    listbox.get(listbox.curselection())

    print("you orderd")


def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())


def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())


window = Tk()


listbox = Listbox(window,
                  bg="white",
                  width=12)

listbox.pack()

listbox.insert(0, "Adam")
listbox.insert(1, "oscar")
listbox.insert(2, "Bell")
listbox.insert(3, "Bella")
listbox.insert(4, "Osca")
listbox.insert(5, "chelsea")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()
submitButton = Button(window, text="Submit", command=submit)
submitButton.pack()

addButton = Button(window, text="Add", command=add)
addButton.pack()
deleteButton = Button(window, text="Delete", command=delete)
deleteButton.pack()

window.mainloop()
