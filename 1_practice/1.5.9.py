import random

class Cell:

    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:

    COORD_LST = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    def __init__(self, N, M):
        self.N, self.M = N, M
        self.pole = [[Cell() for _ in range(self.N)] for _ in range(self.N)]
        self.init()

    def mine_cell(self, cell, row, column):
        cell.mine = True
        cell.around_mines = 0
        self.M -= 1
        for r, c in self.COORD_LST:
            if (0 <= row+r <= self.N-1 and 0 <= column+c <= self.N-1) and not self.pole[row+r][column+c].mine:
                self.pole[row+r][column+c].around_mines += 1
        return False if self.M else True

    def init(self):
        row = 0
        stop = False
        while not stop and row < len(self.pole):
            column = 0
            for cell in self.pole[row]:
                if random.randint(0, 1):
                    stop = self.mine_cell(cell, row, column)
                if stop:
                    break
                column += 1
            row += 1

    def show(self):
        for row in self.pole:
            for column in row:
                print(column.around_mines, end=' ') if column.fl_open else print('#', end=' ')
            print()


pole_game = GamePole(10, 12)
