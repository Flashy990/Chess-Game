# This class stores all the information about the current state of the game.
# It will also check if the moves are valid
# It will also store a move log
class game_state():
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.white_move = True
        self.move_log = []

    def make_move(self, move):
        self.board[move.start_row][move.start_column] = "--"
        self.board[move.end_row][move.end_column] = move.piece_moved
        # record the move in the move log
        self.move_log.append(move)
        # change the turn to the other player
        self.white_move = not self.white_move

class move():

    # maps keys to values
    # key : value
    ranks_to_rows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1,"8": 0}
    rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}
    files_to_columns = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6,"h": 7}
    columns_to_files = {v: k for k, v in files_to_columns.items()}

    def __init__(self, start_square, end_square, board):
        self.start_row = start_square[0]
        self.start_column = start_square[1]
        self.end_row = end_square[0]
        self.end_column = end_square[1]
        self.piece_moved = board[self.start_row][self.start_column]
        self.piece_captured = board[self.end_row][self.end_column]

    def get_chess_notation(self):
        return self.get_rank_file(self.start_row, self.start_column) + self.get_rank_file(self.end_row, self.end_column)

    def get_rank_file(self, r, c):
        return self.columns_to_files[c] + self.rows_to_ranks[r]