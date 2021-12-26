class Team:
    def __init__(self, team_id: int, name: str, short_code: str, common_name: str, logo: str, country_id: int):
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

        if not isinstance(country_id, int):
            raise TypeError("Invalid datatype")

        self.__team_id = team_id
        self.__name = name
        self.__short_code = short_code
        self.__common_name = common_name
        self.__logo = logo
        self.__country_id = country_id

    def get_league_id(self) -> int:
        """Returns team ID"""
        return self.__team_id

    def get_name(self) -> str:
        """Returns name"""
        return self.__name

    def get_short_code(self) -> str:
        """Returns short code"""
        return self.__short_code

    def get_logo(self) -> str:
        """Returns url for logo"""
        return self.__logo

    def get_country_id(self) -> int:
        """Returns country ID"""
        return self.__country_id
