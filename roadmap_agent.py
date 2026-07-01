def generate_roadmap(client, department, role, experience, goal):
    prompt = f"""
    Create a preparation roadmap for a student in the {department} department
    targeting a {role} role.

    Candidate Details:
    - Experience Level: {experience}
    - Career Goal: {goal}

    Design the roadmap specifically to help a {experience} level candidate reach their goal: "{goal}".
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text