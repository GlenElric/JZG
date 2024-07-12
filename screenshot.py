import tkinter as tk
from PIL import ImageGrab # type: ignore

def take_screenshot():
    # Capture the entire screen
    screenshot = ImageGrab.grab()
    
    # Save the screenshot (optional)
    screenshot.save("screenshot.png")
    
    # Display a message (optional)
    label.config(text="Screenshot taken and saved as screenshot.png")

# Create the main window
root = tk.Tk()
root.title("Screenshot Tool")

# Create a button to take the screenshot
button = tk.Button(root, text="Take Screenshot", command=take_screenshot)
button.pack(pady=20)

# Create a label for displaying messages (optional)
label = tk.Label(root, text="")
label.pack()

# Run the main event loop
root.mainloop()
