import datetime

import sqlalchemy as sql
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///football_data_db.db', connect_args={'check_same_thread': False}, echo=True)
session = sessionmaker(autoflush=False, bind=engine)()

metadata = sql.MetaData(
    naming_convention={
        "ix": "ix__%(column_0_label)s",
        "uq": "uq__%(table_name)s__%(column_0_name)s",
        "ck": "ck__%(table_name)s__%(constraint_name)s",
        "fk": "fk__%(table_name)s__%(column_0_name)s__%(referred_table_name)s",
        "pk": "pk__%(table_name)s"
    }
)

Base = declarative_base(metadata=metadata)


class Country(Base):
    __tablename__ = 'countries'
    country_id = sql.Column('country_id', sql.Integer, autoincrement=False, primary_key=True)
    name = sql.Column('name', sql.String(100), nullable=False)
    country_code = sql.Column('country_code', sql.String(100), nullable=True)
    continent = sql.Column('continent', sql.String(100), nullable=True)

    def __init__(self, country_id: int, name: str, country_code: str, continent: str):
        if not isinstance(country_id, int):
            raise TypeError("Invalid datatype")

        if not isinstance(name, str):
            raise TypeError("Invalid datatype")

        if not isinstance(country_code, str) and country_code is not None:
            raise TypeError("Invalid datatype")

        if not isinstance(continent, str) and continent is not None:
            raise TypeError("Invalid datatype")

        self.country_id = country_id
        self.name = name
        self.country_code = country_code
        self.continent = continent

    def __repr__(self):
        return f"<Country:(" \
               f"country_id={self.country_id}, " \
               f"name={self.name}, " \
               f"country_code={self.country_code}, " \
               f"continent={self.continent}" \
               f")> "


class League(Base):
    __tablename__ = 'leagues'
    league_id = sql.Column(
        'league_id',
        sql.Integer,
        ForeignKey('seasons.league_id', ondelete="CASCADE"),
        autoincrement=False,
        primary_key=True
    )
    name = sql.Column('name', sql.String(100), nullable=False)
    country_id = sql.Column(
        'country_id',
        sql.Integer,
        ForeignKey("countries.country_id", ondelete="CASCADE"),
        nullable=False
    )

    # teams = relationship('Team', secondary=league_has_teams, backref="leagues")

    def __init__(self, league_id: int, name: str, country_id: int):
        if not isinstance(league_id, int):
            raise TypeError("Invalid datatype")

        if not isinstance(league_id, int):
            raise TypeError("Invalid datatype")

        if not isinstance(name, str):
            raise TypeError("Invalid datatype")

        self.league_id = league_id
        self.name = name
        self.country_id = country_id

    def __repr__(self):
        return f"<League(" \
               f"league_id={self.league_id}, " \
               f"name={self.name}, " \
               f"country_id={self.country_id}" \
               f")>"


class Team(Base):
    __tablename__ = 'teams'
    team_id = sql.Column(
        'team_id',
        sql.Integer,
        autoincrement=False,
        primary_key=True,
        nullable=False
    )
    name = sql.Column('name', sql.String(100), nullable=False)
    short_code = sql.Column('short_code', sql.String(10), nullable=True)
    logo = sql.Column('logo', sql.String(100), nullable=True)
    common_name = sql.Column('common_name', sql.String(100), nullable=True)

    def __init__(self, team_id: int, name: str, short_code: str, logo: str, common_name: str):
        if not isinstance(team_id, int):
            raise TypeError("Invalid datatype")

        if not isinstance(name, str):
            raise TypeError("Invalid datatype")

        if not isinstance(short_code, str):
            raise TypeError("Invalid datatype")

        if not isinstance(common_name, str):
            raise TypeError("Invalid datatype")

        if not isinstance(logo, str):
            raise TypeError("Invalid datatype")

        self.team_id = team_id
        self.name = name
        self.short_code = short_code
        self.logo = logo
        self.common_name = common_name

    def __repr__(self):
        return f"<Team(" \
               f"team_id={self.team_id}, " \
               f"name={self.name}, " \
               f"short_code={self.short_code}, " \
               f"logo={self.logo}, " \
               f"common_name={self.common_name}" \
               f")>"


class LeagueHasTeam(Base):
    __tablename__ = 'league_has_teams'
    # id = sql.Column('id', sql.Integer, primary_key=True)
    league_id = sql.Column('league_id', sql.Integer, ForeignKey('leagues.league_id'), primary_key=True,
                           autoincrement=False)
    team_id = sql.Column('team_id', sql.Integer, ForeignKey('teams.team_id'), primary_key=True, autoincrement=False)

    def __init__(self, league_id: int, team_id: int):
        if not isinstance(league_id, int):
            raise TypeError("Invalid datatype")

        if not isinstance(team_id, int):
            raise TypeError("Invalid datatype")

        self.league_id = league_id
        self.team_id = team_id

    def __repr__(self):
        return f"<LeagueHasTeam(" \
               f"league_id={self.league_id}, " \
               f"team_id={self.team_id}" \
               f")>"


