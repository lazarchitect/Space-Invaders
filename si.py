"""
TASKS

"""

import pygame

from time import sleep

score = 0
BLACK = (0,0,0)
GREEN = (100, 255, 100)
WHITE = (255, 255, 255)

pygame.init()

COURIER = pygame.font.SysFont("couriernew", 24).render("Press q to quit", 0, (128, 100, 100))

screen = pygame.display.set_mode((800, 800))
x, y = screen.get_size()

screen.fill(WHITE)


shipRect = pygame.Rect(400, 700, 50, 50)
shipImg =  pygame.image.load("ship.png")
shipImg =  pygame.transform.scale(shipImg, (50, 50))
screen.blit(shipImg, (400, 700))

pygame.display.flip() #sets up the window's visuals.
##########################################################

def moveShip(direction):
	
	pygame.draw.rect(screen, WHITE, shipRect)
	pygame.display.update(shipRect)
	if direction == 0:
		shipRect.move_ip(-1, 0)
	else:
		shipRect.move_ip(1, 0)

	screen.blit(shipImg, (shipRect.left, shipRect.top))
	pygame.display.update(shipRect)
	print(shipRect)

##########################################################
while(True):

	sleep(.002)

	pressedKeys = pygame.key.get_pressed()

	if pressedKeys[pygame.K_LEFT] == 1 and shipRect.left > 0:
		moveShip(0)

	elif pressedKeys[pygame.K_RIGHT] == 1 and shipRect.right < 800:
		moveShip(1)	
	
	for event in pygame.event.get():
		

		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (event.key == pygame.K_F4 or event.key == pygame.K_q)):
				exit()
