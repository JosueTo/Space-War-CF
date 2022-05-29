import pygame, sys, os, random, time
from constants import *

class Game:
    def __init__(self):
        pass
    def screeen_draw(self):
        # CONFIGURACIÓN DE BACKGROUND
        # self.background = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/bg42.png')),(screen_width,screen_height))
        screen.blit(BACKGROUND,(0,0))
        # IMPRIMIENDO EL NIVEL Y VIDAS
        self.font = pygame.font.SysFont('comicsans', 30)
        self.lives = 5
        self.lives_label = self.font.render(f'Lives: {self.lives}', 1, (255,255,255))
        self.level = 1
        self.level_label = self.font.render(f'Level: {self.level}', 1,(255,255,255))
        screen.blit(self.lives_label, (10,10))
        screen.blit(self.level_label, (screen_width - self.level_label.get_width() - 10, 10))
    
    def run(self):
        self.screeen_draw()
        player.draw(screen)

class Ship:
    def __init__(self,x,y,health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
    
    def draw(self, window):
        window.blit(self.ship_img,(self.x,self.y))

class Player(Ship):
    def __init__(self,x,y,healt=100):
        super().__init__(x,y,healt)
        self.ship_img = PLAYER_SHIP


pygame.init()

# CONSTANTES DE MI VENTANA
# screen_width = 800
# screen_height = 800
# screen = pygame.display.set_mode((screen_width,screen_height))
# pygame.display.set_caption('Space War')
# clock = pygame.time.Clock()
game = Game()
player = Player(300,650)
player_vel = 10
# LOOP PRINCIPAL
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # MOVIMIENTO DEL PLAYER
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x - player_vel > 0:
        player.x -= player_vel
    if keys[pygame.K_RIGHT] and player.x + player_vel + 50 < screen_width:
        player.x += player_vel
    if keys[pygame.K_UP] and player.y - player_vel > 0:
        player.y -= player_vel
    if keys[pygame.K_DOWN] and player.y + player_vel + 50 < screen_height:
        player.y += player_vel

    game.run()
        
    pygame.display.update()
    clock.tick(60)