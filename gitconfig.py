from tkinter import *
import tkinter as tk
import os

root = tk.Tk()

def config():
    username = usernameEntry.get()
    email = emailEntry.get()
    os.system('git config --global user.name "'+str(username)+'"')
    os.system('git config --global user.email '+str(email))
    usernameEntry.delete(0, END)
    emailEntry.delete(0, END)
    successLabel = tk.Label(text="Configured!")
    successLabel.grid(row=2,column=1)

usernameLabel = tk.Label(text="Username: ")
usernameLabel.grid(row=0,column=0)

usernameEntry = tk.Entry()
usernameEntry.grid(row=0,column=1)

emailLabel = tk.Label(text="Email: ")
emailLabel.grid(row=1,column=0)

emailEntry = tk.Entry()
emailEntry.grid(row=1,column=1)

configButton = tk.Button(text="Git Config",command=config)
configButton.grid(row=2,column=0)

root.mainloop()
