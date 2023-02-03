import streamlit as st
from Generate_CoverLetter import generate

st.set_page_config(page_title="Cover Letter", page_icon="📝")

st.markdown("# Generate Cover Letter")
st.write(
    """Want to generate a cover letter? Just fill out the form below and we'll do the rest!"""
)

# # Inputs for the user to fill out
role = st.text_input("Enter role you are applying for", help="e.g. Software Engineer")
job_description = st.text_area("Enter job description", help="e.g. We are looking for ...")
about_company = st.text_area("Enter about company", help="e.g. We are a startup ...")
name = st.text_input("Enter your name", help="e.g. John Smith")
about_me = st.text_area("Enter about me", help="e.g. I am a student at ...")

# link Generate_CoverLetter.py to this button
if st.button("Generate Cover Letter"):
    st.write("Generating Cover Letter...")
    letter = generate(role, job_description, about_company, name, about_me)
    st.write("Cover Letter Generated!")
    # write cover letter in a text box and allow user to copy with multiline = True
    st.text_area("Cover Letter", value=letter, height=500)
