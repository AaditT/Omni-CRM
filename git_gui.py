from tkinter import *
from tkinter import messagebox
import tkinter as tk
import os
import subprocess


root = tk.Tk()
root.title("Omniscient Git GUI")
root.geometry('1000x1000')

response = StringVar()
response_label = Label(root, textvariable=response,font="Times 15 bold")
response_label.grid(row=5)
response.set("")

def update(s):
    messagebox.showinfo("Alert",str(s))

def get_output(cmd):
    v = subprocess.call(str(cmd))
    if str(v) == "128":
        return ("failed to clone repo")
    elif str(v) == "0":
        return ("successfully cloned repo")

def clone_repo():
    repo = clone_entry.get()
    cmd = "git clone "+str(repo)
    update(get_output(cmd))


clone_label = tk.Label(root,text="Repository: ")
clone_label.grid(row=1,column=1)
clone_entry = tk.Entry(root,width=40)
clone_entry.grid(row=1, column=2)
clone_button = tk.Button(root,text="Clone",command=clone_repo)
clone_button.grid(row=1, column=3)

root.mainloop()