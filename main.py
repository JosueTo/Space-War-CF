import pygame, sys, os, random, time
from constants import *

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

    def get_width(self):
        return self.ship_img.get_width()
    
    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self,x,y,health=100):
        super().__init__(x,y,health)
        self.ship_img = PLAYER_SHIP
        self.laser_img = GREEN_BULLET
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

class Enemy(Ship):
    COLOR_MAP = {
                "yellow": (YELLOW_SHIP,YELLOW_LASER),
                "red": (RED_SHIP,RED_LASER),
                "purple": (PURPLE_SHIP,PURPLE_LASER)
                }

    def __init__(self,x,y,color,health=100):
        super().__init__(x,y,health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel
    
    

pygame.init()

# LOOP PRINCIPAL
def main():
    level = 0
    lives = 5
    main_font = pygame.font.SysFont('comicsans', 30)

    player = Player(300,650)
    player_vel = 10

    enemies = []
    wave_length = 5
    enemy_vel = 1

    def redraw_window():
        # CONFIGURACIÓN DE BACKGROUND
        screen.blit(BACKGROUND,(0,0))
        # IMPRIMIENDO EL NIVEL Y VIDAS
        lives_label = main_font.render(f'Lives: {lives}', 1, (255,255,255))
        level_label = main_font.render(f'Level: {level}', 1,(255,255,255))
        screen.blit(lives_label, (10,10))
        screen.blit(level_label, (screen_width - level_label.get_width() - 10, 10))
        # IMPRIMIENDO ENEMIGOS
        for enemy in enemies:
            enemy.draw(screen)
        # IMPRIMIENDO PLAYER
        player.draw(screen)

    while True:
        
        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, screen_width-100), random.randrange(-1500,100), random.choice(["yellow","red","purple"]))
                enemies.append(enemy)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # MOVIMIENTO DEL PLAYER
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_vel > 0:
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < screen_width:
            player.x += player_vel
        if keys[pygame.K_UP] and player.y - player_vel > 0:
            player.y -= player_vel
        if keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() < screen_height:
            player.y += player_vel
        
        # MOVIMIENTO DE ENEMIGOS
        for enemy in enemies:
            enemy.move(enemy_vel)
        
        redraw_window()    
        pygame.display.update()
        clock.tick(60)

main()