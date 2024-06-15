import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('CTF Challenge')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Flag details
flag_hidden = True
flag_text = "OSCTF{1_5W3ar_I_D1dn'7_BruT3f0rc3}"
hidden_combination = ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right']
input_combination = []

# Player details
player_size = 50
player_pos = [screen_width // 2, screen_height // 2]
player_color = BLUE
player_speed = 5

# Load background image
background_image = pygame.image.load('background.png')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

def show_message(text, font, color, pos):
    message = font.render(text, True, color)
    screen.blit(message, pos)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                input_combination.append('up')
            elif event.key == pygame.K_DOWN:
                input_combination.append('down')
            elif event.key == pygame.K_LEFT:
                input_combination.append('left')
            elif event.key == pygame.K_RIGHT:
                input_combination.append('right')

            # Check if the input combination matches the hidden combination
            if input_combination == hidden_combination:
                flag_hidden = False
            # Limit the input combination length to avoid unnecessary growth
            if len(input_combination) > len(hidden_combination):
                input_combination.clear()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # Ensure player stays within the screen bounds
    player_pos[0] = max(0, min(player_pos[0], screen_width - player_size))
    player_pos[1] = max(0, min(player_pos[1], screen_height - player_size))

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Display the flag if the combination is unlocked
    if flag_hidden:
        show_message("Find the hidden combination to reveal the flag!", small_font, WHITE, (50, 50))
    else:
        show_message(flag_text, small_font, WHITE, (0, 0))

    # Draw the player
    pygame.draw.rect(screen, player_color, (*player_pos, player_size, player_size))

    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)
