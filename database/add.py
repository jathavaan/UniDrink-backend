from xmlrpc.client import DateTime

from database.db import League, session, Country, Team
from model.api import API

api = API()


def add_countries():
    countries = api.get_countries()

    for country in countries:
        country_id = country['country_id']
        name = country['name']
        country_code = country['country_code']
        continent = country['continent']

        new_country = Country(country_id, name, country_code, continent)
        session.add(new_country)
        session.commit()

        print("Added country: " + new_country.__repr__())


def add_leagues():
    leagues = api.get_leagues()

    for league in leagues:
        league_id = league['league_id']
        name = league['name']
        country_id = league['country_id']

        new_league = League(league_id, name, country_id)
        session.add(new_league)
        session.commit()

        print("Added league: " + new_league.__repr__())


def add_teams():
    league_ids = api.get_league_ids()
    leagues = list(map(lambda id: api.get_teams_by_league(id), league_ids))

    for league in leagues:
        for team in league:
            team_id = team['team_id']
            name = team['name']
            short_code = team['short_code']
            common_name = team['common_name']
            logo = team['logo']

            print(team_id, name, short_code, common_name, logo)

            new_team = Team(team_id, name, short_code, logo, common_name)
            session.add(new_team)
            session.commit()
            print("Added team: " + new_team.__repr__())


def add_seasons():
    leagues = api.get_seasons()
    seasons = []
    for league in leagues:
        for season in league:
            season_id = season['team_id']
            league_id = season['league_id']
            name = season['name']
            is_current = False

            if season['is_current'] == 1:
                is_current = True

            start_date = DateTime(season['start_date'])
            end_date = DateTime(season['end_date'])

            new_season = Season(season_id, league_id, name, is_current, start_date, end_date)
            session.add(new_season)
            session.commit()


add_countries()
add_leagues()
add_teams()
add_seasons()
