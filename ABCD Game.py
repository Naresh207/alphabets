import pygame
import random
import string
import sys
import pyttsx3

# Initialize pygame
pygame.init()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ABCD Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont(None, 100)

def display_letter():
    return random.choice(string.ascii_uppercase)

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def speak_letter(letter):
    # Set speech rate and volume
    engine.setProperty('rate', 150)  # Adjust speech rate (words per minute)
    engine.setProperty('volume', 1.0)  # Adjust volume (0.0 to 1.0)
    
    engine.say(letter)
    engine.runAndWait()

def play_game():
    running = True
    clock = pygame.time.Clock()
    
    while running:
        screen.fill(WHITE)
        
        letter = display_letter()
        draw_text(letter, font, BLACK, screen_width // 2, screen_height // 2)
        
        pygame.display.flip()

        speak_letter(letter)
        
        pygame.time.wait(1000)  # Wait for 1 second before showing the next letter
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

        clock.tick(5)  # Control the speed of letter changes

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    play_game()
