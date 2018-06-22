import tkinter

root = tkinter.Tk()
root.title("Generate Media Widgets")
root.geometry("720x150")

global code
code = """
<!DOCTYPE html>
    <hmtl>
        <head>
            <meta charset="utf-8">
            <title>
                Social Media
            </title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body>
"""

global end_code
end_code = """
        </body>
    </html>
"""

def lgen():
    url = l_entry.get()
    url = '"' + url + '"'
    print(code + """
    <!-- LinkedIn Widget HTML ***********************************************-->
            <div>
                <script src=“//platform.linkedin.com/in.js” 
                type=“text/javascript”></script>
                <script type=“IN/MemberProfile” 
                data-id=""" + str(url) + """ data-format=“inline” 
                data-related=“false”></script>
            </div>
    <!-- ********************************************************************-->
    """ + end_code)
    l_entry.insert(0,"")

def ttgen():
    url = tt_entry.get()
    url = '"' + url + '"'
    print(code+"""
    <!-- Twitter Timeline HTML **********************************************-->
            <div>
                <a class="twitter-timeline" width="100px" height="100px" 
                href="""+str(url)+""">Tweets</a> 
                <script async src="https://platform.twitter.com/widgets.js" 
                charset="utf-8">
                </script>
            </div>
    <!-- ********************************************************************-->
    """+end_code)
    tt_entry.insert(0,"")

def fgen():
    url = f_entry.get()
    print(code+"""
    <!-- Google Plus Profile HTML *******************************************-->
            <div>
                <script src="https://apis.google.com/js/platform.js" 
                async defer></script>
                <div class="g-person" data-href="//plus.google.com/"""+url+""""
                data-rel="author">
                </div>
            </div>
    <!-- ********************************************************************-->
    """+end_code)
    f_entry.insert(0, "")

def tttgen():
    url = tt_entry.get()
    url = '"' + url
    print(code+"""
    <!-- Twitter Follow Button HTML *****************************************-->
            <div>
                <a href="""+str(url)+"""?ref_src=twsrc%5Etfw" 
                class="twitter-follow-button" 
                data-show-count="false">Follow</a><script async 
                src="https://platform.twitter.com/widgets.js" 
                charset="utf-8"></script>
            </div>
    <!-- ********************************************************************-->
    """+end_code)
    tt_entry.insert(0,"")

def ygen():
    url = y_entry.get()
    print(code+"""
    <!-- YT Subscribe Button HTML *******************************************-->
            <div>
                <script src="https://apis.google.com/js/platform.js"></script>
                <div class="g-ytsubscribe" data-channel='"""+str(url)+"""'
                data-layout="default" data-count="default"></div>
            </div>
    <!-- ********************************************************************-->
    """+end_code)
    y_entry.insert(0,"")

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

y_label = tkinter.Label(text="Youtube Channel Name: ")
y_label.grid(row=6,column=0)
y_entry = tkinter.Entry()
y_entry.grid(row=6,column=1)
y_button = tkinter.Button(text="YT Subscribe Button HTML",command=ygen)
y_button.grid(row=6,column=2)

root.mainloop()
