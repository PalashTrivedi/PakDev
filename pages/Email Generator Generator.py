import streamlit as st
from Generate_Email import generate_email

st.set_page_config(page_title="Cover Letter", page_icon="✉️")

st.markdown("# Generate Email")
st.write(
    """Want to generate a email? Just fill out the form below and we'll do the rest!"""
)

# # Inputs for the user to fill out
# from_name, to_name, subject, context
from_name = st.text_input("From", help="e.g. John Smith")
to_name = st.text_input("To", help="e.g. ")
subject = st.text_input("Email Subject", help="e.g. Request for a meeting")
context = st.text_area("Context", help="e.g. I want to discuss about coming presentation ...")

# link Generate_CoverLetter.py to this button
if st.button("Generate Email"):
    st.write("Generating Email...")
    email = generate_email(from_name, to_name, subject, context)
    # write cover letter in a text box and allow user to copy with multiline = True
    st.text_area("Email", value=email, height=500)

