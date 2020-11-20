from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter import messagebox


class MusicPlayer:

    def __init__(self, root):
        root.geometry('510x280'), root.title('Mp3 Player')
        self.select_song = Button(root, text='Select Song', width=10, command=self.select_song1, bg='grey')
        self.play = Button(root, text='Play', width=10, command=self.play1, bg='yellow')
        self.pause = Button(root, text='Pause', width=10, command=self.pause1, bg='blue')
        self.stop = Button(root, text='Stop', width=10, command=self.stop1, bg='green')
        self.song_list = Listbox(root, width=30, height=15).grid(column=4)
        self.select_song.grid(column=0, row=1), self.play.grid(column=1, row=1), self.pause.grid(column=2,
                                                                                                 row=1), self.stop.grid(
            column=3, row=1)

        self.music_file = False
        self.playing_state = False


def select_song1(self):
    self.music_file = filedialog.askopenfilename()


def play1(self):
    if self.music_file:
        mixer.init()
        mixer.music.load(self.music_file)
        mixer.music.play()
    else:
        messagebox.showinfo(title=None, message='Load a song')


def pause1(self):
    if not self.playing_state:
        mixer.music.pause()
        self.playing_state = True
    else:
        mixer.music.unpause()
        self.playing_state = False


def stop1(self):
    mixer.music.stop()


root = Tk()
root.config(bg='cyan')
app = MusicPlayer(root)
root.mainloop()
