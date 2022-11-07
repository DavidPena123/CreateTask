import pygame
import sys
import random
from pygame.locals import *
import random
import math
pygame.init()


map = pygame.image.load('pixilart-drawing.png')
snake = pygame.image.load('pixilart-drawing (2).png')
apple = pygame.image.load('pixilart-drawing (1).png')

# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake!')

def snake_touch_apple(xPos, yPos):
  xPos = x
  yPos = y
  #if x,y touches apples position, delete apple and make a new one.

def redrawGameWindow():
  
    WINDOW.blit(map, (0,0))
    WINDOW.blit(snake, (x,y))
    WINDOW.blit(apple, (125,125))
    pygame.display.update()

def main () :
  global x
  global y
  #Character Attributes
  x = 100
  y = 100
  width = 125
  height = 25
  vel = 5
  
  # The main game loop
  looping = True
  while looping :
    pygame.time.delay(30)

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
    redrawGameWindow()

       #Snake collliding with apple, score + 1
       #Snake touches border, you lose screen,show score
       #Snake touches itself, you lose screen,show score
       #Press any button to start
    
 
main()