import webview
import tkinter as tk
from tkinter import messagebox
import requests
 
root = tk.Tk()
root.geometry("500x500")

global contacts
contacts = ["https://twitter.com/kingjames"]

def searchUser():
    usr = entry.get()
    myurl = "https://twitter.com/"+str(usr)
    request = requests.get(myurl)
    if request.status_code == 200:
        webview.create_window('Twitter Timeline',url=myurl)
    else:
        messagebox.showinfo("Alert","404: Twitter user does not exists")
    
def isTwitterUser(usrname):
    turl = "https://twitter.com/"+str(usrname)
    request = requests.get(turl)
    if request.status_code == 200: return True
    else: return False


label = tk.Label(text="Twitter User: ")
label.grid(row=0,column=0)
entry = tk.Entry()
entry.grid(row=0,column=1)
button = tk.Button(text="Generate Timeline",command=searchUser)
button.grid(row=0,column=2)

root.mainloop()
