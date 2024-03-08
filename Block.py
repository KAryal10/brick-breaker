import pygame

WHITE= (255, 255, 255)
BLACK= (0, 0, 0)
RED= (255, 0, 0)
GREEN= (0, 255, 0)
WIDTH= 1280
HEIGHT = 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Block:
  def __init__(self, xPos, yPos, height, width, color):
    self.xPos, self.yPos,self.width, self.height = xPos, yPos, width, height
    self.color = color
    self.damage = 1

    if color==WHITE:
      self.health=1
    elif color== GREEN:
      self.health=2
    else:
      self.health=3

    #Rect variable of block
    self.blockRect= pygame.Rect(self.xPos, self.yPos, self.width, self.height)
    self.block= pygame.draw.rect(screen,self.color,self.blockRect)

  #to display block on the screen
  def display(self):
    if self.health>0:
      self.block = pygame.draw.rect(screen, self.color, self.blockRect)

  def hit(self):
    self.health -=self.damage
    if self.health==2:
      self.color = GREEN
    elif self.health==1:
      self.color=WHITE

  def getRect(self):
    return self.blockRect

  def getHealth(self):
    return self.health
    
    
