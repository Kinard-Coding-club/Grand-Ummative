import subprocess
import sys
import pygame

# Ensure that heartbeat variables are set properly
counter = 0
last = 'null'
process = 'null'

def main():
    global counter, last, process
    
    print("----- DO NOT CLOSE THIS WINDOW! -----")
    print("Initialized pygame")
    pygame.init()

    # Set up a Pygame window (even if not displayed)
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Heartbeat Worker")
    
    running = True
    while running:
        input_detected = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                last = "QUIT"
                process = "Pygame Event Loop"
                input_detected = True
            elif event.type == pygame.KEYDOWN:
                last = f"KEYDOWN {event.key}"
                process = "Keyboard Input"
                input_detected = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                last = f"MOUSEBUTTONDOWN {event.button}"
                process = "Mouse Input"
                input_detected = True
        
        if not input_detected:
            last = 'null'
            process = 'null'
        
        # Heartbeat worker and indicator
        print(f"Heartbeat {counter}: Got a registry event for {last} at {process}")
        counter += 1
        
        pygame.time.delay(1000)  # Delay to prevent spamming the console

    pygame.quit()
    print(f"Heartbeat worker stopped after {counter} heartbeats.")

# Make sure the entry point is execution before executing main code
if __name__ == "__main__":
    main()
