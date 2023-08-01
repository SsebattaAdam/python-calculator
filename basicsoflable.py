from tkinter import *

#labels = an area widget that holds text

window = Tk()

photo =PhotoImage(file='work.png')

label = Label(window, 
              text="Helloiw my friend", 
              font=("Arial", 40, 'bold'),
            fg='green', 
            bg='black',
              bd=12,
                padx=20,
                  pady=20,
                    image=photo ,
                     compound='bottom' )
label.pack()

# label.palce(x=100, y=100)


window.mainloop()