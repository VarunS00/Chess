from pieces.piece import Piece


class King(Piece):

    def __init__(self, row, col, color, image=None):
        super().__init__(row, col, color, image)

        self.name = "king"

    def get_moves(self, board):

        moves = []

        offsets = [
            (-1, -1),
            (-1, 0),
            (-1, 1),

            (0, -1),
            (0, 1),

            (1, -1),
            (1, 0),
            (1, 1)
        ]

        for dr, dc in offsets:

            r = self.row + dr
            c = self.col + dc

            if board.in_bounds(r, c):

                target = board.get_piece(r, c)

                if target is None or target.color != self.color:
                    moves.append((r, c))

        return moves