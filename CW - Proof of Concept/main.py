import pygame
import pygame_gui
import random
import util
import time
import multiprocessing
from draw import *
from models import *

WIDTH, HEIGHT = 1366, 768
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Civil War")
pygame.init()

MAP = pygame.transform.scale(pygame.image.load("map.png"), (WIDTH*0.85, HEIGHT))

manager = pygame_gui.UIManager((WIDTH, HEIGHT))

def second_window():
    pygame.init()
    screen = pygame.display.set_mode((200,200))
    pygame.display.set_caption("Second Window")

    time.sleep(0.5)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0,128,128))
        pygame.display.flip()

    pygame.quit()

# def draw():
#     WIN.blit(MAP, (0,0))

#     cities = util.load_cities()

#     draw_cities(WIN, MAP, cities, (WIDTH*0.85, HEIGHT))

#     pygame.display.update()

def main():

    cities = util.load_cities()

    # button_width, button_height = 100, 50
    # button_color = (0, 255, 0)
    # button_rect = pygame.Rect(WIDTH - button_width - 20, HEIGHT - button_height - 20, button_width, button_height)
    # button_font = pygame.font.Font(None, 36)
    # button_text = button_font.render("Open Window", True, (255, 255, 255))

    hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                                text='Say Hello',
                                                manager=manager)


    run = True
    
    clock = pygame.time.Clock()
    second_window_opened = False
    
    while run:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
              if event.ui_element == hello_button:
                  print('Hello World!')
            manager.process_events(event)

        manager.update(time_delta)

        WIN.blit(MAP, (0,0))
        manager.draw_ui(WIN)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()