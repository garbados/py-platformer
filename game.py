import pygame
import datetime
import random

## assets and constants

class Player(object):
    SCROLL_SPEED = 5
    SPRITE = pygame.image.load('assets/player.png')
    def __init__(self):
        self.coords = [0,0]

class Obstacle(object):
    def __init__(self):
        self.coords = [0,0]

class Time(object):
    def __init__(self):
        self.start = datetime.datetime.now()

    def get_duration(self):
        return datetime.datetime.now() - self.start

player = Player()
obstacles = []
timer = Time()
done = False
while not done:
    # update objects
    # draw stuff
    pygame.screen.fill(0)
    pygame.blit(player.SPRITE, player.coords)
    for obstacle in obstacles:
        pygame.blit(obstacle.SPRITE, obstacle.coords)
    # update the display
    pygame.display.update()
    # handle events