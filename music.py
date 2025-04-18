import pygame
import os

pygame.init() #Initialized all pygame modules. Essential to call this before using any Pygame functino

window = pygame.dsiplay.set_mode((500, 300)) # Creates a window with size 500 pixels and 300 pixels tall
pygame.display.set_caption("Music Player") # Sets title of window

# Set Up Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Sets music_file variable to path of the music file to play
music_file = "music.mp3" 

# Functions loads and plays the music
def play_music():
  pygame.mixer.music.load(music_file) # Loads the music file 
  pygame.mixer.music.play() # Starts playing loaded music

button_width = 150
button_height = 50
button_x = (500 - button_width) // 2
button_y = 100



