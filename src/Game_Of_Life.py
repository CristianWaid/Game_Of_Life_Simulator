from src.game_of_life.Board import Board

test = Board(int(600 / 20))

print("Position X: " + str(test.board[29][29].position_x))
print("Position Y: " + str(test.board[29][29].position_y))
print("Alive: " + str(test.board[29][29].alive))
print()
test.print_board()
