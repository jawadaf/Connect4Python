import Board as board

def drop_piece(col, current_player):
    for r in range(board.ROWS - 1, -1, -1):
        if board.board[r][col] == ' ':
            board.board[r][col] = current_player
            return r
    return -1  # Kolonnen er fuld

def count_consecutive(row, col, row_dir, col_dir):
    count = 0
    symbol = board.board[row][col]
    r = row + row_dir
    c = col + col_dir
    while 0 <= r < board.ROWS and 0 <= c < board.COLS and board.board[r][c] == symbol:
        count += 1
        r += row_dir
        c += col_dir
    return count

def check_win(row, col):
    return (
        count_consecutive(row, col, 1, 0) + count_consecutive(row, col, -1, 0) >= 3 or
        count_consecutive(row, col, 0, 1) + count_consecutive(row, col, 0, -1) >= 3 or
        count_consecutive(row, col, 1, 1) + count_consecutive(row, col, -1, -1) >= 3 or
        count_consecutive(row, col, 1, -1) + count_consecutive(row, col, -1, 1) >= 3
    )

def is_draw():
    return all(board.board[0][c] != ' ' for c in range(board.COLS))
