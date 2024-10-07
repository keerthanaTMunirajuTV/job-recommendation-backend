from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

#configuration of database starts here
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#UserProfile model
class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    skills = db.Column(db.PickleType, nullable=False)
    experience_level = db.Column(db.String(50), nullable=False)
    preferences = db.Column(db.JSON, nullable=False)

#JobPosting model
class JobPosting(db.Model):
    job_id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    required_skills = db.Column(db.PickleType, nullable=False)
    location = db.Column(db.String(50), nullable=False)
    job_type = db.Column(db.String(50), nullable=False)
    experience_level = db.Column(db.String(50), nullable=False)

# Route to add user profile
# @app.route('/user/profile', methods=['POST'])
# def add_profile():
#     data = request.json
#     new_profile = UserProfile(
#         name=data['name'],
#         skills=data['skills'],
#         experience_level=data['experience_level'],
#         preferences=data['preferences']
#     )
#     db.session.add(new_profile)
#     db.session.commit()
#     return jsonify({"message": "Profile added successfully!"}), 201

@app.route('/user/profile', methods=['POST'])
def add_profile():
    
    data = request.json
    
    # Creating a new UserProfile object and adding it to the database
    new_profile = UserProfile(
        name=data['name'],
        skills=data['skills'],
        experience_level=data['experience_level'],
        preferences=data['preferences']
    )
    db.session.add(new_profile)
    db.session.commit()
    
    user_profile = new_profile

    # it Fetches all job postings from the database
    job_postings = JobPosting.query.all()

    # List to store the recommended jobs
    recommendations = []

    # Matching logic based on skills and other criteria
    for job in job_postings:
        match_score = len(set(user_profile.skills) & set(job.required_skills))
        # Adding a job to recommendations if there is a skill match
        if match_score > 0:
            recommendations.append({
                "job_title": job.job_title,
                "company": job.company,
                "location": job.location,
                "job_type": job.job_type,
                "required_skills": job.required_skills,
                "experience_level": job.experience_level
            })

    # Returns a response that includes both a success message and the job recommendations
    return jsonify({
        "message": "Profile added successfully!",
        "recommendations": recommendations
    }), 201


# Route to get job recommendations
@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    user_profile = UserProfile.query.first() 
    job_postings = JobPosting.query.all()  
    recommendations = []

    
    for job in job_postings:
        match_score = len(set(user_profile.skills) & set(job.required_skills))
        if match_score > 0:  
            recommendations.append({
                "job_title": job.job_title,
                "company": job.company,
                "location": job.location,
                "job_type": job.job_type,
                "required_skills": job.required_skills,
                "experience_level": job.experience_level
            })
    return jsonify(recommendations)


@app.route('/job/add', methods=['POST'])
def add_job_postings():
    # Defining some sample job postings
    jobs = [
        {"job_title": "Backend Developer", "company": "Tech Solutions Inc.", "required_skills": ["Python", "Django", "REST APIs"], "location": "Remote", "job_type": "Full-Time", "experience_level": "Intermediate"},
        {"job_title": "Software Engineer", "company": "Innovative Tech Corp.", "required_skills": ["Python", "Microservices", "SQL"], "location": "New York", "job_type": "Full-Time", "experience_level": "Intermediate"},
        {"job_title": "Data Scientist", "company": "Data Analytics Corp.", "required_skills": ["Python", "Data Analysis", "Machine Learning"], "location": "Remote", "job_type": "Full-Time", "experience_level": "Intermediate"}
    ]

    for job in jobs:
        new_job = JobPosting(
            job_title=job['job_title'],
            company=job['company'],
            required_skills=job['required_skills'],
            location=job['location'],
            job_type=job['job_type'],
            experience_level=job['experience_level']
        )
        db.session.add(new_job)
    db.session.commit()
    return jsonify({"message": "Job postings added successfully!"}), 201


# Running the Flask application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # To Create database tables
        print("All Job Postings in Database:", JobPosting.query.all())
    app.run(debug=True)

