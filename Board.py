ROWS = 6
COLS = 7
board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def initialize_board():
    for r in range(ROWS):
        for c in range(COLS):
            board[r][c] = ' '

def display_board():
    print()
    for row in board:
        print('|', end='')
        for cell in row:
            print(f' {cell} |', end='')
        print()
    print('-' * 29)
    print('  0   1   2   3   4   5   6')
