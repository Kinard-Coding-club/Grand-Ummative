# Initalize
print("----- DO NOT CLOSE THIS WINDOW! -----")
print("0:Heartbeat 0: Got a registry event for start at root line")
# Headers
import subprocess
import sys
import pygame
import traceback

# Ensure that heartbeat variables are set properly
counter = 0
line = 0 
last = 'null'
process = 'null'

def main():
    global counter, line, last, process  
    print("1:Heartbeat 0: Got a registry event for counter, line, last, process, at Def-global")
    pygame.init()
    print("2:Heartbeat 0  Got a registry event for Initialized, at Pygame")

    # Set up a Pygame window
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("WHEN I TOLD YOU BRING ME THE PRINCESS I DIDNT MEAN BRING HER IN A BODY BAG!")

    running = True
    try:
        while running:
            counter += 1  # Increment counter every loop
            
            try:
                input_detected = False
                # Define possible expected events
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
                
                if input_detected:
                    print(f"{line}: Heartbeat {counter}: Got a registry event for {last} at {process}")
                    line += 1 
            
            except Exception as e:
                print(f"Error in event handling: {e}")
                print(traceback.format_exc())
                
            # \/ Main code goes below this comment \/

    except KeyboardInterrupt:
        print("\nHeartbeat Worker stopped by user.")
    except Exception as e:
        print(f"Critical Error: {e}")
        print(traceback.format_exc())
    finally:
        pygame.quit()
        print(f"Heartbeat: Worker stopped at {counter} on {last} at {process}.")
    
# Make sure the entry point is execution before executing main code
if __name__ == "__main__":
    main()
