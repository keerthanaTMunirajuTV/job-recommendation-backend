# Job Recommendation Backend Service

## Project Overview

This project is a **Job Recommendation Backend Service** that provides job recommendations based on user profiles. The backend service is built using **Flask** and **SQLAlchemy** and supports operations like adding user profiles, fetching job recommendations, and managing job postings.

The service uses a simple recommendation algorithm to match job postings with user profiles based on skills, experience level, and preferences.

## Features

- **User Profile Management**: Create user profiles with skills, experience level, and preferences.
- **Job Recommendations**: Get job recommendations based on user profiles.
- **Database Integration**: Store and manage user profiles and job postings in a SQL database.
- **RESTful API**: Exposes RESTful endpoints to interact with the service.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.6+
- Flask
- Flask-SQLAlchemy

## Project Structure

job-recommendation-backend/ │ ├── app.py # Main application file ├── jobs.db # SQLite database file ├── README.md # Project documentation ├── requirements.txt # Project dependencies └── job-recommendation-env/ # (Optional) Virtual environment folder

## Setup Instructions

Follow these steps to set up and run the project locally:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/job-recommendation-backend.git
   cd job-recommendation-backend
2. **Create a virtual environment (optional but recommended)**:
    python -m venv job-recommendation-env

3. **Activate the virtual environment**:
on windows
    .\job-recommendation-env\Scripts\activate

4. **Install dependencies**:
    pip install -r requirements.txt
5. **Run the Flask application**:
    python app.py
6. **Access the API**:
    The Flask server will start on http://127.0.0.1:5000/. You can now use Postman or cURL to interact with the API endpoints.


API Endpoints
1. POST /user/profile
    Create a new user profile and get job recommendations in the response.

    URL: http://127.0.0.1:5000/user/profile

    Method: POST

    Request Body:

    json
    Copy code
    {
    "name": "John Doe",
    "skills": ["Python", "Django", "REST APIs"],
    "experience_level": "Intermediate",
    "preferences": {
        "desired_roles": ["Backend Developer"],
        "locations": ["Remote"],
        "job_type": "Full-Time"
    }
    }
    Response:

    json
    Copy code
    {
    "message": "Profile added successfully!",
    "recommendations": [
        {
        "job_title": "Backend Developer",
        "company": "Tech Solutions Inc.",
        "location": "Remote",
        "job_type": "Full-Time",
        "required_skills": ["Python", "Django", "REST APIs"],
        "experience_level": "Intermediate"
        },
        ...
    ]
    }
2. GET /recommendations
    Retrieve job recommendations based on the first user profile in the database.

    URL: http://127.0.0.1:5000/recommendations
    Method: GET
    Response:
    json
    Copy code
    [
    {
        "job_title": "Backend Developer",
        "company": "Tech Solutions Inc.",
        "location": "Remote",
        "job_type": "Full-Time",
        "required_skills": ["Python", "Django", "REST APIs"],
        "experience_level": "Intermediate"
    },
    ...
    ]
3. POST /job/add (Optional)
    Add sample job postings to the database.

    URL: http://127.0.0.1:5000/job/add
    Method: POST
    Response:
    json
    Copy code
    {
    "message": "Job postings added successfully!"
    }

Recommendation Logic
The recommendation algorithm is based on matching user skills with job posting requirements:
    Skills Matching: Matches the skills of the user with the required skills of job postings.
    Experience Level Matching: Filters jobs based on the experience level of the user.
    Preference Matching: Considers user preferences such as desired roles, locations, and job type.
    Example Use Cases
    Create a User Profile: Add a new user profile and get job recommendations in the response.
    Get Job Recommendations: Fetch job recommendations based on the existing user profile in the database.