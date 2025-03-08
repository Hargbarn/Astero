import pygame
from asteroid import Asteroid
from asteroidspawn import AsteroidField
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black_color = (0, 0, 0)
    time = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

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
        pygame.display.flip()

        dt = time.tick(60)/1000 # 60 FPS









if __name__ == "__main__":
    main()
