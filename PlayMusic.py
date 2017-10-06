#!/usr/bin/env python
#-*- cording: utf-8 -*-
# https://www.pygame.org/docs/ref/music.html
#Create by KanameTakano
import pygame.mixer
from mutagen.mp3 import MP3
import time

def PlayMusic(file, fade):
    pygame.mixer.init()
    pygame.mixer.music.load(file) #selct musisc file
    pygame.mixer.music.play() #play
    pygame.mixer.music.fadeout((int(MP3(file).info.length) * 1000) - fade) #ms 500ms fadeout
    time.sleep(MP3(file).info.length)

if __name__ == '__main__':
    PlayMusic("myMusic/test.mp3", 500)
