import streamlit as st

st.header("Quiz")

# Spørgsmål 1
answer1 = st.selectbox("Hvor mange rækker og kolonner har man i Connect 4?",
                       ["Vælg et svar...", "5 rækker og 7 kolonner", "6 rækker og 7 kolonner", "7 rækker og 6 kolonner", "6 rækker og 6 kolonner"])
if answer1 != "Vælg et svar...":
    if answer1 == '6 rækker og 7 kolonner':
        st.success("Korrekt!")
    else:
        st.error("Forkert!")

# Spørgsmål 2
answer2 = st.selectbox("Hvor mange brikker skal man forbinde for at vinde i Connect 4?",
                       ["Vælg et svar...", "3", "4", "5", "6"])
if answer2 != "Vælg et svar...":
    if answer2 == '4':
        st.success("Korrekt!")
    else:
        st.error("Forkert!")

# Spørgsmål 3
answer3 = st.selectbox("I hvilken retning kan man vinde i Connect 4? (Vælg de korrekte svar)",
                       ["Vælg et svar...", "Vandret", "Lodret", "Diagonalt", "Alle ovenstående"])
if answer3 != "Vælg et svar...":
    if answer3 == 'Alle ovenstående':
        st.success("Korrekt!")
    else:
        st.error("Forkert!")

# Spørgsmål 4
answer4 = st.selectbox("Hvem starter spillet i en standardudgave?",
                       ["Vælg et svar...", "Rød", "Gul", "Tilfældige spiller", "Den ældste spiller"])
if answer4 != "Vælg et svar...":
    if answer4 == 'Rød':
        st.success("Korrekt!")
    else:
        st.error("Forkert!")

# Spørgsmål 5
answer5 = st.selectbox("Hvad sker der, hvis brættet er fyldt, og ingen har vundet?",
                       ["Vælg et svar...", "Spillet fortsætter", "Spillet genstartes", "Det bliver uafgjort", "Den med flest brikker vinder"])
if answer5 != "Vælg et svar...":
    if answer5 == 'Det bliver uafgjort':
        st.success("Korrekt!")
    else:
        st.error("Forkert!")

# Spørgsmål 6
answer6 = st.selectbox("Hvad er det bedste førstetræk i Connect 4?",
                       ["Vælg et svar...", "Midterkolonnen", "Sidekolonnen", "Hjørnekolonnen", "Tilfældig kolonne"])
if answer6 != "Vælg et svar...":
    if answer6 == 'Midterkolonnen':
        st.success("Korrekt!")
    else:
        st.error("Forkert!")