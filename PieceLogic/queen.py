from PieceLogic.piece import Piece

class Queen(Piece):
    
    def __init__(self, row, col, color, image=None):
        #Calls the Piece constructor to initialize common attributes
        super().__init__(row, col, color, image)
        #Sets the name attribute to "queen"
        self.name = "queen"
    #Returns legal moves for the queen
    def get_moves(self, board):
        #Creates an empty list to store moves
        moves = []
        #Defines the 8 possible directions a queen can move in (vertical, horizontal, diagonal)
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),

            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1)
        ]
        #Iterates through each direction to find legal moves for the queen
        for dr, dc in directions:
            #Starts from the queen's current position
            r = self.row
            c = self.col
            #Moves in the current direction until it goes out of bounds or encounters a piece
            while True:

                r += dr
                c += dc
                #Checks if the new position is within the boundaries of the board
                if not board.in_bounds(r, c):
                    break
                #Gets the piece at the new position
                target = board.get_piece(r, c)
                #If there is no piece at the new position, it is a valid move
                if target is None:
                    moves.append((r, c))

                else:
                    #If there is a piece at the new position, check if it is an enemy piece
                    if target.color != self.color:
                        moves.append((r, c))

                    break
        #Returns the list of legal moves for the queen
        return moves