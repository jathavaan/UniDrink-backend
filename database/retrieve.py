from database.db import session, Country, League, Season, Standing, Team, league_has_teams, engine

print("\n")


def get_countries():
    results = session.query(Country).all()
    if len(results) == 0:
        return None
    else:
        return results


def get_leagues():
    results = session.query(League).all()
    if len(results) == 0:
        return None
    else:
        return results


def get_teams():
    results = session.query(Team).all()
    if len(results) == 0:
        return None
    else:
        return results


def get_seasons():
    results = session.query(Season).all()
    if len(results) == 0:
        return None
    else:
        return results


def get_standings():
    results = session.query(Standing).all()
    if len(results) == 0:
        return None
    else:
        return results


def get_table():
    results = (session.query(league_has_teams, League, Team).join(League).join(Team)).all()

    if len(results) == 0:
        return None
    else:
        return results


print(get_countries())
print()
print(get_leagues())
print()
print(get_teams())
print()
print(get_seasons())
print()
print(get_standings())
print()
print(get_table())
