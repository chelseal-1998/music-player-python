from tkinter import *
import pygame
import os

window = Tk()
window.geometry("400x200")

label1=Label(window,text="Music player", font="times 20")
label1.grid(row=1,column=1)

pygame.mixer.init()

def ply():
    pygame.mixer.music.load('positions - Ariana Grande.wav')
    pygame.mixer.music.play()

def pse():
    pygame.mixer.music.pause()

def unpse():
    pygame.mixer.music.unpause()

def stop():
    pygame.mixer.music.stop()



play_button = Button(window , text="Play Button", command=ply)
pause_button = Button(window, text="Pause Button", command=pse)
unpause_Button = Button(window , text="Unpause Button",command=unpse)
stop_Button = Button(window, text="Stop Button" , command=stop)

stop_Button.grid()
unpause_Button.grid()
pause_button.grid()
play_button.grid()

songs_list = os.listdir()
songs_listbox=StringVar(window)
songs_listbox.set("select songs")
menu=OptionMenu(window, songs_listbox,songs_list)
menu.grid(row=4, column=4)

window.mainloop()
