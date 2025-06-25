ROWS = 6
COLS = 7
board = [[' ' for _ in range(COLS)] for _ in range(ROWS)] # List Comprehension til at oprette et tomt spillebræt(board)...
# [' ' for _ in range(COLS)]: Laver en liste med 7 tomme felter (én række). Eksempel: [' ', ' ', ' ', ' ', ' ', ' ', ' ']
# for _ in range(ROWS): Gentager det for 6 rækker.

def initialize_board(): # En funktion, der nulstiller brættet
    for r in range(ROWS): # går igennem alle rækker (fra 0 til 5)
        for c in range(COLS): # går igennem alle kolonner (fra 0 til 6)
            board[r][c] = ' ' # sætter hvert felt til ' ' (tom plads)

def display_board(): # Viser brættet i konsollen (ikke i Streamlit). Bruges kun i WorkingProgram.py
    print() # Laver en tom linje
    for row in board: # Går igennem hver række i brættet
        print('|', end='') # Starter rækken med en lodret streg. end='' betyder 'ikke gå linje ned'
        for cell in row: # Går igennem hver celle i rækken
            print(f' {cell} |', end='') # Udskriver hver celle med mellemrum og streg
        print() # En ny linje
    print('-' * 29) # Printer en vandret linje under brættet. '-' * 29 = 29 bindestreger.
    print('  0   1   2   3   4   5   6') # Printer kolonnenumrene så spilleren kan vælge kolonne
