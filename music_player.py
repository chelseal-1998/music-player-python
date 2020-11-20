from tkinter import *
from pygame import mixer
from tkinter import filedialog

root = Tk()
root.title("Music player")
root.geometry("263x150")
root.config(bg="black")


def play():
    root.file = filedialog.askopenfilename(filetypes=(("wav files", "*.wav"), ("all files", "*.*")))
    mixer.init()
    mixer.music.load(root.file)
    mixer.music.play()


play_button = Button(root, text="play", command=play , bg="green")
play_button.grid(row=1 , column=0)


def pause():
    mixer.music.pause()

pse_button = Button(root, text="pause" , command=pause , bg="yellow")
pse_button.grid(row=1 , column=1)

def unpause():
    mixer.music.unpause()

unpause_button = Button(root, text="unpause" , command=unpause , bg="light blue")
unpause_button.grid(row=1 , column=2)

def stop():
    mixer.music.stop()

stop_button = Button(root , text="stop" , command= stop , bg="red")
stop_button.grid(row=1 , column=3)

stop_button.grid()
unpause_button.grid()
pse_button.grid()
play_button.grid()
root.mainloop()
