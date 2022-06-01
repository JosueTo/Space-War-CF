from pickle import TRUE
import pygame, sys, os, random, time

# CONSTANTES DE PANTALLA
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Space War')
clock = pygame.time.Clock()
FPS = 60
# IMAGENES DEL JUEGO
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/bg42.png')),(screen_width,screen_height))
# PLAYER
PLAYER_SHIP = pygame.image.load(os.path.join('Assets/Player/ship_player.png'))
# ENEMIES
YELLOW_SHIP = pygame.transform.rotozoom(pygame.image.load(os.path.join('Assets/enemies/yellow-ship.png')),180,1)
RED_SHIP = pygame.transform.rotozoom(pygame.image.load(os.path.join('Assets/enemies/red-ship.png')),180,1)
PURPLE_SHIP = pygame.transform.rotozoom(pygame.image.load(os.path.join('Assets/enemies/purple-ship.png')),180,1)
# BULLET / LASER
GREEN_BULLET = pygame.image.load(os.path.join('Assets/bullets/green-bullet.png'))
YELLOW_LASER = pygame.image.load(os.path.join('Assets/bullets/yellow-laser.png'))
RED_LASER = pygame.image.load(os.path.join('Assets/bullets/red-laser.png'))
PURPLE_LASER = pygame.image.load(os.path.join('Assets/bullets/purple-laser.png'))
