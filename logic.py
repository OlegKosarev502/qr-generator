import os
import qrcode
from tkinter import filedialog

img_path = 'C:/Dev/python-eel/img/result.png'

def clear_folder():
    if (os.path.exists(img_path)):
        os.remove(img_path)

def close_callback(*args):
    clear_folder()

def generate_qr(url):
    clear_folder()
    img = qrcode.make(url)
    img.save(img_path)

def save_img():
    filedialog.asksaveasfile()
