import pygame

GREEN = (100, 255, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

backgroundColor = WHITE
BulletColor = GREEN

class Bullet():
	

	def __init__(self, screen, x, y):
		self.rect = pygame.Rect(x, y, int(screen.get_width()/240), int(screen.get_height()/27))
		

	def advance(self, screen):
		# if self.advanceToggle:
		pygame.draw.rect(screen, backgroundColor, self.rect)
		pygame.display.update(self.rect)
		self.rect.move_ip(0, -2)
		pygame.draw.rect(screen, BulletColor, self.rect)
		pygame.display.update(self.rect)
		# self.advanceToggle = False
		# else:
			# self.advanceToggle = True


