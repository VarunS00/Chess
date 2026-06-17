class Move:

    def __init__(
        self,
        start_row,
        start_col,
        end_row,
        end_col,
        piece,
        captured=None
    ):

        self.start_row = start_row
        self.start_col = start_col

        self.end_row = end_row
        self.end_col = end_col

        self.piece = piece
        self.captured = captured

        self.castle = False
        self.en_passant = False
        self.promotion = False

    def __repr__(self):

        return (
            f"{self.piece.name}: "
            f"({self.start_row},{self.start_col}) -> "
            f"({self.end_row},{self.end_col})"
        )