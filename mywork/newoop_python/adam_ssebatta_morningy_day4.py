from tkinter import *
import random
from tkinter import messagebox
root = Tk()
root.title("Reciept")

root.geometry('1280x720')
bg_color = 'yellow'

c_phone = StringVar()
item = StringVar()
Rate = IntVar()
Quantity = IntVar()


c_name = StringVar()
bill_no = StringVar()
x = random.randint(1000, 9999)
bill_no.set(str(x))

global l
l = []


def welcom():
    textarea.delete(1.0, END)
    textarea.insert(END, " WELCOME TO  ADAM'S RECIEPT")
    textarea.insert(END, f'\n Bill no: \t\t{bill_no.get()}')
    textarea.insert(END, f'\n customer name: \t\t{c_name.get()}')
    textarea.insert(END, f'\n customer phone: \t\t{c_phone.get()}')
    textarea.insert(END, f'\n======================================')
    textarea.insert(END, '\nProduct \t\t qty\t\tprice')
    textarea.insert(END, f"\n======================================")
    textarea.configure(font='arial 15 bold')


def additm():
    n = Rate.get()
    m = Quantity.get() * n
    l.append(m)
    if item.get() == '':
        messagebox.showwarning('Error', 'Please enter the item')
        return
    else:
        textarea.insert(10.0 + float(len(l)-1),
                        f'{item.get()}\t\t{Quantity.get()}\t\t{m}\n')


def gbill():
    if c_name.get() == '' or c_phone.get() == '':
        messagebox.showerror("eneter customer ditails")
    else:
        text = textarea.get(10.0, (10.0 + float(len(l))))
        welcom()
        textarea.insert(END, text)
        textarea.insert(END, f'\n=======================================')
        textarea.insert(END, f'\nTotal amount: \t\t{sum(l)}')
        textarea.insert(END, f'\n=======================================')
        savebill()


def savebill():
    op = messagebox.askyesno('Save bill', 'Do you want to save the bill?')
    if op > 0:
        bill_details = textarea.get(1.0, END)
        f1 = open("bills/" + str(bill_no.get()) + ".txt", "w")
        f1.write(bill_details)
        f1.close()
        messagebox.showinfo(
            'saved bill', f'bill_no:{bill_no.get()} Saved succesfully')

    else:
        return


def clear():
    c_name.set('')
    c_phone.set('')
    item.set('')
    Rate.set('')
    Quantity.set('0')
    welcom()


def exit():
    op = messagebox.askyesno('Exit', 'Do you really want toi exit')
    if op > 0:
        root.destroy()
    else:
        return


title = Label(root, text="RECEIPT PROGRAM", bg=bg_color, fg='green',
              font=('times new romman', 25, 'bold'), relief=GROOVE)

title.pack(fill=X)


# customer details
F1 = LabelFrame(root, text="Customer deatils", bg=bg_color,  fg='blue', font=(
    'times new romman', 18, 'bold'), relief=GROOVE)
F1.place(x=0, y=80, relwidth=1)

custlabel = Label(F1, text='customer name', font=(
    'times new romman', 18, 'bold'), bg=bg_color, fg='blue',)
custlabel.grid(row=0, column=0, padx=10, pady=5)
custname_txt = Entry(F1, width=15, font='arial 15 bold',
                     relief=SUNKEN, textvariable=c_name)
custname_txt.grid(row=0, column=1, padx=10, pady=5)

custphoneNo_lbl = Label(F1, text='phone no', font=(
    'times new romman', 18, 'bold'), bg=bg_color, fg='blue',)
custphoneNo_lbl.grid(row=0, column=2, padx=10, pady=5)
custphone_txt = Entry(F1, width=15, font='arial 15 bold',
                      relief=SUNKEN, textvariable=c_phone)
custphone_txt.grid(row=0, column=3, padx=10, pady=5)


# ==================PRODUCT DETAILS =================
F2 = LabelFrame(root, text="Product details", bg=bg_color,  fg='blue', font=(
    'times new romman', 18, 'bold'), relief=GROOVE)
F2.place(x=20, y=180, width=630, height=500)


itm = Label(F2, text="Product Name", font=(
    'times new rommon', 18, 'bold'), bg=bg_color, fg='blue')
itm.grid(row=0, column=0, padx=30, pady=20)
itm_txt = Entry(F2, width=15, font='arial 15 bold',
                relief=SUNKEN, textvariable=item)
itm_txt.grid(row=0, column=1, padx=20, pady=20)

rate = Label(F2, text="Product rate", font=(
    'times new rommon', 18, 'bold'), bg=bg_color, fg='blue')
rate.grid(row=1, column=0, padx=30, pady=20)
rate_txt = Entry(F2, width=15, font='arial 15 bold',
                 relief=SUNKEN, textvariable=Rate)
rate_txt.grid(row=1, column=1, padx=20, pady=20)


quantity = Label(F2, text="Product quantity", font=(
    'times new rommon', 18, 'bold'), bg=bg_color, fg='blue')
quantity.grid(row=2, column=0, padx=20, pady=20)
quantity_txt = Entry(F2, width=15, font='arial 15 bold',
                     relief=SUNKEN, textvariable=Quantity)
quantity_txt.grid(row=2, column=1, padx=20, pady=20)


# ========button ===========
buton1 = Button(F2, text='Add item', font='arial 15 bold', width=15, command=additm,
                padx=5, pady=10, bg='lime')
buton1.grid(row=3, column=0, padx=10, pady=30)

buton2 = Button(F2, text='Generate Bill', font='arial 15 bold', width=15, command=gbill,
                padx=5, pady=10, bg='lime')
buton2.grid(row=3, column=1, padx=10, pady=30)

buton3 = Button(F2, text='Clear', font='arial 15 bold', width=15, command=clear,
                padx=5, pady=10, bg='lime')
buton3.grid(row=4, column=0, padx=10, pady=30)

buton4 = Button(F2, text='Exit', font='arial 15 bold', width=15, command=exit,
                padx=5, pady=10, bg='lime')
buton4.grid(row=4, column=1, padx=10, pady=30)


# =========BILL AREA =================
F3 = Frame(root, relief=GROOVE, bd=10)
F3.place(x=700, y=180, width=500, height=500)
bill_title = Label(F3, text='Bill Area', font='arial 15 bold',
                   relief=GROOVE, bd=7).pack(fill=X)

# bill_title = Label(F3, text='Bill Area', font='arial 15 bold',
#                    relief=GROOVE, bd=7).pack(fill=X)
scroll_y = Scrollbar(F3, orient=VERTICAL)
textarea = Text(F3, yscrollcommand=scroll_y)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack()

welcom()


root.mainloop()
