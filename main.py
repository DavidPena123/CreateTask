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

def add_body(body):
  for coords in body:
    pygame.draw.rect(WINDOW, (0, 0, 255), (coords[0], coords[1], 25, 25))

def redrawGameWindow():
   
    WINDOW.blit(map, (50,50))
    pygame.display.update()
    
def movement_boundaries(x, y, width, height, vel):
  cordinates = apple_spawn()
  print(cordinates)
  snakeLength = 0
  body = []
  char = False
  looping = True
  while looping:
    fpsClock.tick(30)
    pygame.time.delay(90)
    redrawGameWindow()
    for event in pygame.event.get():
      if event.type == QUIT:
        looping = False
    head = []
    head.append(x)
    head.append(y)
    body.append(head)
    add_body(body)
  
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
      
    
    if len(body) > snakeLength:
      del body[0]
      
    WINDOW.blit(apple_image, (cordinates[0],cordinates[1]))
    pygame.display.update()
    
    if x == cordinates[0] and y == cordinates[1]:
      cordinates = apple_spawn()
      print(cordinates)
      snakeLength += 1
      
  
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