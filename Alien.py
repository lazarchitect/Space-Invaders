import pygame

backgroundColor = (255, 255, 255)

class Alien():
	def __init__(self, screen, variant, x, y):

		self.x = x
		self.y = y

		self.w = int(screen.get_width()/30)
		self.h = int(screen.get_height()/15)

		self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
		self.img = pygame.transform.scale(pygame.image.load(variant+".png"), (self.w, self.h))

	#direction can be -1 for left, 1 for right, or 0 for down. 
	def move(self, screen, direction):
		pygame.draw.rect(screen, backgroundColor, self.rect)
		pygame.display.update(self.rect)

		if direction == -1: #move left, so neg x
			self.rect.move_ip(-30, 0)
		elif direction == 1:
			self.rect.move_ip(30, 0)
		else:
			self.rect.move_ip(0, 20)


		screen.blit(self.img, (self.rect.left, self.rect.top))

		pygame.display.update(self.rect)