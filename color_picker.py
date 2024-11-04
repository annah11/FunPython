import tkinter as tk

def display_color(color_name, hex_color, rgb_color):
    """Updates the label to show the selected color name, hex, and RGB values."""
    color_label.config(text=f"Selected Color: {color_name}\nHex: {hex_color}\nRGB: {rgb_color}", bg=hex_color)
    color_label.pack()

# Set up main tkinter window
root = tk.Tk()
root.title("Basic Color Picker")
root.geometry("300x200")

# Label to display the selected color
color_label = tk.Label(root, text="No color selected", font=("Arial", 14))

# Color data for primary colors
colors = {
    "Red": ("#FF0000", (255, 0, 0)),
    "Yellow": ("#FFFF00", (255, 255, 0)),
    "Blue": ("#0000FF", (0, 0, 255)),
}

# Create buttons for each color
for color_name, (hex_color, rgb_color) in colors.items():
    color_button = tk.Button(root, text=color_name, bg=hex_color, fg="white", font=("Arial", 12),
                             command=lambda name=color_name, hex=hex_color, rgb=rgb_color: display_color(name, hex, rgb))
    color_button.pack(pady=5, fill="x")

# Run the application
root.mainloop()
