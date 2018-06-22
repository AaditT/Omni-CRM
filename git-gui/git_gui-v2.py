# Written by Aadit Trivedi
# June 19, 2018

from tkinter import *
from tkinter import Label, Entry, Button
import tkinter
import tkinter as tk
import git
from git import Repo
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from tkinter import messagebox
import os

root = tk.Tk()

global repo
global hasOpenedRepo
hasOpenedRepo = False

def openFile():
    if hasOpenedRepo:
        index = repo.index
        global filename
        filename = askopenfilename(title="Select File")
        fileLabel = tk.Label(root, text=filename,font="Helvetica 10 bold")
        fileLabel.grid(row=1,column=1)
        def push():
            os.chdir(reponame)
            repo.git.add(str(filename))
            repo.git.commit()
            
        pushButton = tk.Button(root, text="Commit to Repository",command=push)
        pushButton.grid(row=1,column=2)
    else:
        messagebox.showinfo("Alert","Please open a repository before adding a file :)")

def openRepo():
    global reponame
    reponame = askdirectory(title="Select Repo")
    repoLabel = tk.Label(root, text=reponame,font="Helvetica 10 bold")
    repoLabel.grid(row=0,column=1)
    global repo
    repo = Repo(reponame)
    print (repo.git.status())
    global hasOpenedRepo
    hasOpenedRepo = True
    assert not repo.bare

openrepob = Button(root, text="Open Repository...",command=openRepo)
openrepob.grid(row=0,column=0)
openfileb = Button(root, text="Open file...",command=openFile)
openfileb.grid(row=1,column=0)


root.mainloop()
