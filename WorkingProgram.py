import Player as player
import Rules as rules
import Board as board

# Hovedprogram (konsolversion)
board.initialize_board()

while True:
    board.display_board()
    col = player.get_player_move() # henter kolonnenummeret fra spilleren

    row = rules.drop_piece1(col) # forsøger at lægge brikken i den valgte kolonne
    if row == -1: # hvis kolonnen er fyldt
        print("Kolonnen er fuld. Vælg en anden.")
        continue

    if rules.check_win(row, col): # tjekker om den nyeste brik vandt
        board.display_board() # hvis nogen vandt: vis brættet igen og udskriv vinderbesked og afslut spillet med break
        print(f"Spiller {rules.current_player} vinder!")
        break # afslut

    if rules.is_draw(): # hvis brættet er fyldt og ingen har fundet
        board.display_board()
        print("Spillet ender uafgjort!")
        break # afslut

    # Skift spiller
    rules.current_player = 'O' if rules.current_player == 'X' else 'X'
