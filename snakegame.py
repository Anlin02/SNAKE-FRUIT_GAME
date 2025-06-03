# step 1 import libraries
import pygame
import sys #used to exit the game
import random


# step 2 initialise the pygame and set up display
pygame.init()

WIDTH=600
HEIGHT=600
CELL_SIZE=20

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake Game")

# step 3:colors and clock
WHITE =(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
BLACK=(0,0,0)

clock=pygame.time.Clock() #controls games speed(helps to control fram rate
font=pygame.font.SysFont(None,36)
# step 4 define snake and fruit
snake=[(100,100),(90,100),(80,100)]
snakedirection="RIGHT"
#make a boundary rect
food=(random.randrange(0,WIDTH//CELL_SIZE)*CELL_SIZE
      ,random.randrange(0,HEIGHT//CELL_SIZE)*CELL_SIZE)
score = 0

# step 5:draw snake and food
def drawsnake(snake):
    for cellblock in snake:
        pygame.draw.rect(screen,GREEN,pygame.Rect(cellblock[0],cellblock[1],CELL_SIZE,CELL_SIZE))
def drawfood(food):
    pygame.draw.rect(screen,RED,pygame.Rect(food[0],food[1],CELL_SIZE,CELL_SIZE))
def drawscore(score):
    score_surface=font.render(f"Score:{score}",True,WHITE)
    screen.blit(score_surface,(10,10))
# step 6 move the snake
def snakemovement(snake,snakedirection):
    global food,score
    headX,headY=snake[0]

    if snakedirection=="UP":
        newhead=(headX,headY-CELL_SIZE)
    elif snakedirection=="DOWN":
        newhead=(headX,headY+CELL_SIZE)
    elif snakedirection=="RIGHT":
        newhead=(headX+CELL_SIZE,headY)
    elif snakedirection=="LEFT":
        newhead=(headX-CELL_SIZE,headY)

    snake.insert(0,newhead)
    if newhead==food:
        food = (random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE
                , random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE)
        score=score+1
        return True
    else:
        snake.pop()
        return False

def collision(snake):
    head=snake[0]
    # collision with walls
    if head[0]<0 or head[0]>WIDTH or head[1]<0 or head[1]>=HEIGHT:
        return True
    # collision with itself
    if head in snake[1:]:
        return True
    return False
def showgameover():
    screen.fill(BLACK)


    score_surface = font.render(f"Score:{score}", True, WHITE)
    screen.blit(score_surface, (WIDTH//2-100,HEIGHT//3+40))
    game_over_t=font.render("Game Over!..",True,RED)
    screen.blit(game_over_t,(WIDTH//2-70,HEIGHT//3))

    restart_button=pygame.Rect(WIDTH//2-100,HEIGHT//2,200,40)
    exit_button=pygame.Rect(WIDTH//2-100,HEIGHT//2+60,200,40)

    pygame.draw.rect(screen,GREEN,restart_button)
    pygame.draw.rect(screen,GREEN,exit_button)

    restart_text=font.render("Restart",True,WHITE)
    exit_text=font.render("EXIT",True,WHITE)

    screen.blit(restart_text,(restart_button.x+60,restart_button.y+8))
    screen.blit(exit_text,(exit_button.x+75,exit_button.y+8))

    pygame.display.flip()
    return restart_button,exit_button

# step 4 main game loop
running =True
game_over=False

while running:
    # fill in the screen
    if not game_over:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP and snakedirection!="DOWN":
                    snakedirection="UP"
                elif event.key==pygame.K_DOWN and snakedirection!="UP":
                    snakedirection="DOWN"
                elif event.key==pygame.K_LEFT and snakedirection!="RIGHT":
                    snakedirection="LEFT"
                elif event.key==pygame.K_RIGHT and snakedirection!="LEFT":
                    snakedirection="RIGHT"
        # move the snake
        snakemovement(snake,snakedirection)
        if collision(snake):
            game_over=True
            continue

        #draw everything
        drawsnake(snake)
        drawfood(food)
        drawscore(score)

        pygame.display.flip()
        clock.tick(10)
    else:
        restart,exitt=showgameover()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if restart.collidepoint(event.pos):
                    snake=[(100,100),(90,100),(80,100)]
                    snakedirection="RIGHT"
                    food=(random.randrange(0,WIDTH//CELL_SIZE)*CELL_SIZE,random.randrange(0,HEIGHT//CELL_SIZE)*CELL_SIZE)
                    score=0
                    game_over=False
                elif exitt.collidepoint(event.pos):
                    running=False
pygame.quit()
sys.exit()





