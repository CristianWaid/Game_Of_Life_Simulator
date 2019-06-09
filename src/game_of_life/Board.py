import random

from src.game_of_life.Cell import Cell


class Board:
    board = []
    population: int
    size: int

    def __init__(self, size: int):
        Board.generate_board(size)
        self.size = size

    @staticmethod
    def generate_board(size: int):
        for i in range(size):
            Board.board.append([])
            for j in range(size):
                Board.board[i].append(Cell(False, 0, j, i))

    @staticmethod
    def print_board():
        for i in range(len(Board.board)):
            for j in range(len(Board.board[i])):
                if Board.board[i][j].alive:
                    print("X", end=" ")
                else:
                    print("O", end=" ")
            print()

    @staticmethod
    def print_board_neighbours():
        for i in range(len(Board.board)):
            for j in range(len(Board.board[i])):
                print(str(Board.board[i][j].number_of_neighbours) + " ", end=" ")
            print()

    @staticmethod
    def random():
        return bool(random.getrandbits(1))

    @staticmethod
    def get_correct_cell(cell_to_check: int):

        if cell_to_check < 0:
            return len(Board.board) - 1
        elif cell_to_check == len(Board.board):
            return 0
        else:
            return cell_to_check

    @staticmethod
    def check_for_neighbours():
        for i in range(len(Board.board)):
            for j in range(len(Board.board[i])):
                if Board.board[i][Board.get_correct_cell(j + 1)].alive:  # right
                    Board.board[i][j].number_of_neighbours = Board.board[i][j].number_of_neighbours + 1
                if Board.board[i][Board.get_correct_cell(j - 1)].alive:  # left
                    Board.board[i][j].number_of_neighbours = Board.board[i][j].number_of_neighbours + 1
                if Board.board[Board.get_correct_cell(i + 1)][j].alive:  # lower
                    Board.board[i][j].number_of_neighbours = Board.board[i][j].number_of_neighbours + 1
                if Board.board[Board.get_correct_cell(i - 1)][j].alive:  # upper
                    Board.board[i][j].number_of_neighbours = Board.board[i][j].number_of_neighbours + 1
                if Board.board[Board.get_correct_cell(i + 1)][Board.get_correct_cell(j + 1)].alive:  # upper_right
                    Board.board[i][j].number_of_neighbours = Board.board[i][j].number_of_neighbours + 1
                if Board.board[Board.get_correct_cell(i - 1)][Board.get_correct_cell(j + 1)].alive:  # lower_right
                    Board.board[i][j].number_of_neighbours = Board.board[i][j].number_of_neighbours + 1
                if Board.board[Board.get_correct_cell(i - 1)][Board.get_correct_cell(j - 1)].alive:  # lower_left
                    Board.board[i][j].number_of_neighbours = Board.board[i][j].number_of_neighbours + 1
                if Board.board[Board.get_correct_cell(i + 1)][Board.get_correct_cell(j - 1)].alive:  # upper_left
                    Board.board[i][j].number_of_neighbours = Board.board[i][j].number_of_neighbours + 1

    @staticmethod
    def update():
        for i in range(len(Board.board)):
            for j in range(len(Board.board[i])):
                if not Board.board[i][j].alive:
                    if Board.board[i][j].number_of_neighbours == 3:
                        Board.board[i][j].alive = True
                if Board.board[i][j].alive:
                    if Board.board[i][j].number_of_neighbours < 2:
                        Board.board[i][j].alive = False
                    if Board.board[i][j].number_of_neighbours == 2 or Board.board[i][j].number_of_neighbours == 3:
                        Board.board[i][j].alive = True
                    if Board.board[i][j].number_of_neighbours > 3:
                        Board.board[i][j].alive = False
        Board.reset_neighbours()

    @staticmethod
    def reset_neighbours():
        for i in range(len(Board.board)):
            for j in range(len(Board.board[i])):
                Board.board[i][j].number_of_neighbours = 0

    def life_cycle(self):
        self.check_for_neighbours()
        self.update()
