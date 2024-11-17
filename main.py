from constants import *
from player import Player 
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import pygame
import sys

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))

        for thing in updatable:
            thing.update(dt)

        for thing in asteroids:
            if thing.collision(player):
                print("Game over!")
                sys.exit(0)

            for shot in shots:
                if thing.collision(shot):
                    shot.kill()
                    thing.split()

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        delta = clock.tick(60)
        dt = delta / 1000

if __name__ == "__main__":
    main()
