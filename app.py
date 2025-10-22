from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
import joblib
import re
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# -------------------------------
# Load trained models and vectorizer
# -------------------------------
models = {}
for filename in os.listdir(r'C:\Users\Jagapathi\OneDrive\Desktop\AI4Jobs\models'):
    if filename.endswith('.pkl') and filename != 'vectorizer.pkl':
        model_name = filename.replace('.pkl', '').replace('_', ' ')
        models[model_name] = joblib.load(os.path.join(r'C:\Users\Jagapathi\OneDrive\Desktop\AI4Jobs\models', filename))

vectorizer = joblib.load(r'C:\Users\Jagapathi\OneDrive\Desktop\AI4Jobs\models\vectorizer.pkl')

# -------------------------------
# Text cleaning function (same as notebook)
# -------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

# -------------------------------
# Routes
# -------------------------------
@app.route('/')
@login_required
def home():
    return render_template('index.html', models=models.keys())

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=True)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/predict', methods=['POST'])
@login_required
def predict():
    if request.method == 'POST':
        jobdesc = request.form['jobdesc']
        model_choice = request.form['model']
        
        model = models.get(model_choice)

        if model:
            cleaned = clean_text(jobdesc)
            vect = vectorizer.transform([cleaned])
            pred = model.predict(vect)[0]
            result = "Fake Job Posting 🚫" if pred == 1 else "Real Job Posting ✅"
        else:
            result = "Invalid model selected."

        return render_template('index.html', prediction=result, models=models.keys())

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
