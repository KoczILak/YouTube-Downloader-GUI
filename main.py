import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

def path():
    global save_path
    save_path = filedialog.askdirectory()

def Download_Video():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download(save_path)
    tk.Label(window, text='Your Video is downloaded!', font='arial 15', fg="White", bg="#EC7063").place(x=10, y=255)

window = tk.Tk()
window.geometry("600x300")
window.config(bg="#EC7063")
window.resizable(width=False, height=False)
window.title('YouTube Video Downloader')

link = tk.StringVar()
tk.Label(window, text='                   Youtube Video Downloader                    ', font='arial 20 bold', fg="White", bg="Black").pack()
tk.Label(window, text='Paste Your YouTube Link Here:', font='arial 20 bold', fg="Black", bg="#EC7063").place(x=5, y=60)
tk.Label(window, text='Select Your Path Here:', font='arial 20 bold', fg="Black", bg="#EC7063").place(x=5, y=150)

link_enter = tk.Entry(window, width=53, textvariable=link, font='arial 15 bold', bg="lightgreen").place(x=5, y=100)

tk.Button(window, text='CHOOSE YOUR SAVE PATH', font='arial 15 bold', fg="white", bg='black', padx=2, command=path).place(x=150, y=200)
tk.Button(window, text='DOWNLOAD VIDEO', font='arial 15 bold', fg="white", bg='black', padx=2, command=Download_Video).place(x=385, y=255)

window.mainloop()