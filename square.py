class square:
    def __init__(self, square_id, colour):
        self.square_id = square_id
        self.counter = 0
        self.colour = colour
        self.area = 10

    def is_dividable(self):
        if self.counter % 5 == 0:
            return True
        return False

