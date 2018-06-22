# Script that creates a GUI which users can easily create HTML widgets with

import tkinter

root = tkinter.Tk()
root.title("Generate Media Widgets")
root.geometry("720x100")

def lgen():
    url = l_entry.get()
    url = '"' + url + '"'
    print("""
    <!-- LinkedIn Widget HTML **************************************************-->
    <script src=“//platform.linkedin.com/in.js” type=“text/javascript”></script>
    <script type=“IN/MemberProfile” 
    data-id="""+ url+ """ data-format=“inline” 
    data-related=“false”></script>
    <!-- ***********************************************************************-->
    """)
    l_entry.insert(0,"")

def ttgen():
    url = tt_entry.get()
    url = '"' + url + '"'
    print("""
    <!-- Twitter Timeline HTML *************************************************-->
    <a class="twitter-timeline" width="100px" height="100px" 
    href="""+url+""">Tweets</a> 
    <script async src="https://platform.twitter.com/widgets.js" charset="utf-8">
    </script>
    <!-- ***********************************************************************-->
    """)
    tt_entry.insert(0,"")

def fgen():
    url = f_entry.get()
    print("""
    <!-- Google Plus Profile HTML **********************************************-->
    <script src="https://apis.google.com/js/platform.js" async defer></script>
    <div class="g-person" data-href="//plus.google.com/"""+url+"""" data-rel="author">
    </div>
    <!-- ***********************************************************************-->
    """)
    f_entry.insert(0, "")

def tttgen():
    url = tt_entry.get()
    url = '"' + url
    print("""
    <!-- Twitter Follow Button HTML ********************************************-->
    <a href="""+url+"""?ref_src=twsrc%5Etfw" class="twitter-follow-button" 
    data-show-count="false">Follow</a><script async 
    src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    <!-- ***********************************************************************-->
    """)
    tt_entry.insert(0,"")

l_label = tkinter.Label(text="LinkedIn User URL: ")
l_label.grid(row=2,column=0)
l_entry = tkinter.Entry()
l_entry.grid(row=2,column=1)
l_button = tkinter.Button(text="LinkedIn Plugin HTML",command=lgen)
l_button.grid(row=2,column=2)

tt_label = tkinter.Label(text="Twitter User URL: ")
tt_label.grid(row=3,column=0)
tt_entry = tkinter.Entry()
tt_entry.grid(row=3,column=1)
tt_button = tkinter.Button(text="Twitter Timeline HTML",command=ttgen)
tt_button.grid(row=3,column=2)
ttt_button = tkinter.Button(text="User Follow Button HTML",command=tttgen)
ttt_button.grid(row=3,column=3)

f_label = tkinter.Label(text="Google Plus User ID: ")
f_label.grid(row=5,column=0)
f_entry = tkinter.Entry()
f_entry.grid(row=5,column=1)
f_button = tkinter.Button(text="Google Plus Widget HTML",command=fgen)
f_button.grid(row=5,column=2)

root.mainloop()
