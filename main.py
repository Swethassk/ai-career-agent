import os
from google import genai
from dotenv import load_dotenv
from roadmap_agent import generate_roadmap
from interview_agent import generate_questions
from project_agent import generate_project

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# 1. Collect the new inputs from the user
department = input("Enter your Department: ")
role = input("Enter your target role: ")
experience = input("Enter your Experience Level: ")
goal = input("Enter your Career Goal: ")

try:
    # 2. Pass the new arguments to each function
    roadmap = generate_roadmap(client, department, role, experience, goal)
    questions = generate_questions(client, department, role, experience, goal)
    project = generate_project(client, department, role, experience, goal)

    print("\n===== ROADMAP =====\n")
    print(roadmap)

    print("\n===== INTERVIEW QUESTIONS =====\n")
    print(questions)

    print("\n===== PROJECT RECOMMENDATION =====\n")
    print(project)

except Exception as e:
    print("\nGemini API Error:")
    print(e)