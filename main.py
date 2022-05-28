import pygame, sys, os, random, time

class Game:
    def __init__(self):
        pass
    def screeen_draw(self):
        # CONFIGURACIÓN DE BACKGROUND
        self.background = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/bg42.png')),(screen_width,screen_height))
        screen.blit(self.background,(0,0))
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

if __name__ == '__main__':
# La declaración anterior elimina la pequeña posibilidad de ejecutar codigo no deseado al trabajar con multiples archivos. Es una buena practica.
    pygame.init()

    # CONSTANTES DE MI VENTANA
    screen_width = 800
    screen_height = 800
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption('Space War')
    clock = pygame.time.Clock()
    game = Game()

    # LOOP PRINCIPAL
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        game.run()
        
        pygame.display.update()
        clock.tick(60)