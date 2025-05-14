import Player as player
import Rules as rules
import Board as board

# Hovedprogram
board.initialize_board()

while True:
    board.display_board()
    col = player.get_player_move()

    row = rules.drop_piece(col)
    if row == -1:
        print("Kolonnen er fuld. Vælg en anden.")
        continue

    if rules.check_win(row, col):
        board.display_board()
        print(f"Spiller {rules.current_player} vinder!")
        break

    if rules.is_draw():
        board.display_board()
        print("Spillet ender uafgjort!")
        break

    # Skift spiller
    rules.current_player = 'O' if rules.current_player == 'X' else 'X'
