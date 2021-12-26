import ast

from flask import Blueprint, render_template, request, session

fb_data = Blueprint('fb_data', __name__, static_folder="static", template_folder="templates")


@fb_data.route('/')
def football_data():
    options = [{'league_id': 237, 'country_id': 42, 'name': 'Premier League'}]
    return render_template('football_data.html', options=options)


@fb_data.route('/', methods=["GET", "POST"])
def populateTable():
    if request.method == 'POST':
        data = request.form.get('select-league')
        data_dict = ast.literal_eval(data)
        session['league'] = data_dict

        return data_dict
    else:
        return url_for('football_data')
