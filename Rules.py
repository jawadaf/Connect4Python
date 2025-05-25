import Board as board

current_player = 'X' 
# bruges kun i konsol-versionen (WorkingProgram.py). (starter med 'X', altså rød spiller)
# i Streamlit-versionen bruges i stedet st.session_state.current_player så man ikke skal bruge globale variabler

# Bruges i Connect4.py (webversion)
def drop_piece(col, current_player): # forsøger at droppe en brik i kolonne col
    for r in range(board.ROWS - 1, -1, -1): # Den starter oppefra og går ned
        if board.board[r][col] == ' ': # Hvis den finder et tomt felt ' ', placerer den spillerens symbol der
            board.board[r][col] = current_player 
            return r # Returnerer rækkenummeret r hvor brikken blev placeret
    return -1  # hvis kolonnen er fuld returnere -1

# Bruges i WorkingProgram.py (konsolversion)
def drop_piece1(col): # Næsten identisk med drop_piece, men bruger den globale current_player
    for r in range(board.ROWS - 1, -1, -1):
        if board.board[r][col] == ' ':
            board.board[r][col] = current_player
            return r
    return -1  

def count_consecutive(row, col, row_dir, col_dir): # Tæller hvor mange ens brikker (X eller O) der er på stribe i én bestemt retning
    count = 0 # starter med 0 ens symboler i træk
    symbol = board.board[row][col] # gemmer det symbol vi leder efter i denne retning f.eks. 'X' eller 'O'. Det er brikken som lige blev placeret (i check_win())
    r = row + row_dir # bevæger os et skridt i den ønskede retning. 
    c = col + col_dir # bevæger os et skridt i den ønskede retning. 
    # fx row_dir = 1, col_dir = 0 - én række ned
    # fx row_dir = -1, col_dir = 0 - én række op
    # fx row_dir = 1, col_dir = 1 → diagonalt ned mod højre
    while 0 <= r < board.ROWS and 0 <= c < board.COLS and board.board[r][c] == symbol: # Så længe vi stadig er inden for brættets grænser og feltet indeholder det samme symbol så tæller vi op
        count += 1 # Vi har fundet en brik mere på stribe - læg én til i tælleren
        r += row_dir # Gå videre i den samme retning
        c += col_dir # Gå videre i den samme retning
    return count # Når vi enten løber ud af brættet, eller rammer en anden brik - returnér antallet af brikker på stribe i denne retning

def check_win(row, col):
    return (
        count_consecutive(row, col, 1, 0) + count_consecutive(row, col, -1, 0) >= 3 or # Lodret ned (1, 0) og op (-1, 0)
        count_consecutive(row, col, 0, 1) + count_consecutive(row, col, 0, -1) >= 3 or # Vandret højre (0, 1) og venstre (0, -1)
        count_consecutive(row, col, 1, 1) + count_consecutive(row, col, -1, -1) >= 3 or # Diagonal ned-højre (1, 1) og op-venstre (-1, -1)
        count_consecutive(row, col, 1, -1) + count_consecutive(row, col, -1, 1) >= 3 # Diagonal ned-venstre (1, -1) og op-højre (-1, 1)
    )

def is_draw():
    return all(board.board[0][c] != ' ' for c in range(board.COLS))
# Tjekker om toppen af alle kolonner er fyldt (altså ingen tomme felter ' ')
# Hvis ja: så er det uafgjort = returnerer True
