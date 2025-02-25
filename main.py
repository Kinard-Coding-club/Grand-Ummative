#headers
print("----- DO NOT CLOSE THIS WINDOW! -----")
global debug
debug = True
if debug == True:
    print("Debug mode is enabled.")
    print("Importing modules...")
import traceback
import sys
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
def log(Message):
    if debug == True:
        print(Message)
    else:
        pass
log('Initalizing variables...')
# Initialize all variables
global counter, line, last, process, key, location, playerHp, playerX, playerY, playerSpeed, playerJump, playerJumping, tile_size
debug = False
tile_size = 128
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
log("Variables have been initialized. Press [ENTER] at any time to dump variables.")

def draw_tiles(screen, tileset, tile_images):
    for row in range(len(tileset)):
        for col in range(len(tileset[row])):
            tile_type = tileset[row][col]
            if tile_type != 0:  # Skip dead space
                try:
                    tile_image = tile_images[tile_type]
                except KeyError:
                    tile_image = pygame.image.load('/resources/sprites/error.png')
                    print("ERROR! BAD TILE!")
                screen.blit(tile_image, (col * tile_size, row * tile_size))

class scripted():
    def tile(int):
        print(f"Loading scripted entity {int}...") # This is just a placeholder for now.

def load(room):
    global location
    location = 'loader'
    delay = random.randint(5, 8)
    background = pygame.image.load(f"/resources/sprites/loader.gif")
    print(f"Loading room: {room}. Please wait {delay} seconds.")
    time.sleep(delay)
    print(f"Room {room} loaded.")
    location = room

def goto(room):
    global location
    print(f"Room has been changed to Room changed to {room}")
    location = room
    enemy(0, 'destroy')

class player:
    def destroy():
        print("Player has been destroyed")
    
    def kill():
        global playerHp
        playerHp = 0
        if debug != True:
            goto('gameover')
        else:
            print(f"Player has been killed. Player HP is now {playerHp}. Debug flag is set, wfi().")
            value = input("Continue? [Y/N]: ").lower()
            if value == 'y':
                goto('gameover')
            else:
                print("Exiting...")
                sys.exit()
    
    def draw(x, y, handle1, handle2):
        global playerX, playerY, playerJumping
        attacks = {
            0: '/resources/sprites/player.gif',
            1: '/resources/sprites/player_attack2.gif'
        }
        actions = {
            0: {
                'anim': '/resources/sprites/player_swing.gif',
                'script': {
                    "action": "swing",
                    "damage": 10,
                    "cooldown": 1.5
                }
            }
        }
        idle = pygame.image.load('/resources/sprites/player.gif')
        walking = pygame.image.load('/resources/sprites/player_walk.gif')
        player_rect = pygame.Rect(x, y, 50, 50)
        screen.blit(idle, player_rect.topleft)
        print(f"Player drawn at {x}, {y}")

        # Handle player actions
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            playerX -= playerSpeed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            playerX += playerSpeed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            playerY -= playerSpeed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            playerY += playerSpeed
        if keys[pygame.K_SPACE] and not playerJumping:
            playerJumping = True
            playerY -= playerJump

        if playerJumping:
            playerY += playerJump // 2  # Simulate gravity
            if playerY >= 0:  # Assuming ground level is y = 0
                playerY = 0
                playerJumping = False

class enemy:
    enemies = {
        0: {
            'name': 'Example enemy',
            'idle-anim': '/resources/sprites/enemy1.gif',
            'attack-anim': '/resources/sprites/enemy1_attack.gif',
            'health': '100',
            'speed': '0', # 0 is stationary, does not require a movement gif
            'damage': '100'
        },
        1: {
            'name': 'Trap',
            'idle-anim': '/resources/sprites/trap.gif',
            'attack-anim': '/resources/sprites/trap_attack.gif',
            'health': '*', # Means that this enemy cannot be killed
            'speed': '0',
            'damage': f'{playerHp}'
        }
    }
    
    def draw(id, x, y, takesDamage):
        try:
            print(f"Enemy {id} has been spawned at {x}, {y}.")
            pygame.draw.rect(screen, 255, 0, 0), pygame.rect(100, 100, 50, 50)
            player_rect = pygame.Rect(playerX, playerY, 50, 50)
            enemy_rect = pygame.rect(x, y, 50, 50)
            if player_rect.colliderect(enemy_rect):
                goto('gameover')
        except Exception as e:
            print(f"Failed to load entity: {e}")
    
    def destroy(id):
        if id == 'all'.lower():
            for enemy_id in list(enemy.enemies.keys()):
                del enemy.enemies[enemy_id]
            print("All enemies have been destroyed.")
        else:
            if id in enemy.enemies:
                del enemy.enemies[id]
                print(f"Enemy {id} has been destroyed.")
            else:
                print(f"Enemy {id} does not exist.")

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
                    if debug == True:
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

        # Room HANDLER
        if location == 'Menu':
            # Code to draw the menu room
            background = pygame.image.load("/resources/sprites/menu.png")
            screen.blit(background, (0, 0))
            play_button = pygame.image.load("/resources/sprites/play_button.png")
            play_button_rect = play_button.get_rect(center=(400, 300))
            screen.blit(play_button, play_button_rect.topleft)
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()
            
            if play_button_rect.collidepoint(mouse_pos):
                if mouse_click[0]:  # Left mouse button clicked
                    load(1)
        elif location == 'gameover':
            background = pygame.image.load("/resources/sprites/gameover.png")
            screen.blit(background, (0, 0))
            print("Game over. Press [ENTER] to exit.")
            if event.key == pygame.K_RETURN:
                load('1')
        elif location == '0':
            background = pygame.image.load("/resources/sprites/error.png")
            screen.blit(background, (0, 0))

            # Tilesets should always be created like this.
            tiles = {
                1: pygame.image.load('/resources/sprites/grass.png'),
                2: pygame.image.load('/resources/sprites/dirt.png'),
                3: pygame.image.load('/resources/sprites/mossybricks.png'),
                # 1-5 for static tiles, 6-8 for scripted tiles, 9 for spawnpoints. !!!DO NOT DEFINE 9 OR THE GAME WILL BREAK!!!
            }

            tileset = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #Dead space
                [0, 9, 0, 0, 3, 0, 5, 0, 0, 0, 0], #Obstacles
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #Ground
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], #Dirt, stone, ect...
            ]
            # Tilesets are always loaded starting with the bottom left corner of the window.
            draw_tiles(screen, tileset, tiles)

            enemy(0, 'draw', 150, 150)
            player(70, 50)
        elif location == '1':
            background = pygame.image.load("/resources/sprites/room1.png")
            screen.blit(background, (0, 0))
            tiles = {
                1: pygame.image.load('/resources/sprites/grass.png'),
                2: pygame.image.load('/resources/sprites/dirt.png'),
                3: pygame.image.load('/resources/sprites/dark.png'),
                4: pygame.image.load('/resources/sprites/stonebricks.png'),
                6: pygame.image.load('/resources/sprites/branch.png')
            }
            tileset = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 9, 9, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
            ]
            draw_tiles(screen, tileset, tiles)
            player.draw(70, 50, 'player', 'player')
            enemy.draw(1, 150, 150, True)

    pygame.quit()
    sys.exit()
    print(10/0) # This line will never be reached as it is placed after an exit statement. Its just a joke.

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