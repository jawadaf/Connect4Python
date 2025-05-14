import streamlit as st
import Board as board
import Rules as rules

# Initialiser session state én gang
if 'board' not in st.session_state:
    board.initialize_board()
    st.session_state.board = [row.copy() for row in board.board]
    st.session_state.current_player = 'X'
    st.session_state.game_over = False
    st.session_state.message = ""

# Opdater board.board så dine eksisterende funktioner virker
board.board = st.session_state.board

st.title("Connect 4")

# Funktion til at få spillerens navn baseret på symbol
def get_player_name(symbol):
    return "Rød" if symbol == 'X' else "Gul"

# Kolonneknapper
col_buttons = st.columns(board.COLS)
for i in range(board.COLS):
    with col_buttons[i]:
        clicked = st.button("↓", key=f"btn_{i}", use_container_width=True, disabled=st.session_state.game_over)
        if clicked:
            row = rules.drop_piece(i, st.session_state.current_player)
            st.session_state.board = [row.copy() for row in board.board]
            if row == -1:
                st.session_state.message = "Kolonnen er fuld!"
            elif rules.check_win(row, i):
                player_name = get_player_name(st.session_state.current_player)
                st.session_state.message = f"Spiller {player_name} vinder!"
                st.session_state.game_over = True
            elif rules.is_draw():
                st.session_state.message = "Spillet ender uafgjort!"
                st.session_state.game_over = True
            else:
                st.session_state.current_player = 'O' if st.session_state.current_player == 'X' else 'X'

# Tegn brættet med st.columns
for row in board.board:
    cols = st.columns(board.COLS)
    for i in range(board.COLS):
        cell = row[i]
        symbol = '🔴' if cell == 'X' else '🟡' if cell == 'O' else '⬛'
        # Vis hver celle centreret i sin kolonne
        cols[i].markdown(f"<div style='text-align: center; font-size: 28px'>{symbol}</div>", unsafe_allow_html=True)

# Vis besked
st.subheader(st.session_state.message)

# Genstart-knap
if st.button("Genstart spil"):
    board.initialize_board()
    st.session_state.board = [row.copy() for row in board.board]
    st.session_state.current_player = 'X'
    st.session_state.game_over = False
    st.session_state.message = ""