class Piece:
    def __init__(self, color, position):
        self.color = color  # 'white' or 'black'
        self.position = position

    def get_valid_moves(self, board):
        raise NotImplementedError("This method should be implemented by subclasses")

class Pawn(Piece):
    def __str__(self):
        return "P" if self.color == "white" else "p"
    
    def get_valid_moves(self, board):
        valid_moves = []
        x, y = self.position
        direction = -1 if self.color == "white" else 1  # White pawns move up, black pawns move down

        # Move forward one square
        if board.is_valid_position(x + direction, y) and board.is_empty(x + direction, y):
            valid_moves.append((x + direction, y))

        # Move forward two squares from starting position
        if (self.color == "white" and x == 6 or self.color == "black" and x == 1) and board.is_empty(x + direction, y) and board.is_empty(x + 2 * direction, y):
            valid_moves.append((x + 2 * direction, y))

        # Capture diagonally
        for dy in [-1, 1]:
            nx, ny = x + direction, y + dy
            if board.is_valid_position(nx, ny) and board.is_occupied_by_enemy(nx, ny, self.color):
                valid_moves.append((nx, ny))

        return valid_moves


class Rook(Piece):
    def __str__(self):
        return "R" if self.color == "white" else "r"
    
    def get_valid_moves(self, board):
        # Rook moves horizontally or vertically
        valid_moves = []
        x, y = self.position

        # Check moves in all 4 directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x, y
            while True:
                nx += dx
                ny += dy
                if board.is_valid_position(nx, ny) and board.is_empty(nx, ny):
                    valid_moves.append((nx, ny))
                elif board.is_occupied_by_enemy(nx, ny, self.color):
                    valid_moves.append((nx, ny))
                    break
                else:
                    break

        return valid_moves


class Knight(Piece):
    def __str__(self):
        return "N" if self.color == "white" else "n"
    
    def get_valid_moves(self, board):
        # Knight moves in an L-shape (8 possible moves)
        valid_moves = []
        x, y = self.position
        knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                        (1, -2), (1, 2), (2, -1), (2, 1)]

        for dx, dy in knight_moves:
            nx, ny = x + dx, y + dy
            if board.is_valid_position(nx, ny) and (board.is_empty(nx, ny) or board.is_occupied_by_enemy(nx, ny, self.color)):
                valid_moves.append((nx, ny))

        return valid_moves


class Bishop(Piece):
    def __str__(self):
        return "B" if self.color == "white" else "b"
    
    def get_valid_moves(self, board):
        # Rook moves horizontally or vertically
        valid_moves = []
        x, y = self.position

        # Check moves in all 4 directions
        directions = [(-1, -1), (1, 1), (1, -1), (-1, 1)]
        for dx, dy in directions:
            nx, ny = x, y
            while True:
                nx += dx
                ny += dy
                if board.is_valid_position(nx, ny) and board.is_empty(nx, ny):
                    valid_moves.append((nx, ny))
                elif board.is_occupied_by_enemy(nx, ny, self.color):
                    valid_moves.append((nx, ny))
                    break
                else:
                    break

        return valid_moves
    
class Queen(Piece):
    def __str__(self):
        return "Q" if self.color == "white" else "q"
    
    def get_valid_moves(self, board):
        # Rook moves horizontally or vertically
        valid_moves = []
        x, y = self.position

        # Check moves in all 4 directions
        directions = [(-1, -1), (1, 1), (1, -1), (-1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x, y
            while True:
                nx += dx
                ny += dy
                if board.is_valid_position(nx, ny) and board.is_empty(nx, ny):
                    valid_moves.append((nx, ny))
                elif board.is_occupied_by_enemy(nx, ny, self.color):
                    valid_moves.append((nx, ny))
                    break
                else:
                    break

        return valid_moves
    
class King(Piece):
    def __str__(self):
        return "K" if self.color == "white" else "k"
    
    def get_valid_moves(self, board):
        valid_moves = []
        x, y = self.position

        # King moves one square in any direction
        directions = [(-1, -1), (1, 1), (1, -1), (-1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if board.is_valid_position(nx, ny):
                if board.is_empty(nx, ny) or board.is_occupied_by_enemy(nx, ny, self.color):
                    valid_moves.append((nx, ny))

        return valid_moves

class Board:
    def __init__(self):
        # Initialize the board as an 8x8 grid
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self):
        # Place pieces in the initial positions on the board
        self.board[0][0] = Rook("black", (0, 0))
        self.board[0][1] = Knight("black", (0, 1))
        self.board[0][2] = Bishop("black", (0, 2))
        self.board[0][3] = Queen("black", (0, 3))
        self.board[0][4] = King("black", (0, 4))
        self.board[0][5] = Bishop("black", (0, 5))
        self.board[0][6] = Knight("black", (0, 6))
        self.board[0][7] = Rook("black", (0, 7))
        # Add other black pieces...

        # Add white pieces similarly (mirroring black pieces)
        self.board[7][0] = Rook("white", (7, 0))
        self.board[7][1] = Knight("white", (7, 1))
        self.board[7][2] = Bishop("white", (7, 2))
        self.board[7][3] = Queen("white", (7, 3))
        self.board[7][4] = King("white", (7, 4))
        self.board[7][5] = Bishop("white", (7, 5))
        self.board[7][6] = Knight("white", (7, 6))
        self.board[7][7] = Rook("white", (7, 7))
        # Add white pawns
        for i in range(8):
            self.board[6][i] = Pawn("white", (6, i))
            self.board[1][i] = Pawn("black", (1, i))

    def is_valid_position(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def is_empty(self, x, y):
        return self.board[x][y] is None

    def is_occupied_by_enemy(self, x, y, color):
        piece = self.board[x][y]
        return piece and piece.color != color

    def display(self):
        # Display the board (basic representation)
        for row in self.board:
            print(" ".join([str(piece) if piece else "." for piece in row]))
