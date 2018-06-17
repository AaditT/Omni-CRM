from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
import os
global userFile
userFile = StringVar()
userFile.set("")
def openFile():
    global filename
    filename = askopenfilename(title="Select File")
    userFile.set(filename)
def cdLocal():
    global localrepo
    localrepo = local.get()
    os.system("cd "+str(localrepo))
    userFile.set(localrepo)
def push():    
    remoteRepo = realRepo.get()
    commitMessage = commitEntry.get()
    os.system("git init")
    os.system("git add "+filename)
    os.system('git commit -m "'+str(commitMessage)+'"')
    os.system("git remote add origin "+str(remoteRepo))
    os.system("git push origin master")
localrepolabel = tk.Label(text="Local Repository File Path:")
localrepolabel.grid(row=0,column=0)
local = tk.Entry()
local.grid(row=0,column=1)
enterlocal = tk.Button(text="Change Directory",command=cdLocal)
enterlocal.grid(row=0,column=2)
button = tk.Button(text="Open File",command=openFile)
button.grid(row=1,column=0)
label = tk.Label(text=userFile)
label.grid(row=2,column=0)
commitLabel = tk.Label(text="Enter message:")
commitLabel.grid(row=3,column=0)
commitEntry = tk.Entry()
commitEntry.grid(row=3, column=1)
repoLabel = tk.Label(text="Remote repo URL:")
repoLabel.grid(row=4,column=0)
realRepo = tk.Entry()
realRepo.grid(row=4,column=1)
uploadButton = tk.Button(text="Push",command=push)
uploadButton.grid(row=5, column=0)
root.mainloop()
