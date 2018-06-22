# Written by Aadit Trivedi
# June 15, 2018

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import tkinter as tk
import os
from os import chdir
from PIL import ImageTk, Image


root = tk.Tk()
root.title("Omniscient CRM Git GUI")
root.geometry('1000x1000')

def quit():
    root.destroy()

def update(s):
    messagebox.showinfo("Alert",str(s))

def openFile():
    global filename
    filename = askopenfilename(title="Select File")
    print(filename)
    fileLabel = tk.Label(root, text=filename,font="Helvetica 8 bold")
    fileLabel.grid(row=4,column=2)
    def push():
        pass
    pushButton = tk.Button(root, text="Push File",command=push)
    pushButton.grid(row=4,column=3)

def openRepo():
    global reponame
    reponame = askdirectory(title="Select Repo")
    repoLabel = tk.Label(root, text=reponame,font="Helvetica 8 bold")
    repoLabel.grid(row=3,column=2)
    pushButton = tk.Button(root, text="Push File")
    pushButton.grid(row=3,column=3)
    chdir(reponame)

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

def clone_repo():
    global repo
    repo = clone_entry.get()
    cmd = "git clone "+str(repo)
    if FileNotFoundError:
        update("'"+str(repo)+"' not a git repository")
        clone_entry.delete(0,END)
    else:
        repository = ''
        index = find_str(repo, ".git")
        while repo[index] is not "/":
            repository = repository + repo[index]
            index = index - 1
        repository = reverse_string(repository)
        repository = ''.join([c for c in repository if c.isalpha()])
        chdir(repository)
        update("Successfully cloned '"+str(repository)+"'")
        clone_entry.delete(0, END)

def createnew():
    newdir = new_entry.get()
    newdir = str(newdir)
    os.mkdir(newdir)
    chdir(newdir)
    update("Created '"+str(newdir)+"' directory")
    new_entry.delete(0,END)

logo = ImageTk.PhotoImage(Image.open("/Users/aadittrivedi/Desktop/omniomni.png"))
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

new_label = tk.Label(root,text="New Repository: ")
new_label.grid(row=2,column=1)
new_entry = tk.Entry(root)
new_entry.grid(row=2,column=2)
new_button = tk.Button(root,text="Create Repository",command=createnew)
new_button.grid(row=2,column=3)

openRepoButton = tk.Button(root,text="Open existing repository...",command=openRepo)
openRepoButton.grid(row=3, column=1)

openFileButton = tk.Button(text="Open File...",command=openFile)
openFileButton.grid(row=4,column=1)

quitButton = tk.Button(text="QUIT",command=quit)
quitButton.grid(row=5,column=1)

root.mainloop()
