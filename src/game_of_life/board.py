from src.game_of_life.cell import Cell


# represents the board of the Game of Life Simulation
class Board:

    def __init__(self, size: int):
        self.board = self.generate_board(size)
        self.size = size  # size of the board
        self.generation = 0  # current generation
        self.population = 0  # current population

    # generates a board with "dead" Cells (called in "__init__" method)
    @staticmethod
    def generate_board(size: int):
        board = []
        for i in range(size):
            board.append([])
            for j in range(size):
                board[i].append(Cell(False, 0, j, i))
        return board

    # prints the board to the console (replaced by Tkinter GUI, useful for debugging)
    def print_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].alive:
                    print("X", end=" ")
                else:
                    print("O", end=" ")
            print()

    # prints number of neighbours for each Cell (for debugging)
    def print_board_neighbours(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(str(self.board[i][j].number_of_neighbours) + " ", end=" ")
            print()

    # returns a valid list index (to avoid index out of bounds)
    def get_correct_cell(self, cell_to_check: int):
        if cell_to_check < 0:
            return len(self.board) - 1
        elif cell_to_check == len(self.board):
            return 0
        else:
            return cell_to_check

    # count and set number of alive Cells for each Cell in 2D-List
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

    # implementation of the Game of Life rules
    # updates the board (sets Cells to alive = True || alive = False & resets the number of neighbours)
    # counts population and generation
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

    # simulates a whole lifecycle
    def life_cycle(self):
        self.population = 0
        self.check_for_neighbours()
        self.update()
