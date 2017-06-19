import pygame

RED = (255, 100, 100)
WHITE = (255, 255, 255)

backgroundColor = WHITE
BulletColor = RED

class EnemyBullet():
	

	def __init__(self, screen, x, y, w, h):
		self.rect = pygame.Rect(x, y, w, h)
		
	def advance(self, screen):
		
		pygame.draw.rect(screen, backgroundColor, self.rect)
		pygame.display.update(self.rect)
		
		self.rect.move_ip(0, 2)
		
		pygame.draw.rect(screen, BulletColor, self.rect)
		pygame.display.update(self.rect)