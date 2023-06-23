# Maap, row sama col nya kebalek, otakku ikut kebalek :v #males_ngebenerin
import pygame
import time
import Matchstick01, Matchstick02, Matchstick03

matchstick_kepake = Matchstick02

# Font
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 20)

# Dimensions of the screen
screen_width = 800
screen_height = 800

# Colors
background_color = (255, 255, 255)  # White
matchstick_color = (165, 42, 42)  # Brown
grid_color_light = (255, 255, 255)  # Light color for grid squares
grid_color_dark = (200, 200, 200)  # Dark color for grid squares
border_color = (0, 0, 0)  # Border color

# Grid parameters
grid = 5
row_grid_size = max(ord(pair[0][1]) - ord('1') for pair in matchstick_kepake.new_stack) + 1  # Count the maximum row index
col_grid_size = max(ord(pair[0][0]) - ord('A') for pair in matchstick_kepake.new_stack) + 1  # Count the maximum column index
# grid_cell_size = screen_height // (grid_size * 2)
grid_cell_size = screen_height // 15

# Border width
border_width = 2

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Matchstick Animation")

scroll_x = 0
scroll_y = 0
scroll_speed = 5  # Adjust this value as desired

for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            scroll_y -= scroll_speed
        elif event.key == pygame.K_DOWN:
            scroll_y += scroll_speed
        elif event.key == pygame.K_LEFT:
            scroll_x -= scroll_speed
        elif event.key == pygame.K_RIGHT:
            scroll_x += scroll_speed
scroll_x = max(0, min(scroll_x, screen_height - screen_width))
scroll_y = max(0, min(scroll_y, screen_width - screen_height))

screen.blit(screen, (0, 0), (scroll_x, scroll_y, screen_width, screen_height))

# Set the background color
screen.fill(background_color)

# Calculate the position of the grid at the center of the screen
grid_x = (screen_width - (grid_cell_size * row_grid_size)) // 2
grid_y = (screen_height - (grid_cell_size * col_grid_size)) // 2

# Main animation loop
running = True
burning = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if the matchstick is not burning
    if not burning:
        # Delay for a short time before starting the animation
        time.sleep(1)
        burning = True

    else:
        # Clear the screen
        screen.fill(background_color)

        # Draw the border
        pygame.draw.rect(screen, border_color, (grid_x - border_width, grid_y - border_width, grid_cell_size * col_grid_size + 2 * border_width, grid_cell_size * row_grid_size + 2 * border_width), border_width)

        # Draw the grid
        for row in range(row_grid_size):
            for col in range(col_grid_size):
                if (row + col) % 2 == 0:
                    pygame.draw.rect(screen, grid_color_light, (grid_x + col * grid_cell_size, grid_y + row * grid_cell_size, grid_cell_size, grid_cell_size))
                else:
                    pygame.draw.rect(screen, grid_color_dark, (grid_x + col * grid_cell_size, grid_y + row * grid_cell_size, grid_cell_size, grid_cell_size))

        # Draw the text (buat A,B,C,D,E,F,G) 
        for row in range(col_grid_size):
            text_surface = my_font.render(chr(row + 65), False, (0, 0, 0))
            screen.blit(text_surface, (grid_x + grid_cell_size // 3 + row * grid_cell_size, grid_y - 30))
        
            # text_surface = my_font.render(str(matchstick_kepake.rCounts), False, (0, 0, 0))
            # screen.blit(text_surface, (grid_x + grid_cell_size // 3 + row * grid_cell_size, grid_y - 30))
            
        for row in range(row_grid_size):
            text_surface = my_font.render(str(row + 1), False, (0, 0, 0))
            screen.blit(text_surface, (grid_x - 20, grid_y + grid_cell_size // 3 + row * grid_cell_size))
            
            # text_surface = my_font.render(str(matchstick_kepake.cCounts), False, (0, 0, 0))
            # screen.blit(text_surface, (grid_x + 60, grid_y + grid_cell_size // 3 + col * grid_cell_size))


        # Matchstick input (terserah mau diganti file yg mana)
        matchsticks = matchstick_kepake.new_stack
        
        for start, end in matchsticks:
            start_row = int(start[1]) - 1
            start_col = ord(start[0]) - 65
            end_row = int(end[1]) - 1
            end_col = ord(end[0]) - 65

            start_x = grid_x + start_col * grid_cell_size + grid_cell_size // 2
            start_y = grid_y + start_row * grid_cell_size + grid_cell_size // 2
            end_x = grid_x + end_col * grid_cell_size + grid_cell_size // 2
            end_y = grid_y + end_row * grid_cell_size + grid_cell_size // 2

            pygame.draw.line(screen, matchstick_color, (start_x, start_y), (end_x, end_y), 5)
            pygame.draw.circle(screen, matchstick_color, (start_x, start_y), 10)

        pygame.display.update()

        burning = False

    time.sleep(0.5)
pygame.quit()