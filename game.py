from chess_logic import Board, Rook, Pawn  # Importing the necessary classes

class Game:
    def __init__(self):
        self.board = Board()  # Create a new chessboard
        self.turn = "white"   # White goes first

    def switch_turn(self):
        # Switch turns after a move
        self.turn = "black" if self.turn == "white" else "white"

    def make_move(self, piece, new_position):
        # Ensure the move is valid before updating the board
        x, y = piece.position
        if new_position in piece.get_valid_moves(self.board):
            self.board.board[x][y] = None  # Clear old position
            piece.position = new_position  # Move the piece
            self.board.board[new_position[0]][new_position[1]] = piece  # Place it in the new position
            self.switch_turn()
            return True
        return False
