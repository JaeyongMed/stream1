import streamlit as st

# Get user input
user_input = st.text_input("Enter your text:")

# Create a download link for the text file
if st.button("Download"):
    with open("user_text.txt", "w") as file:
        file.write(user_input)
    st.download_button(
        label="Download Text File",
        data="user_text.txt",
        file_name="user_text.txt",
        mime="text/plain"
    )