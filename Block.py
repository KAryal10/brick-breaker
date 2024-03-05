import pygame

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
    self.block= pygame.draw.rect(screen,self.color,self.bolckRect)

  #to display block on the screen
  def display(self):
    if self.health>0:
      self.block = pygame.draw.rect(screen, self.color, self.blockRect)

  def hit(self):
    self.health -=self.damage

  def getRect(self):
    return self.blockRect

  def getHealth(self):
    return self.health
    
    
