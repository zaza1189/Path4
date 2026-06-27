class Matrix:

    def __init__(self, draws):
        self.grid = []

        for draw in draws:
            self.grid.append(draw.cards)

    def rows(self):
        return len(self.grid)

    def cols(self):
        if len(self.grid) == 0:
            return 0
        return len(self.grid[0])

    def get(self, row, col):
        return self.grid[row][col]

    def print(self):
        print("=== Matrix ===")

        for row in self.grid:
            print(" ".join(row))