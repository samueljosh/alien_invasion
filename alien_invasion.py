import pygame 
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship 

import game_functions as gf

def run_game():
    # Inicializa o jogo e cria um objeto para tela
    pygame.init()
    
    ai_settings = Settings()
    
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Cria o botão Play
    play_button = Button(ai_settings, screen, "Play")
    
    # Cria uma instância para armazenar dados estatísticos do jogo
    # e cria painel de pontuação
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
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
      gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
      
      if stats.game_active :
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens ,bullets)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
      
      gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

      
      
      
		

run_game()
		
			
		
