import docx2txt

def extract_resume_data(filepath):
    text = docx2txt.process(filepath)
    # Simplified parsing
    data = {
        "name": "Extracted Name",
        "email": "example@email.com",
        "skills": ["Python", "Machine Learning"],
    }
    return data
