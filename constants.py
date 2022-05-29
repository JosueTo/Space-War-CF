import pygame, sys, os, random, time


screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Space War')
clock = pygame.time.Clock()
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/bg42.png')),(screen_width,screen_height))
PLAYER_SHIP = pygame.transform.scale(pygame.image.load(os.path.join('Assets/Player/ship_player.png')),(screen_width,screen_height))