from tkinter import *
from pytube import YouTube

def vidDownload():
    link=text1.get(1.0,END)
    print(link)
    gj=YouTube(str(link))
    stream = gj.streams.first()


   # Destination="/home/ganesh/Downloads"
   # print(Destination)
    text1.delete(1.0,END)
    text1.insert(INSERT,"Downloading in progress")
    stream.download()
    text1.delete(1.0,END)
    text1.insert(INSERT,"Downloding Successful")

root=Tk()
root.geometry("500x200")
root.title("Gj_Downloader")
label=Label(root,text="Video Link")
label.pack()
text1=Text(root,width=200,height=2,border=3)
text1.pack()
label2=Label(root,text="Destination")
label2.pack()
text2=Text(root,width=200,height=2,border=4)
text2.pack()
button=Button(root,text="Download",width=6,height=2,command=vidDownload)
button.pack()

root.mainloop()