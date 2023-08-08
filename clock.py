from tkinter import *

window = Tk()
window.title("Clock")

from time import strftime
from time import sleep
def show_time():
    time = strftime("%H:%M:%S %p")
    clock.config(text=time)
    clock.after(1000, show_time)
clock = Label(window, font=("cursive", 40, "bold"), background="black", foreground="green", padx=200, pady=400)

clock.pack(anchor="center")
show_time()
if __name__ == '__main__':
    window.mainloop()