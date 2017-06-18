
import pygame
from Ship import Ship
from Alien import Alien
from Bullet import Bullet 
from Barrier import Barrier
from time import sleep

import ctypes
ctypes.windll.user32.SetProcessDPIAware() #to negate Windows' 125% stretching

score = 0
BLACK = (0,0,0)
GREEN = (100, 255, 100)
WHITE = (255, 255, 255)

backgroundColor = WHITE

pygame.init()

ticks = pygame.time.get_ticks
bulletClock = ticks()
bulletAvailable = True

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
x, y = screen.get_size()

screen.fill(backgroundColor)
# backgroundImage = pygame.transform.scale(pygame.image.load("space.jpg"), (x, y))
# screen.blit(backgroundImage, (0,0))

quitMsg = pygame.font.SysFont("couriernew", 24).render("Spacebar to shoot. Press q to quit", 0, (128, 100, 100))
screen.blit(quitMsg, (10, 10))

ship = Ship(screen, x/2, y-120)
ship.move(screen, 0)

barriers = []
for i in range(5):
	tempVar = Barrier(screen, x * (5+(20*i))/100, y -200)
	barriers.append(tempVar)
	screen.blit(tempVar.image, (tempVar.x, tempVar.y))

bullets = []

pygame.display.flip() #sets up the window's visuals.

##########################################################

while(True):

	sleep(.002)

	# screen.blit(backgroundImage, (0,0))	

	screen.blit(quitMsg, (10, 10))
	pygame.display.update([10, 10, 500, 40])

	if ticks() - bulletClock > 500: # can only shoot a bullet twice a second. in the original game there was no timer except there could only be one friendly bullet up at once...
		bulletAvailable = True
	
	for eachBullet in bullets:
		eachBullet.advance(screen)
		if eachBullet.rect.bottom == 0:
			bullets.remove(eachBullet)

		boom = eachBullet.rect.collidelist(barriers)
		if boom != -1:
			barriers[boom].degrade(screen)
			bullets.remove(eachBullet)
			if barriers[boom].quality == 0:
				del barriers[boom]


	pressedKeys = pygame.key.get_pressed()


	if pressedKeys[pygame.K_SPACE] == 1 and bulletAvailable: #shoot!
		bullets.append(Bullet(screen, ship.rect.centerx, ship.rect.top-20))
		bulletAvailable = False
		bulletClock = ticks()

	if pressedKeys[pygame.K_LEFT] == 1 and ship.rect.left > 0:
		ship.move(screen, 0)

	if pressedKeys[pygame.K_RIGHT] == 1 and ship.rect.right < x: 
		ship.move(screen, 1)
		# its not elif because if it was, the ship would move left when both keys are pressed. this is a handy way to get the desired behavior	
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (event.key == pygame.K_F4 or event.key == pygame.K_q)):
				exit()
