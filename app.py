from datetime import timedelta

from flask import Flask, render_template

from model.api import API
from views.football_data.fb_data import fb_data

app = Flask(__name__)
app.secret_key = 'trx0rua*TZU-tkm6ren'
app.permanent_session_lifetime = timedelta(minutes=60)

app.register_blueprint(fb_data, url_prefix="/football_data")

api = API()


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    fb_db.create_all()
    app.run(debug=True)
