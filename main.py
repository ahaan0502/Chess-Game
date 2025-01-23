import tkinter as tk
from game import Game  # Importing the game logic
from chess_logic import Board, Rook, Pawn, Knight, Bishop, Queen, King  # Importing the board and pieces

# Initialize the game logic
game = Game()

selected_piece = None  # Track the currently selected piece

def draw_board():
    # Clear the current board and redraw the pieces
    for row in range(8):
        for col in range(8):
            color = 'white' if (row + col) % 2 == 0 else 'black'
            piece = game.board.board[row][col]  # Get the piece at this position

            piece_text = str(piece) if piece else ""  # Show piece symbol if it exists
            square = tk.Button(root, text=piece_text, width=5, height=2, bg=color, command=lambda row=row, col=col: on_square_click(row, col))
            square.grid(row=row, column=col)


def on_square_click(row, col):
    global selected_piece
    
    piece = game.board.board[row][col]  # Get the piece at the clicked position
    
    # If no piece is selected and a piece is clicked, select the piece
    if selected_piece is None and piece:
        selected_piece = piece
        print(f"Piece selected: {piece} at ({row},{col})")
        
        # Highlight valid moves (you can implement this by changing button colors or adding a visual cue)
        valid_moves = selected_piece.get_valid_moves(game.board)
        print(f"Valid moves for {piece}: {valid_moves}")
        
        # You could show valid moves on the GUI by changing button colors or using an extra variable to track valid moves.

    # If a piece is selected and the clicked square is a valid move, move the piece
    elif selected_piece and (row, col) in selected_piece.get_valid_moves(game.board):
        print(f"Move {selected_piece} to ({row},{col})")
        
        # Update the board (move the piece)
        old_x, old_y = selected_piece.position
        game.board.board[row][col] = selected_piece  # Move the piece to the new square
        game.board.board[old_x][old_y] = None  # Clear the previous square
        selected_piece.position = (row, col)  # Update the piece's position

        # Switch turns
        game.switch_turn()

        # Clear the selection
        selected_piece = None
        
        # Redraw the board after the move
        draw_board()


# Create the main window
root = tk.Tk()
root.title("Chess Game")

# Draw the chessboard
draw_board()

# Start the Tkinter event loop
root.mainloop()
