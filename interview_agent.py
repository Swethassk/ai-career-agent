def generate_questions(client, department, role, experience, goal):
    prompt = f"""
    Generate 5 interview questions for a student in the {department} department
    preparing for a {role} role.

    Candidate Details:
    - Experience Level: {experience}
    - Career Goal: {goal}

    Ensure the questions are tailored to their experience level and help them achieve their career goal.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text