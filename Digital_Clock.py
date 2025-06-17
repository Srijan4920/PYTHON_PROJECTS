import tkinter as tk
import time
import math
from datetime import datetime

root = tk.Tk()
root.title("Stylish Digital Clock")
root.geometry("500x550")
root.resizable(False, False)

# Themes
themes = {
    "Dark": {"bg": "#2C3E50", "fg": "white", "clock_fg": "cyan", "day_fg": "orange"},
    "Light": {"bg": "white", "fg": "black", "clock_fg": "blue", "day_fg": "green"}
}
current_theme = "Dark"

def toggle_theme():
    global current_theme
    current_theme = "Light" if current_theme == "Dark" else "Dark"
    apply_theme()

def apply_theme():
    theme = themes[current_theme]
    root.config(bg=theme["bg"])
    clock_label.config(bg=theme["bg"], fg=theme["clock_fg"])
    day_label.config(bg=theme["bg"], fg=theme["day_fg"])
    date_label.config(bg=theme["bg"], fg=theme["fg"])
    canvas.config(bg=theme["bg"])

def update():
    now = datetime.now()
    current = now.strftime("%H:%M:%S")
    clock_label.config(text=current)
    day_label.config(text=now.strftime("%A"))
    date_label.config(text=now.strftime("%d %B %Y"))
    update_analog(now)
    root.after(1000, update)

# Analog clock hands
def update_analog(now):
    canvas.delete("hands")
    cx, cy = 125, 125

    def draw_hand(angle, length, width, color):
        angle_rad = math.radians(angle)
        x = cx + length * math.sin(angle_rad)
        y = cy - length * math.cos(angle_rad)
        canvas.create_line(cx, cy, x, y, width=width, fill=color, tags="hands")

    draw_hand((now.hour % 12 + now.minute/60) * 30, 40, 6, "blue")
    draw_hand(now.minute * 6, 60, 4, "green")
    draw_hand(now.second * 6, 70, 2, "red")

# UI
clock_label = tk.Label(root, font=("Courier", 50, "bold"))
clock_label.pack(pady=10)

day_label = tk.Label(root, font=("Arial", 20, "italic"))
day_label.pack()

date_label = tk.Label(root, font=("Arial", 16))
date_label.pack()

tk.Button(root, text="Toggle Theme", command=toggle_theme).pack(pady=10)

# Analog Clock
canvas = tk.Canvas(root, width=250, height=250)
canvas.pack(pady=20)
canvas.create_oval(25, 25, 225, 225, width=4)

for i in range(12):
    angle = math.radians(i * 30)
    x1 = 125 + 90 * math.sin(angle)
    y1 = 125 - 90 * math.cos(angle)
    x2 = 125 + 100 * math.sin(angle)
    y2 = 125 - 100 * math.cos(angle)
    canvas.create_line(x1, y1, x2, y2, width=2)

apply_theme()
update()
root.mainloop()
