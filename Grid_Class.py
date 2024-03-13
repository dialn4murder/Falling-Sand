import pygame
import square


class Grid_Class:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.empty_square = square.square(0, (0, 0, 0))
        self.white_square = square.square(1, (255, 255, 255))
        self.column = self.width // self.empty_square.area
        self.row = self.height // self.empty_square.area
        self.grid = [[self.empty_square for _ in range(self.column)] for _ in range(self.row)]

    def print_grid(self):
        for row in range(self.row):
            for column in range(self.column):
                print(self.grid[row][column].square_id, end=" ")
            print()

    def draw(self, screen):
        for row in range(self.row):
            for column in range(self.column):
                cell_val = self.grid[row][column]
                cell_rect = pygame.Rect(column * self.white_square.area + 1, row * self.white_square.area + 1,
                                        self.white_square.area - 1, self.white_square.area - 1)
                pygame.draw.rect(screen, cell_val.colour, cell_rect)
                if cell_val.square_id == 1:
                    if row < self.row-1:
                        self.check_fall(row, column)

    def draw_cursor(self, x, y):
        row = x // self.empty_square.area
        column = y // self.empty_square.area
        self.grid[column][row] = self.white_square

    def check_fall(self, row, column):
        if self.grid[row + 1][column] == self.empty_square:
            self.grid[row][column].counter += 1
            print(self.grid[row][column].counter)
            if self.grid[row][column].is_dividable():
                self.grid[row][column] = self.empty_square
                self.grid[row + 1][column] = self.white_square
