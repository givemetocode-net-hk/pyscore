from flask import Flask, render_template, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os

app = Flask(__name__)
app.secret_key = 'https://poe.com/s/I7zLN5f2n1OAU96wsZeY'
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User data
users = {'root': 'root'}

class User(UserMixin):
    def __init__(self, username):
        self.username = username

    def get_id(self):
        return self.username

@login_manager.user_loader
def load_user(username):
    return User(username) if username in users else None

def read_scores(file_path):
    scores = {}
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 3:
                    score_id = parts[0]
                    score_info = ' '.join(parts[1:])
                    scores[score_id] = score_info
    return scores

@app.route('/', methods=['GET', 'POST'])
def index():
    scores = read_scores('score.txt')
    user_score = None

    if request.method == 'POST':
        user_id = request.form['user_id']
        user_score = scores.get(user_id, "Score not found.")

    return render_template('index.html', user_score=user_score)


if __name__ == '__main__':
    app.run(debug=True)