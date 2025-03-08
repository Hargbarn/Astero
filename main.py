import pygame
from asteroid import Asteroid
from asteroidspawn import AsteroidField
from constants import *
import sys
from player import Player
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black_color = (0, 0, 0)
    time = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable,drawable)

    asteroid = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        screen.fill(black_color)
        for object in drawable:
            object.draw(screen)
        for asteroid in asteroids:
            if asteroid.collision(player):
                sys.exit("Collision !!! Game Over !")
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()
        pygame.display.flip()

        dt = time.tick(60)/1000 # 60 FPS









if __name__ == "__main__":
    main()
