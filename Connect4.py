import streamlit as st
import Board as board
import Rules as rules

st.title("Connect 4")

# Initialiser session state én gang når man åbner siden.
if 'board' not in st.session_state: # st.session_state er som en slags hukommelse, der bevares mellem klik og genindlæsninger.
    board.initialize_board()
    st.session_state.board = [row.copy() for row in board.board] # List of Comprhension. En kopi af brættet gemmes i session_state (så man kan bruge det i Streamlit)
    st.session_state.current_player = 'X'
    st.session_state.game_over = False # Spillet er igang
    st.session_state.message = "" # vise beskeder (vinder, uafgjort, fejl osv.).

# Opdater board.board så mine eksisterende funktioner virker
board.board = st.session_state.board

# Funktion til at få spillerens navn baseret på symbol
def get_player_name(symbol):
    return "Rød" if symbol == 'X' else "Gul" # Ternary Operator

# Opretter 7 kolonner i Streamlit (fordi board.COLS = 7). (knapper)
col_buttons = st.columns(board.COLS)

for i in range(board.COLS): # Loop igennem kolonnerne
    with col_buttons[i]: # For hver kolonne laver jeg en pil-knap "↓". Knapperne har unikke keys, så Streamlit ved, hvilken der er trykket. De er deaktiveret, hvis spillet er slut.
        clicked = st.button("↓", key=f"btn_{i}", use_container_width=True, disabled=st.session_state.game_over)
        if clicked: # Hvis en knap blev trykket...
            row = rules.drop_piece(i, st.session_state.current_player) # Forsøg at droppe en brik i kolonne 'i'
            st.session_state.board = [row.copy() for row in board.board] # Brættet opdateres i session_state.
            if row == -1: # Hvis kolonnen er fyldt
                st.session_state.message = "Kolonnen er fuld!"
            elif rules.check_win(row, i): # Tjekker om den seneste brik skaber en vinder...
                player_name = get_player_name(st.session_state.current_player)
                st.session_state.message = f"Spiller {player_name} vinder!" # Viser en vinderbesked
                st.session_state.game_over = True
            elif rules.is_draw(): # Hvis der ikke er nogen ledige felter = uafgjort
                st.session_state.message = "Spillet ender uafgjort!"
                st.session_state.game_over = True
            else:
                st.session_state.current_player = 'O' if st.session_state.current_player == 'X' else 'X' # Ternary Operator. Hvis ingen har vundet eller det er uafgjort, skift spiller.

for row in board.board: # går igennem hver række i board.board som er en 2D-liste (en liste af lister)
    cols = st.columns(board.COLS) # skaber 7 visuelle kolonner i Streamlit. cols bliver en liste med 7 kolonne-objekter.
    for i in range(board.COLS): # En indre løkke, der går gennem hver kolonne i rækken. i går fra 0 til 6 (7 kolonner).
        cell = row[i] # Henter cellens værdi i kolonnen i
        symbol = '🔴' if cell == 'X' else '🟡' if cell == 'O' else '⬛' # Konvertere værdien til en emoji
        # Viser symbolet i kolonnen i...
        cols[i].markdown(f"<div style='text-align: center; font-size: 28px'>{symbol}</div>", unsafe_allow_html=True)
        # cols[i]: den aktuelle kolonne i brugergrænsefladen
        # .markdown(...): bruges til at vise HTML-indhold (emoji).
        # f"<div style='text-align: center; font-size: 28px'>{symbol}</div>": HTML-kode til: 1. centrere emoji 2. gøre emoji stor (28px)
        # unsafe_allow_html=True betyder, at Streamlit godt må tolke HTML – ellers bliver det bare vist som tekst.

# Vis besked
st.subheader(st.session_state.message)

# Genstart-knap. Tømmer brættet. Nulstiller spiller, besked og game over-flag.
if st.button("Genstart spil"):
    board.initialize_board()
    st.session_state.board = [row.copy() for row in board.board]
    st.session_state.current_player = 'X'
    st.session_state.game_over = False
    st.session_state.message = ""