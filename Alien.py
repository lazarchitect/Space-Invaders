import pygame

class Alien():
	def __init__(self, variant):
		self.img = pygame.image.load(variant+".png")