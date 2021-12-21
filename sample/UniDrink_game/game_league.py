from sample.UniDrink_game.game_game import Game
from sample.UniDrink_game.game_team import Team
from sample.UniDrink_game.game_user import User


class League:
    def __init__(self):
        self.__teams = list[Team]
        self.__games = list[Game]
        self.__players = list[User]

    def get_teams(self) -> list[Team]:
        teams = self.__teams
        return teams

    def add_team(self, team: Team) -> bool:
        if not isinstance(team, Team):
            raise TypeError

        if team in self.get_teams():
            return False

        self.__teams.append(team)
        return True

    def remove_team(self, team: Team) -> bool:
        if not isinstance(team, Team):
            raise TypeError

        if team not in self.get_teams():
            return False

        self.__teams.remove(team)
        return True

    def get_games(self) -> list[Game]:
        games = self.__games
        return games

    def add_game(self, game: Game) -> bool:
        if not isinstance(game, Game):
            raise TypeError

        if game in self.get_games():
            return False

        self.__games.append(game)
        map(lambda player: self.__add_player(player), game.get_players())
        return True

    def remove_game(self, game: Game) -> bool:
        if not isinstance(game, Game):
            raise TypeError

        if game not in self.get_games():
            return False

        self.__games.remove(game)
        map(lambda player: self.__remove_player(player), game.get_players())  # Removes players that was in in the game
        return True

    def get_players(self) -> list[User]:
        players = self.__players
        return players

    def __add_player(self, player: User):
        if not isinstance(player, User):
            raise TypeError

        if player not in self.get_players():
            self.__players.append(player)

    def __remove_player(self, player: User):
        number_of_games = 0
        if not isinstance(player, User):
            raise TypeError

        for game in self.get_games():
            for p in game.get_players():
                if p == player:
                    number_of_games += 1

        if player in self.get_players() and number_of_games == 1:
            self.__players.remove(player)
