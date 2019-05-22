class Cell:
    alive: bool = False
    number_of_neighbours: int = 0

    def __init__(self, alive: bool, number_of_neighbours: int):
        self.alive = alive
        self.number_of_neighbours = number_of_neighbours
