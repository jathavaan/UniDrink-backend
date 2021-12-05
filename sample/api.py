"""
API documentation:
https://app.sportdataapi.com/documentation
"""
import requests


class API:
    def __init__(self):
        self.__base_url = "https://app.sportdataapi.com/api/v1/soccer/"
        self.__api_key = "35180e80-4c9a-11ec-b94b-1b36a8153030"
        self.__leagues = self.__setup_leagues()
        self.__seasons = self.__setup_seasons()
        self.__teams = self.__setup_teams()

    def __get_base_url(self) -> str:
        return self.__base_url

    def __get_api_key(self) -> str:
        return self.__api_key

    # LEAGUE

    def __setup_leagues(self) -> requests:
        url = f"{self.__get_base_url()}leagues"

        headers = {
            "apikey": self.__get_api_key()
        }

        params = {
            ("subscribed", True)
        }

        return requests.get(url, headers=headers, params=params).json()

    def get_leagues(self) -> list[dict]:
        return self.__leagues['data']

    def get_league_ids(self) -> list[int]:
        return list(map(lambda leagues: leagues['league_id'], self.get_leagues()))

    # SEASON

    def __setup_seasons(self):
        seasons = []
        for league_id in self.get_league_ids():
            url = f"{self.__get_base_url()}seasons"

            headers = {
                "apikey": self.__get_api_key()
            }

            params = (
                ("league_id", str(league_id)),
            )

            seasons.append(requests.get(url, headers=headers, params=params).json()['data'])

        return seasons

    def get_seasons(self) -> list:
        return self.__seasons

    def get_seasons_by_id(self, league_id: int) -> list:
        if not isinstance(league_id, int):
            raise TypeError("Invalid datatype")

        if league_id not in self.get_league_ids():
            raise ValueError("Could not find any leagues that have the following ID:", league_id)

        seasons = self.get_seasons()
        s = []

        for league in seasons:
            for season in league:
                if season['league_id'] == league_id:
                    s.append(season)

        return s

    def get_current_season(self, league_id: int):
        return next(filter(lambda season: season['is_current'] == 1, self.get_seasons_by_id(league_id)))

    # MATCH

    # TEAM

    def __setup_teams(self):
        leagues = self.get_leagues()
        league_ids = self.get_league_ids()
        teams = []

        for league_id in league_ids:
            country_id = next(filter(lambda league: league['league_id'] == league_id, leagues))['country_id']

            url = f"{self.__get_base_url()}teams"

            headers = {
                "apikey": self.__get_api_key()
            }

            params = (
                ("country_id", country_id),
            )

            j = requests.get(url, headers=headers, params=params).json()

            teams.append(j)

        return teams

    def get_teams(self):
        return self.__teams

    # PLAYER


api = API()
print("Ligaer:", api.get_leagues())
print("Liga ID:", api.get_league_ids())
print("Sesonger:", api.get_seasons())
print("Pågående sesong:", api.get_current_season(237))
print(api.get_teams())
