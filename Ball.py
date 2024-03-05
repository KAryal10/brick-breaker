import pygame

WIDTH= 1280
HEIGHT = 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Ball:
  def __init__ (self,xPos,yPos, radius, speed, color):
    self.xPos, self.yPos, self.radius = xPos, yPos, radius
    self.speed = speed
    self.color= color
    self.xFac, self.yFac = 1 , 1
    self.ball = pygame.draw.circle(screen, self.color, (self.xPos,self.yPos), self.radius)

  def display(self):
    self.ball = pygame.draw.circle(screen, self.color, (self.xPos,self.yPos), self.radius)

  def update(self):
    self.xPos += self.xFac*self.speed
    self.yPos += self.yFac*self.speed

    #setting vertical boundary on the screen for the ball
    if self.xPos <=0 or self.xPos >= WIDTH:
      self.xFac *= -1

    #setting upper boundary on the creen for the ball
    if self.yPos<=0:
      self.yFac *= -1

    if self.yPos >= HEIGHT:
      return True

    return False

  def reset(self):
    self.xPos = WIDTH
    self.yPos = HEIGHT
    self.xFac, self.yFac = -1,-1

  def hit(self):
    self.yFac *= -1

  def getRect(self):
    return self.ball
      
