import pygame

backgroundColor = (255, 255, 255)

class Ship():


	def __init__(self, screen, x, y):
		w = int(screen.get_width()/20)
		h = int(screen.get_height()/11)
		self.rect = pygame.Rect(x, y, w, h)
		self.img =  pygame.transform.scale(pygame.image.load("ship.png"), (w, h))
	

	def move(self, screen, direction):
		
		pygame.draw.rect(screen, backgroundColor, self.rect)
		pygame.display.update(self.rect)
		if direction == 0:	
			self.rect.move_ip(-1, 0)
		else:
			self.rect.move_ip(1, 0)

		screen.blit(self.img, (self.rect.left, self.rect.top))
		pygame.display.update(self.rect)
		# print(shipRect)