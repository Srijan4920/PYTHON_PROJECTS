import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        feet = feet_entry.get()
        inches = inches_entry.get()

        # Handle empty entries
        feet = int(feet) if feet else 0
        inches = int(inches) if inches else 0

        # Convert feet and inches to meters
        total_inches = feet * 12 + inches
        height_m = total_inches * 0.0254

        if height_m <= 0 or weight <= 0:
            raise ValueError("Height and weight must be positive numbers.")

        bmi = round(weight / (height_m ** 2), 2)

        # Determine category and color
        if bmi < 18.5:
            category = "Underweight"
            color = "blue"
        elif 18.5 <= bmi <= 24.9:
            category = "Normal weight"
            color = "green"
        elif 25 <= bmi <= 29.9:
            category = "Overweight"
            color = "orange"
        else:
            category = "Obese"
            color = "red"

        result_label.config(text=f"BMI: {bmi}\nCategory: {category}", fg=color)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight, feet, and inches.")

def reset_fields():
    """Clear all input fields and result label."""
    weight_entry.delete(0, tk.END)
    feet_entry.delete(0, tk.END)
    inches_entry.delete(0, tk.END)
    result_label.config(text="", fg="black")

# GUI setup
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("320x320")
window.resizable(False, False)

tk.Label(window, text="BMI Calculator", font=("Helvetica", 16, "bold")).pack(pady=10)

tk.Label(window, text="Weight (kg):").pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

tk.Label(window, text="Height:").pack()
frame = tk.Frame(window)
frame.pack()

tk.Label(frame, text="Feet").grid(row=0, column=0, padx=5)
feet_entry = tk.Entry(frame, width=5)
feet_entry.grid(row=0, column=1)

tk.Label(frame, text="Inches").grid(row=0, column=2, padx=5)
inches_entry = tk.Entry(frame, width=5)
inches_entry.grid(row=0, column=3)

# Buttons frame
btn_frame = tk.Frame(window)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Calculate BMI", command=calculate_bmi).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Reset", command=reset_fields).grid(row=0, column=1, padx=10)

result_label = tk.Label(window, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

window.mainloop()
