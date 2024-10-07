from client_imports import *


GUI_EVENTS = [
    pygame_gui.UI_BUTTON_PRESSED
]

def main():
    WIDTH, HEIGHT = 1366, 768

    pygame.init()
    ui_god = UIGod()
    ui_god.set_resolution(WIDTH, HEIGHT)

    clock = pygame.time.Clock()

    run=True
    while run:
        time_delta = clock.tick(60)/1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type in GUI_EVENTS:
                ui_god.process_event(event)

            ui_god.manager.process_events(event)

        ui_god.update(time_delta)

    pygame.quit()





if __name__ == "__main__":
    main()