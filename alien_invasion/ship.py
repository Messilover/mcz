import pygame

class Ship():

	def __init__(self, screen, ai_set):
		self.screen = screen
		self.image = pygame.image.load('C:/Users/hp/alien_invasion/images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.ai_set = ai_set
		self.moving_right = False
		self.moving_left = False
		self.center = float(self.rect.centerx)
		
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_set.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_set.ship_speed
		self.rect.centerx = self.center
	
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
	def center_ship(self):
		self.center = self.screen_rect.centerx