class Season(Base):
    __tablename__ = 'seasons'
    season_id = sql.Column('season_id', sql.Integer, autoincrement=False, primary_key=True)
    league_id = sql.Column('league_id', sql.Integer, nullable=False)
    name = sql.Column('name', sql.String(100), nullable=False)
    is_current = sql.Column('is_current', sql.Boolean, nullable=False)
    start_date = sql.Column('start_date', sql.DateTime, nullable=False)
    end_date = sql.Column('end_date', sql.DateTime, nullable=False)

    def __init__(self, season_id: int, league_id: int, name: str, is_current: bool, start_date: datetime.date,
                 end_date: datetime.date):
        if not isinstance(season_id, int):
            raise TypeError("Invalid datatype")

        if not isinstance(league_id, int):
            raise TypeError("Invalid datatype")

        if not isinstance(name, str):
            raise TypeError("Invalid datatype")

        if not isinstance(is_current, bool):
            raise TypeError("Invalid datatype")

        if not isinstance(start_date, datetime.date):
            raise TypeError("Invalid datatype")

        if not isinstance(end_date, datetime.date):
            raise TypeError("Invalid datatype")

        self.season_id = season_id
        self.league_id = league_id
        self.name = name
        self.is_current = is_current
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"<Season(" \
               f"season_id={self.season_id}, " \
               f"league_id={self.league_id}, " \
               f"name={self.name}, " \
               f"is_current={self.is_current}, " \
               f"start_date={self.start_date}, " \
               f"end_date={self.end_date}" \
               f")>"


class Standing(Base):
    __tablename__ = 'standings'
    standing_id = sql.Column('standing_id', sql.Integer, autoincrement=True, primary_key=True)
    season_id = sql.Column(
        'season_id',
        sql.Integer,
        # ForeignKey('seasons.season_id', ondelete="CASCADE"),
        nullable=False
    )
    league_id = sql.Column(
        'league_id',
        sql.Integer,
        # ForeignKey('seasons.league_id', ondelete="CASCADE"),
        nullable=False
    )
    team_id = sql.Column(
        'team_id',
        sql.Integer,
        # ForeignKey('teams.team_id', ondelete="CASCADE"),
        nullable=False
    )

    # season = relationship('Season', backref='standings')
    # league = relationship('Season', backref='standings')
    # team = relationship('Team', backref='teams')

    has_group = sql.Column('has_group', sql.Boolean, nullable=False)
    points = sql.Column('points', sql.Integer, nullable=False)
    position = sql.Column('position', sql.Integer, nullable=False)
    status = sql.Column('status', sql.String(100), nullable=True)
    result = sql.Column('result', sql.String(100), nullable=True)

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

    def __init__(
            self, season_id: int, league_id: int, team_id: int, has_group: bool, points: int, position: int,
            status: str, result: str,
            total_games_played: int, total_games_won: int, total_games_draw: int, total_games_lost: int,
            total_goals_diff: int, total_goals_scored: int, total_goals_against: int,
            home_games_played: int, home_games_won: int, home_games_draw: int, home_games_lost: int,
            home_goals_diff: int, home_goals_scored: int, home_goals_against: int,
            away_games_played: int, away_games_won: int, away_games_draw: int, away_games_lost: int,
            away_goals_diff: int, away_goals_scored: int, away_goals_against: int
    ):
        # Add datatype validation
        self.season_id = season_id
        self.league_id = league_id
        self.team_id = team_id
        self.has_group = has_group
        self.points = points
        self.position = position
        self.status = status
        self.result = result

        self.total_games_played = total_games_played
        self.total_games_won = total_games_won
        self.total_games_draw = total_games_draw
        self.total_games_lost = total_games_lost
        self.total_goals_diff = total_goals_diff
        self.total_goals_scored = total_goals_scored
        self.total_goals_against = total_goals_against

        self.home_games_played = home_games_played
        self.home_games_won = home_games_won
        self.home_games_draw = home_games_draw
        self.home_games_lost = home_games_lost
        self.home_goals_diff = home_goals_diff
        self.home_goals_scored = home_goals_scored
        self.home_goals_against = home_goals_against

        self.away_games_played = away_games_played
        self.away_games_won = away_games_won
        self.away_games_draw = away_games_draw
        self.away_games_lost = away_games_lost
        self.away_goals_diff = away_goals_diff
        self.away_goals_scored = away_goals_scored
        self.away_goals_against = away_goals_against

    def __repr__(self):
        return f"<Standing(" \
               f"standing_id={self.standing_id}, " \
               f"season_id={self.season_id}, " \
               f"team_id={self.team_id}" \
               f")>"


def init_db():
    Base.metadata.create_all(bind=engine)
    print(metadata.tables)  # prints out the tables in the database


init_db()
