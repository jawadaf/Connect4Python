import streamlit as st

st.header("Quiz")

answer1 = st.selectbox("Hvor mange rækker og kolonner har et standard Connect 4-spil?", ["Vælg et svar...", "5 rækker og 7 kolonner", "6 rækker og 7 kolonner", "7 rækker og 6 kolonner", "6 rækker og 6 kolonner"])
if answer1 != "Vælg et svar...": 
    if answer1 == '6 rækker og 7 kolonner': st.success("Right!")
else: st.error("Wrong!")

answer2 = st.selectbox("Hvor mange brikker skal man forbinde for at vinde i Connect 4?", ["Vælg et svar...", "3", "4", "5", "6"])
if answer2 != "Vælg et svar...": 
    if answer2 == '4': st.success("Right!")
else: st.error("Wrong!")

answer3 = st.selectbox("I hvilken retning kan man vinde i Connect 4? (flere svar mulige)", ["Vælg et svar...", "Vandret", "Lodret", "Diagonalt", "Alle ovenstående"])
if answer3 != "Vælg et svar...":
    if answer3 == 'Alle ovenstående': st.success("Right!")
else: st.error("Wrong!")

answer4 = st.selectbox("Hvem starter spillet i en standardudgave?", ["Vælg et svar...", "Rød", "Guld", "Tilfældige spiller", "Den ældste spiller"])
if answer4 != "Vælg et svar...":
    if answer4 == 'Rød': st.success("Right!")
else: st.error("Wrong!")

answer5 = st.selectbox("Hvad sker der, hvis brættet er fyldt, og ingen har vundet?", ["Vælg et svar...", "Spillet fortsætter", "Spillet genstartes", "Det bliver uafgjort", "Den med flest brikker vinder"])
if answer5 != "Vælg et svar...":
    if answer5 == 'Det bliver uafgjort': st.success("Right!")
else: st.error("Wrong!")

answer6 = st.selectbox("(True/False) Det bedste første træk i Connect 4 er ofte i midterkolonnen.", ["Vælg et svar...", "True", "False"])
if answer6 != "Vælg et svar...":
    if answer6 == 'True': st.success("Right!")
else: st.error("Wrong!")