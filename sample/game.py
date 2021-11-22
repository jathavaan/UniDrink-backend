from sample.user import User


class Game:
    def __init__(self, players: list[User]):
        self.__players = players

    def add_player(self, player: User) -> bool:
        if not isinstance(player, User):
            raise TypeError

        if player in self.get_players():
            return False

        self.__players.append(player)
        return True

    def get_players(self) -> list[User]:
        player_list = self.__players
        return player_list

    def remove_player(self, player: User) -> bool:
        if not isinstance(player, User):
            raise TypeError

        if player not in self.get_players():
            return False

        self.__players.remove(player)
        return True
