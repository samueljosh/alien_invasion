import pygame 
from pygame.sprite import Group

from settings import Settings
from ship import Ship 

import game_functions as gf

def run_game():
    # Inicializa o jogo e cria um objeto para tela
    pygame.init()
    
    ai_settings = Settings()
    
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #cria uma espaçonave 
    ship = Ship(ai_settings, screen)
    #Cria um grupo no qual serão armazenado os projéteis
    bullets = Group()
    # Cria um grupo de aliens
    aliens = Group()

    # Cria a frota de aliens
    gf.create_fleet(ai_settings, screen,ship, aliens)
    
    #inicia o laco principal do jogo
    while True:
      gf.check_events(ai_settings, screen, ship, bullets)
      ship.update()
      gf.update_bullets(bullets)
      gf.update_aliens(ai_settings, aliens)
      gf.update_screen(ai_settings, screen, ship, aliens, bullets)

      
      
      
		

run_game()
		
			
		
