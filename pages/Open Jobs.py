import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from open_jobs import open_jobs

st.markdown("# Open Jobs")

role = st.text_input("Role", help="e.g Python Developer")
location = st.text_input("Location", help="e.g new york")
limit = st.slider("Limit", 5, 200, step=10)

if st.button("Search Jobs"):
    st.write("Loading...")
    jobs = open_jobs(role, location, limit)
    df = pd.DataFrame(jobs)
    df.columns = ['Title', 'Company', 'Location', 'Job_Link', 'Description']
    AgGrid(df)
    st.write("Done")
