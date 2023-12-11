import pygame
import tkinter
from tkinter.filedialog import askdirectory
import os

class MusicPlayerGUI:
    def __init__(self):
        self.player = tkinter.Tk()
        self.player.title("Music Player")
        self.player.geometry("310x250")
        
        self.var = tkinter.StringVar()
        self.var.set("Select the song to play")
        
        os.chdir(askdirectory())
        self.songlist = os.listdir()
        
        self.playing = tkinter.Listbox(self.player, font="Helvetica 12 bold", width=28, bg="black", fg="white", selectmode=tkinter.SINGLE)
        
        for item in self.songlist:
            self.playing.insert(0, item)
        
        pygame.init()
        pygame.mixer.init()
        
    def run(self):
        text = tkinter.Label(self.player, font="Helvetica", textvariable=self.var).grid(row=0, columnspan=3)
        self.playing.grid(columnspan=3)
        
        player_buttons = MusicPlayerButtons(self.player, self.playing, self.var)
        player_buttons.setup_buttons()
        
        self.player.mainloop()

class MusicPlayerButtons:
    def __init__(self, player, playing, var):
        self.player = player
        self.playing = playing
        self.var = var
        
    def play(self):
        pygame.mixer.music.load(self.playing.get(tkinter.ACTIVE))
        name = self.playing.get(tkinter.ACTIVE)
        self.var.set(f"{name[:16]}..." if len(name) > 18 else name)
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def resume(self):
        pygame.mixer.music.unpause()

    def setup_buttons(self):
        playB = tkinter.Button(self.player, width=7, height=1, font="Helvetica", text="Play", command=self.play, bg="lightgreen").grid(row=2, column=0)
        pauseB = tkinter.Button(self.player, width=7, height=1, font="Helvetica", text="Pause", command=self.pause, bg="lightblue", fg="black").grid(row=2, column=1)
        resumeB = tkinter.Button(self.player, width=9, height=1, font="Helvetica", text="Resume", command=self.resume, bg="lightpink", fg="black").grid(row=2, column=2)

class MusicPlayerDataLoader:
    def __init__(self):
        pass
    # You can add methods here to load song data if necessary.

if __name__ == "__main__":
    gui = MusicPlayerGUI()
    gui.run()
