import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Uma classe que administra projéteis disparados pela espaçonave"""
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        
        #Cria um retângulo para o projétil em (0, 0) e, em seguida 
        #define a posição correta
        
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #Armazena a posição do projétil como um valor decimal
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor