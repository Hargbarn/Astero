import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black_color = (0, 0, 0)
    pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(black_color)
        pygame.display.flip()
        dt = pygame.time.Clock().tick(60)/1000 # 60 FPS









if __name__ == "__main__":
    main()
