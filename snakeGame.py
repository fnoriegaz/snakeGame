#snakeGame by fnoriega
import pygame
from random import *

#initialize and define env
pygame.init()
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WIDTH=800
HEIGHT=600
BGCOLOUR = WHITE

BUTTONWIDTH = 64
BUTTONHEIGHT = 32
STARTXPOS = round(WIDTH/4)
STARTYPOS = round(HEIGHT/4)

LOWSPEED = 3200000
MIDDLESPEED1 = 2200000
MIDDLESPEED2 = 1500000
FASTSPEED = 1000000

gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('SnakeGame by fnoriega')
gameDisplay.fill(BGCOLOUR)

class GameTile(object):
    def __init__(self):
        self.textFont = pygame.font.Font('freesansbold.ttf',64)
        self.text = "SNAKE GAME"
        self.textSurface = self.textFont.render(self.text, True, BLUE, BGCOLOUR)

    def drawTitle(self):
        gameDisplay.blit(self.textSurface, (round(WIDTH/4),round(HEIGHT/2)))

class Button(object):
    def __init__(self, text, xpos, ypos, colour=BLACK):
        self.xpos = xpos
        self.ypos = ypos
        self.colour = colour
        self.textFont = pygame.font.Font('freesansbold.ttf',round(BUTTONWIDTH/2))
        self.text = text
        self.textSurface = self.textFont.render(self.text, True, self.colour, BGCOLOUR)

    def drawButton(self):
        gameDisplay.blit(self.textSurface, (self.xpos,self.ypos))



class Cube(object):
    def __init__(self,cubeW, cubeH):
        self.xpos = randint(0,WIDTH)
        self.ypos = randint(0,HEIGHT)
        self.cubeW = cubeW
        self.cubeH = cubeH

    def drawCube(self,xpos,ypos,COLOUR):
        pygame.draw.rect(gameDisplay, BGCOLOUR, (self.xpos,self.ypos,self.cubeW,self.cubeH))
        self.xpos = xpos
        self.ypos = ypos
        pygame.draw.rect(gameDisplay, COLOUR, (self.xpos,self.ypos,self.cubeW,self.cubeH))



class Snake(Cube):
    def __init__(self,snakeW,snakeH):
        self.size=1
        self.body =[[0,0]]
        Cube.__init__(self,snakeW,snakeH)

    def checkSelfCollide(self):
        for i in range(1,self.size):
            if self.body[0][0] == self.body[i][0] and self.body[0][1] == self.body[i][1]:
                return True

    def drawSnake(self,xpos,ypos,COLOUR,hasEaten):
        if hasEaten:
            for i in range(self.size):
                pygame.draw.rect(gameDisplay, BGCOLOUR, (self.body[i][0],self.body[i][1],self.cubeW,self.cubeH))

            self.size += 1
            self.body.insert(0,[xpos,ypos])

            for i in range(self.size):
                if i==0:
                    pygame.draw.rect(gameDisplay, WHITE, (self.body[i][0],self.body[i][1],self.cubeW,self.cubeH))
                else:
                    pygame.draw.rect(gameDisplay, COLOUR, (self.body[i][0],self.body[i][1],self.cubeW,self.cubeH))

        else:
            for i in range(self.size):
                pygame.draw.rect(gameDisplay, BGCOLOUR, (self.body[i][0],self.body[i][1],self.cubeW,self.cubeH))

            self.body.insert(0,[xpos,ypos])
            self.body.pop()
            for i in range(self.size):
                if i==0:
                    pygame.draw.rect(gameDisplay, RED, (self.body[i][0],self.body[i][1],self.cubeW,self.cubeH))
                else:
                    pygame.draw.rect(gameDisplay, COLOUR, (self.body[i][0],self.body[i][1],self.cubeW,self.cubeH))
        return self.size



running = False
startButton = Button("START", STARTXPOS, STARTYPOS, GREEN)
quitButton = Button("QUIT", WIDTH - STARTXPOS - round(BUTTONWIDTH/2), STARTYPOS, RED)
startButton.drawButton()
quitButton.drawButton()
startL = STARTXPOS - BUTTONWIDTH/4
startR = STARTXPOS + BUTTONWIDTH + BUTTONWIDTH/2
startT = STARTYPOS - BUTTONHEIGHT/4
startB = STARTYPOS + BUTTONHEIGHT + BUTTONHEIGHT/2

