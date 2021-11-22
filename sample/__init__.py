from flask import Flask, redirect, url_for
from user import User
import datetime

app = Flask(__name__)


@app.route('/')
def home():
    try:
        user = User("Jathavaan", "Shankarr", datetime.datetime(2001, 7, 12), "pogbanathan", "G@laxys6")
        return f"<h3>{user.to_string()}</h3>"
    except Exception as e:
        return str(e)


@app.route('/<name>')
def user(name):
    return f"Hello {name}"


@app.route('/admin')
def admin():
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
