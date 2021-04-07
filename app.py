from tkinter import *
import logic

logic.clear_folder()

root = Tk()
root.title("QR GENERATOR")
root.geometry("480x400")

save_state = DISABLED
default_url = StringVar(root, "https://www.google.com/")

def generate():
    url = entry.get()
    logic.generate_qr(url)

header = Label(root, text="PASS URL")
entry = Entry(root, textvariable=default_url, width=32)

generate_button = Button(
    root,
    text="GENERATE",
    padx=12,
    command=generate
)

img_mock = Label(root, text="VALUE-2") # QR IMG

save_button = Button(
    root,
    text="SAVE",
    state=save_state,
    padx=12,
    command=logic.save_img
)

header.grid(row="0", column="0")
entry.grid(row="1", column="0")
generate_button.grid(row="1", column="1")
img_mock.grid(row="2", column="0")
save_button.grid(row="3", column="0")

root.mainloop()
