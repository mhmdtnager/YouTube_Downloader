from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("500x300")
root.resizable(0,0)
root.title("YouTube Video Downloader")

Label(root , text="Youtube Donloader",font="arial 15 bold").pack()
link = StringVar()
Label(root , text="Past Link Here",font="arial 15 bold").place(x=160 , y=60)
link_enter = Entry(root, width=70 ,textvariable=link).place(x=32 , y=90)


def high():
    video = YouTube(str(link.get()))
    video.streams.get_highest_resolution().download()
    Label(root , text="DOWNLOADED",font="arial 15 bold").place(x=180 , y=210)

Button(root , text="High resolution",font="arial 15 bold" , bg="red",padx=2 ,command=high ,foreground="white").place(x=150 , y=150)

def low():
    video = YouTube(str(link.get()))
    video.streams.get_lowest_resolution().download()
    Label(root , text="DOWNLOADED",font="arial 15 bold").place(x=180 , y=210)

Button(root , text="Low resolution",font="arial 15 bold" , bg="blue",padx=4 ,command=low , foreground="white" ).place(x=150 , y=200)

def audio_only():
    video = YouTube(str(link.get()))
    video.streams.get_audio_only().download()
    Label(root , text="DOWNLOADED",font="arial 15 bold").place(x=180 , y=210)

Button(root , text="Only Audio",font="arial 15 bold" , bg="yellow",padx=22 ,command=audio_only ).place(x=150 , y=250)

root.mainloop()