import pygame

class Striker:
  def __init__ (self, xPos, yPos, width,height, speed, color):
    self.xPos,self.yPos,self.width,self.height=xPos,yPos,width,height
    self.speed=speed
    self.color=color

    #Rect variable which stores coordinates of striker
    self.strikerRect=pygame.Rect(self.xPos, self.yPos, self.width, self.height)
    self.striker= pygame.draw.recct(screen,self.color,self.strikerRect)

  #display object on screen
  def display(self):
    self.striker= pygame.draw.recct(screen,self.color,self.strikerRect)

  #updating striker Object
  def update(self, xFac):
    self.xPos =+ self.speed*xFac

    #placing striker inside screen
    if self.xPos<=0:
      self.xPos=0
    elif self.xPos+self.width>=WIDTH:
      self.xPos=Width-self.width

    self.strikerRect= pygame.Rect(self.xPos, self.yPos, self.width, self.height)

  def getRect(self):
    return self.strikerRect
