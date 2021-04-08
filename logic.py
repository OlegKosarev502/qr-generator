import os
from qrcode import make as make_qr
from tkinter import filedialog
from PIL import Image 

img_path = 'C:/Dev/qr-generator/img/result.png'

def clear_folder():
    if (os.path.exists(img_path)):
        os.remove(img_path)

def close_callback(*args):
    clear_folder()

def generate_qr(url):
    clear_folder()
    img = make_qr(url)
    img.save(img_path)

def save_img():
    image = Image.open("img/result.png")
    file_name = filedialog.asksaveasfilename(
        title="Save file",
        filetypes=(("PNG", "*.png"), ("All Files", "*.*"))
    )
    image.save(str(file_name) + '.png', 'PNG')
