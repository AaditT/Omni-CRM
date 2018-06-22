import webview
import tkinter as tk
from tkinter import messagebox
 
root = tk.Tk()
root.geometry("500x500")

global contacts
contacts = ["https://twitter.com/kingjames"]

def searchUser():
    usr = entry.get()
    myurl = "https://twitter.com/"+str(usr)
    if myurl not in contacts:
        messagebox.showinfo("Alert", "Not saved as a contact")
    else:
        webview.create_window('Twitter Timeline',url=myurl)
    

label = tk.Label(text="Twitter User: ")
label.grid(row=0,column=0)
entry = tk.Entry()
entry.grid(row=0,column=1)
button = tk.Button(text="Search",command=searchUser)
button.grid(row=0,column=2)

root.mainloop()
