# Import required libraries
import streamlit as st
import json

from resume_generator import generate_resume_from_linkedin, generate_resume_from_manual
from resume_enhancer import enhance_resume_from_pdf

# Set up Streamlit app configuration
st.set_page_config(page_title="AI Resume Builder", layout="centered")

# App Title
st.title("🤖 AI-Powered Resume Builder")

# Sidebar for selecting functionality
option = st.sidebar.radio("Choose an option:", [
    "1️⃣ Build from LinkedIn",
    "2️⃣ Generate Resume from Manual Input",
    "3️⃣ Enhance Existing Resume"
])

# Option 1: Build resume from LinkedIn URL
if option == "1️⃣ Build from LinkedIn":
    st.header("🌐 Build Resume from LinkedIn")

    linkedin_url = st.text_input("Enter your LinkedIn Profile URL")

    st.markdown("""
    ### ⚠️ Important Note:

    Due to LinkedIn’s restrictions, we cannot directly fetch detailed profile data from a LinkedIn URL.

    To generate a full resume, please follow these steps:

    1. Go to [LinkedIn Data Export](https://www.linkedin.com/settings/data-export-page)
    2. Select **"Download larger data archive"**
    3. Click **"Request archive"**
    4. Once the archive is ready, download the ZIP file
    5. Unzip the file, and upload **`Profile.json`** below
    """)

    uploaded_json = st.file_uploader("Upload your LinkedIn `Profile.json`", type="json")

    if uploaded_json and st.button("Generate Resume"):
        with st.spinner("Reading LinkedIn data and generating resume..."):
            try:
                profile_data = json.load(uploaded_json)
                resume = generate_resume_from_linkedin(profile_data)
                st.success("Resume generated from LinkedIn data!")
                st.text_area("Your AI-generated Resume:", resume, height=400)
            except json.JSONDecodeError:
                st.error("❌ The uploaded file is not a valid JSON. Please upload the correct `Profile.json` file from LinkedIn.")
            except Exception as e:
                st.error(f"❌ An unexpected error occurred: {e}")

# Option 2: Build resume from manual input
elif option == "2️⃣ Generate Resume from Manual Input":
    st.header("📝 Generate Resume from Manual Input")

    # Input fields for skills, education, and projects
    skills = st.text_area("Enter your skills (comma separated):")
    education = st.text_area("Enter your education details:")
    projects = st.text_area("Enter your projects:")

    # Button to generate resume
    if st.button("Generate Resume"):
        if skills and education and projects:
            resume = generate_resume_from_manual(skills, education, projects)  # Call resume generator function
            st.success("Resume generated successfully!")
            # Display resume text in a scrollable box
            st.text_area("Your AI-generated Resume:", resume, height=400)
        else:
            st.warning("Please fill all the fields to generate resume.")

# Option 3: Enhance existing uploaded resume
elif option == "3️⃣ Enhance Existing Resume":
    # Upload PDF resume
    uploaded_file = st.file_uploader("Upload your old resume (PDF)", type=["pdf"])
    if uploaded_file and st.button("Enhance Resume"):
        with st.spinner("Analyzing and rewriting..."):
            result = enhance_resume_from_pdf(uploaded_file)  # Call enhancer function
            st.success("Enhanced Resume ready!")
            # Download button for enhanced resume
            st.download_button("Download Enhanced Resume", result, file_name="enhanced_resume.pdf")
