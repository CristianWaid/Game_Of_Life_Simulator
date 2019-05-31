from src.game_of_life.Board import Board

test = Board(4)


def start_game():
    for i in range(5):
        print("xxxxxxxx")
        test.print_board()
        print()
        print()
        test.check_for_neighbours()
        test.print_board_neighbours()
        print()
        print()
        test.update()
