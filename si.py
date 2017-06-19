import pygame
from Ship import Ship
from Alien import Alien
from Bullet import Bullet 
from Barrier import Barrier
from EnemyBullet import EnemyBullet
from time import sleep
from random import choice

import ctypes
ctypes.windll.user32.SetProcessDPIAware() #to negate Windows' 125% stretching

score = 0
BLACK = (0,0,0)
GREEN = (100, 255, 100)
WHITE = (255, 255, 255)

backgroundColor = WHITE

pygame.init()
ticks = pygame.time.get_ticks

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
x, y = screen.get_size()

screen.fill(backgroundColor)
# backgroundImage = pygame.transform.scale(pygame.image.load("space.jpg"), (x, y))
# screen.blit(backgroundImage, (0,0))

quitMsg = pygame.font.SysFont("couriernew", 24).render("Spacebar to shoot. Press q to quit", 0, (128, 100, 100))
screen.blit(quitMsg, (10, 10))


#########################################################
ship = Ship(screen, x/2, y-120)
ship.move(screen, 0)

barriers = []
for i in range(5):
	tempVar = Barrier(screen, x * (5+(20*i))/100, y - 250)
	barriers.append(tempVar)
	screen.blit(tempVar.image, (tempVar.x, tempVar.y))

bullets = []
bulletWidth = int(screen.get_width()/240)
bulletHeight = int(screen.get_height()/27)
bulletClock = ticks()
bulletAvailable = True

enemybullets = []

aliens = []
alienMoveClock = ticks()
alienShotClock = ticks()
alienDirection = 1
alienDirectionCounter = 0
for alienRow in range(14):
	for alienCol in range(5):
		alienX = 100 + (alienRow * 120)
		alienY = 100 + (alienCol * 100)
		tempAlien = Alien(screen, "variant1", alienX, alienY)
		aliens.append(tempAlien)
		screen.blit(tempAlien.img, (tempAlien.x, tempAlien.y))


pygame.display.flip() #sets up the window's visuals.

##########################################################

while(True):

	sleep(.002)

	# screen.blit(backgroundImage, (0,0))	

	screen.blit(quitMsg, (10, 10))
	pygame.display.update([10, 10, 500, 40])

	if ticks() - bulletClock > 500: # can only shoot a bullet twice a second. in the original game there was no timer except there could only be one friendly bullet up at once...
		bulletAvailable = True

	if ticks() - alienShotClock > 500:
		alienShotClock = ticks()
		shooter = choice(aliens)
		enemybullets.append(EnemyBullet(screen, shooter.rect.centerx, shooter.rect.bottom, bulletWidth, bulletHeight))

	if ticks() - alienMoveClock > 1000:
		alienMoveClock = ticks()
		for eachAlien in aliens:
			eachAlien.move(screen, alienDirection)
		alienDirectionCounter += 1
		if alienDirectionCounter == 6:
			for eachAlien in aliens:
				eachAlien.move(screen, 0)
			alienDirectionCounter = 0
			alienDirection *= -1		
	
	for eachBullet in bullets:
		eachBullet.advance(screen)
		if eachBullet.rect.bottom == 0:
			bullets.remove(eachBullet)

		barrierHit = eachBullet.rect.collidelist(barriers) # did this bullet hit a barrier? -1 if no (see pygame.Rect docs)
		if barrierHit != -1:
			barriers[barrierHit].degrade(screen)
			bullets.remove(eachBullet)
			pygame.draw.rect(screen, backgroundColor, eachBullet.rect)
			pygame.display.update(eachBullet.rect)
			if barriers[barrierHit].quality == 0:
				del barriers[barrierHit]

		alienHit = eachBullet.rect.collidelist(aliens)
		if alienHit != -1:
			bullets.remove(eachBullet)
			pygame.draw.rect(screen, backgroundColor, eachBullet.rect)
			pygame.display.update(eachBullet.rect)
			pygame.draw.rect(screen, backgroundColor, aliens[alienHit].rect)
			pygame.display.update(aliens[alienHit].rect)
			del aliens[alienHit]

			#TO DO: INCREASE SCORE

	for eachEnemyBullet in enemybullets:
		eachEnemyBullet.advance(screen)		
		if eachEnemyBullet.rect.top == y:
			enemybullets.remove(eachEnemyBullet)

		barrierHit = eachEnemyBullet.rect.collidelist(barriers) # did this bullet hit a barrier? -1 if no (see pygame.Rect docs)
		if barrierHit != -1:
			barriers[barrierHit].degrade(screen)
			enemybullets.remove(eachEnemyBullet)
			pygame.draw.rect(screen, backgroundColor, eachEnemyBullet.rect)
			pygame.display.update(eachEnemyBullet.rect)
			if barriers[barrierHit].quality == 0:
				del barriers[barrierHit]	

		shipHit = eachEnemyBullet.rect.colliderect(ship)	#note colliderect not collidelist
		if shipHit:
			enemybullets.remove(eachEnemyBullet)
			pygame.draw.rect(screen, backgroundColor, eachEnemyBullet.rect)
			pygame.display.update(eachEnemyBullet.rect)

			#TO DO: LOSE A LIFE



	pressedKeys = pygame.key.get_pressed()


	if pressedKeys[pygame.K_SPACE] == 1 and bulletAvailable: #shoot!
		bullets.append(Bullet(screen, ship.rect.centerx, ship.rect.top-bulletHeight, bulletWidth, bulletHeight))
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
