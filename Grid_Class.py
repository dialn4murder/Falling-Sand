import pygame
import square


class Grid_Class:
    def __init__(self, width, height):
        # efines the width and height of the application
        self.width = width
        self.height = height
        # Defines an empty and white square based on the square class
        self.empty_square = square.square(0, (0, 0, 0))
        self.white_square = square.square(1, (255, 255, 255))
        # Calculates the maximum width / height of the grid based on application size and area of the squares
        self.column = self.width // self.empty_square.area
        self.row = self.height // self.empty_square.area
        # Creates the grid with empty squares
        self.grid = [[self.empty_square for _ in range(self.column)] for _ in range(self.row)]

    def print_grid(self):
        # Prints the grid based on square id
        for row in range(self.row):
            for column in range(self.column):
                print(self.grid[row][column].square_id, end=" ")
            print()

    def draw(self, screen):
        for row in range(self.row):
            for column in range(self.column):
                # Gets current cell
                cell_val = self.grid[row][column]
                # Defines the cell area
                cell_rect = pygame.Rect(column * self.white_square.area + 1, row * self.white_square.area + 1,
                                        self.white_square.area - 1, self.white_square.area - 1)
                # Draws the square based on the squares colour value
                pygame.draw.rect(screen, cell_val.colour, cell_rect)
                # If its a white square
                if cell_val.square_id == 1:
                    # Makes sure the squares won't go out of bounds
                    if row < self.row-1:
                        # Calls check fall makes sure it has an empty cell below the cell
                        self.check_fall(row, column)

    def draw_cursor(self, x, y):
        # Calculates the grid position based on the x and y value
        row = x // self.empty_square.area
        column = y // self.empty_square.area
        # Makes the cell a white square where the cursor was
        self.grid[column][row] = self.white_square

    def check_fall(self, row, column):
        # Makes sure the cell below is empty
        if self.grid[row + 1][column] == self.empty_square:
            # Adds to the counter which slows the animation
            self.grid[row][column].counter += 1
            # Checks if the counter is dividable
            if self.grid[row][column].is_dividable():
                # Swaps cells
                self.grid[row][column] = self.empty_square
                self.grid[row + 1][column] = self.white_square
