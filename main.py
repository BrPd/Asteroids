import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	time_obj = pygame.time.Clock()
	dt = 0 # delta time

	
#-----------------game loop---------------------
	while True:
		for event in pygame.event.get():  # makes the window's close button work
			if event.type == pygame.QUIT:
				return
		
		updatable.update(dt)
		
		for asteroid in asteroids:
			if asteroid.collides_with(player):
				print("Game over!")
				sys.exit()
			for shot in shots:
				if shot.collides_with(asteroid):
					asteroid.split()
					shot.kill()

		screen.fill("black")
		for obj in drawable:
			obj.draw(screen)
		pygame.display.flip()  # refreshes screen
		
		# limit the framerate to 60 FPS 
		dt = time_obj.tick(60) / 1000  # millisec => sec
		# dt is smaller on a fast computer (because frames update more frequently), 
		# or larger on a slower computer (because frames take longer), 
		# using dt in your calculations keeps the "real-world" timing consistent.


if __name__ == "__main__":
    main()
