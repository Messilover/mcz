import sys
import pygame
from bullet import Bullet
from alien import Alien
import random
from time import sleep

def check_events(ai_set, screen, ship, bullets, aliens, stats, play_button):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				sys.exit()
			if event.key == pygame.K_RIGHT:
				ship.moving_right = True
			if event.key == pygame.K_LEFT:
				ship.moving_left = True
			if event.key == pygame.K_SPACE:
				if len(bullets) < ai_set.bullet_allowed:
					new_bullet = Bullet(ai_set, screen, ship)
					bullets.add(new_bullet)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = False
			if event.key == pygame.K_LEFT:
				ship.moving_left = False	
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_button(ai_set, screen, stats, play_button, 
				mouse_x, mouse_y, ship, aliens, bullets)
			
def check_button(ai_set, screen, stats, play_button, 
	mouse_x, mouse_y, ship, aliens, bullets):
	if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
		ai_set.initialize_dynamic_set()
		stats.game_active = True
		pygame.mouse.set_visible(False)
		stats.reset_stats()
		aliens.empty()
		bullets.empty()
		aliens_flock(ai_set, screen, aliens)
		ship.center_ship()

def aliens_flock(ai_set, screen, aliens):
	alien = Alien(ai_set, screen)
	width_allowed = screen.get_rect().width - 2 * alien.rect.width
	width_each = 2 * alien.rect.width
	number_max = int(width_allowed / width_each)
	number_set = []
	for number in range(number_max):
		number_set.append(random.randint(0,number_max))
	for number in set(number_set):
		alien = Alien(ai_set, screen)
		alien.rect.x = width_each * number
		alien.rect.y = 50
		aliens.add(alien)
		
def alien_bottom(ai_set, stats, screen, ship, aliens, bullets):
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_set, stats, screen, ship, aliens, bullets)
		
def ship_hit(ai_set, stats, screen, ship, aliens, bullets):
	if stats.ship_left > 0:
		stats.ship_left -= 1
		aliens.empty()
		bullets.empty()
		aliens_flock(ai_set, screen, aliens)
		ship.center_ship()
		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

def bullet_update(ai_set, screen, bullets, aliens):
	bullets.update()
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	if len(aliens) == 0:
		bullets.empty()
		ai_set.increase_speed()
		aliens_flock(ai_set, screen, aliens)
			
def alien_update(ai_set, screen, bullets, aliens, ship, stats):
	aliens.update()
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_set, stats, screen, ship, aliens, bullets)
	alien_bottom(ai_set, stats, screen, ship, aliens, bullets)
	
def gift_update(screen, gift):
	gift.update()
	

def update_screen(ai_set, screen, ship, bullets, aliens, stats, play_button, gift):
		screen.fill(ai_set.bg_color)
		ship.blitme()
		aliens.draw(screen)
		gift.blitme()
		mss = 'Live: ' + str(stats.ship_left)
		play_button.prep_mss(mss)
		play_button.draw_button2()
		for bullet in bullets.sprites():
			bullet.draw_bullet()
		if not stats.game_active:
			play_button.draw_button1()
		pygame.display.flip()