# HNG Stage-0 Backend Task - Public API

This project implements a simple public API that returns basic information in JSON format, including:
- The registered email address used for the HNG12 Slack workspace.
- The current datetime in ISO 8601 format.
- The GitHub URL of the project's codebase.

## Project Description

The goal of this project is to create an API that meets the following requirements:
- **Email**: The registered email for the HNG12 Slack workspace.
- **Current Datetime**: The current UTC time in ISO 8601 format.
- **GitHub URL**: A link to the GitHub repository of the project.

The API should handle GET requests to the `/api/` endpoint and return the required information as a JSON response.

## Project Setup

Follow these steps to set up and run the project locally:

### 1. Clone the Repository

Start by cloning the repository to your local machine:

git clone https://github.com/Okpara007/HNG_Stage-0.git
cd HNG_Stage-0 

2. Set Up a Virtual Environment
It's recommended to create a virtual environment for the project:
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install Dependencies
Install the required dependencies using pip:
pip install -r requirements.txt

4. Run the Development Server
To start the Django development server and test the project locally:
python manage.py runserver
The project will now be running at http://127.0.0.1:8000/
