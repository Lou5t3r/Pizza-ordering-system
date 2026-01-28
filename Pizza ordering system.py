import tkinter as tk
from tkinter import ttk

checkbox_vars = []
checkbox_vars_drinks = []

def on_checkbox_click():
    for i, var in enumerate(checkbox_vars):
        if var.get() == 1:
            entry_boxes[i].pack()
            entry_boxes[i].focus()

def validate_entry(value):
    if value.isdigit() and 1 <= int(value) <= 10:
        return True
    elif value == '':
        return True
    else:
        return False

def tableNumber_validate(value):
    if value.isdigit() and 1 <= int(value) <= 25:
        return True
    elif value =='':
        return True
    else:
        return False

def calculate_total_price():
    total_price = 0

# calculate topping prices---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    for i, var in enumerate(checkbox_vars[:len(toppings)]):
        if var.get() == 1:
            topping_price = toppings[i]['price']
            quantity = entry_boxes[i].get()
            if quantity.isdigit() and 1 <= int(quantity) <= 10:
                total_price += topping_price * int(quantity)

# Calculate drinks price-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    for i, var in enumerate(checkbox_vars_drinks):
        if var.get() == 1:
            drink_index = i
            if 0 <= drink_index < len(drinks):
                drink_price = drinks[drink_index]['price']
                quantity = entry_boxes_drinks[i].get()
                if quantity.isdigit() and 1 <= int(quantity) <= 10:
                    total_price += drink_price * int(quantity)

    total_price_label.config(text=f"Total Price: £{total_price:.2f}")

root = tk.Tk()
root.geometry("970x700")
root.title("Pizza Shed")

label = tk.Label(root, text="Welcome to Pizza shed", foreground='red', font=('Ink Free', 28))
label.pack(padx=20, pady=20)
# Table number label-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
table_title_frame = tk.Frame(root)
table_title_frame.pack(anchor=tk.W)
table_label = tk.Label(table_title_frame, text="Enter the table number(1-25)", foreground='red', font=('Ink Free', 16, 'bold'))
table_label.pack(padx=210)
# Table number entry-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
combo = ttk.Combobox(root , values=["1", "2", "3", "4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25"])
combo.pack()
combo.set("Table number here")
combo['state']='readonly'
# Toppings title--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
toppings_title_frame = tk.Frame(root)
toppings_title_frame.pack(anchor=tk.W)
toppings_label = tk.Label(toppings_title_frame, text="Select the toppings on the pizza(1-10)", foreground='red', font=('Ink Free', 16, 'bold'))
toppings_label.pack()
# Toppings--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
toppings = [
    {"name": "Cheese and tomato", "price": 3.50},
    {"name": "Ham and pineapple", "price": 4.20},
    {"name": "Vegetarian", "price": 5.20},
    {"name": "Meat feast", "price": 5.80},
    {"name": "Seafood", "price": 5.60}
]
# Toppings checkbox--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
checkbox_vars = []
entry_boxes = []
for topping in toppings:
    topping_frame = tk.Frame(root)
    topping_frame.pack(anchor=tk.W)

    topping_checkbox_var = tk.IntVar()
    checkbox_vars.append(topping_checkbox_var)
    topping_checkbox = tk.Checkbutton(topping_frame, text=f"{topping['name']} (£{topping['price']:.2f})", variable=topping_checkbox_var, command=on_checkbox_click)
    topping_checkbox.pack(side=tk.LEFT)

    entry = tk.Entry(topping_frame, validate="key")
    entry['validatecommand'] = (entry.register(validate_entry), '%P')
    entry['invalidcommand'] = 'bell'
    entry.pack(side=tk.LEFT)
    entry_boxes.append(entry)
# Pizza base title---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
base_title_frame = tk.Frame(root)
base_title_frame.pack(anchor=tk.W)
base_label = tk.Label(base_title_frame, text="Select pizza base", foreground='dark red', font=('Ink Free', 14, 'bold'))
base_label.pack()

