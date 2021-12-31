from database.db import Country, Season, Standing, Team, engine, League, session


def get_countries():
    results = session.query(Country).all()
    return results


def get_leagues():
    """
    leagues = []
    with engine.connect() as con:
        results = con.execute('SELECT * FROM leagues')

        data = {}
        for result in results:
            league_id, name, country_id = result

            data['league_id'] = league_id
            data['name'] = name
            data['country'] = country_id

            leagues.append(data)

    return leagues
    """

    results = session.query(League).all()
    for r in results:
        print(r)
    return results


def get_teams():
    results = session.query(Team).all()
    return results


def get_seasons():
    results = session.query(Season).all()
    return results


def get_standings():
    results = session.query(Standing).all()
    return results


def get_table(league_id: int):
    if not isinstance(league_id, int):
        raise TypeError("Invalid datatype")

    table = []

    with engine.connect() as con:
        results = con.execute(
            f'SELECT position, logo, teams.name, total_games_played, total_games_won, total_games_draw, total_games_lost, total_goals_scored, total_goals_against, total_goals_diff, points FROM league_has_teams INNER JOIN leagues ON leagues.league_id INNER JOIN teams ON teams.team_id INNER JOIN standings WHERE league_has_teams.league_id == leagues.league_id AND league_has_teams.team_id == teams.team_id AND teams.team_id == standings.team_id AND standings.league_id == {league_id}')
        for result in results:
            pos, logo, name, played, won, draw, lost, scored, against, diff, points = result
            data = {
                "position": pos,
                "logo": logo,
                "name": name,
                "played": played,
                "won": won,
                "draw": draw,
                "lost": lost,
                "scored": scored,
                "against": against,
                "diff": diff,
                "points": points
            }

            table.append(data)

    return table


print(get_table(237))
