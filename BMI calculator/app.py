import ttkbootstrap as ttk
from tkinter import messagebox

def bmi(weight, height):
    bmi_value = round(weight / (height * height), 1)
    if bmi_value < 18.5:
        found = "UnderWeight"
    elif 18.5 <= bmi_value < 24.9:
        found = "Normal Weight"
    elif 25<= bmi_value < 29.9:
        found = "Overweight"
    elif 30 <= bmi_value < 35:
        found = "Obesity"
    else:
        found = "Severe Obesity"
    return found, bmi_value

def bmi_calculator():
    try:
        weight2 = float(weight.get())
        height2 = float(height.get())
        found, bmi_value = bmi(weight2, height2)
        entry_bmi.configure(text=f"BMI: {bmi_value} {found}")
    except ValueError as e:
        messagebox.showerror("ERROR", str(e))
        

root = ttk.Window(themename="solar")
root.title("BMI Calculator")
root.geometry("600x400")

ttk.Label(root, text="Weight (kg)").pack()
weight = ttk.Entry(root)
weight.pack()

ttk.Label(root, text="Height (m)").pack(pady=2)
height = ttk.Entry(root)
height.pack()

ttk.Button(root, text="calculate", command=bmi_calculator).pack(pady=10)

entry_bmi = ttk.Label(root, text="BMI:")
entry_bmi.pack()


root.mainloop()