from PieceLogic.piece import Piece
#Creates the Rook class, which inherits from Piece
class Rook(Piece):

    def __init__(self, row, col, color, image=None):
        super().__init__(row, col, color, image)

        self.name = "rook"

    def get_moves(self, board):

        moves = []

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for dr, dc in directions:

            r = self.row
            c = self.col

            while True:

                r += dr
                c += dc

                if not board.in_bounds(r, c):
                    break

                target = board.get_piece(r, c)

                if target is None:
                    moves.append((r, c))

                else:

                    if target.color != self.color:
                        moves.append((r, c))

                    break

        return moves