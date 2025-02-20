#headers
global debug
debug = True
import traceback
import sys
import os
import random
import time
try:
    import pygame
    if not pygame.display.get_init():
        raise ImportError("Pygame display module could not be initialized.")
except ImportError as e:
    print(f"Error: {e}")
    if debug == True:
        print("Logic and console will still execute.")
    else:
        print("Exiting...")
        sys.exit()
#Headers end

# Initialize all variables

global counter, line, last, process, key, location, playerHp, playerX, playerY, playerSpeed, playerJump, playerJumping
debug = False
counter = 0
line = 0
last = 'null'
process = 'null'
key = 'null'
location = 'loader'
playerHp = 100
playerX = 0
playerY = 0
playerSpeed = 5
playerJump = 10
playerJumping = False
#Start
print("----- DO NOT CLOSE THIS WINDOW! -----")
print("Console has been opened. Press [Enter] to dump all variables.")
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
                    print(f"counter: {counter}, line: {line}, last: {last}, process: {process}, key: {key}, location: {location}, playerHp: {playerHp}, playerX: {playerX}, playerY: {playerY}, playerSpeed: {playerSpeed}, playerJump: {playerJump}, playerJumping: {playerJumping}, debug: {debug}")
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
        def goto(room):
            print(f"Room has been changed to Room changed to {room}")
            location = room
            enemy(0, 'destroy')
        
        if location == 'Menu':
            # Code to draw the menu room
            background = pygame.image.load("/resources/sprites/menu.png")
            screen.blit(background, (0, 0))


        def player():
            print(f"{line}:Heartbeat {counter}: Player is at {location}")
        
        def killPlayer():
            playerHp = 0
            if debug == True:
                print(f"Got a player kill event. Player HP is now {playerHp}. Debug flag is set, wfi.")
                input("Press enter to continue...")
                goto('gameover')
            print(f"Got a player kill event. Player HP is now {playerHp}. Debug flag is not set, automatically changing rooms.")
            goto('gameover')
            

        
        def enemy(name, func):
            if func == 'draw':
                if name == 0:
                    print("Example enemy")
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(100, 100, 50, 50))
                    player_rect = pygame.Rect(playerX, playerY, 50, 50)
                    enemy_rect = pygame.Rect(100, 100, 50, 50)
                    if player_rect.colliderect(enemy_rect):
                        killPlayer()
                elif name == 1:
                    print("Enemy 1 has been spawned.")
                    sprite1 = "/resources/sprites/enemy1.png"
                    try:
                        print(f"{sprite1}")
                    except:
                        print("Failed to load sprite.")
                        pygame.draw.circle(screen, (0, 255, 0), (150, 150), 25)
                else:
                    print("Error, enemy does not exist.")
            elif func == 'destroy':
                if name == 0:
                    print("All instances under Enemy have been destroyed")
                elif name == 1:
                    print("Enemy 1 has been destroyed.")
                else:
                    print("Error, enemy does not exist.")
        enemy(0)
        if playerHp == 0:
            goto('gameover')

        player()
        # Code above here
        if process != 'null':
            print(f"{line}:Heartbeat {counter}: Got a registry event at {last} using {process}")
    
    pygame.quit()
    print(10/0) # This is just a joke
    sys.exit()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"exception: {e}")
        if debug == True:
            print("All other logic will be executed.")
        else:
            print("Exiting...")
            sys.exit()
#end