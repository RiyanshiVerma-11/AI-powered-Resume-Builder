# resume_generator.py

import json

def generate_resume_from_linkedin(profile_data):
    first_name = profile_data.get("firstName", "")
    last_name = profile_data.get("lastName", "")
    full_name = f"{first_name} {last_name}"

    headline = profile_data.get("headline", "")
    summary = profile_data.get("summary", "")

    positions = profile_data.get("positions", {}).get("values", [])
    jobs = "\n".join(
        f"- {pos.get('title')} at {pos.get('company', {}).get('name', '')} ({pos.get('startDate', {}).get('year', '')})"
        for pos in positions
    )

    skills = [skill.get("skill", {}).get("name") for skill in profile_data.get("skills", {}).get("values", [])]
    skill_list = ", ".join(skills)

    return f"""
Name: {full_name}
Headline: {headline}
Summary: {summary}

Experience:
{jobs}

Skills:
{skill_list}
"""


def generate_resume_from_manual(skills, education, projects):
    resume_text = f"""
    # 📄 AI-Generated Resume

    ## 🎯 Skills
    {skills}

    ## 🎓 Education
    {education}

    ## 🛠️ Projects
    {projects}

    ---
    *Generated using AI Resume Builder.*
    """
    return resume_text
