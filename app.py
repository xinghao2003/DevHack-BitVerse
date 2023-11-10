import stat
import streamlit as st
import file_loader as fl
import candidate_parse as cp
import job_parse as jp
import result
from config import temp_path

st.title("BitVerse - Candidate Vetting")

job_container = st.container()


def job_files_load():
    if (st.session_state.job_files is not None):
        process = job_container.status(
            "Processing data from file...", expanded=True)

        fl.load_files(st.session_state.job_files, process)
        content = jp.extract_job_details(st.session_state.job_files, process)
        if (content == None or len(content) == 0):
            st.error("Job details could not be extracted")
            return
        st.session_state.title = content[0]['title']
        st.session_state.descriptions = content[0]['descriptions']
        st.session_state.skills = content[0]['skills']


with job_container:
    st.subheader("Job Details", divider=True)
    st.file_uploader("Extract job details from files", type=[
        'pdf', 'docx', 'doc', 'txt'], accept_multiple_files=False, key="job_files", on_change=job_files_load)
    st.text_input("Title", key="title")
    st.text_area("Description", key="descriptions")
    st.text_area("Requirements", key="skills")

candidate_container = st.container()


def candidate_files_load():
    if (st.session_state.candidate_files is not None and type(st.session_state.candidate_files) is list and len(st.session_state.candidate_files) > 0):
        process = candidate_container.status(
            "Processing data from file...", expanded=True)
        fl.load_files(st.session_state.candidate_files, process)
        content = cp.add_candidates_to_list(
            st.session_state.candidate_files, process)
        if (content == None or len(content) == 0):
            st.error("Candidate details could not be extracted")
            return
        candidate_container.dataframe(content, column_order=(
            "id", "education", "skills", "experiences"))


with candidate_container:
    st.subheader("Candidates", divider=True)
    st.file_uploader("Extract candidates details from files", type=[
                     'pdf', 'docx', 'doc', 'txt', 'csv', 'xlsx', 'xls'], accept_multiple_files=True, key="candidate_files", on_change=candidate_files_load)

result_container = st.container()

def get_result(parsed_job_details, parsed_candidates):
    process = result_container.status("Generating result...")
    content = result.result(parsed_job_details, parsed_candidates, process)
    status = fl.combine_resumes(content)

    result_container.dataframe(content, column_order=(
        "id", "education", "skills", "experiences"))
    with open(f'{temp_path}resumes.zip', "rb") as fp:
        result_container.download_button(
            label="Download result in resume form",
            data=fp,
            file_name="resumes.zip",
            mime="application/zip"
        )

with result_container:
    st.subheader("Results", divider=True)
    parsed_job_details = jp.parsed_job_details
    parsed_candidates = cp.parsed_candidates
    if (len(parsed_job_details) > 0 and len(parsed_candidates) > 0):
        result_container.button("Generate result", type="primary", key="generate_result",
                            help="Generate result from candidates data and job details", on_click=get_result, args=(parsed_job_details, parsed_candidates))