import pygame

backgroundColor = (255, 255, 255)

# This class represents the walls that the ship can hide behind. They take damage when hit, by a friendly or enemy bullet.
class Barrier():

	def __init__(self, screen, x, y): #x and y are coords of top left corner (as is tradition (here in canada))
		
		self.x = x
		self.y = y

		self.w = int(screen.get_width()/10)
		self.h = int(screen.get_height()/13)

		self.quality = 5 # the lower the quality, the worse for wear the wall is. at zero, the wall falls apart. 

		self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

		self.image = pygame.transform.scale(pygame.image.load("barrier_quality_"+str(self.quality)+".png"), (self.w, self.h))


	# this is what you get when a bullet hits a barrier... motherfucker
	def degrade(self, screen):

		pygame.draw.rect(screen, backgroundColor, self.rect)
		pygame.display.update(self.rect)
		
		self.quality -= 1

		if self.quality == 0:
			return

		else:
			self.image = pygame.transform.scale(pygame.image.load("barrier_quality_"+str(self.quality)+".png"), (self.w, self.h))
			
			screen.blit(self.image, (self.x, self.y))

			pygame.display.update(self.rect)