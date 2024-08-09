import streamlit as st

# Title of the app
st.title('Job Application Form')

# Create a form for user input
with st.form(key='job_application_form'):
    st.header('Applicant Information')

    name = st.text_input('Full Name')
    email = st.text_input('Email Address')
    phone = st.text_input('Phone Number')
    resume = st.file_uploader('Upload Your Resume (PDF only)', type=['pdf'])

    st.header('Cover Letter')
    cover_letter = st.text_area('Write your cover letter here')

    # Submit button
    submit_button = st.form_submit_button('Submit Application')

    if submit_button:
        if not (name and email and phone and resume and cover_letter):
            st.error('Please fill in all fields and upload a resume.')
        else:
            st.success('Your application has been submitted successfully!')
            # Here you can add code to process or save the form data