quitL = WIDTH - STARTXPOS - round(BUTTONWIDTH/2) - BUTTONWIDTH/4
quitR = WIDTH - STARTXPOS - round(BUTTONWIDTH/2) - BUTTONWIDTH/4 + BUTTONWIDTH + BUTTONWIDTH/2
quitT = STARTYPOS - BUTTONHEIGHT/4
quitB = STARTYPOS + BUTTONHEIGHT + BUTTONHEIGHT/2

title = GameTile()
title.drawTitle()

startScreen = True
while startScreen:

    for event in pygame.event.get():
        mouseX, mouseY = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouseX>(startL) and mouseX<(startR):
                if mouseY>(startT) and mouseY<(startB):
                    running = True
                    startScreen = False

            if mouseX>(quitL) and mouseX<(quitR):
                if mouseY>(quitT) and mouseY<(quitB):
                    running = False
                    startScreen = False

        if event.type == pygame.QUIT:
            running = False
            startScreen = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running=False
                startScreen = False
    pygame.display.update()

gameDisplay.fill(BGCOLOUR)

cubeW=20
cubeH=20
cubeCOLOUR=BLACK
cube = Cube(cubeW,cubeH)
cubeXpos = range(0,WIDTH,cubeW)[randint(0,WIDTH/cubeW-1)]
cubeYpos = range(0,HEIGHT,cubeH)[randint(0,HEIGHT/cubeH-1)]
cube.drawCube(cubeXpos,cubeYpos,cubeCOLOUR)

snakeCOLOUR = BLUE
snake = Snake(cubeW,cubeH)
snakeXpos = range(0,WIDTH,cubeW)[randint(0,WIDTH/cubeW-1)]
snakeYpos = range(0,HEIGHT,cubeH)[randint(0,HEIGHT/cubeH-1)]
snake.drawSnake(snakeXpos,snakeYpos,snakeCOLOUR,False)


dx=0
dy=0
points=1
snakeSpeed = LOWSPEED
while running:

    if points>10:
        snakeSpeed = MIDDLESPEED1
    if points>20:
        snakeSpeed = MIDDLESPEED2
    if points>30:
        snakeSpeed = FASTSPEED

    for i in range(snakeSpeed):
        a=1

    snakeXpos+=dx
    snakeYpos+=dy
    points=snake.drawSnake(snakeXpos,snakeYpos,snakeCOLOUR,False)
    if snake.checkSelfCollide():
        running = False
    cube.drawCube(cubeXpos,cubeYpos,cubeCOLOUR)

    if snakeXpos<0 or snakeXpos>(WIDTH-round(cubeW/2)):
        running = False

    if snakeYpos<0 or snakeYpos>(HEIGHT-round(cubeH/2)):
        running = False

    if snakeXpos==cubeXpos and snakeYpos==cubeYpos:
        points=snake.drawSnake(snakeXpos,snakeYpos,snakeCOLOUR,True)
        cubeXpos = range(0,WIDTH,cubeW)[randint(0,WIDTH/cubeW-1)]
        cubeYpos = range(0,HEIGHT,cubeH)[randint(0,HEIGHT/cubeH-1)]
        cube.drawCube(cubeXpos,cubeYpos,cubeCOLOUR)




    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx=-cubeW
                dy=0
            if event.key == pygame.K_RIGHT:
                dx=+cubeW
                dy=0
            if event.key == pygame.K_UP:
                dx=0
                dy=-cubeH
            if event.key == pygame.K_DOWN:
                dx=0
                dy=cubeH
            if event.key == pygame.K_SPACE:
                dx=0
                dy=0
            if event.key == pygame.K_TAB:
                if randint(1,2)==1:
                    dx=cubeW
                else:
                    dx=-cubeW

                if randint(1,2)==1:
                    dy=cubeH
                else:
                    dy=-cubeH

        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running=False



    pygame.display.update()
