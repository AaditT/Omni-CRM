from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import tkinter as tk
import os
from PIL import ImageTk, Image
import subprocess
import keyboard


root = tk.Tk()
root.title("Omniscient CRM Git GUI")
root.geometry('1000x1000')



def quit():
    root.destroy()
def update(s):
    messagebox.showinfo("Alert",str(s))
def get_output(cmd):
    v = subprocess.call(str(cmd))
    if str(v) == "128":
        return ("failed to clone repo")
    elif str(v) == "0":
        return ("successfully cloned repo")
    subprocess.call("cd")
def openFile():
    global filename
    filename = askopenfilename(title="Select File")
    print(filename)
    fileLabel = tk.Label(root, text=filename,font="Helvetica 8 bold")
    fileLabel.grid(row=4,column=2)
    pushButton = tk.Button(root, text="Push File")
    pushButton.grid(row=4,column=3)
def openRepo():
    global reponame
    reponame = askopenfilename(title="Select Repo")
def clone_repo():
    global repo
    repo = clone_entry.get()
    cmd = "git clone "+str(repo)
    update(get_output(cmd))
    clone_entry.delete(0, END)
def find_str(s, char):
    index = 0
    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index
            index = index + 1
def reverse_string(original):
    new = ''
    index = len(original)
    while index > 0:
        new = new + original[index-1]
        index = index - 1
    return(new)
def open_repo():
    repository = ''
    index = find_str(repo, ".git")
    while repo[index] is not "/":
        repository = repository + repo[index]
        index = index - 1
    repository = reverse_string(repository)
    repository = ''.join([c for c in repository if c.isalpha()])
    keyboard.press_and_release('ctrl+c')
    os.system("cd "+str(repository))

logo = ImageTk.PhotoImage(Image.open("https://photos.app.goo.gl/9hrx9bKMfcUi76c39"))
panel = Label(root, image = logo)
panel.grid(row=0,column=1)

title_label = Label(root, text="Omniscient CRM Git GUI",font=("Helvetica", 14))
title_label.grid(row=0,column=1)

clone_label = tk.Label(root,text="Repository: ")
clone_label.grid(row=1,column=1)
clone_entry = tk.Entry(root,width=40)
clone_entry.grid(row=1, column=2)
clone_button = tk.Button(root,text="Clone",command=clone_repo)
clone_button.grid(row=1, column=3)
openRepoButton = tk.Button(root,text="Open existing repo...",command=openRepo)
openRepoButton.grid(row=2, column=1)
cd_button = tk.Button(root, text="Enter repo directory",command = open_repo)
cd_button.grid(row=3,column=1)
openFileButton = tk.Button(text="Open File...",command=openFile)
openFileButton.grid(row=4,column=1)
quitButton = tk.Button(text="QUIT",command=quit)
quitButton.grid(row=6,column=1)

root.mainloop()
