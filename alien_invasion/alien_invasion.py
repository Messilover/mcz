import sys
import pygame
from alien_settings import Settings
from ship import Ship
import game_function
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from append import Gift

def run_game():
	pygame.init()
	ai_set = Settings()
	screen = pygame.display.set_mode((ai_set.screen_width,ai_set.screen_height))
	pygame.display.set_caption("Alien Invasion")
	play_button = Button(ai_set, screen, "Play")
	ship = Ship(screen, ai_set)
	stats = GameStats(ai_set)
	bullets = Group()
	aliens = Group()
	gift = Gift(screen, ai_set, ship)
	game_function.aliens_flock(ai_set, screen, aliens)
	
	while True:
		game_function.check_events(ai_set, screen, ship, bullets, aliens, stats, play_button)
		if stats.game_active:
			ship.update()
			game_function.bullet_update(ai_set, screen, bullets, aliens)
			game_function.alien_update(ai_set, screen, bullets, aliens, ship, stats)
			game_function.gift_update(screen, gift)
			
		game_function.update_screen(ai_set, screen, ship, bullets,
			aliens, stats, play_button, gift)
		
if __name__ == '__main__':
	run_game()