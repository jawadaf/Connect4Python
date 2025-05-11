import Rules as rules
import Board as board

def get_player_move():
    while True:
        try:
            col = int(input(f"Spiller {rules.current_player}, vælg en kolonne (0-6): "))
            if 0 <= col < board.COLS:
                return col
            else:
                print("Ugyldig kolonne. Prøv igen.")
        except ValueError:
            print("Indtast venligst et tal.")
