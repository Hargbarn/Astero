import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black_color = (0, 0, 0)
    time = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)
        screen.fill(black_color)
        player.draw(screen)
        pygame.display.flip()

        dt = time.tick(60)/1000 # 60 FPS









if __name__ == "__main__":
    main()
