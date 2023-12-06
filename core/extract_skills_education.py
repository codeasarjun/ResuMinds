def extract_education_and_skills(text):
    # Extract education information manually
    education_start = text.find("Education")
    education_end = text.find("Skills") if "Skills" in text else len(text)
    education_text = text[education_start:education_end].strip()

    # Extract skills information manually
    skills_start = text.find("Skills") if "Skills" in text else -1
    skills_text = text[skills_start:].strip()

    return education_text, skills_text
