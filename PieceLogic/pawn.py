from PieceLogic.piece import Piece

from constants import BLACK, WHITE

#Creates the Pawn class, which inherits from Piece
class Pawn(Piece):

    def __init__(self, row, col, color, image=None):
        #Calls the Piece constructor to initialize common attributes
        super().__init__(row, col, color, image)
        #Sets the name attribute to "pawn"
        self.name = "pawn"
    #Returns legal moves for the pawn
    def get_moves(self, board):
        #Creates an empty list to store moves
        moves = []
        #Determines the direction of the pawn movement based on the color
        direction = -1 if self.color == WHITE else 1
        #Determines starting position for pawns
        start_row = 6 if self.color == WHITE else 1
        #Calculates the row in front of the pawn
        r = self.row + direction
        #Check if the square in front of the pawn is within the boundaries
        if board.in_bounds(r, self.col):
            #Checks if the square in front of the pawn is empty
            if board.get_piece(r, self.col) is None:
                #Adds the move to the list of legal moves
                moves.append((r, self.col))
                #Calculates the row two squares in front of the pawn
                r2 = self.row + direction * 2
                #Checks if the pawn is in its starting position
                if self.row == start_row:
                    #Checks if square is withing boundaries and empty
                    if (board.in_bounds(r2, self.col) and board.get_piece(r2, self.col) is None):
                        #Adds the move to the list of legal moves
                        moves.append((r2, self.col))
        #Checks diagonal captures for the pawn
        for dc in (-1, 1):
            #Calculates the column for diagonal capture
            c = self.col + dc
            #Checks if the square is within boundaries
            if board.in_bounds(r, c):
                #Gets the piece on the diagonal square
                piece = board.get_piece(r, c)
                #Checks if the diagonal square contains an enemy piece
                if piece and piece.color != self.color:
                    #Adds the move to the list of legal moves
                    moves.append((r, c))
        #Returns the list of legal moves for the pawn
        return moves