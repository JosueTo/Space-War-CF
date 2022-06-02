import pygame, sys, os, random, time
from constants import *

class Laser:
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self,window):
        window.blit(self.img,(self.x,self.y))
    
    def move(self,vel):
        self.y += vel
    
    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)
    
    def collision(self, obj):
        return collide(self,obj)

class Ship:
    COOLDOWN = 30
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
        for laser in self.lasers:
            laser.draw(screen)
    
    def move_lasers(self,vel,obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(screen_height):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1
    
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x+39,self.y,self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

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
    
    def move_lasers(self,vel,objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(screen_height):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)
    
    def draw(self, window):
        super().draw(window)
        self.healthbar(window)
    
    def healthbar(self,window):
        pygame.draw.rect(window,(255,0,0),(self.x,self.y + self.ship_img.get_height() + 10,self.ship_img.get_width(),10))
        pygame.draw.rect(window,(0,255,0),(self.x,self.y + self.ship_img.get_height() + 10,self.ship_img.get_width() * (self.health/self.max_health),10))

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
    
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x+22,self.y+55,self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

pygame.init()

def collide(obj1,obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask,(offset_x,offset_y)) != None


# LOOP PRINCIPAL
def main():
    run = True
    level = 0
    lives = 5
    main_font = pygame.font.SysFont('comicsans', 30)
    lost_font = pygame.font.SysFont('comicsans', 40)

    player = Player(300,650)
    player_vel = 8
    laser_vel = 6

    enemies = []
    wave_length = 5
    enemy_vel = 1

    lost = False
    lost_count = 0

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
        # MENSAJE AL PERDER
        if lost:
            lost_label = lost_font.render('GAME OVER!', 1, (255,255,255))
            screen.blit(lost_label,(screen_width/2 - lost_label.get_width()/2,350))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        # COMPROBAR SI EL PLAYER PERDIÓ
        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1
        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue
        # SUBIR NIVEL Y LLAMAR LA SIGUIENTE OLA DE ENEMIGOS
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
        if keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() + 15 < screen_height:
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()
        
        # MOVIMIENTO DE ENEMIGOS
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel,player)

            if random.randrange(0,2*60) == 1:
                enemy.shoot()
            
            if collide(enemy,player):
                player.health -= 10 
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > screen_height:
                lives -= 1
                enemies.remove(enemy)
            
        player.move_lasers(-laser_vel,enemies)

def main_menu():
    title_font = pygame.font.SysFont('comicsans',30)
    run = True
    while run:
        screen.blit(BACKGROUND,(0,0))
        title_label = title_font.render('Presiona cualquier boton del mouse para iniciar...',1,(255,255,255))
        screen.blit(title_label,(screen_width/2 - title_label.get_width()/2,400))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()

main_menu()