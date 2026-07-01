import streamlit as st
import os
from google import genai
from dotenv import load_dotenv

# Import the existing agent functions
from roadmap_agent import generate_roadmap
from interview_agent import generate_questions
from project_agent import generate_project

# Load local environment variables (for local running)
load_dotenv()

# Configure Streamlit page layout
st.set_page_config(
    page_title="AI Career Prep Agent",
    page_icon="🎓",
    layout="centered"
)

# App Title & Description
st.title("🎓 AI Career Preparation Agent")
st.subheader("Get a customized roadmap, interview prep, and project ideas.")
st.write("Fill out your details below to generate your personalized career plan.")

# Initialize the Gemini Client
# Reads from Streamlit Secrets when deployed, or falls back to local environment (.env)
api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("🔑 API Key not found. Please add `GEMINI_API_KEY` to your secrets (Cloud) or `.env` file (Local).")
    st.stop()

client = genai.Client(api_key=api_key)

# Form Layout for Inputs
with st.form("user_profile_form"):
    st.markdown("### 🧑‍💼 User Profile")
    
    col1, col2 = st.columns(2)
    with col1:
        department = st.text_input("Department / Branch", placeholder="e.g. Cloud Computing")
        experience = st.selectbox(
            "Experience Level", 
            ["Beginner", "Intermediate", "Advanced"]
        )
    with col2:
        role = st.text_input("Target Role", placeholder="e.g. Cloud Engineer")
        goal = st.text_input("Career Goal", placeholder="e.g. Get a job in 6 months")
        
    submit_button = st.form_submit_button(label="Generate Career Plan 🚀")

# When the form is submitted
if submit_button:
    if not department or not role or not goal:
        st.warning("⚠️ Please fill in all fields before submitting.")
    else:
        with st.spinner("🧠 Generating your custom career plan with Gemini..."):
            try:
                # Call agent functions using the inputs
                roadmap = generate_roadmap(client, department, role, experience, goal)
                questions = generate_questions(client, department, role, experience, goal)
                project = generate_project(client, department, role, experience, goal)

                # Display Results in neat tabs
                tab1, tab2, tab3 = st.tabs(["📅 Roadmap", "❓ Interview Questions", "💻 Recommended Project"])
                
                with tab1:
                    st.success("### 7-Day Roadmap")
                    st.write(roadmap)
                    
                with tab2:
                    st.success("### Top 5 Interview Questions")
                    st.write(questions)
                    
                with tab3:
                    st.success("### Suggested Practical Project")
                    st.write(project)
                    
            except Exception as e:
                st.error(f"Error calling Gemini API: {e}")