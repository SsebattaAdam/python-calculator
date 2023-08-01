from tkinter import *
#buttons in python

count = 0
window = Tk()
def click():
    global count
    count +=1
    print(count)
  #  print("you have clicked the button")

button = Button(window,
               text='Click me',
                command=click,
                font=("Arial", 30),
                fg="blue",
                bg="green",
                activeforeground="black",
                activebackground="yellow",
                state= ACTIVE,

                
                )



button.pack()



window.mainloop()

