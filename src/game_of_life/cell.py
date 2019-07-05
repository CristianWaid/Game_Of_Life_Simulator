class Cell:
    # represents the cells of the Game of Life Simulation
    def __init__(self, alive: bool, number_of_neighbours: int, position_x: int, position_y: int):
        self.alive = alive  # status of cell (alive = True || alive = False )
        self.number_of_neighbours = number_of_neighbours  # current number of alive neighbour cells
        self.position_x = position_x  # saves x-position in 2D List
        self.position_y = position_y  # saves y-position in 2D List
