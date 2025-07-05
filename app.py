import streamlit as st
from resume_parser import parse_resume
from jd_input import get_job_description
from reviewer import analyze_resume
from utils import format_feedback

st.set_page_config(page_title="AI Resume Reviewer", layout="centered")

st.title("🤖 AI Resume Reviewer Agent")

uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
job_description = st.text_area("Paste Job Description (Optional)", height=200)

if uploaded_file:
    with st.spinner("Extracting and analyzing resume..."):
        resume_text = parse_resume(uploaded_file)
        jd_text = get_job_description(job_description)
        analysis = analyze_resume(resume_text, jd_text)
        feedback = format_feedback(analysis)

    st.markdown("### 📝 Resume Review Report")
    st.markdown(feedback, unsafe_allow_html=True)