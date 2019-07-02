import random

from src.game_of_life.Cell import Cell


class Board:

    def __init__(self, size: int):
        self.board = self.generate_board(size)
        self.size = size
        self.generation = 0
        self.population = 0

    @staticmethod
    def generate_board(size: int):
        board = []
        for i in range(size):
            board.append([])
            for j in range(size):
                board[i].append(Cell(False, 0, j, i))
        return board

    def print_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].alive:
                    print("X", end=" ")
                else:
                    print("O", end=" ")
            print()

    def print_board_neighbours(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(str(self.board[i][j].number_of_neighbours) + " ", end=" ")
            print()

    @staticmethod
    def random():
        return bool(random.getrandbits(1))

    def get_correct_cell(self, cell_to_check: int):

        if cell_to_check < 0:
            return len(self.board) - 1
        elif cell_to_check == len(self.board):
            return 0
        else:
            return cell_to_check

    def check_for_neighbours(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][self.get_correct_cell(j + 1)].alive:  # right
                    self.board[i][j].number_of_neighbours = self.board[i][j].number_of_neighbours + 1
                if self.board[i][self.get_correct_cell(j - 1)].alive:  # left
                    self.board[i][j].number_of_neighbours = self.board[i][j].number_of_neighbours + 1
                if self.board[self.get_correct_cell(i + 1)][j].alive:  # lower
                    self.board[i][j].number_of_neighbours = self.board[i][j].number_of_neighbours + 1
                if self.board[self.get_correct_cell(i - 1)][j].alive:  # upper
                    self.board[i][j].number_of_neighbours = self.board[i][j].number_of_neighbours + 1
                if self.board[self.get_correct_cell(i + 1)][self.get_correct_cell(j + 1)].alive:  # upper_right
                    self.board[i][j].number_of_neighbours = self.board[i][j].number_of_neighbours + 1
                if self.board[self.get_correct_cell(i - 1)][self.get_correct_cell(j + 1)].alive:  # lower_right
                    self.board[i][j].number_of_neighbours = self.board[i][j].number_of_neighbours + 1
                if self.board[self.get_correct_cell(i - 1)][self.get_correct_cell(j - 1)].alive:  # lower_left
                    self.board[i][j].number_of_neighbours = self.board[i][j].number_of_neighbours + 1
                if self.board[self.get_correct_cell(i + 1)][self.get_correct_cell(j - 1)].alive:  # upper_left
                    self.board[i][j].number_of_neighbours = self.board[i][j].number_of_neighbours + 1

    def update(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if not self.board[i][j].alive:
                    if self.board[i][j].number_of_neighbours == 3:
                        self.board[i][j].alive = True
                if self.board[i][j].alive:
                    if self.board[i][j].number_of_neighbours < 2:
                        self.board[i][j].alive = False
                    if self.board[i][j].number_of_neighbours == 2 or self.board[i][j].number_of_neighbours == 3:
                        self.board[i][j].alive = True
                    if self.board[i][j].number_of_neighbours > 3:
                        self.board[i][j].alive = False
                    if self.board[i][j].alive:
                        self.population += 1
                self.board[i][j].number_of_neighbours = 0
        self.generation += 1

    def reset_neighbours(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j].number_of_neighbours = 0

    def life_cycle(self):
        self.population = 0
        self.check_for_neighbours()
        self.update()
