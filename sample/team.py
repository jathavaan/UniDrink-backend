from api import API


class Team:
    def __init__(self, id: int):
        if not isinstance(id, int):
            raise TypeError

        if id < 1 or id > 20:
            raise ValueError("Team ID cannot be less than 1 and greater than 20.")

        api = API()  # Creates an instance of API
        teams = api.get_FPL_gi_teams()  # List of teams and additional information

        name = None
        short_name = None
        position = None
        played = None
        win = None
        points = None

        for teamDict in teams:
            if id == teamDict['id']:
                name = teamDict['name']
                short_name = teamDict['short_name']
                position = teamDict['position']
                played = teamDict['played']
                win = teamDict['win']
                points = teamDict['points']
                break

        self.__name = name
        self.__short_name = short_name
        self.__position = position
        self.__played = played
        self.__win = win
        self.__points = points

    def get_name(self) -> str:
        return self.__name

    def get_short_name(self) -> str:
        return self.__short_name

    def get_position(self) -> int:
        return self.__position

    def get_played(self) -> int:
        return self.__played

    def get_win(self) -> int:
        return self.__win

    def get_points(self) -> int:
        return self.__points

    def to_string(self) -> str:
        return f"{self.get_name()} [{self.get_short_name()}] has played {self.get_played()} game(s) this season and " \
               f"have a total of {self.get_points()} points from {self.get_win()} win(s). {self.get_short_name()} are " \
               f"currently holding pos. {self.get_position()} in the league!"


team = Team(1)
print(team.to_string())
