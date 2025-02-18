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
    pygame.display.set_caption("🗿 I ate the name for lunch. Good game, I promise!")
    
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
                else:
                    counter += 1
                    line += 1
                    last = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    process = 'KEYDOWN'
        
        screen.fill((0, 0, 0))
        pygame.display.flip()
        
        if process != 'null':
            print(f"{line}:Heartbeat {counter}: Got a registry event at {last} using {process}")
    
    pygame.quit()
    sys.exit()
    print(10/0)

if __name__ == "__main__":
    main()
#end