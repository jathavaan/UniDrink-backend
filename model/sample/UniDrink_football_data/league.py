from typing import Type

from team import Team


class League:
    def __init__(self, league_id: int, country_id: int, name: str):
        if not isinstance(league_id, int):
            raise TypeError("Invalid datatype")

        if not isinstance(league_id, int):
            raise TypeError("Invalid datatype")

        if not isinstance(name, str):
            raise TypeError("Invalid datatype")

        self.__league_id = league_id
        self.__country_id = country_id
        self.__name = name
        self.__teams = list[Team]  # a list with Team objects

    def get_league_id(self) -> int:
        """Returns league ID"""
        return self.__league_id

    def get_country_id(self) -> int:
        """Returns country ID"""
        return self.__country_id

    def get_name(self) -> str:
        """Returns league name"""
        return self.__name

    def get_teams(self) -> Type[list[Team]]:
        return self.__teams

