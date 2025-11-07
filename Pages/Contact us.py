import streamlit as st

def kontakt_os():
    st.title("Contact us")
    name = st.text_input("Name:")
    email = st.text_input("E-mail:")
    message = st.text_area("Message:")

    if st.button("Send message"):
        st.success(f"Thank you {name} for your message! We will get back to you as soon as possible.")
        st.write(f"**Name:** {name}")
        st.write(f"**E-mail:** {email}")
        st.write(f"**Message:** {message}")

if __name__ == "__main__":
    kontakt_os()
