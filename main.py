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
apple_image = pygame.image.load('pixilart-drawing (1).png')

# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake!')

def apple_spawn():
    aValue = 1
    bValue = 1
    xValue = random.randint(50,500)
    yValue = random.randint(50,500)
    
    if xValue < 25:
      aValue = 0
    if yValue < 25:
      bValue = 0
      
    value = xValue % 25
    value = 25 - value
    for j in range(value):
      xValue += 1
      
    secondValue = yValue % 25
    secondValue = 25 - secondValue
    for j in range(secondValue):
      yValue += 1
      
    if aValue == 0:
      xValue = 0
    if bValue == 0:
      yValue = 0
      
    cordinates = [xValue, yValue]
    return cordinates

def snake_touch_apple(x, y):
  xPos = x - 25
  yPos = y - 25
  snake_cords = [xPos, yPos]
  return snake_cords


def redrawGameWindow():
   
    WINDOW.blit(map, (50,50))
    pygame.display.update()
    
def movement_boundaries(x, y, width, height, vel):
  cordinates = apple_spawn()
  print(cordinates)
  char = False
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
    apple = WINDOW.blit(apple_image, (cordinates[0],cordinates[1]))
    pygame.display.update()
    
    if char == True:
      pygame.draw.rect(WINDOW, (0, 0, 255), (x - 25, y - 25, 25, 25))
    snake_touch_apple(x, y)
    if player.colliderect(apple):
      cordinates = apple_spawn()
      print(cordinates)
      char = True
      
      
  
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