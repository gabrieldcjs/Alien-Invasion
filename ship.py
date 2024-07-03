import pygame

class Ship:
    
    def __init__(self, ai_game):
        # Inicializa a nave e sua posição inicial

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load(
            "/Users/gabrieldiniz/dev/AlienInvasion/ship.bmp")
        self.rect = self.image.get_rect()
        # Coloca a nave na parte inferior central da tela
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # Desenha a nave na tela na posição atual
        self.screen.blit(self.image, self.rect)