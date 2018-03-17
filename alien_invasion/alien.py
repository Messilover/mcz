import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	
	def __init__(self, ai_set, screen):
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_set = ai_set
		self.image = pygame.image.load('C:/Users/hp/alien_invasion/images/alien.bmp')
		self.rect = self.image.get_rect()
		self.rect.x = self.rect.width
		self.rect.y = 0
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		
	def update(self):
		self.y += self.ai_set.alien_speed
		self.rect.y = self.y
	
	def blitme(self):
		self.screen.blit(self.image, self.rect)