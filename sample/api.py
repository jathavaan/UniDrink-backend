"""
API documentation:
https://app.sportdataapi.com/documentation
"""
import requests
from abc import ABC, abstractmethod


class API(ABC):

    @abstractmethod
    def __init__(self):
        self.__base_url = "https://app.sportdataapi.com/api/v1/soccer/"
        self.__api_key = "35180e80-4c9a-11ec-b94b-1b36a8153030"

    def get_base_url(self) -> str:
        return self.__base_url

    def get_api_key(self) -> str:
        return self.__api_key


class IAPI(ABC):
    @abstractmethod
    def get_response(self) -> requests: pass

    @abstractmethod
    def get_status_code(self) -> int: pass

    @abstractmethod
    def get_json(self) -> dict: pass


class LeagueAPI(API, IAPI):
    pass

    def __init__(self):
        super().__init__()

        headers = {
            "apikey": super().get_api_key()
        }

        params = {
            ("subscribed", True)
        }

        url = f"{super().get_base_url()}leagues/"
        self.__response = requests.get(url, headers=headers, params=params)

    def get_response(self) -> requests:
        return self.__response

    def get_status_code(self) -> int:
        return self.get_response().status_code

    def get_json(self) -> dict:
        return self.get_response().json()['data']

    def get_league_ids(self) -> list[int]:
        league_data = self.get_json()
        id_list = []
        for data in league_data:
            id_list.append(data['league_id'])

        return id_list

    def get_country_id(self, id: int) -> int:
        self.__id_validation(id)

        for league in self.get_json():
            if league['league_id'] == id:
                return league['country_id']

    def get_name(self, id: int) -> str:
        self.__id_validation(id)

        for league in self.get_json():
            if league['league_id'] == id:
                return league['name']

    def __id_validation(self, id: int):
        if not isinstance(id, int):
            raise TypeError

        if id not in self.get_league_ids():
            raise ValueError("Could not find any leagues that have the following ID:", id)


class TeamAPI(API, IAPI):

    def __init__(self, leagueId: int):
        super().__init__()
        league_ids = LeagueAPI().get_league_ids()
        print(league_ids)

    def get_response(self) -> requests:
        pass

    def get_status_code(self) -> int:
        pass

    def get_json(self) -> dict:
        pass


class MatchAPI(API, IAPI):

    def __init__(self):
        super().__init__()

    def get_response(self) -> requests:
        pass

    def get_status_code(self) -> int:
        pass

    def get_json(self) -> dict:
        pass


class PlayerAPI(API, IAPI):

    def __init__(self):
        super().__init__()

    def get_response(self) -> requests:
        pass

    def get_status_code(self) -> int:
        pass

    def get_json(self) -> dict:
        pass


class StatisticsAPI(API, IAPI):

    def __init__(self):
        super().__init__()

    def get_response(self) -> requests:
        pass

    def get_status_code(self) -> int:
        pass

    def get_json(self) -> dict:
        pass


api = LeagueAPI()
print(api.get_json())
print(api.get_league_ids())
print(api.get_name(237))
print(api.get_country_id(237))

print()

api2 = TeamAPI(1)
