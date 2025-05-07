# FitTrack: A Fitness Tracker Web Application

FitTrack is a full-stack web application built using **Flask** and **Streamlit**, allowing users to track workouts, log meals, view daily summaries, and analyze fitness data interactively.

---

## Features

-  User Registration & Login (Secure authentication)
-  Workout Logging (type, duration, calories)
-  Meal Logging (calories, macros)
-  Streamlit Dashboard for data visualization
-  Workout History with filtering
-  BMI Calculator
-  Daily Summary (Calories burned vs. consumed)

---

##  Technologies Used

- **Backend:** Python, Flask, SQLite
- **Frontend:** HTML, Jinja Templates, CSS
- **Visualization:** Streamlit
- **Authentication:** Werkzeug Password Hashing
- **IDE:** Visual Studio Code

---

## ⚙️ Setup Instructions (in VS Code)

### 1. Clone the Project or Open in VS Code

```bash
git clone <your_repo_url>
cd <project_folder>

#2 CREATE A VIRUTAL ENVIRONMENT 

#FOR WINDOWS 
python -m venv venv
.\venv\Scripts\activate

#FOR MAC 
python3 -m venv venv
source venv/bin/activate

#3 INSTALL DEPENDENCIES 
pip install -r requirements.txt

#IF REQUIREMENTS IS MISSING: 
pip install flask streamlit
pip freeze > requirements.txt

#SET EVIRONMENT VARIABLES 

#FOR WINDOWS 
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"

#FOR MAC 
export FLASK_APP=app.py
export FLASK_ENV=development

#5 RUN FLASK APP 
flask run

#6 RUN STREAMLIT DASHBOARD 
streamlit run streamlit_dashboard.py
