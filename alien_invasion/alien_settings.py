class Settings():

	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (230,230,230)
		self.bullet_width = 4
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullet_allowed = 3
		self.ship_limit = 3
		self.speed_up = 1.1
		self.initialize_dynamic_set()
		
	def initialize_dynamic_set(self):
		self.ship_speed = 1.5
		self.bullet_speed = 2	
		self.alien_speed = 0.2
		
	def increase_speed(self):
		self.ship_speed *= self.speed_up
		self.bullet_speed *= self.speed_up
		self.alien_speed *= self.speed_up
	