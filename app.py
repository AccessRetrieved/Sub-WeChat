from tkinter import *
import subprocess
import tkmacosx

root = Tk()
root.geometry('300x300')
root.title("Wechat Launcher")

def l():
    subprocess.call(['open', '/Applications/WeChat.app/Contents/MacOS/WeChat'])

launch = tkmacosx.Button(root, text='Launch Sub-Wechat', borderless=1, activebackground='black', activeforeground='white', command=l, width=200, height=100)
launch.place(relx=0.5, rely=0.5, anchor=CENTER)


root.mainloop()