import datetime

from model.sample.database.db import League, session, Country, Team, Season, Standing, LeagueHasTeam
from model.sample.database.retrieve import get_standings
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

        # print("Added country: " + new_country.__repr__())


def add_leagues():
    leagues = api.get_leagues()

    for league in leagues:
        league_id = league['league_id']
        name = league['name']
        country_id = league['country_id']

        new_league = League(league_id, name, country_id)
        session.add(new_league)
        session.commit()

        # print("Added league: " + new_league.__repr__())


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

            new_team = Team(team_id, name, short_code, logo, common_name)
            session.add(new_team)
            session.commit()
            # print("Added team: " + new_team.__repr__())


def add_seasons():
    leagues = api.get_seasons()

    for league in leagues:
        for season in league:
            print(season)
            season_id = season['season_id']
            league_id = season['league_id']
            name = season['name']
            is_current = False

            if season['is_current'] == 1:
                is_current = True

            format = '%Y-%m-%d'

            start_date = datetime.datetime.strptime(season['start_date'], format).date()
            end_date = datetime.datetime.strptime(season['end_date'], format).date()

            new_season = Season(season_id, league_id, name, is_current, start_date, end_date)
            session.add(new_season)
            session.commit()

            print("Added season: " + new_season.__repr__())


def add_standings():
    leagues = api.get_standings()
    for league in leagues:
        season_id = league['season_id']
        league_id = league['league_id']
        has_groups = False

        if league['has_groups'] == 1:
            has_groups = True

        standings = league['standings']

        for team in standings:
            overall = team['overall']
            home = team['home']
            away = team['away']

            team_id = team['team_id']
            position = team['position']
            points = team['points']
            status = team['status']
            result = team['result']

            # Overall
            total_games_played = overall['games_played']
            total_won = overall['won']
            total_draw = overall['draw']
            total_lost = overall['lost']
            total_goals_diffs = overall['goals_diff']
            total_goals_scored = overall['goals_scored']
            total_goals_against = overall['goals_against']

            # Home
            home_games_played = home['games_played']
            home_won = home['won']
            home_draw = home['draw']
            home_lost = home['lost']
            home_goals_diffs = home['goals_diff']
            home_goals_scored = home['goals_scored']
            home_goals_against = home['goals_against']

            # Away
            away_games_played = away['games_played']
            away_won = away['won']
            away_draw = away['draw']
            away_lost = away['lost']
            away_goals_diffs = away['goals_diff']
            away_goals_scored = away['goals_scored']
            away_goals_against = away['goals_against']

            new_standing = Standing(
                season_id, league_id, team_id, has_groups, points, position, status, result,
                total_games_played, total_won, total_draw, total_lost, total_goals_diffs, total_goals_scored,
                total_goals_against,
                home_games_played, home_won, home_draw, home_lost, home_goals_diffs, home_goals_scored,
                home_goals_against,
                away_games_played, away_won, away_draw, away_lost, away_goals_diffs, away_goals_scored,
                away_goals_against
            )

            session.add(new_standing)
            session.commit()

            # print("Added standing: " + new_standing.__repr__())


def populate_leagues_has_teams():
    standings = get_standings()
    for standing in standings:
        team_id = standing.team_id
        league_id = standing.league_id

        new_league_has_team = LeagueHasTeam(league_id, team_id)
        session.add(new_league_has_team)
        session.commit()

        # print("Added league/team connection: " + new_league_has_team.__repr__())
