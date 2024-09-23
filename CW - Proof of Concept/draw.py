import pygame

def draw_cities(WIN, MAP, cities, map_size):
    for city in cities:
        x, y = (map_size[0]*(city.position[0]/3203)), (map_size[1]*(city.position[1]/2414))

        pygame.draw.circle(MAP, (0,0,0), (x,y), 5)
        pygame.draw.circle(MAP, (120,23,5), (x,y), 4)

        font = pygame.font.SysFont('Georgia', int(map_size[1]/50))
        text = font.render(city.name, False, (0,0,0))
        text_rect = text.get_rect()
        text_rect.centerx = x
        text_rect.y = y+2

        WIN.blit(text, text_rect)

    pygame.display.update()
    return