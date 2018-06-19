from tkinter import Tk, Label, Button, Entry
import tkinter as tk
from git import Repo
from tkinter.filedialog import askdirectory
from tkinter import messagebox

class untrackedfiles:

    def __init__(self, master):
        self.master = master
        master.title("Git Stats GUI")
        
        self.open_button = Button(master, text="Open existing repository...",command=self.openRepo)
        self.open_button.grid(row=0,column=0)
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row = 5, column = 0)    

    def openRepo(self):

        def untracked_files():
            repo = Repo(reponame)
            untracked_list = repo.untracked_files
            if untracked_list == []:
                untracked_label = Label(text="All files tracked!")
                untracked_label.grid(row=2, column=0)
            else:
                untracked_label = Label(text=str(untracked_list))
                untracked_label.grid(row=2, column=0)

        def untfiles_info_command():
            messagebox.showinfo("Info: Untracked Files","View Untracked Files: Query the active branch, query untracked files or whether the repository data has been modified")

        global reponame
        reponame = askdirectory(title="Select Repo")
        repoLabel = tk.Label(root, text=reponame,font="Helvetica 8 bold")
        repoLabel.grid(row=0,column=1)
        global repo
        repo = Repo(reponame)
        assert not repo.bare
        self.untfiles_button = Button(text="View Untracked Files", command=untracked_files)
        self.untfiles_button.grid(row = 1, column = 0)
        self.untfiles_info = Button(text="?",command=untfiles_info_command)
        self.untfiles_info.grid(row=1,column=1)

root = Tk()
my_gui = untrackedfiles(root)
root.mainloop()
