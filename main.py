import pygame
import sys
import random
from pygame.locals import *

pygame.init()


 
# Colours
BACKGROUND = (0, 0, 0)
 
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BLACK = (0, 0, 0)
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake!')

# The main function that controls the game
def main () :
  #Character Attributes
  x = 50
  y = 50
  width = 40
  height = 60
  vel = 5
  
  # The main game loop
  looping = True
  while looping :
    pygame.time.delay(50)

    for event in pygame.event.get() :
      if event.type == QUIT:
        looping = False
    
    # Movement and Boundaries    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > 0:
      x -= vel
      
    if keys[pygame.K_RIGHT] and x < WINDOW_WIDTH - width:
      x += vel
      
    if keys[pygame.K_UP] and y > 0:
      y -= vel
      
    if keys[pygame.K_DOWN] and y < WINDOW_HEIGHT - height:
      y += vel
      
      
    #Fills character movement  
    WINDOW.fill(BLACK)
      
    #Character
    pygame.draw.rect(WINDOW, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

    
 
main()