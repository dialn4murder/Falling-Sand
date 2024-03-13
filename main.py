import pygame
import Grid_Class

# Typical pygame boilerplate
pygame.init()
screen_width = 720
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

# Calls the grid class which creates the grid and draws onto the grid
game_grid = Grid_Class.Grid_Class(screen_width, screen_height)

while running:

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # When left mouse is pressed it will get the position of the mouse
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            # It will call the method to draw a square where the mouse was
            game_grid.draw_cursor(pos[0], pos[1])

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    # Draws the grid, empty squares and white squares
    game_grid.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
game_grid.print_grid()
