import tkinter as tk
import random

window = tk.Tk()
window.title("Canvas Tiles")
canvas = tk.Canvas(window, width=1000, height=1000)
canvas.pack()

colors = ["red", "green", "blue", "yellow", "indigo", "orange", "grey","purple","pink","navy","brown","cyan","lime","magenta"]
color_index = random.randint(0, len(colors)-1)

def handle_click(event):
    global color_index
    x = event.x
    y = event.y
    canvas.create_rectangle(x-50, y-50, x+50, y+50, fill=colors[color_index], outline="")
    color_index = random.randint(0, len(colors)-1)

canvas.bind("<Button-1>", handle_click)

# Create a grid
grid_size = 15
cell_size = 50
for row in range(grid_size):
    for col in range(grid_size):
        x1 = col * cell_size
        y1 = row * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        canvas.create_rectangle(x1, y1, x2, y2, outline="grey")

def handle_cell_click(event):
    global color_index
    x = event.x
    y = event.y
    col = x // cell_size
    row = y // cell_size
    x1 = col * cell_size
    y1 = row * cell_size
    x2 = x1 + cell_size
    y2 = y1 + cell_size
    canvas.create_rectangle(x1, y1, x2, y2, fill=colors[color_index], outline="")
    color_index = random.randint(0, len(colors)-1)

canvas.bind("<Button-1>", handle_cell_click)

# Start the main event loop
window.mainloop()
