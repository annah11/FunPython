import tkinter as tk
from tkinter import colorchooser

def pick_color():
    color_code = colorchooser.askcolor(title="Choose color")
    if color_code:
        hex_color = color_code[1]  
        rgb_color = color_code[0]  
        display_color(hex_color, rgb_color)

def display_color(hex_color, rgb_color):
    color_label.config(text=f"Selected Color: {hex_color}\nRGB: {rgb_color}", bg=hex_color)
    color_label.pack()

root = tk.Tk()
root.title("Color Picker")
root.geometry("300x150")

color_label = tk.Label(root, text="No color selected", font=("Arial", 14))

pick_button = tk.Button(root, text="Pick a Color", command=pick_color)
pick_button.pack(pady=20)

root.mainloop()
