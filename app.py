import os
import eel
import qrcode

img_path = 'C:/Dev/python-eel/web/img/result.png'

def clear_folder():
    if (os.path.exists(img_path)):
        os.remove(img_path)

def close_callback(*args):
    clear_folder()

# Set web files folder.
eel.init('web')

# Expose this function to JavaScript.
@eel.expose
def generate_qr(url):
    clear_folder()
    img = qrcode.make(url)
    img.save(img_path)

# Run the application.
eel.start('index.html', size=(400, 480), close_callback=close_callback)
