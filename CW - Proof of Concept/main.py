import pygame
import random
import util
from draw import *
from models import *

WIDTH, HEIGHT = 1366, 768
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Civil War")
pygame.init()

MAP = pygame.transform.scale(pygame.image.load("map.png"), (WIDTH*0.85, HEIGHT))

def draw():
    WIN.blit(MAP, (0,0))

    cities = util.load_cities()
    draw_cities(WIN, MAP, cities, (WIDTH*0.85, HEIGHT))

    pygame.display.update()

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw()

    pygame.quit()

if __name__ == "__main__":
    main()