import pygame, sys, random, time, pyautogui
 
# check for initializing errors
check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("PyGame successfully initialized!")
 
# Play surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Automated Snake game!')
 
# Colors
red = pygame.Color(255, 0, 0) # gameover
green = pygame.Color(0, 0, 0) #snake
black = pygame.Color(0, 0, 0) #score
white = pygame.Color(165, 42, 42) #background
brown = pygame.Color(255, 255, 255) #food
 
# FPS controller
fpsController = pygame.time.Clock()
 
# Important varibles
snakePos = [100, 50]
snakeBody = [[100,50], [90,50], [80,50]]
 
foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True
 
score = 0
 
# Game over function
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    GOsurf = myFont.render('Game over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    playSurface.blit(GOsurf,GOrect)
    showScore(0)
    pygame.display.flip()
   
    time.sleep(1)
    pygame.quit() #pygame exit
    sys.exit() #console exit
   
def showScore(choice=1):
    sFont = pygame.font.SysFont('monaco', 24)
    Ssurf = sFont.render('Score : {0}'.format(score) , True, black)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (80, 10)
    else:
        Srect.midtop = (360, 120)
    playSurface.blit(Ssurf,Srect)

#selfPlay. Done by, VARUN
def selfPlay(foodPos, snakePos):
    if snakePos[0]<foodPos[0]:
        snakePos[0] += 10
    elif snakePos[0]>foodPos[0]:
        snakePos[0] -= 10
    elif snakePos[1]>foodPos[1]:
        snakePos[1] -= 10
    elif snakePos[1]<foodPos[1]:
        snakePos[1] += 10

# Main Logic of the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    selfPlay(foodPos, snakePos)
       
    # Snake body mechanism
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()
       
    #Food Spawn
    if foodSpawn == False:
        foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
    foodSpawn = True
   
    #Background
    playSurface.fill(white)
   
    #Draw Snake
    for pos in snakeBody:
        pygame.draw.rect(playSurface, green, pygame.Rect(pos[0],pos[1],10,10))
   
    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0],foodPos[1],10,10))
   
    # Bound
    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()
       
    # Self hit
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()
   
    #common stuff
    showScore()
    pygame.display.flip()
   
    fpsController.tick(24)
