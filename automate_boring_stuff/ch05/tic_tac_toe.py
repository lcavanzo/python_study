# Tic tac toe game

"""
displaying a tic tac toe game
"""

theBoard = {
    "top-L": "Osnip-next-choice",
    "top-M": "O",
    "top-R": "O",
    "mid-L": "X",
    "mid-M": "X",
    "mid-R": " ",
    "low-L": " ",
    "low-M": " ",
    "low-R": "X",
}


def print_board(board):
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])


turn = "X"
for i in range(9):
    print(f"Turn for {turn}. Move on which space? ")
    move = input()
    theBoard[move] = turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"

    print_board(theBoard)
