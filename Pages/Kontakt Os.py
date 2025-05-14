import streamlit as st

def kontakt_os():
    st.title("Kontakt Os")
    navn = st.text_input("Navn:")
    email = st.text_input("Email:")
    besked = st.text_area("Besked:")

    if st.button("Send besked"):
        st.success("Tak for din besked! Vi vil vende tilbage hurtigst muligt!")
        st.write(f"**Navn:** {navn}")
        st.write(f"**E-mail:** {email}")
        st.write(f"**Besked:** {besked}")

if __name__ == "__main__":
    kontakt_os()
