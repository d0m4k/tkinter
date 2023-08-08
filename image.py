import tkinter as tk
from os import path, listdir
from PIL import Image, ImageTk
root = tk.Tk()
root.title("Image Viewer")

for image_name in listdir("images"):
    tk.Label(root, text=image_name, background="grey",foreground="whitesmoke").pack()
    if len(listdir("images")):
        print()

img_name = tk.Entry(root)
img_name.pack(padx=100)


        
def clicked():
    img_ = img_name.get()
    new_win = tk.Toplevel(root)
    new_win.title(img_)
    image = Image.open(f"images/{img_}")
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(new_win, image=photo)
    label.image = photo
    label.pack()

show = tk.Button(root, text="show", command=clicked)
show.pack(padx=100)

root.mainloop()