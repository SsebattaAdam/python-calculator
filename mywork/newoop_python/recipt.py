import tkinter as tk
from tkinter import messagebox


def add_details_to_receipt():
    customer_name = customer_name_entry.get()
    item_name = item_name_entry.get()
    item_quantity = item_quantity_entry.get()
    item_price = item_price_entry.get()

    if not customer_name or not item_name or not item_quantity or not item_price:
        messagebox.showwarning("Error", "Please fill in all fields.")
        return

    receipt_text = receipt_textbox.get("1.0", tk.END)
    receipt_text += f"Customer: {customer_name}\n" \
                    f"Item: {item_name}\n" \
                    f"Quantity: {item_quantity}\n" \
                    f"Unit Price: ${item_price}\n"

    receipt_textbox.delete("1.0", tk.END)
    receipt_textbox.insert(tk.END, receipt_text)


def print_receipt():
    receipt_text = receipt_textbox.get("1.0", tk.END)

    if not receipt_text.strip():
        messagebox.showwarning("Error", "No details added to the receipt.")
        return

    total_price = int(item_quantity_entry.get()) * \
        float(item_price_entry.get())

    receipt_text += f"Total Price: ${total_price:.2f}\n"

    receipt_textbox.delete("1.0", tk.END)
    receipt_textbox.insert(tk.END, receipt_text)


def clear_fields():
    customer_name_entry.delete(0, tk.END)
    item_name_entry.delete(0, tk.END)
    item_quantity_entry.delete(0, tk.END)
    item_price_entry.delete(0, tk.END)
    receipt_textbox.delete("1.0", tk.END)


# Create the main application window
app = tk.Tk()
app.title("Receipt Printing Program")
app.configure(bg="#f0f0f0")  # Set background color

# Create and arrange the widgets
title_label = tk.Label(app, text="Receipt Printing Program",
                       font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title_label.grid(row=0, columnspan=3, padx=10, pady=10)

customer_name_label = tk.Label(app, text="Customer Name:", bg="#f0f0f0")
customer_name_label.grid(row=1, column=0, padx=5, pady=5)
customer_name_entry = tk.Entry(app)
customer_name_entry.grid(row=1, column=1, padx=5, pady=5)

item_name_label = tk.Label(app, text="Item Name:", bg="#f0f0f0")
item_name_label.grid(row=2, column=0, padx=5, pady=5)
item_name_entry = tk.Entry(app)
item_name_entry.grid(row=2, column=1, padx=5, pady=5)

item_quantity_label = tk.Label(app, text="Quantity:", bg="#f0f0f0")
item_quantity_label.grid(row=3, column=0, padx=5, pady=5)
item_quantity_entry = tk.Entry(app)
item_quantity_entry.grid(row=3, column=1, padx=5, pady=5)

item_price_label = tk.Label(app, text="Unit Price:", bg="#f0f0f0")
item_price_label.grid(row=4, column=0, padx=5, pady=5)
item_price_entry = tk.Entry(app)
item_price_entry.grid(row=4, column=1, padx=5, pady=5)

add_button = tk.Button(app, text="Add to Receipt",
                       command=add_details_to_receipt, bg="#2196f3", fg="white")
add_button.grid(row=5, column=0, padx=5, pady=5)

print_button = tk.Button(app, text="Print Receipt",
                         command=print_receipt, bg="#4caf50", fg="white")
print_button.grid(row=5, column=1, padx=5, pady=5)

clear_button = tk.Button(app, text="Clear Fields",
                         command=clear_fields, bg="#f44336", fg="white")
clear_button.grid(row=5, column=2, padx=5, pady=5)

receipt_textbox = tk.Text(app, height=10, width=40,
                          borderwidth=2, relief="groove")
receipt_textbox.grid(row=6, columnspan=3, padx=5, pady=5)

# Start the application event loop
app.mainloop()
