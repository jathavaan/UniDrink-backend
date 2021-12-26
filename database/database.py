import sqlalchemy as sql

from base import Base


class Country(Base):
    __tablename__ = 'countries'
    country_id = sql.Column('country_id', sql.Integer, autoincrement=False, primary_key=True)
    name = sql.Column('name', sql.String(100), nullable=False)
    country_code = sql.Column('country_code', sql.String(100), nullable=False)
    continent = sql.Column('continent', sql.String(100), nullable=False)


class League(Base):
    __tablename__ = 'leagues'
    league_id = sql.Column('league_id', sql.Integer, autoincrement=False, primary_key=True)
    name = sql.Column('name', sql.String(100), nullable=False)
    country_id = sql.Column('country_id', sql.Integer, nullable=False)


class Team(Base):
    __tablename__ = 'teams'
    team_id = sql.Column('team_id', autoincrement=False, primary_key=True)
    name = sql.Column('name', sql.String(100), nullable=False)
    short_code = sql.Column('short_code', sql.String(10), nullable=False)
    logo = sql.Column('logo', sql.String(100), nullable=True)
    common_name = sql.Column('common_name', sql.String(100), nullable=True)


class Season(Base):
    __tablename__ = 'seasons'
    season_id = sql.Column('season_id', sql.Integer, autoincrement=False, primary_key=True)
    league_id = sql.Column('league_id', sql.Integer, nullable=False)
    name = sql.Column('name', sql.String(100), nullable=False)
    is_current = sql.Column('is_current', sql.Boolean, nullable=False)
    start_date = sql.Column('start_date', sql.DateTime, nullable=False)
    end_date = sql.Column('end_date', sql.DateTime, nullable=False)


class Standing(Base):
    __tablename__ = 'standings'
    standing_id = sql.Column('standing_id', sql.Integer, autoincrement=True, primary_key=True)
    season_id = sql.Column('season_id', sql.Integer, nullable=False)
    league_id = sql.Column('league_id', sql.Integer, nullable=False)
    team_id = sql.Column('team_id', sql.Integer, nullable=False)
    has_group = sql.Column('has_group', sql.Boolean, nullable=False)
    points = sql.Column('points', sql.Integer, nullable=False)
    status = sql.Column('status', sql.String(100), nullable=False)
    result = sql.Column('result', sql.String(100), nullable=False)

    total_games_played = sql.Column('total_games_played', sql.Integer, nullable=False)
    total_games_won = sql.Column('total_games_won', sql.Integer, nullable=False)
    total_games_draw = sql.Column('total_games_draw', sql.Integer, nullable=False)
    total_games_lost = sql.Column('total_games_lost', sql.Integer, nullable=False)
    total_goals_diff = sql.Column('total_goals_diff', sql.Integer, nullable=False)
    total_goals_scored = sql.Column('total_goals_scored', sql.Integer, nullable=False)
    total_goals_against = sql.Column('total_goals_against', sql.Integer, nullable=False)

    home_games_played = sql.Column('home_games_played', sql.Integer, nullable=False)
    home_games_won = sql.Column('home_games_won', sql.Integer, nullable=False)
    home_games_draw = sql.Column('home_games_draw', sql.Integer, nullable=False)
    home_games_lost = sql.Column('home_games_lost', sql.Integer, nullable=False)
    home_goals_diff = sql.Column('home_goals_diff', sql.Integer, nullable=False)
    home_goals_scored = sql.Column('home_goals_scored', sql.Integer, nullable=False)
    home_goals_against = sql.Column('home_goals_against', sql.Integer, nullable=False)

    away_games_played = sql.Column('away_games_played', sql.Integer, nullable=False)
    away_games_won = sql.Column('away_games_won', sql.Integer, nullable=False)
    away_games_draw = sql.Column('away_games_draw', sql.Integer, nullable=False)
    away_games_lost = sql.Column('away_games_lost', sql.Integer, nullable=False)
    away_goals_diff = sql.Column('away_goals_diff', sql.Integer, nullable=False)
    away_goals_scored = sql.Column('away_goals_scored', sql.Integer, nullable=False)
    away_goals_against = sql.Column('away_goals_against', sql.Integer, nullable=False)
