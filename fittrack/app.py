from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3, os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def get_db():
    conn = sqlite3.connect('database.db')
    return conn

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        flash('Registered successfully!')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db()
        user = conn.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()
        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            return redirect(url_for('dashboard'))
        flash('Invalid credentials')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/workouts', methods=['GET', 'POST'])
def workouts():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    conn = get_db()
    if request.method == 'POST':
        data = (session['user_id'], request.form['type'], request.form['duration'], request.form['calories'])
        conn.execute("INSERT INTO workouts (user_id, type, duration, calories) VALUES (?, ?, ?, ?)", data)
        conn.commit()
    workouts = conn.execute("SELECT * FROM workouts WHERE user_id=?", (session['user_id'],)).fetchall()
    return render_template('workouts.html', workouts=workouts)

@app.route('/history')
def history():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    conn = get_db()
    data = conn.execute("SELECT * FROM workouts WHERE user_id=?", (session['user_id'],)).fetchall()
    return render_template('history.html', workouts=data)

@app.route('/nutrition', methods=['GET', 'POST'])
def nutrition():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    conn = get_db()
    if request.method == 'POST':
        data = (session['user_id'], request.form['meal'], request.form['calories'], request.form['protein'])
        conn.execute("INSERT INTO nutrition (user_id, meal, calories, protein) VALUES (?, ?, ?, ?)", data)
        conn.commit()
    meals = conn.execute("SELECT * FROM nutrition WHERE user_id=?", (session['user_id'],)).fetchall()
    return render_template('nutrition.html', meals=meals)

@app.route('/workout_history')
def workout_history():
    filter_type = request.args.get('type', '')
    db = get_db()
    if filter_type:
        workouts = db.execute('SELECT * FROM workouts WHERE type = ? ORDER BY date DESC', (filter_type,)).fetchall()
    else:
        workouts = db.execute('SELECT * FROM workouts ORDER BY date DESC').fetchall()
    return render_template('workout_history.html', workouts=workouts)

@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    bmi = status = None
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height_cm = float(request.form['height'])
        height_m = height_cm / 100
        bmi = round(weight / (height_m ** 2), 2)
        if bmi < 18.5:
            status = "Underweight"
        elif 18.5 <= bmi < 25:
            status = "Normal"
        elif 25 <= bmi < 30:
            status = "Overweight"
        else:
            status = "Obese"
    return render_template('bmi.html', bmi=bmi, status=status)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/streamlit')
def streamlit_redirect():
    return redirect("http://localhost:8501")

if __name__ == '__main__':
    app.run(debug=True)
