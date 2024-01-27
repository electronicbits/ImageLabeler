import tkinter as tk
from PIL import Image, ImageTk
import os
import shutil
import glob

# Configuration
image_folder = 'path/to/your/images'  # Update this to your images folder
output_folders = {
    '1': 'brand_new',
    '2': 'renovated',
    '3': 'old',
    '4': 'trash_dump'
}

# Ensure output directories exist
for folder in output_folders.values():
    os.makedirs(os.path.join(image_folder, folder), exist_ok=True)

# Load all images
images = glob.glob(os.path.join(image_folder, '*.*'))
current_image_idx = 0

# Initialize GUI
root = tk.Tk()
root.title("Image Labeling Tool")

# Image Panel
image_panel = tk.Label(root)
image_panel.pack()

def show_image(image_path):
    img = Image.open(image_path)
    img = img.resize((800, 600), Image.ANTIALIAS)  # Resize image
    img = ImageTk.PhotoImage(img)
    image_panel.configure(image=img)
    image_panel.image = img  # Keep a reference

def move_image(image_path, category):
    destination = os.path.join(image_folder, category, os.path.basename(image_path))
    shutil.move(image_path, destination)

def load_next_image():
    global current_image_idx
    if current_image_idx < len(images) - 1:
        current_image_idx += 1
        show_image(images[current_image_idx])
    else:
        print("No more images.")
        root.destroy()  # Close the application if no more images

def on_key_press(event):
    category = output_folders.get(event.char)
    if category:
        move_image(images[current_image_idx], category)
        load_next_image()

root.bind('<Key>', on_key_press)

# Start by showing the first image
if images:
    show_image(images[current_image_idx])
else:
    print("No images found in the folder.")

root.mainloop()
