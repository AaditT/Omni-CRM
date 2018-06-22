import tkinter
import webbrowser

root = tkinter.Tk()
root.title("Generate MJML Email Template")
root.geometry("500x500")

global code
code = """

<!-- ****************************************************-->
<mjml>

"""

def gen():
    added_code = """"""
    if str(bc_entry.get()) is not "" and len(str(bc_entry.get())) == 6:
        added_code += """
        <mj-body background-color="#"""+str(bc_entry.get())+"""">
        <mj-column>
        """
    else:
        added_code += """
        <body>
        """
    if str(i_entry.get()) is not "":
        if str(iw_entry.get()) is not "" and str(ih_entry.get()) is not "":
            added_code+= """
            <mj-image width='"""+str(iw_entry.get())+"""px' height='"""+str(ih_entry.get())+"""px' src='"""+str(i_entry.get())+"""'></mj-image>            
            """
        else:
            added_code+= """
            <mj-image width="100" src='"""+str(i_entry.get())+"""'></mj-image>            
            """
    if str(h_entry.get()) is not "":
        if str(hs_entry.get()) is not "":
            added_code+= """
            <mj-text align='center' font-size='"""+hs_entry.get()+"""px' color="#F45E43" font-family="helvetica">"""+str(h_entry.get())+"""</mj-text>
            """
        else:
            added_code+= """
            <mj-text align='center' font-size="30px" color="#F45E43" font-family="helvetica">"""+str(h_entry.get())+"""</mj-text>"""


    added_code += """
    </mj-column>
    </mj-body>
    </mjml>
<!-- ****************************************************-->
    """
    global code
    code += added_code
    
    print(code)
    def openn():
        webbrowser.open_new_tab("https://mjml.io/try-it-live/By-dBEq-X")

    openb = tkinter.Button(text="Open in MJML Editor",command=openn)
    openb.grid(row=11,column=0)



bc_label = tkinter.Label(text="Background Color HTML Code: ")
bc_label.grid(row=0,column=0)
bc_entry = tkinter.Entry()
bc_entry.grid(row=0,column=1)

i_label = tkinter.Label(text="Logo URL: ")
i_label.grid(row=1,column=0)
i_entry = tkinter.Entry()
i_entry.grid(row=1,column=1)

iw_label = tkinter.Label(text="Logo Width (pixels): ")
iw_label.grid(row=2,column=0)
iw_entry = tkinter.Entry()
iw_entry.grid(row=2,column=1)

ih_label = tkinter.Label(text="Logo Height (pixels): ")
ih_label.grid(row=3,column=0)
ih_entry = tkinter.Entry()
ih_entry.grid(row=3,column=1)

h_label = tkinter.Label(text="Headline: ")
h_label.grid(row=4,column=0)
h_entry = tkinter.Entry()
h_entry.grid(row=4,column=1)

hs_label = tkinter.Label(text="Headline Font Size (pixels): ")
hs_label.grid(row=5,column=0)
hs_entry = tkinter.Entry()
hs_entry.grid(row=5,column=1)

send = tkinter.Button(text="Generate MJML",command=gen)
send.grid(row=10,column=0)

root.mainloop()
