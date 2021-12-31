from datetime import timedelta

import sqlalchemy.exc
from flask import Flask, render_template

from database.add import add_countries, add_leagues, add_teams, add_seasons, add_standings, populate_leagues_has_teams
from database.retrieve import get_countries, get_leagues, get_teams, get_seasons, get_standings
from views.football_data.fb_data import fb_data

app = Flask(__name__)
app.register_blueprint(fb_data, url_prefix="/football_data")
app.secret_key = 'trx0rua*TZU-tkm6ren'
app.permanent_session_lifetime = timedelta(minutes=60)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    try:
        if len(get_countries()) == 0:
            add_countries()
    except sqlalchemy.exc.IntegrityError as e:
        print(str(e))

    try:
        if len(get_leagues()) == 0:
            add_leagues()
    except sqlalchemy.exc.IntegrityError as e:
        print(str(e))

    try:
        if len(get_teams()) == 0:
            add_teams()
    except sqlalchemy.exc.IntegrityError as e:
        print(str(e))

    try:
        if len(get_seasons()) == 0:
            add_seasons()
    except sqlalchemy.exc.IntegrityError as e:
        print(str(e))

    try:
        if len(get_standings()) == 0:
            add_standings()
            populate_leagues_has_teams()
    except sqlalchemy.exc.IntegrityError as e:
        print(str(e))

    app.run(debug=True)
