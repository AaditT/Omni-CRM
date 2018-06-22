import tkinter
import webbrowser
root = tkinter.Tk()
root.title("Generate MJML Email Template")
root.geometry("800x800")
def gen():
    b_color = bc_entry.get()
    pc = pc_entry.get()
    h = h_entry.get()
    hf = hs_entry.get()
    b1 = b_entry.get()
    bl = bl_entry.get()
    b2 = bb_entry.get()
    bll = bbl_entry.get()
    b3 = bbb_entry.get()
    blll = bbbl_entry.get()
    it = ft_entry.get()
    st = fts_entry.get()
    tt = ftss_entry.get()
    ct = ftsss_entry.get()
    firstfeatureimage = firstfeatureimage_entry.get()
    secondfeatureimage = secondfeatureimage_entry.get()
    print("""
    <!--
    Written by Aadit Trivedi
    June 20, 2018
    Omniscient CRM
    Color palette: https://coolors.co/8eaebc-accbd7-6aadc0-025374-016f92
    -->
    <mjml>
      <mj-head background-color="#FFFFFF">
        <mj-title>"""+str(h)+"""</mj-title>
        <mj-attributes>
          <mj-text font-family="Calibri" color="#025374" font-size="18px"/>
          <mj-class name="pill" font-weight="700" color="#6AADC0" border-radius="100px" border="2px solid #6AADC0" font-size="16px" line-height="16px" padding=" 20 20 20" inner-padding="5px 20px 5px 20px" background-color="transparent" />
        </mj-attributes>
      </mj-head>

      <mj-body background-color="#"""+str(b_color)+"""">
        <!-- Section for the header -->
        <mj-section padding="0px 0px 0px 0px" background-color='#"""+str(pc)+"""'>
          <mj-column>
              <mj-image width='100px' height='100' src='https://email164606341.files.wordpress.com/2018/06/omni-image.png'></mj-image>
          </mj-column>
        </mj-section>
        <!-- Section for the initial announcement and text-->
        <mj-section background-color='#"""+str(pc)+"""'>
          <mj-column>
            <mj-text align="center" padding="0px 0px 20px 0px" font-size='"""+str(hf)+"""px' font-family="Gill Sans MT" padding="0px 0px 5px 0px">"""+str(h)+"""</mj-text>
            <mj-divider padding="0px 0px 20px 0px" width="80%" border-color="#606060" padding="20 0px 20px 0px"></mj-divider>
            <mj-text>"""+str(it)+"""</mj-text>
          </mj-column>
        </mj-section>
        <!-- Column section with the buttons for new features and Training videos -->
        <mj-section background-color='#"""+str(pc)+"""'>
          <mj-column>
            <!-- Button 1 -->
            <mj-image align="center" padding="0px 0px 0px 0px" width="300px" height="200px" src='"""+str(firstfeatureimage)+"""'/>
            <mj-text align="center">"""+str(tt)+"""</mj-text>
            <mj-button mj-class="pill" padding="0px 0px 20px 0px"href='"""+str(bl)+"""' > """+str(b1)+""" </mj-button>
            <!-- Button 2 -->
            <mj-image align="center"  padding="0px 0px 0px 0px" width="300px" height="200px" src='"""+str(secondfeatureimage)+"""'"></mj-image>
            <mj-text align="center"> """+str(st)+"""</mj-text>
              <mj-button mj-class="pill" href='"""+str(bll)+"""' > """+str(b2)+""" </mj-button>
          </mj-column>
        </mj-section>
        <!-- Survey Section -->
        <mj-section  padding="10px 38px 20px 38px" background-color='#"""+str(pc)+"""'>
          <mj-column>
            <mj-text padding=" 0px 20px 20px 0px" align="center">"""+str(ct)+"""</mj-text>
            <mj-button mj-class='pill' padding="50 0 50 0" href='""" + str(blll) + """'>""" + str(b3) + """</mj-button>
          </mj-column>
        </mj-section>
        <mj-section background-color="#252020">
          <mj-column>
            <mj-text color="#5577FF" text-decoration="underline"align="center">
              <a href="http://www.omnisrv.com/sitemap"> Sitemap </a>
            </mj-text>
            <mj-text color="#979292" align="center"> Copyright © 2016 Omni. All rights reserved </mj-text>
            <mj-text align="center">
              Powered by <a text-decoration="underline"href="http://www.igreentechservices.com/?utm_medium=refferal&utm_source=omnisrv.com" text-decoration="underline">iGreenTech Services</a>
            </mj-text>
          </mj-column>
        </mj-section>
    <!-- Social media section -->

        <mj-section background-color="#8EAEBC">
            <mj-column>
              <mj-text padding-top="20px" mj-class="desc" align="center" font-size="15px" font-style="italic">Stay Connected</mj-text>
            </mj-column>
          </mj-section>

          <mj-section background-color="#8EAEBC" padding="0" padding-bottom="30px">
            <mj-group>
              <mj-column>
                <mj-image padding="5 10" width="25px" src="https://cdn3.iconfinder.com/data/icons/2018-social-media-black-and-white-logos/1000/2018_social_media_popular_app_logo_twitter-512.png" href="https://twitter.com/OMNIGlobal2016" />
              </mj-column>
              <mj-column>
                <mj-image padding="5 10" width="25px" src="https://cdn3.iconfinder.com/data/icons/2018-social-media-black-and-white-logos/1000/2018_social_media_popular_app_logo_facebook-512.png" href="https://www.facebook.com/OMNI2016/" />
              </mj-column>
              <mj-column>
                <mj-image padding="5 10" width="25px" src="https://cdn3.iconfinder.com/data/icons/2018-social-media-black-and-white-logos/1000/2018_social_media_popular_app_logo_instagram-512.png" href="https://www.instagram.com/omni_global_2016/?hl=en" />
              </mj-column>
              <mj-column>
                <mj-image padding="5 10" width="25px" src="https://cdn3.iconfinder.com/data/icons/2018-social-media-black-and-white-logos/1000/2018_social_media_popular_app_logo_linkedin-512.png" href="https://www.linkedin.com/company/omni-global-group?" />
              </mj-column>
              <mj-column>
                <mj-image padding="5 10" width="25px" src="https://cdn3.iconfinder.com/data/icons/2018-social-media-black-and-white-logos/1000/2018_social_media_popular_app_logo_youtube-512.png" href="https://www.youtube.com/channel/UCzzSzF3WQ_A8Gtfy9TFH-zw" />
              </mj-column>
            </mj-group>
          </mj-section>
      </mj-body>
    </mjml>


    """)


