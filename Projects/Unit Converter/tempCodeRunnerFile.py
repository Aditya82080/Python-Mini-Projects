import tkinter as tk
from tkinter import ttk, messagebox

def convert_units():
    try:
        value = float(entry_value.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()
        unit_type = combo_type.get()

        if unit_type == "Length":
            result = convert_length(value, from_unit, to_unit)
        elif unit_type == "Mass":
            result = convert_mass(value, from_unit, to_unit)
        elif unit_type == "Temperature":
            result = convert_temperature(value, from_unit, to_unit)
        elif unit_type == "Volume":
            result = convert_volume(value, from_unit, to_unit)
        else:
            raise ValueError("Invalid unit type selected.")

        if result is not None:
            label_result.config(text=f"{value} {from_unit} = {result:.2f} {to_unit}")
        else:
            label_result.config(text="Conversion failed. Check your inputs.")
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def update_units(event):
    unit_type = combo_type.get()
    if unit_type == "Length":
        units = ['meter', 'kilometer', 'centimeter', 'millimeter', 'micrometer', 'nanometer', 'mile', 'yard', 'foot', 'inch']
    elif unit_type == "Mass":
        units = ['kilogram', 'gram', 'milligram', 'metric ton', 'pound', 'ounce']
    elif unit_type == "Temperature":
        units = ['Celsius', 'Fahrenheit', 'Kelvin']
    elif unit_type == "Volume":
        units = ['liter', 'milliliter', 'cubic meter', 'cubic centimeter', 'gallon', 'quart', 'pint', 'cup', 'fluid ounce']
    else:
        units = []

    combo_from['values'] = units
    combo_to['values'] = units

# Conversion functions (same as in the text-based code above)
def convert_length(value, from_unit, to_unit):
    length_factors = {
        'meter': 1, 'kilometer': 1000, 'centimeter': 0.01, 'millimeter': 0.001,
        'micrometer': 1e-6, 'nanometer': 1e-9, 'mile': 1609.34,
        'yard': 0.9144, 'foot': 0.3048, 'inch': 0.0254
    }
    try:
        value_in_meters = value * length_factors[from_unit.lower()]
        return value_in_meters / length_factors[to_unit.lower()]
    except KeyError:
        return None

def convert_mass(value, from_unit, to_unit):
    mass_factors = {
        'kilogram': 1, 'gram': 0.001, 'milligram': 1e-6,
        'metric ton': 1000, 'pound': 0.453592, 'ounce': 0.0283495
    }
    try:
        value_in_kg = value * mass_factors[from_unit.lower()]
        return value_in_kg / mass_factors[to_unit.lower()]
    except KeyError:
        return None

def convert_temperature(value, from_unit, to_unit):
    try:
        if from_unit.lower() == 'celsius':
            temp_c = value
        elif from_unit.lower() == 'fahrenheit':
            temp_c = (value - 32) * 5/9
        elif from_unit.lower() == 'kelvin':
            temp_c = value - 273.15
        else:
            return None

        if to_unit.lower() == 'celsius':
            return temp_c
        elif to_unit.lower() == 'fahrenheit':
            return (temp_c * 9/5) + 32
        elif to_unit.lower() == 'kelvin':
            return temp_c + 273.15
        else:
            return None
    except:
        return None

def convert_volume(value, from_unit, to_unit):
    volume_factors = {
        'liter': 1, 'milliliter': 0.001, 'cubic meter': 1000,
        'cubic centimeter': 0.001, 'gallon': 3.78541,
        'quart': 0.946353, 'pint': 0.473176, 'cup': 0.24,
        'fluid ounce': 0.0295735
    }
    try:
        value_in_liters = value * volume_factors[from_unit.lower()]
        return value_in_liters / volume_factors[to_unit.lower()]
    except KeyError:
        return None

# GUI Setup
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x300")

# Input for unit type
label_type = tk.Label(root, text="Select Unit Type:")
label_type.pack()
combo_type = ttk.Combobox(root, values=["Length", "Mass", "Temperature", "Volume"])
combo_type.bind("<<ComboboxSelected>>", update_units)
combo_type.pack()

# Input for value
label_value = tk.Label(root, text="Enter Value:")
label_value.pack()
entry_value = tk.Entry(root)
entry_value.pack()

# Dropdown for from and to units
label_from = tk.Label(root, text="From Unit:")
label_from.pack()
combo_from = ttk.Combobox(root)
combo_from.pack()

label_to = tk.Label(root, text="To Unit:")
label_to.pack()
combo_to = ttk.Combobox(root)
combo_to.pack()

# Convert button
btn_convert = tk.Button(root, text="Convert", command=convert_units)
btn_convert.pack()

# Result display
label_result = tk.Label(root, text="", font=("Arial", 14))
label_result.pack()

root.mainloop()
