# validate_chess_board
"""
In this chapter, we used the dictionary value
{'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
to represent a chess board.
Write a function named isValidChessBoard() that takes a dictionary argument and returns
True or False depending on if the board is valid.

A valid board will have exactly one black king and exactly one white king.
Each player can only have at most 16 pieces, at most 8 pawns, and all pieces
must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space
'9z'. The piece names begin with either a 'w' or 'b' to represent white or black,
followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.
This function should detect when a bug has resulted in an improper chess board.
"""


def is_valid_dashboard(board):
    """
    Create the official board
    """
    flag = True
    official_board = {}
    ROWS = 8
    COLUMNS = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for row in range(ROWS):
        for cell in range(ROWS):
            # print(f"{cell+1}{COLUMNS[row]}")
            official_board[f"{cell+1}{COLUMNS[row]}"] = " "
    if flag is True:
        flag = validate_pieces_position(board, official_board)
    if flag is True:
        flag = validate_total_pieces(board)

    return flag


def validate_pieces_position(board, official_board):
    """
    Validate if the board has the correct arithmetic notation
    """
    flag = True
    for k in board.keys():
        if k not in official_board.keys():
            # print(f"The position {k} is invalid")
            flag = False
    return flag
    # TODO, add Exception


def validate_total_pieces(board):
    """
    Separate color pieces and count total number of pieces for each side
    """
    flag = True
    side_pieces = {}
    total_white_pieces = 0
    total_black_pieces = 0
    for piece in board.values():
        if piece[0] == "w":
            side_pieces.setdefault(piece, 0)
            side_pieces[piece] = side_pieces[piece] + 1
            total_white_pieces += 1
        else:
            side_pieces.setdefault(piece, 0)
            side_pieces[piece] = side_pieces[piece] + 1
            total_black_pieces += 1
    if total_white_pieces > 16 or total_black_pieces > 16:
        # print(total_black_pieces)
        # print(total_white_pieces)
        # print("you have a lot pieces")
        flag = False
        # Validate correct number of kings(1 each side) and pawns(16 each side) only
    for piece in side_pieces.keys():
        if piece == "wking" and side_pieces["wking"] > 1:
            # print("white you have more than one king")
            flag = False
        elif piece == "bking" and side_pieces["bking"] > 1:
            # print("black you have more than one king")
            flag = False
        elif piece == "wpawn" and side_pieces["wpawn"] > 8:
            # print("white you have more than eight pawn")
            flag = False
        elif piece == "bpawn" and side_pieces["bpawn"] > 8:
            # print("black you have more than eight pawn")
            flag = False
    return flag


# valid Dashboard
v_current_board_position = {
    "1h": "bking",
    "6c": "wqueen",
    "2g": "bbishop",
    "5h": "bqueen",
    "3e": "wking",
}
# Invalid Dashboard
i_current_board_position = {
    "1h": "wking",
    "2h": "wking",
    "3j": "wking",
    "4h": "wking",
    "33h": "wking",
    "34h": "wking",
    "5e": "wking",
    "6h": "wking",
    "7h": "wking",
    "8h": "wking",
    "9h": "wking",
    "11h": "wking",
    "12h": "wking",
    "13h": "wking",
    "14h": "wking",
    "15h": "wking",
    "16h": "wking",
    "17h": "bking",
    "3h": "bking",
    "6c": "wqueen",
    "2g": "bbishop",
    "3g": "bbishop",
    "5h": "bqueen",
    "3e": "wking",
    "3z": "wking",
}

print(is_valid_dashboard(i_current_board_position))
