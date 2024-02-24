# ResuMinds 📝💡
ResuMinds is a project aimed at assisting HR professionals and users in ranking resumes based on their relevance to a job description (JD). Users can upload both the JD and candidate resumes, and the system will rank the resumes according to their compatibility with the provided JD.

# Technologies Used
Flask 🌐: Flask is a lightweight web framework for Python, used here to build the backend of the application. It provides flexibility and simplicity in developing web applications.
Python 🐍: Python is the primary programming language used for developing the backend logic of ResuMinds. Its extensive libraries and readability make it suitable for various tasks, including data processing and analysis.

# Methodology
The project utilizes a matching algorithm to assess the compatibility of resumes with the provided JD. The algorithm parses both the JD and candidate resumes, extracting key information such as skills, experience, and education requirements. It then compares this information to determine the relevance of each resume to the job description. Finally, the resumes are ranked based on their similarity score to the JD, with the most relevant ones appearing at the top of the list.

**Usage**
Upload JD :arrow_up: Start by uploading the job description (JD) by clicking on the corresponding button.<br>
Upload Resumes :arrow_up: After uploading the JD, proceed to upload candidate resumes.<br>
Ranking :1234: Once all resumes are uploaded, the system will automatically rank them based on their compatibility with the JD.<br>
View Results :eyes: Users can then view the ranked list of resumes, with the most suitable candidates listed at the top.<br>

Step 1 User need to upload the resumes and job description to the portal.

<hr>
<img src="https://github.com/codeasarjun/Resume-Parser/blob/main/images/upload_page.png">
<hr>

Step 2 User will redirect to the result page after button click.

Step 3 User will able to see the basic insights of all upload resumes and rating for it, based on given job description.

<hr>
<img src="https://github.com/codeasarjun/Resume-Parser/blob/main/images/result_page.png">
<hr>



📁 resuminds<br>
├── 📁 core<br>
│   ├── 📄 extract_name.py<br>
│   └── 📄 extract_skills_education.py<br>
├── 📁 images<br>
├── 📁 raw_resumes<br>
├── 📁 templates<br>
│   ├── 📄 index.html<br>
│   └── 📄 results.html<br>
├── 📄 app.py<br>
└── 📄 README.md<br>

images: Folder for storing images related to the project.<br>
raw_resumes: Folder for storing raw resumes uploaded by users.<br>



# Future Enhancements
Implement a more sophisticated matching algorithm to improve accuracy.
Enhance the user interface for better user experience.
Integrate additional features such as keyword highlighting and candidate filtering options.
  Resume Parser<br>
        core -  all the supporting functions<br>
        images - visual view of app<br>
        raw_resumes -will have all the resumes and JD<br>
        templates - all the html files<br>

