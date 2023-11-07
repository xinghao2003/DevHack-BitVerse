import csv
from io import StringIO
from turtle import up
from altair import Data
import streamlit as st
import pandas as pd
from main import *

st.write("""
# BitVerse
""")

candidate_container = st.container()

candidate_container.subheader("Candidates data from sourcing")

candidate_container.file_uploader("Upload CSV", type=[
    "csv"], key="candidates", help="Upload candidates data from sourcing", accept_multiple_files=False)

candidates_df = pd.DataFrame()

if (st.session_state.candidates is not None):
    candidates_df = pd.read_csv(st.session_state.candidates)
    candidate_container.dataframe(candidates_df)

job_container = st.container()

job_container.subheader("Job details for candidates vetting")

job_container.file_uploader("Upload TXT", type=[
    "txt"], key="job", help="Upload job details for candidates vetting", accept_multiple_files=False)

job_details = ""

if (st.session_state.job is not None):
    # To read file as string:
    stringio = StringIO(st.session_state.job.getvalue().decode("utf-8"))
    job_details = stringio.read()
    job_container.write(job_details)

result_container = st.container()

result_container.subheader("Vetting results")

if (st.session_state.candidates is not None and st.session_state.job is not None):
    result_container.button("Generate result", type="primary", key="generate_result",
                            help="Generate result from candidates data and job details", on_click=get_result, args=(candidates_df, job_details, result_container))

# new_df = df[df["Candidate ID"] == 2]

# new_df = pd.concat([new_df, df[df["Candidate ID"] == 3]])

# st.dataframe(new_df)
