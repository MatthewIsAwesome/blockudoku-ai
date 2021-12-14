import copy
import random

board = [[False]*9]*9

pieces = [
    [ # Single
        [True]
    ],
    [ # 2 Line
        [True, True]
    ],
    [ # 3 Line
        [True, True, True]
    ],
    [ # 4 Line
        [True, True, True, True]
    ],
    [ # 5 Line
        [True, True, True, True, True]
    ],
    [ # 6 Line
        [True, True, True, True, True, True]
    ],
    [ # Mini L
        [True, True],
        [True, False]
    ],
    [ # T
        [True, True, True],
        [False, True, False]
    ],
    [ # J
        [True, True, True],
        [False, False, True]
    ],
    [ # L
        [True, True, True],
        [True, False, False]
    ],
    [ # Long L/J
        [True, True, True],
        [True, False, False],
        [True, False, False]
    ],
    [ # Long T
        [True, True, True],
        [False, True, False],
        [False, True, False]
    ],
    [ # Z
        [True, True, False],
        [False, True, True]
    ],
    [ # S
        [False, True, True],
        [True, True, False]
    ],
    [ # O
        [True, True],
        [True, True]
    ],
    [ # C
        [True, True, True],
        [True, False, True]
    ],
    [ # +
        [False, True, False],
        [True, True, True],
        [False, True, False]
    ],
    [ # /
        [False, False, True],
        [False, True, False],
        [True, False, False]
    ],
    [ # \
        [False, True],
        [True, False]
    ]
]

def __rotate__(piece, repeat=0):
    """
    internal method for rotating each piece randomly
    """
    # rotates a piece
    rotated = copy.deepcopy(piece)
    for i in range(repeat):
        rotated = list(zip(*rotated[::-1]))
    return rotated

def get_queue(length=3):
    """
    gets a queue of pieces
    rotates each piece randomly
    """
    return [__rotate__(random.choice(pieces), repeat=random.choice((0, 1, 2, 3))) for i in range(length)] 

# def possible_perms(board, pieces):
#     """
#     Gets the 
#     """
#     perms = dict()
#     if len(pieces) == 1:
#         return [clean(state) for state in board_states(board, pieces[0])]
#     for i in range(len(pieces)):
#         perms[pieces[i]] = possible_perms(board, pieces[:i] + pieces[i+1:])
#     return perms


# def board_states(board, piece):
#     states = []
#     for i in range(len(board)-len(piece)):
#         for j in range(len(board[0])-len(piece[0])):
#             if board[i][j] == '.':
#                 states.append(place(board, piece, i, j))

def place(board, piece, i, j):
    """
    Places a piece on the board, outputs resulting board
    Does not check for collisions
    Does not modify input
    """

    newBoard = copy.deepcopy(board)
    for x in range(len(piece)):
        for y in range(len(piece[0])):
            newBoard[i+x][j+y] = piece[x][y] or newBoard[x][y]
    return newBoard

def clean(board):
    """
    Removes all completed lines and squares on a board, modifies input
    """

    # Checks all rows, columns, and 3x3 squares
    
    # Check rows
    for i in range(len(board)):
        if all(board[i][j] for j in range(9)):
            for j in range(9):
                board[i][j] = False
    
    # Check columns
    for j in range(len(board)):
        if all(board[i][j] for i in range(9)):
            for j in range(9):
                board[i][j] = False
    
    # Check 3x3 squares
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if all(board[i+x][j+y] for x in range(3) for y in range(3)):
                for x in range(3):
                    for y in range(3):
                        board[i+x][j+y] = False

def print_board(board):
    """
    prints board in console for debugging
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            print("🟦" if board[i][j] else "⬛", end=" ")
        print()

def check_piece_collision(board, piece, i, j):
    """
    Checks if a piece will collide with the board
    """
    for x in range(len(piece)):
        for y in range(len(piece[0])):
            if piece[x][y] and board[i+x][j+y]:
                return True
    return False

def make_ai_move(board, pieces):
    """
    makes the best possible move for a given board state and piece queue
    modifies board and pieces to reflect the move
    """

    # piece = pieces.pop(random.randint(0, len(pieces)-1))

    # return place(board, piece, 0, 0)

    raise NotImplementedError

def main():
    print("Usage: python play.py")
    exit()
    global board
    input("Press enter to continue...")
    board = place(board, random.choice(pieces), 0, 0)
    print_board(board)
    main()

if __name__ == "__main__":
    main()
