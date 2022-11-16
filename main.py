import pygame
import sys
import random
from pygame.locals import *
import random
import math
pygame.init()

#images
map = pygame.image.load('pixilart-drawing.png')
apple_image = pygame.image.load('pixilart-drawing (1).png')

# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
font = pygame.font.SysFont("comicsans", 30, True, True)
pygame.display.set_caption('Snake!')



#def play_again(answer):
  #return None
def apple_spawn(body):
  numList = []
  for i in range(50,501):
    numList.append(i)
  for i in range(800):
    aValue = 1
    bValue = 1
    xValue = random.randint(50,425)
    yValue = random.randint(50,425)

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
    for coords in body:
      if cordinates[0] == coords[0] and cordinates[1] == coords[1]:
        xValue += 25
        yValue += 25
      cordinates = [xValue, yValue]
    for coords in body:
      if cordinates[0] == coords[0] and cordinates[1] == coords[1]:
        continue
    if cordinates[0] in numList and cordinates[1] in numList:
       return cordinates
  return cordinates

def check_death(body, x, y):
  if x < 50 or x > 525:
    return 1
  
  if y < 50 or y > 525:
    return 1
  
  for coords in body:
    if coords[0] == x and coords[1] == y:
      return 1
    
  return 0
def add_body(body, x, y):
  body_color = 50
  for coords in body:
    pygame.draw.rect(WINDOW, (0, 0, body_color), (coords[0], coords[1], 25, 25))
    body_color += 10
    if body_color > 200:
      body_color = 50
def redrawGameWindow():
   
    WINDOW.blit(map, (50,50))
    pygame.display.update()
    
def movement_boundaries(x, y, width, height, vel):
  directionX = 0
  directionY = 0
  loop = True
  body = []
  cordinates = apple_spawn(body)
  print(cordinates)
  snakeLength = 0
  score = 0
  text = font.render("Score: " + str(score), 1, (0, 255, 255))
  looping = True
  while looping:
    fpsClock.tick(30)
    pygame.time.delay(90)
    redrawGameWindow()
    
    if check_death(body, x, y) == 1:
      looping = False
      
    for event in pygame.event.get():
      if event.type == QUIT:
        looping = False
        
    head = []
    head.append(x)
    head.append(y)
    body.append(head)
    add_body(body, x, y)
  
    # Movement and Boundaries    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
      directionX = -25
      directionY = 0
    elif keys[pygame.K_RIGHT] and x < WINDOW_WIDTH - width:
      directionX = +25
      directionY = 0
    elif keys[pygame.K_UP] and y > 0:
      directionY = -25
      directionX = 0
    elif keys[pygame.K_DOWN] and y < WINDOW_HEIGHT - height:
      directionY = +25
      directionX = 0

      
    if len(body) > snakeLength:
      del body[0]
    
      
    text = font.render("Score: " + str(score), 1, (0, 255, 255))
    WINDOW.blit(text, (0,10))
    WINDOW.blit(apple_image, (cordinates[0],cordinates[1]))
    x += directionX
    y += directionY
    pygame.display.update()
    
    if x == cordinates[0] and y == cordinates[1]:
      cordinates = apple_spawn(body)
      print(cordinates)
      snakeLength += 1
      score += 1
      WINDOW.fill(pygame.Color("black"))
  #while loop:
  #  for event in pygame.event.get():
  #    if event.type == QUIT:
  #      loop = False
  #  play_again(answer)  
  #  pygame.display.update()
     #Snake touches border, you lose screen,show score
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