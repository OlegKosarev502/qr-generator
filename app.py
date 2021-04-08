from tkinter import *
from PIL import ImageTk, Image 
import logic
import threading

# TODO: Code refactoring
# TODO: Improve UI

logic.clear_folder()

root = Tk()
root.title("QR GENERATOR")
root.geometry("440x440")

default_url = StringVar(root, "https://www.google.com/")

def insert_img():
    load = Image.open("img/result.png")
    render = ImageTk.PhotoImage(load)
    qr_img = Label(root, image=render)
    qr_img.image = render
    qr_img.grid(row="2", column="0")

    save_button.config(state=NORMAL)

def generate():
    url = entry.get()
    logic.generate_qr(url)
    threading.Timer(1.0, insert_img).start()

header = Label(root, text="PASS URL")
entry = Entry(root, textvariable=default_url, width=32)

generate_button = Button(
    root,
    text="GENERATE",
    padx=12,
    command=generate
)

save_button = Button(
    root,
    text="SAVE",
    state=DISABLED,
    padx=12,
    command=logic.save_img
)

header.grid(row="0", column="0")
entry.grid(row="1", column="0")
generate_button.grid(row="1", column="1")
save_button.grid(row="3", column="0")

root.mainloop()