bc_label = tkinter.Label(text="Background Color HTML Code: ")
bc_label.grid(row=0,column=0)
bc_entry = tkinter.Entry()
bc_entry.grid(row=0,column=1)

pc_label = tkinter.Label(text=" Background Color HTML Code: ")
pc_label.grid(row=0,column=2)
pc_entry = tkinter.Entry()
pc_entry.grid(row=0,column=3)

h_label = tkinter.Label(text="Headline: ")
h_label.grid(row=4,column=0)
h_entry = tkinter.Entry()
h_entry.grid(row=4,column=1)

hs_label = tkinter.Label(text="Headline Font Size (pixels): ")
hs_label.grid(row=5,column=0)
hs_entry = tkinter.Entry()
hs_entry.grid(row=5,column=1)

b_label = tkinter.Label(text="Button 1: ")
b_label.grid(row=6,column=0)
b_entry = tkinter.Entry()
bl_entry = tkinter.Entry()
b_entry.grid(row=6,column=1)
bl_entry.grid(row=6, column=2)
b_entry.insert(0, "Text")
bl_entry.insert(0, "Link")

bb_label = tkinter.Label(text="Button 2: ")
bb_label.grid(row=7,column=0)
bb_entry = tkinter.Entry()
bbl_entry = tkinter.Entry()
bb_entry.grid(row=7,column=1)
bbl_entry.grid(row=7,column=2)
bb_entry.insert(0, "Text")
bbl_entry.insert(0, "Link")

bbb_label = tkinter.Label(text="Button 3: ")
bbb_label.grid(row=8,column=0)
bbb_entry = tkinter.Entry()
bbbl_entry = tkinter.Entry()
bbb_entry.grid(row=8,column=1)
bbbl_entry.grid(row=8,column=2)
bbb_entry.insert(0, "Text")
bbbl_entry.insert(0, "Link")


ft_text = tkinter.Label(text="Initial Text: ")
ft_text.grid(row=9,column=0)
ft_entry = tkinter.Entry()
ft_entry.grid(row=9,column=1)

fts_text = tkinter.Label(text="First Feature: ")
fts_text.grid(row=10,column=0)
fts_entry = tkinter.Entry()
fts_entry.grid(row=10,column=1)
fts_entry.insert(0,"Text")
firstfeatureimage_entry = tkinter.Entry()
firstfeatureimage_entry.grid(row=10,column=2)
firstfeatureimage_entry.insert(0,"Image Link")

ftss_text = tkinter.Label(text="Second Feature: ")
ftss_text.grid(row=11,column=0)
ftss_entry = tkinter.Entry()
ftss_entry.grid(row=11,column=1)
ftss_entry.insert(0,"Text")
secondfeatureimage_entry = tkinter.Entry()
secondfeatureimage_entry.grid(row=11,column=2)
secondfeatureimage_entry.insert(0,"Image Link")

ftsss_text = tkinter.Label(text="Closing Text: ")
ftsss_text.grid(row=12,column=0)
ftsss_entry = tkinter.Entry()
ftsss_entry.grid(row=12,column=1)

send = tkinter.Button(text="Generate MJML",command=gen)
send.grid(row=20,column=0)

root.mainloop()
