# imports for the game 
import pygame as pg
import random as rd
from pygame.locals import * 

# pygame init 
pg.init()

# colors for the game
red = (255,0,0)
blue = (51,153,255)
grey = (192,192,192)
green = (51, 102,0)
yellow = (0,255,255)

# window height and width 
win_width = 600
win_height = 400

# create the window, caption and displaying
window = pg.display.set_mode((win_width, win_height))
pg.display.set_caption("Snake Game")

# snake block and speed of the snake 
snake = 10  # snake block size 
# later to be calculated based on the level of the game

snake_speed = 15 # snake base speed 

clock = pg.time.Clock() # clock object to control the frame rate of the game

# font styles for the game
font_style = pg.font.SysFont("comicsans", 20)
score_font = pg.font.SysFont("calibri", 26)

# function to display the score of the game
def user_score(score):
    number = score_font.render("Score: " + str(score), True, red) # render the score text with the score value
    window.blit(number, (10, 10)) # display the score at the top left corner of the window

# function to display our game and main loop of the game
def game_snake(snake_size, snake_list):
    for x in snake_list: # iterate through the list of snake segments and draw each segment on the window
        pg.draw.rect(window, green, [x[0], x[1], snake_size, snake_size]) # draw a rectangle for each segment of the snake using the coordinates stored in the snake length list
    

# function to display the message when the game is over
def message(msg):
    mesg = font_style.render(msg, True, red)
    window.blit(mesg, [win_width/6, win_height/3])

# function of our game: main game loop
def game_loop():
    gameOver = False
    gameClose = False

    x1 = win_width/2
    y1 = win_height/2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

# generate random coordinates for the food, ensuring that they are aligned with the snake's block size and within the game window boundaries
    foodx = round(rd.randrange(0, win_width - snake)/10.0)*10.0
    foody = round(rd.randrange(0, win_height - snake)/10.0)*10.0

# main game loop that runs until the game is over
    while not gameOver: 
        while gameClose == True:
            window.fill(grey)
            message("Game Over! Press P-Play Again or Q-Quit")
            user_score(snake_length-1) # display the score of the game, which is the length of the snake minus 1 (since the initial length is 1)
            pg.display.update() # update the display to show the game over message and score

# event loop to check for user input when the game is over
            for event in pg.event.get():
                if event.type == pg.QUIT: # if the user clicks the close button on the window, set gameOver to True to exit the game
                    gameOver = True
                    gameClose = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q: # if the 'Q' key is pressed, set gameOver to True to exit the main game loop and end the game
                        gameOver = True
                        gameClose = False
                    if event.key == pg.K_p: # if the 'P' key is pressed, call the game_loop function to restart the game
                        game_loop()

# main game loop
        for event in pg.event.get():

            if event.type == pg.QUIT:
                gameOver = True # if the user clicks the close button on the window, set gameOver to True to exit the main game loop and end the game

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x1_change = -snake # move left by snake block size from current position
                    y1_change = 0 # stop vertical movement when moving horizontally, so y1_change is set to 0
                
                if event.key == pg.K_RIGHT:
                    x1_change = snake # move right by snake block size from current position
                    y1_change = 0 # stop horizontal movement when moving vertically, so x1_change is set to 0
                
                if event.key == pg.K_UP:
                    x1_change = 0 # stop horizontal movement when moving vertically, so x1_change is set to 0
                    y1_change = -snake # move up by snake block size from current position
                
                if event.key == pg.K_DOWN:
                    x1_change = 0 # stop horizontal movement when moving vertically, so x1_change is set to 0
                    y1_change = snake # move down by snake block size from current position

        if (x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0): # check if the snake has hit the boundaries of the window
            gameClose = True # set gameClose to True to display the game over message and score
        x1 += x1_change # update the x-coordinate of the snake's head based on the change in x
        y1 += y1_change # update the y-coordinate of the snake's head based on the change in y
        window.fill(grey) # fill the window with grey color to clear the previous frame
        pg.draw.rect(window, yellow, [foodx, foody, snake, snake]) # draw the food on the window at the random coordinates generated earlier
        snake_size = [] # initialize an empty list to store the coordinates of the snake's body segments
        snake_size.append(x1) # add the new x-coordinate of the snake's head to the snake size list
        snake_size.append(y1) # add the new y-coordinate of the snake's head to
        snake_list.append(snake_size) # add the new snake size (head coordinates) to the snake length list
        if len(snake_list) > snake_length: # check if the length of the snake size list exceeds the current length of the snake
            del snake_list[0] # if the length of the snake size list exceeds the current length of the snake, remove the oldest segment (the tail) from the snake length list
            
        for x in snake_list[:-1]: # check if the snake has collided with itself by iterating through the snake length list (excluding the head) and checking if any segment has the same coordinates as the head
            if x == snake_size: # if a collision is detected (the head has the same coordinates as a body segment), set gameClose to True to display the game over message and score
                gameClose = True

        game_snake(snake, snake_list) # call the game_snake function to draw the snake on the window based on the current length and coordinates of the snake segments
        user_score(snake_length -1) # display the current score of the game, which is the length of the snake minus 1 (since the initial length is 1)
        pg.display.update() # update the display to show the new frame with the snake and score

        if x1 == foodx and y1 == foody: 
            foodx = round(rd.randrange(0, win_width - snake)/10.0)*10.0 # generate new random coordinates for the food when the snake eats it
            foody = round(rd.randrange(0, win_height - snake)/10.0)*10.0 # generate new random coordinates for the food when the snake eats it
            snake_length += 1 # increase the length of the snake by 1 when it eats the food

        clock.tick(snake_speed) # control the frame rate of the game based on the snake speed

            
    pg.quit() # quit the game when the snake eats the food (this line can be removed if you want the game to continue after eating the food)
    quit()
    
game_loop() # call the game_loop function to start the game