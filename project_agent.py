def generate_project(client, department, role, experience, goal):
    prompt = f"""
    Suggest one practical project for a student in the {department} department
    targeting a {role} role.

    Candidate Details:
    - Experience Level: {experience}
    - Career Goal: {goal}

    Include:
    - Project title
    - Features (appropriate for a {experience} level)
    - Technologies
    - How this project helps them achieve their goal: "{goal}"
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text