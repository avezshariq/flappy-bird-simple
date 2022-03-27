import pygame
import random
pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 60)

# Variables
fps = 60
obs_x1 = 1280
obs_x2 = 1280 + 500
obs_x3 = 1280 + 500 + 500
obs_speed = 10
bird_y = 220
gravity = 5
score = 0
pipe_height = 450
gap = 220

# Assets
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Flappy Bird -  The Game')
bird = pygame.image.load('bird.png')
obs = pygame.image.load('obstacle.png')
bg = pygame.image.load('background.png')
splaash = pygame.image.load('splash.png')
game_over = pygame.image.load('game_over.png')
score_label = pygame.image.load('score.png')
zero = pygame.image.load('0.png')
one = pygame.image.load('1.png')
two = pygame.image.load('2.png')
three = pygame.image.load('3.png')
four = pygame.image.load('4.png')
five = pygame.image.load('5.png')
six = pygame.image.load('6.png')
seven = pygame.image.load('7.png')
eight = pygame.image.load('8.png')
nine = pygame.image.load('9.png')

# Stages
splash = True
game = True
over = True

go_down = 1
################[ SPLASH ]################
while splash:

    ## Keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            splash = False
            over = False

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    splash = False

    ## Value Updates
    # Obstacle1
    if obs_x1 > -100:
        obs_x1 -= obs_speed
    else:
        obs_x1 = 1280

    # Obstacle2
    if obs_x2 > -100:
        obs_x2 -= obs_speed
    else:
        obs_x2 = 1280

    # Obstacle3
    if obs_x3 > -100:
        obs_x3 -= obs_speed
    else:
        obs_x3 = 1280

    # Bird
    if go_down:
        bird_y += 5
        if bird_y > 400:
            go_down = 0
    else:
        bird_y -= 5
        if bird_y < 220:
            go_down = 1

    ## Display
    screen.blit(bg, (0,0))
    screen.blit(obs, (obs_x1, -250))
    screen.blit(obs, (obs_x2, -250))
    screen.blit(obs, (obs_x3, -250))
    screen.blit(bird, (100, bird_y))
    screen.blit(splaash, (200,50))
    pygame.display.update()
    clock.tick(fps)

################[ GAME ]################
## Initialise Obstacles
obs_x1 = 1280
obs_x2 = 1280 + 500
obs_x3 = 1280 + 500 + 500
obs_y1 = random.randint(-350, -100)
obs_y2 = random.randint(-350, -100)
obs_y3 = random.randint(-350, -100)
while game:

    ## Keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            over = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bird_y -= gravity*3

    ## Useful for Debugging Collisions
    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_w]:
        #bird_y -= gravity*3
    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_s]:
        #bird_y += gravity*3

    ## Value Updates
    # Bird
    bird_y += gravity
    if bird_y < 0:
        bird_y = 0
    if bird_y > 650:
        bird_y = 650

     # Obstacle1
    if obs_x1 > -100:
        obs_x1 -= obs_speed
    else:
        obs_x1 = 1280
        score += 1
        obs_y1 = random.randint(-350, -100)

    # Obstacle2
    if obs_x2 > -100:
        obs_x2 -= obs_speed
    else:
        obs_x2 = 1280
        score += 1
        obs_y2 = random.randint(-350, -100)

    # Obstacle3
    if obs_x3 > -100:
        obs_x3 -= obs_speed
    else:
        obs_x3 = 1280
        score += 1
        obs_y3 = random.randint(-350, -100)

    ## Collision
    # Obstacle1
    if 0 < obs_x1 < 200:
        if not(obs_y1 + pipe_height < bird_y < obs_y1 + pipe_height + gap):
            game = False

    # Obstacle2
    if 0 < obs_x2 < 200:
        if not(obs_y2 + pipe_height < bird_y < obs_y2 + pipe_height + gap):
            game = False

    # Obstacle3
    if 0 < obs_x3 < 200:
        if not(obs_y3 + pipe_height < bird_y < obs_y3 + pipe_height + gap):
            game = False

    ## Display
    screen.blit(bg, (0,0))
    screen.blit(obs, (obs_x1, obs_y1))
    screen.blit(obs, (obs_x2, obs_y2))
    screen.blit(obs, (obs_x3, obs_y3))
    screen.blit(bird, (100, bird_y))
    text = font.render('Score: ' + str(score), True, (255,255,255))
    screen.blit(text, (25,25))
    pygame.display.update()
    clock.tick(fps)

################[ SHOW SCORE ]################
score = str(score)
num_start = 670

## Display
screen.blit(game_over, (0,0))
screen.blit(score_label, (350,150))
for num in score:
    if num == '0':
        screen.blit(zero, (num_start, 152))
    elif num == '1':
        screen.blit(one, (num_start, 152))
    elif num == '2':
        screen.blit(two, (num_start, 152))
    elif num == '3':
        screen.blit(three, (num_start, 152))
    elif num == '4':
        screen.blit(four, (num_start, 152))
    elif num == '5':
        screen.blit(five, (num_start, 152))
    elif num == '6':
        screen.blit(six, (num_start, 152))
    elif num == '7':
        screen.blit(seven, (num_start, 152))
    elif num == '8':
        screen.blit(eight, (num_start, 152))
    else:
        screen.blit(nine, (num_start, 152))
    num_start += 60
pygame.display.update()
print('Score: ', score)

################[ EXIT ]################
while over:

    ## Keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = False

    clock.tick(fps/10) # To save on CPU resources XD

pygame.quit()
