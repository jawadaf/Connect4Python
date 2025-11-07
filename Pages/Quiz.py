import streamlit as st

st.header("Quiz")

# Question 1
answer1 = st.selectbox("How many rows and columns are there in Connect 4?",
                       ["Choose an answer...", "5 rows and 7 columns", "6 rows and 7 columns", "7 rows and 6 columns", "6 rows and 6 columns"])
if answer1 != "Choose an answer...":
    if answer1 == "6 rows and 7 columns":
        st.success("Correct!")
    else:
        st.error("Incorrect!")

# Question 2
answer2 = st.selectbox("How many discs do you need to connect to win in Connect 4?",
                       ["Choose an answer...", "3", "4", "5", "6"])
if answer2 != "Choose an answer...":
    if answer2 == "4":
        st.success("Correct!")
    else:
        st.error("Incorrect!")

# Question 3
answer3 = st.selectbox("In which directions can you win in Connect 4? (Choose the correct answer)",
                       ["Choose an answer...", "Horizontally", "Vertically", "Diagonally", "All of the above"])
if answer3 != "Choose an answer...":
    if answer3 == "All of the above":
        st.success("Correct!")
    else:
        st.error("Incorrect!")

# Question 4
answer4 = st.selectbox("Who starts the game in the standard version?",
                       ["Choose an answer...", "Red", "Yellow", "Random player", "The oldest player"])
if answer4 != "Choose an answer...":
    if answer4 == "Red":
        st.success("Correct!")
    else:
        st.error("Incorrect!")

# Question 5
answer5 = st.selectbox("What happens if the board is full and no one has won?",
                       ["Choose an answer...", "The game continues", "The game restarts", "It's a draw", "The player with the most discs wins"])
if answer5 != "Choose an answer...":
    if answer5 == "It's a draw":
        st.success("Correct!")
    else:
        st.error("Incorrect!")

# Question 6
answer6 = st.selectbox("What is considered the best opening move in Connect 4?",
                       ["Choose an answer...", "Middle column", "Side column", "Corner column", "Random column"])
if answer6 != "Choose an answer...":
    if answer6 == "Middle column":
        st.success("Correct!")
    else:
        st.error("Incorrect!")