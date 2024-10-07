import pygame
import pygame_gui
from con_mgr import *
import asyncio
from pygame_gui.core import ObjectID

class UIGod:
    def __init__(self):
        self.WIDTH = None
        self.HEIGHT = None
        self.main_surface = None
        self.manager = None
        self.MAP = None
        self.map_update = False
        self.main_menu_panel = None
        self.ip_input = None
        self.connect_btn = None
        self.name_input = None
        self.game_interface = None
        self.actions_rect = None
        self.troop_move_btn = None
        self.chat_btn = None

        pygame.display.set_caption("Civil War")

    def update(self, time_delta):
        self.manager.update(time_delta)

        if self.map_update:
            self.main_surface.blit(self.MAP, (0,0))
        self.manager.draw_ui(self.main_surface)
        pygame.display.update()

    def set_resolution(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        self.main_surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'theme.json')

        self.gen_game_interface()
        self.gen_main_menu()
        

    def gen_main_menu(self):
        self.main_menu_panel=pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect((0,0), (self.WIDTH, self.HEIGHT)),
            starting_height=10,
            manager=self.manager
        )

        main_menu_title=pygame_gui.elements.UITextBox(
            html_text="Civil War Game",
            relative_rect=pygame.Rect((self.WIDTH/3, self.HEIGHT*0.1), (self.WIDTH/3, self.HEIGHT*0.2)),
            starting_height=11,
            manager=self.manager,
            container=self.main_menu_panel,
            object_id=ObjectID(object_id='#large_textbox')
        )

        ip_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.WIDTH/3, self.HEIGHT*0.2), (self.WIDTH/3, self.HEIGHT*0.25)),
            text="Enter IP Address:",
            manager=self.manager,
            container=self.main_menu_panel,
            object_id=ObjectID(object_id='#main_menu_label')
        )

        print(self.WIDTH, self.HEIGHT, self.main_menu_panel.relative_rect.width, self.main_menu_panel.relative_rect.height)
        self.ip_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((self.WIDTH*0.4, self.HEIGHT*0.35), (self.WIDTH*0.2, self.HEIGHT*0.05)),
            manager=self.manager,
            container=self.main_menu_panel,
            #object_id=ObjectID(object_id='#main_menu_input')
        )

        name_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.WIDTH/3, self.HEIGHT*0.32), (self.WIDTH/3, self.HEIGHT*0.25)), 
            text="Enter name:",
            manager=self.manager,
            container=self.main_menu_panel,
            object_id=ObjectID(object_id='#main_menu_label')
        )

        self.name_input=pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((self.WIDTH*0.4, self.HEIGHT*0.48), (self.WIDTH*0.2, self.HEIGHT*0.05)),
            manager=self.manager,
            container=self.main_menu_panel,
            #object_id=ObjectID(object_id='#main_menu_input')
        )

        self.connect_btn=pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.WIDTH*0.44, self.HEIGHT*0.58), (self.WIDTH*0.12, self.HEIGHT*0.05)), 
            text='Connect', 
            container=self.main_menu_panel,
            manager=self.manager
        )
    
    def close_main_menu(self):
        self.main_menu_panel.hide()
        self.gen_game_interface()
        pygame.display.update()

    def gen_game_interface(self):
        if self.MAP is None:
            self.MAP = pygame.transform.scale(pygame.image.load("Resources\map.png"), (self.WIDTH*0.85, self.HEIGHT))
        else:
            self.MAP = pygame.transform.scale(self.MAP, (self.WIDTH*0.85, self.HEIGHT))

        self.game_interface = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(0, 0, self.WIDTH, self.HEIGHT),
            starting_height=0,
            manager=self.manager,
            object_id=ObjectID(object_id='#transparent_panel')
        )
        
        self.actions_rect = pygame_gui.elements.UIPanel(
            relative_rect= pygame.Rect(self.WIDTH*0.85, self.HEIGHT*0.4, self.WIDTH*0.15, self.HEIGHT*0.6),
            starting_height=1,
            manager=self.manager,
            container=self.game_interface
        )

        self.troop_move_btn = pygame_gui.elements.UIButton(
            relative_rect=((50, 10)), 
            text='Move', 
            container=self.actions_rect, 
            manager=self.manager
        )

        self.chat_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((10, 100), (50, 30)), 
            text='Chat', 
            starting_height=2,
            container=self.actions_rect, 
            manager=self.manager
        )

        self.main_surface.blit(self.MAP, (0,0))
        pygame.display.update()

    def process_event(self, event):
        # BUTTON EVENTS
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.connect_btn:
                print('Connecting...')
                ip = self.ip_input.text
                name = self.name_input.text
                asyncio.run(Connection_Manager.send_message(ip, name, f'Hello! This is player {name}. Its great to connect :)'))

                self.close_main_menu()

            elif event.ui_element == self.chat_btn:
                print()

