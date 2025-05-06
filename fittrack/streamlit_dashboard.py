import sqlite3
import pandas as pd
import streamlit as st
import os

st.set_page_config(page_title="FitTrack Dashboard", layout="centered")

st.title("Your Fitness Progress Dashboard")

# Detect the path of the database
db_path = os.path.join(os.path.dirname(__file__), 'fittrack.db')
if not os.path.exists(db_path):
    st.error("Database not found! Make sure you ran init_db.py and added some data through the Flask app.")
    st.stop()

# Connect to DB and load data
conn = sqlite3.connect(db_path)
workouts = pd.read_sql_query("SELECT * FROM workouts", conn)
meals = pd.read_sql_query("SELECT * FROM meals", conn)
conn.close()

# Validate data
if workouts.empty and meals.empty:
    st.warning("No data found. Please log some workouts and meals first.")
    st.stop()

# ---- Dashboard ----
st.header("Workout Summary")
if not workouts.empty:
    st.bar_chart(workouts.groupby('type')['calories'].sum())
    st.write("Total Calories Burned:", workouts['calories'].sum())
    st.write("Total Minutes:", workouts['duration'].sum())
else:
    st.info("No workouts logged yet.")

st.header("Nutrition Summary")
if not meals.empty:
    st.bar_chart(meals.groupby('meal')['calories'].sum())
    st.write("Total Calories Consumed:", meals['calories'].sum())
    st.write("Total Protein (g):", meals['protein'].sum())
else:
    st.info("No meals logged yet.")

