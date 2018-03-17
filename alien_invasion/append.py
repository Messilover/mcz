import pygame

class Gift():
	
	def __init__(self, screen, ai_set, ship):
		self.screen = screen
		self.ai_set = ai_set
		self.ship = ship
		self.screen_rect = self.screen.get_rect()
		self.image = pygame.image.load('C:/Users/hp/alien_invasion/images/gift.bmp')
		self.rect = self.image.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.top = self.screen_rect.top
		self.y = 0
		self.speed = 0.5
		self.bullet = False
		
	def update(self):
		self.y += self.speed
		self.rect.centery = self.y
		if self.rect.bottom == self.ship.rect.top and not self.bullet:
			self.ai_set.bullet_width = self.screen_rect.width / 2
			self.bullet = True
			
			
	def blitme(self):
		self.screen.blit(self.image, self.rect)