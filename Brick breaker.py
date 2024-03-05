#importing necessary packages
import pygame
import random
from Ball import Ball
from StrikerClass import Striker
from Block import Block

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
pygame.display.set_caption("Break the block")

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
            blockList.append(Block(i,j,blockHeight,blockWidth, random.choice([WHITE,GREEN,RED])))
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
                    return True


def main():
    isRunning = True
    lives = 5
    score = 0
    scoreText= pygame.font.render("score", True, WHITE)
    scoreTextRect = scoreText.get_rect()
    scoreTextRect.center = (20, HEIGHT-10)

    livesText = pygame.font.render("Lives", True, RED) 
    livesTextRect = livesText.get_rect() 
    livesTextRect.center = (WIDTH-120, HEIGHT-10) 

    striker = Striker(0, HEIGHT-50, 100, 20, 10, WHITE)
    strikerXFac = 0

    ball = Ball(0, HEIGHT-100, 8, 5, WHITE)

    blockWidth, blockHeight = 30, 10
    horizontalSpace, verticalSpace = 15, 15
    blockList= populateBlock(blockWidth, blockHeight, horizontalSpace, verticalSpace)


    while running:
        screen.fill(BLACK) 
        screen.blit(scoreText, scoreTextRect) 
        screen.blit(livesText, livesTextRect) 

        scoreText = pygame.font.render("Score : " + str(score), True, WHITE) 
        livesText = pygame.font.render("Lives : " + str(lives), True, RED)

        if not listOfBlocks: 
            listOfBlocks = populateBlock(blockWidth, blockHeight, horizontalSpace, verticalSpace)

        if lives <= 0: 
            running = gameOver() 
  
            while listOfBlocks: 
                listOfBlocks.pop(0) 
  
            lives = 5
            score = 0
            listOfBlocks = populateBlock(blockWidth, blockHeight, horizontalSpace, verticalSpace)

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT: 
                    strikerXFac = -1
                if event.key == pygame.K_RIGHT: 
                    strikerXFac = 1
            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                    strikerXFac = 0
                    
        if(collisionCheck(striker.getRect(), ball.getRect())): 
            ball.hit() 
        for block in listOfBlocks: 
            if(collisionCheck(block.getRect(), ball.getRect())): 
                ball.hit() 
                block.hit() 
  
                if block.getHealth() <= 0: 
                    listOfBlocks.pop(listOfBlocks.index(block)) 
                    score += 10
                    
        striker.update(strikerXFac) 
        lifeLost = ball.update() 
  
        if lifeLost: 
            lives -= 1
            ball.reset() 
            print(lives) 

        striker.display() 
        ball.display() 

        for block in listOfBlocks: 
            block.display() 
  
        pygame.display.update() 
        clock.tick(FPS) 