base_frame = tk.Frame(root)
base_frame.pack(anchor=tk.W)
# Pizza base checkbox------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
base_checkbox_var = tk.IntVar()
base_checkbox = tk.Checkbutton(base_frame, text="Traditional?", variable=base_checkbox_var)
base_checkbox.pack(side=tk.LEFT)

base_checkbox_var = tk.IntVar()
base_checkbox = tk.Checkbutton(base_frame, text="Thin and crispy?", variable=base_checkbox_var)
base_checkbox.pack(side=tk.LEFT)

checkbox_vars.append(base_checkbox_var)
# Extra toppings title-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
extratoppings_label_frame = tk.Frame(root)
extratoppings_label_frame.pack(anchor=tk.W)

extratoppings_label_frame = tk.Label(extratoppings_label_frame, text="Extra toppings?", foreground='red', font=('Ink Free', 14, 'bold'))
extratoppings_label_frame.pack()

extra_toppings_frame = tk.Frame(root)
extra_toppings_frame.pack(anchor=tk.W)
# Extra toppings checkbox--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
extra_toppings = [
    "Extra Cheese",
    "Pepperoni",
    "Onions",
    "Peppers"
]
checkbox_vars_extra = []
for extra_topping in extra_toppings:
    extra_topping_checkbox_var = tk.IntVar()
    checkbox_vars_extra.append(extra_topping_checkbox_var)

    extra_topping_checkbox = tk.Checkbutton(extra_toppings_frame, text=extra_topping, variable=extra_topping_checkbox_var)
    extra_topping_checkbox.pack(side=tk.LEFT)

checkbox_vars.append(base_checkbox_var)
# Drinks title-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
drinks_label_frame = tk.Frame(root)
drinks_label_frame.pack(anchor=tk.W)

drinks_label = tk.Label(drinks_label_frame, text="Select drinks(1-10)", foreground='dark cyan', font=('Ink Free', 16, 'bold'))
drinks_label.pack()

drinks_frame = tk.Frame(root)
drinks_frame.pack(anchor=tk.W)
# Drinks checkbox--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
drinks = [
    {"name": "Cola", "price": 0.90},
    {"name": "Lemonade", "price": 0.80},
    {"name": "Fizzy Orange", "price": 0.90}
]
checkbox_vars_drinks = []
entry_boxes_drinks = []
for drink in drinks:
    drink_checkbox_var = tk.IntVar()
    checkbox_vars_drinks.append(drink_checkbox_var)
    drink_checkbox = tk.Checkbutton(drinks_frame, text=f"{drink['name']} (£{drink['price']:.2f})", variable=drink_checkbox_var, command=on_checkbox_click)
    drink_checkbox.pack(side=tk.LEFT, padx=1, pady=1)

    drink_entry = tk.Entry(drinks_frame, validate="key")
    drink_entry['validatecommand'] = (drink_entry.register(validate_entry), '%P')
    drink_entry['invalidcommand'] = 'bell'
    drink_entry.pack(side=tk.LEFT)
    entry_boxes_drinks.append(drink_entry)
# Calculator-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
calculate_button = tk.Button(root, text="Calculate Price", command=calculate_total_price)
calculate_button.pack(pady=10)

total_price_label = tk.Label(root, text="Total Price: £0.00", foreground='green', font=('Ink Free', 16, 'bold'))
total_price_label.pack()
#Payment options----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
payment_combo = ttk.Combobox(root, values=["Cash", "Card"])
payment_combo.pack()
payment_combo.set("Select payment option")
payment_combo['state']='readonly'
#Additional requests label----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
requests_label_frame = tk.Frame(root)
requests_label_frame.pack(anchor=tk.W)

requests_label = tk.Label(requests_label_frame, text = "Additional customer requests", foreground='red', font=('Ink Free', 16, 'bold'))
requests_label.pack(padx=215)
#additional requests----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
requests_frame = tk.Frame(root)
requests_frame.pack(anchor=tk.W)

requests_entry = tk.Entry(requests_frame, width = 70)
requests_entry.pack(padx=215)

root.mainloop()
