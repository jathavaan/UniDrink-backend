from sample.api import API

api = API()


class League:
    def __init__(self, league_id: int):
        if not isinstance(league_id, int):
            raise TypeError("Invalid datatype")

        league = api.get_league_by_id(league_id)

        self.__league_id = league['league_id']
        self.__country_id = league['country_id']
        self.__name = league['name']
        self.__teams = self.__setup_teams(league_id)

    def get_league_id(self) -> int:
        return self.__league_id

    def get_country_id(self) -> int:
        return self.__country_id

    def get_name(self) -> str:
        return self.__name

    def __setup_teams(self, league_id: int):
        if not isinstance(league_id, int):
            raise TypeError("Invalid datatype")

        return list(map(lambda team: Team(team['team_id'], team['name'], team['short_code'], team['logo']),
                        api.get_teams_by_league(league_id)))

    def __set_position(self, league_id: int, team_id: int):
        if not isinstance(league_id, int):
            raise TypeError("Invalid datatype")

        if not isinstance(team_id, int):
            raise TypeError("Invalid datatype")

        if league_id not in api.get_league_ids():
            raise ValueError("Could not find a league ID that matches:", league_id)

        teams = api.get_teams_by_league(league_id)
        standings = api.get_league_standings(league_id)

        """
        for team in teams:
            print(team)
            for league in standings:
                print(league)
        """
        return None

    def get_teams(self) -> list:
        return self.__teams

    def to_string(self) -> str:
        teams = ""

        for team in self.get_teams():
            teams += "\t" + team.to_string() + "\n"

        return f"{self.get_name()} " \
               f"\n=> League ID: {self.get_league_id()} " \
               f"\n=> Country ID: {self.get_country_id()}" \
               f"\n=> Teams: \n{teams}"


class Team:
    def __init__(self, team_id: int, name: str, short_code: str, logo: str):
        if not isinstance(team_id, int):
            raise TypeError("Invalid datatype")

        if not isinstance(name, str):
            raise TypeError("Invalid datatype")

        if not isinstance(short_code, str):
            raise TypeError("Invalid datatype")

        if not isinstance(logo, str):
            raise TypeError("Invalid datatype")

        self.__team_id = team_id
        self.__name = name
        self.__short_code = short_code
        self.__logo = logo
        self.__setup_stats()

    def get_name(self) -> str:
        return self.__name

    def get_team_id(self) -> int:
        return self.__team_id

    def get_short_code(self) -> str:
        return self.__short_code

    def get_logo(self) -> str:
        return self.__logo

    def get_league_id(self) -> int:
        team_id = self.get_team_id()

        print(api.get_standings())


    def to_string(self) -> str:
        return f"{self.get_name()} [{self.get_short_code()}] | Team ID: {self.get_team_id()}"

    def __setup_stats(self):
        team_id = self.get_team_id()
        seasons = api.get_seasons()
        league_ids = api.get_league_ids()

        for league_id in league_ids:
            standings = api.get_league_standings(league_id)
            seasons = api.get_seasons_by_id(league_id)
            current_season = seasons[0]
            for season in seasons:
                if season['is_current'] == 1:
                    current_season = season
                    break

            season_id = current_season['season_id']



class Standings:
    def __init__(self, league_id: int):
        if not isinstance(league_id, int):
            raise TypeError("Invalid datatype")

        if league_id not in api.get_league_ids():
            raise ValueError("Could not find a league ID tha matches:", league_id)

        standings = api.get_league_standings(league_id)

        print(standings)