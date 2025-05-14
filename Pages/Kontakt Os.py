import streamlit as st

def kontakt_os():
    st.title("Kontakt os")
    navn = st.text_input("Indtast dit navn:")
    email = st.text_input("Indtast din e-mail:")
    besked = st.text_area("Skriv din besked:")

    if st.button("Send besked"):
        st.success("Tak for din besked! Vi vil vende tilbage hurtigst muligt.")
        st.write(f"**Navn:** {navn}")
        st.write(f"**E-mail:** {email}")
        st.write(f"**Besked:** {besked}")

if __name__ == "__main__":
    kontakt_os()
