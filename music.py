import pygame
import os

pygame.init() #Initialized all pygame modules. Essential to call this before using any Pygame functino
pygame.mixer.init()

window = pygame.display.set_mode((500, 300)) # Creates a window with size 500 pixels and 300 pixels tall
pygame.display.set_caption("Music Player") # Sets title of window

# Set Up Colors
PINK = (255, 182, 193)
GREEN = (0, 255, 0)

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

# Loop keeps application running
running = True
while running:
  for event in pygame.event.get(): # Retrieves a list of all events that occured since the last time the loop ran
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.MOUSEBUTTONDOWN: # Mouse Button clic
      mouse_x, mouse_y = pygame.mouse.get_pos() # Returns position of mouse cursor when the button was clicked
      if button_x < mouse_x < button_x + button_width and button_y < mouse_y < button_y + button_height: # Checks if mouse click happened inside the bounds of the play button
        play_music()

# Fill the window with white
  window.fill(PINK)

  pygame.draw.rect(window, GREEN, (button_x, button_y, button_width, button_height))
  font = pygame.font.Font(None, 36)
  text = font.render("Play Music", True, PINK)
  window.blit(text, (button_x + 20, button_y + 10))

  pygame.display.update()

pygame.quit()

