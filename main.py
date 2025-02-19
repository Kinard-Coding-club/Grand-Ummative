# Headers
import pygame
import traceback
import sys
import os
import random
import time

# Initialize all variables

global counter, line, last, process, key, location
counter = 0
line = 0
last = 'null'
process = 'null'
key = 'null'
location = 'loader'

#Start
print("----- DO NOT CLOSE THIS WINDOW! -----")
def main():
    global counter, line, last, process, key, location  # Declare global variables
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("🗿 I ate the name for lunch. Good game I promise")
    
    running = True
    while running:
        # Define all Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    last = 'K_RETURN'
                    process = 'KEYDOWN-HANDLER'
                    key = 'RETURN'
                elif event.key == pygame.K_ESCAPE:
                    key = 'ESCAPE'
                    last = 'K_ESCAPE'
                    process = 'KEYDOWN-HANDLER'
                    location = 'pause'
                elif event.key in (pygame.K_UP, pygame.K_w):
                    key = 'UP'
                    last = 'K_UP or K_w'
                    process = 'KEYDOWN-HANDLER'
                    location = 'move_up'
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    key = 'DOWN'
                    last = 'K_DOWN or K_s'
                    process = 'KEYDOWN-HANDLER'
                    location = 'move_down'
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    key = 'LEFT'
                    last = 'K_LEFT or K_a'
                    process = 'KEYDOWN-HANDLER'
                    location = 'move_left'
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    key = 'RIGHT'
                    last = 'K_RIGHT or K_d'
                    process = 'KEYDOWN-HANDLER'
                    location = 'move_right'
                elif event.key == pygame.K_SPACE:
                    key = 'SPACE'
                    last = 'K_SPACE'
                    process = 'KEYDOWN-HANDLER'
                    location = 'jump'
                else:
                    counter += 1
                    line += 1
                    last = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    process = 'KEYDOWN'
        
        screen.fill((0, 0, 0))
        pygame.display.flip()
        # Code under here
        def player():
            print(f"{line}:Heartbeat {counter}: Player is at {location}")
        
        def enemy(name):
            if name == 0:
                print("Example enemy")
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(100, 100, 50, 50))
            elif name == 1:
                print("Enemy 1 has been spawned.")
                sprite1 = "/resources/sprites/enemy1.png"
                print(f"{sprite1}")
            else:
                print("Error, enemy does not exist.")
        
        player()
        if process != 'null':
            print(f"{line}:Heartbeat {counter}: Got a registry event at {last} using {process}")
    
    pygame.quit()
    print(10/0)
    sys.exit()

if __name__ == "__main__":
    main()
#end