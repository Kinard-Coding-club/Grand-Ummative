# Headers
import pygame
import traceback
import sys
import os
import random
import time

# Initialize all variables
counter = 0
line = 0
last = 'null'
process = 'null'
docker = 'false'

# Start
print("----- DO NOT CLOSE THIS WINDOW! -----")
if os.name == 'nt':
    print("Using NTOS (Not a dockerable!)")
else:
    print("Using Linux. Checking /dev directory")
    if os.name != 'nt':
        if os.path.exists('/dev'):
            print("/dev directory exists.")
        else:
            print("/dev directory does not exist. Entering web mode...")
            docker = 'true'

def main():
    if docker == 'true':
        import pygameweb
        pygameweb.init()
        pygame.init()
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Pygame Web Example")

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((0, 0, 0))
            pygame.display.flip()

        pygame.quit()
    else:
        pygame.init()
        if process != 'null':
            print(f"{line}:Heartbeat {counter}: Got a registry event at {last} using {process}")

if __name__ == "__main__":
    main()
#end