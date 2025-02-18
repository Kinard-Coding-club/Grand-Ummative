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
#Start
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
    pygame.init()
    
    if process != null:
        print(f"{line}:Heartbeat {counter}: Got a registry event at {last} using {process}")
if __name__ == "__main__":
    main()
#end