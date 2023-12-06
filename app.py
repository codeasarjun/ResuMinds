from flask import Flask, render_template, request, redirect, url_for
import os
import fitz  # PyMuPDF
# ResumeNectar
from core.extract_name import extract_candidate_info
from core.extract_skills_education import extract_education_and_skills



app = Flask(__name__)

# Define the folder for raw resumes
UPLOAD_FOLDER = 'raw_resumes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)



def process_jd(jd_path):
    with open(jd_path, 'r',encoding='utf-8') as f:
        jd_content = f.read()
    return jd_content

def process_resume(resume_path, jd_content):
    with open(resume_path, 'rb') as f:
        pdf_document = fitz.open(f)
        text = ""
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            text += page.get_text()
    # Extract candidate information manually
    candidate_name, candidate_email = extract_candidate_info(text)

    # Extract education and skills information manually
    education_text, skills_text = extract_education_and_skills(text)

     

    
    # Simple matching algorithm: count the occurrences of JD words in the resume
    jd_words = set(word.lower() for word in jd_content.split())
    resume_words = text.lower().split()
    match_count = sum(1 for word in resume_words if word in jd_words)

    # Adjust the threshold based on JD length
    jd_length = len(jd_words)
    threshold = min(jd_length // 5, 10)

    # Assign a star rating based on the match count
    star_rating = min(match_count // threshold, 5) + 1
    
    
    return candidate_name, candidate_email,education_text, skills_text,star_rating

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get uploaded JD and resumes
    jd_file = request.files['jd']
    resume_files = request.files.getlist('resumes[]')

    # Save JD
    jd_path = os.path.join(app.config['UPLOAD_FOLDER'], jd_file.filename)
    jd_file.save(jd_path)

    # Process JD
    jd_content = process_jd(jd_path)

    # Process and analyze each resume
    results = []
    for resume_file in resume_files:
        resume_path = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
        resume_file.save(resume_path)
        star_rating = process_resume(resume_path, jd_content)
        print(star_rating)
        results.append({'resume_name': resume_file.filename, 'star_rating': star_rating})

    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
