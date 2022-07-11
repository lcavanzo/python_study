"""Validating if a chess dictionary position is valid"""

# takes a dictionary argument and returns True or False depending on if the board is valid.
## A valid board will have exactly one black king and exactly one white
## king. Each player can only have at most 16 pieces, at most 8 pawns, and
## all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t
## be on space '9z' . The piece names begin with either a 'w' or 'b' to repre-
## sent white or black, followed by 'pawn' , 'knight' , 'bishop' , 'rook' , 'queen' , or
##'king' . This function should detect when a bug has resulted in an improper
## chess board.

# Entry example
##{'h1': 'bking', 'c6': 'wqueen','g2': 'bbishop', 'h5': 'bqueen', 'e3': 'wking'}

def is_valid_chess_board(chess_board, chess_possition):
    """check if a chess position is valid"""
    valid = True
    for player_possition_piece,player_piece in chess_possition.items():
        if player_possition_piece not in chess_board.keys():
            print(f"{player_piece} is out of a valid board ->"
                f" \"{player_possition_piece}\"")
            valid = False
            break

    check_player_pieces = _valid_number_player_pieces(chess_possition)
    if valid == False or check_player_pieces == False:
        print(valid)
    else:
        print(valid)




def _valid_number_player_pieces(player_pieces):
    """checking the number of player's pieces"""
    w_pieces = {
        'wpawn': 0, 'wrook': 0, 'wking': 0, 'wqueen':0, 'wbishop': 0,
        'wknight': 0
    }
    b_pieces = {
        'bpawn': 0, 'brook': 0, 'bking': 0, 'bqueen':0, 'bbishop': 0,
        'bknight': 0
    }
    total_wpieces = 0
    total_bpieces = 0

    for piece in player_pieces.values():
        if piece in w_pieces:
            w_pieces[piece] +=1
        elif piece in b_pieces:
            b_pieces[piece] +=1

    if w_pieces['wpawn'] > 8:
        print("white player has more than 8 pawns")
    if b_pieces['bpawn'] > 8:
        print("black player has more than 8 pawns")
    if w_pieces['wrook'] > 2:
        print("while player has more than 2 rooks")
    if b_pieces['brook'] > 2:
        print("black player has more than 2 rooks")
    if w_pieces['wking'] > 1:
        print("while player has more than 1 king")
    if b_pieces['bking'] > 1:
        print("black player has more than 1 king")
    if w_pieces['wqueen'] > 1:
        print("while player has more than 1 queen")
    if b_pieces['bqueen'] > 1:
        print("black player has more than 1 queen")
    if w_pieces['wbishop'] > 2:
        print("while player has more than 2 bishop")
    if b_pieces['bbishop'] > 2:
        print("black player has more than 2 bishop")
    if w_pieces['wknight'] > 2:
        print("while player has more than 2 knight")
    if b_pieces['bknight'] > 2:
        print("black player has more than 2 knight")

    for number in w_pieces.values():
        total_wpieces += number
    for number in b_pieces.values():
        total_bpieces += number

    if total_wpieces > 16 and total_bpieces > 16:
        return False

    ## Print pieces information
    #print(total_wpieces)
    #print(total_bpieces)
    #print(f"white pieces: {w_pieces}")
    #print(f"black pieces: {b_pieces}")


def _creating_board():
    """Creating chess board"""
    chess_col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    chess_board = {}
    for col in range(0, 8):
        for row in range(1,9):
            chess_board[chess_col[col] + f"{row}" ] = ' '
    return chess_board
    #print(chess_board)

chess_possition = { 'a1': 'wpawn', 'a2':'wking', 'b3':'wking',
    'f7':'bpawn','h4': 'bpawn', 'g1': 'bpawn', 'g2': 'bpawn', 
    'g3': 'bpawn', 'g4': 'bpawn', 'g5':'bpawn', 'g6': 'bpawn',
    'b4': 'bpawn','z2':'wpawn',
}
#chess_possition = {
#    'h1': 'bking', 'c6': 'wqueen','g2': 'bbishop',
#    'h5': 'bqueen', 'e3': 'wking',
#}

chess_board = _creating_board()
is_valid_chess_board(chess_board, chess_possition)


