import subprocess
import tkinter as tk

root = tk.Tk()
root.title("Omniscient Git GUI")
root.geometry('1000x1000')

def quit():
    root.destroy()

def run_command(cmd):
    cmd = cmd.split()
    new_cmd = []
    for word in cmd:
        new_cmd.append(str(word))
    result = subprocess.check_output([new_cmd])
    print(result)

quitButton = tk.Button(text=“Quit”,command=quit)
quitButton.grid(row=5,column=0)

root.mainloop()
