class Cell:
    alive: bool = False
    number_of_neighbours: int = 0

    def __init__(self, alive: bool, number_of_neighbours: int, position_x: int, position_y: int):
        self.alive = alive
        self.number_of_neighbours = number_of_neighbours
        self.position_x = position_x
        self.position_y = position_y
