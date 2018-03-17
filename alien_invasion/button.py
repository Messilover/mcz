import pygame.font

class Button():
	
	def __init__(self, ai_set, screen, msg):
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.width = 200
		self.height = 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)
		self.font_number = pygame.font.SysFont(None, 40)
		self.font_rect = pygame.Rect(0, 0, 150, 40)
		self.font_rect.right = self.screen_rect.right
		self.font_rect.top = self.screen_rect.top
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		self.prep_msg(msg)
		
	def prep_msg(self, msg):
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
		
	def prep_mss(self, mss):
		self.font_image = self.font_number.render(mss, True, self.text_color,
			(230, 230, 230))
		self.font_image_rect = self.font_image.get_rect()
		self.font_image_rect.center = self.font_rect.center
		
	def draw_button1(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
		
	def draw_button2(self):
		self.screen.fill((230, 230, 230), self.font_rect)
		self.screen.blit(self.font_image, self.font_image_rect)