from flask import Blueprint, render_template, request

import model.sample.database.retrieve as retrieve

fb_data = Blueprint('fb_data', __name__, static_folder="static", template_folder="templates")


# add.main()


@fb_data.route('/', methods=["GET", "POST"])
def football_data():
    leagues = retrieve.get_leagues()
    table = retrieve.get_table(237)  # Sets standard league
    print(table)

    if request.method == "POST":
        league = request.form.get('select-league')
        league_id = int(league)
        table = retrieve.get_table(league_id)

        return render_template('football_data.html', leagues=leagues, table=table)
    else:
        return render_template('football_data.html', leagues=leagues, table=table)
