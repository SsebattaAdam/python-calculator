import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = combo_operation.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        else:
            result = "Invalid operation"

        label_result.config(text=str(result))
    except ValueError:
        label_result.config(text="Invalid input")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create input fields and labels
label_num1 = tk.Label(window, text="Number 1:")
label_num1.pack()

entry_num1 = tk.Entry(window)
entry_num1.pack()

label_num2 = tk.Label(window, text="Number 2:")
label_num2.pack()

entry_num2 = tk.Entry(window)
entry_num2.pack()

# Create operation selection dropdown
label_operation = tk.Label(window, text="Operation:")
label_operation.pack()

operations = ["+", "-", "*", "/"]
combo_operation = ttk.Combobox(window, values=operations)
combo_operation.pack()

# Create calculate button
button_calculate = tk.Button(window, text="Calculate", command=calculate)
button_calculate.pack()

# Create label for displaying result
label_result = tk.Label(window, text="Result:")
label_result.pack()

# Run the main event loop
window.mainloop()
