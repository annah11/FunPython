import tkinter as tk
from tkinter import colorchooser

def pick_color():
    # Opens a color chooser dialog and returns the color in hexadecimal
    color_code = colorchooser.askcolor(title="Choose color")
    if color_code:
        hex_color = color_code[1]  # hex color code
        rgb_color = color_code[0]  # RGB tuple
        display_color(hex_color, rgb_color)

def display_color(hex_color, rgb_color):
    # Display the chosen color and its values in the UI
    color_label.config(text=f"Selected Color: {hex_color}\nRGB: {rgb_color}", bg=hex_color)
    color_label.pack()

# Set up main tkinter window
root = tk.Tk()
root.title("Color Picker")
root.geometry("300x150")

# Label to display the selected color
color_label = tk.Label(root, text="No color selected", font=("Arial", 14))

# Button to open color picker dialog
pick_button = tk.Button(root, text="Pick a Color", command=pick_color)
pick_button.pack(pady=20)

# Run the application
root.mainloop()
