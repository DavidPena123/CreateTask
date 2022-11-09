import pygame
import sys
import random
from pygame.locals import *
import random
import math
pygame.init()

#images
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

def apple_spawn():
  
    xValue = random.randint(0,500)
    yValue = random.randint(0,500)
    value = xValue % 25
    value = 25 - value
    for j in range(value):
      xValue += 1
      
    secondValue = yValue % 25
    secondValue = 25 - secondValue
    for j in range(secondValue):
      yValue += 1
    cordinates = [xValue, yValue]
    return cordinates

def snake_touch_apple():
  xPos = 0
  yPos = 0
  if xPos == x and yPos == y:
    return True
  else:
    return False
  #if x,y touches apples position, delete apple and make a new one.

def redrawGameWindow():
   
    WINDOW.blit(map, (0,0))
    pygame.display.update()
    
def movement_boundaries(x, y, width, height, vel):
  cordinates = apple_spawn()
  print(cordinates)
  looping = True
  while looping:
    pygame.time.delay(120)
    redrawGameWindow()
    for event in pygame.event.get():
      if event.type == QUIT:
        looping = False
  
    # Movement and Boundaries    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
      x -= vel
      
    elif keys[pygame.K_RIGHT] and x < WINDOW_WIDTH - width:
      x += vel
       
    elif keys[pygame.K_UP] and y > 0:
      y -= vel
      
    elif keys[pygame.K_DOWN] and y < WINDOW_HEIGHT - height:
      y += vel
    
    player = pygame.draw.rect(WINDOW, (0, 0, 255), (x, y, 25, 25))
    WINDOW.blit(apple, (cordinates[0],cordinates[1]))
    pygame.display.update()
     
     #Snake collliding with apple, score + 1
     #Snake touches border, you lose screen,show score
     #Snake touches itself, you lose screen,show score
     #Press any button to start
    
def main () :
  #Character Attributes
  x = 100
  y = 100
  width = 25
  height = 25
  vel = 25
  redrawGameWindow()
  movement_boundaries(x, y, width, height, vel)

    
     
   


    
 
main()