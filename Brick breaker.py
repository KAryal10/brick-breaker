#importing necessary packages
import pygame
import random

pygame.init()

#setting up variable for the dimension of screen
WIDTH= 1280
HEIGHT = 750

#Colors needed in the game
WHITE= (255, 255, 255)
BLACK= (0, 0, 0)
RED= (255, 0, 0)
GREEN= (0, 255, 0)

#setting up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.dsiplay.set_caption("Break the block")

#for the frame rate control
clock= pygame.time.Clock()
FPS=30

#to check collision
def collisionCheck(block,ball):
    if pygame.Rect.colliderect(block,ball):
        return True
    return False

#Populate list of blocks on screen
def populateBlock(blockWidth,blockHeight, horizontalSpace, verticalSpace):
    blockList=[]
    for i in range(0, WIDTH, horizontalSpace+blockWidth):
        for j in range(0, HEIGHT//2, verticalSpace+blockHeight):
            blockList.append(Block(i,j,blockHeight,blockWidth, random.choice([WHITE,GREEN,RED])
    return blockList

#function to implement when the game is over
def gameOver():
    isOver= True
    while isOver:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    return true


                
