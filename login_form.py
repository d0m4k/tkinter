import tkinter as tk

window = tk.Tk()
window.title("Login")

def login():
    user = username.get()
    passw = password.get()
    print(f"usernme: {user} Password: {passw}")

label_usr = tk.Label(window, text="Username")
label_usr.pack()
username = tk.Entry(window)
username.pack(padx=100)

label_pas = tk.Label(window, text="Password")
label_pas.pack()
password = tk.Entry(window, show="*")
password.pack(padx=100)

submit = tk.Button(window, text="Login", command=login)
submit.pack(pady=10)


window.mainloop()