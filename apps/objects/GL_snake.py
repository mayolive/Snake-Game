""" SETUP """
from __future__ import with_statement
import sys, os
SNAKE_API_LOCATION = '/Users/olivermay/Dropbox/Programing Course/Oli Practice/app'
sys.path.append(SNAKE_API_LOCATION)
os.environ['DJANGO_SETTINGS_MODULE'] = 'snake.settings'
from django.conf import settings
import random

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from apps.objects.models import PlayerSnake, EnemySnake, SnakeFood


window = 0                                             # glut window number
width, height = 500, 500                               # window size
field_width, field_height = 50, 50                     # internal resolution
interval = 200 # update interval in milliseconds


def random_position():
    # randint return a number between 1 and 50, we want a number between 0 and 49 inclusive
    return random.randint(0, 50) - 1

all_snake_food_position = [SnakeFood(random_position(), random_position()).position]



def refresh2d_custom(width, height, internal_width, internal_height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, internal_width, 0.0, internal_height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
def player_direction(*args):
    
    if args[0] == 'w':
        player_snake.dir = (0, 1)                     # up
    if args[0] == 's':
        player_snake.dir = (0, -1)                    # down
    if args[0] == 'a':
        player_snake.dir = (-1, 0)                    # left
    if args[0] == 'd':
        player_snake.dir = (1, 0)                     # right
    player_snake.save()


def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()                                            # done drawing a rectangle
    
def add_vect((x1, y1), (x2, y2)):
    return ((x1 + x2) % 50, (y1 + y2) % 50)

def draw_snake(snake):
    glColor3f(1.0, 1.0, 1.0)
    for x, y in snake.body:
        draw_rect(x, y, 1, 1)

def draw_snake_food_position():
    glColor3f(1.0, 1.0, 1.0)
    for x, y in all_snake_food_position:
        draw_rect(x, y, 1, 1)


#I think draw needs to have no arguments given the use of draw in initialisation
#draw is therefore the high level function that calls draw snake
def draw():                                                     # draw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)          # clear the screen
    glLoadIdentity()                                            # reset position
    refresh2d_custom(width, height, field_width, field_height)
    draw_snake(player_snake)
    draw_snake_food_position()
    glutSwapBuffers()                                           # important for double buffering

def player_collision(player_snake, new_point):
    if new_point in player_snake.body:
        player_snake.alive = False
        print "Game over - Your score was " + str(len(player_snake.body))
        sys.exit()

def update(value):


    new_point = add_vect(player_snake.body[0],player_snake.dir)
    #first check if the snake has collided with itself or an enemy
    player_collision(player_snake, new_point)
    
    # update snake with a new position (every 200ms)
    # this just updates the snake's body and food, it doesnt do any drawing
    
    player_snake.body.insert(0,new_point)
    if new_point not in all_snake_food_position:
        #only remove the last point if snake doesn't eat food
        player_snake.body.pop()
    else:
        all_snake_food_position.remove(new_point)
        all_snake_food_position.append(SnakeFood(random_position(), random_position()).position)

    glutTimerFunc(interval, update, 0) # trigger next update


player_snake = PlayerSnake()

# initialization
glutInit()                                                      # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                               # set window size
glutInitWindowPosition(0, 0)                                    # set window position
window = glutCreateWindow("noobtuts.com")                       # create window with title
glutDisplayFunc(draw)                                           # set draw function callback
glutIdleFunc(draw)                                              # draw all the time
glutTimerFunc(interval, update, 0)                              # trigger next update (actually triggers the first update - next updates are triggered by update itself)
glutKeyboardFunc(player_direction)
glutMainLoop()                                                  # start everything


