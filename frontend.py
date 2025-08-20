import streamlit as st

# Page Title
st.title("Job Submission Interface")

# Button Options


col1, col2, col3 = st.columns(3)
with col1:
    btn1 = st.button("Button 1",type='primary',use_container_width=True)
with col2:
    btn2 = st.button("Button 2",type='primary',use_container_width=True)
with col3:
    show_form = st.button("Add Job",type='primary',use_container_width=True)

# Form Display Logic
if show_form:
    st.subheader("Enter Job Details")
    with st.form("job_form"):
        job_title = st.text_input("Job Title")
        company_name = st.text_input("Company Name")
        job_url = st.text_input("Job URL")
        job_description = st.text_area("Job Description")
        location = st.text_input("Location")

        submit_button = st.form_submit_button("Submit")

        if submit_button:
            st.success("Job information submitted successfully!")
            st.write("### Submitted Data")
            st.write(f"**Job Title:** {job_title}")
            st.write(f"**Company Name:** {company_name}")
            st.write(f"**Job URL:** {job_url}")
            st.write(f"**Description:** {job_description}")
            st.write(f"**Location:** {location}")
