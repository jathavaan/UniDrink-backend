import requests


class API:
    def __init__(self):
        self.__general_information_url = "https://fantasy.premierleague.com/api/bootstrap-static/"
        self.__general_information_response = requests.get(self.get_general_information_url())
        self.__general_information_json = self.get_general_information_response().json()

        self.__live_data_url = f"https://fantasy.premierleague.com/api/event/{self.__get_current_gameweek()}/live/"
        self.__live_data_response = requests.get(self.get_live_data_url())
        self.__live_data_json = self.get_live_data_response().json()

    def get_general_information_url(self) -> str:
        return self.__general_information_url

    def get_live_data_url(self) -> str:
        return self.__live_data_url

    def __set_live_data_url(self):
        gameweek = self.__get_current_gameweek()
        self.__live_data_url = f""

    def get_general_information_response(self) -> requests:
        return self.__general_information_response

    def get_live_data_response(self) -> requests:
        return self.__live_data_response

    def get_general_information_status_code(self) -> int:
        return self.get_general_information_response().status_code

    def get_live_data_status_code(self) -> int:
        return self.get_live_data_response().status_code

    def get_general_information_json(self) -> requests:
        return self.get_general_information_response().json()

    def get_live_data_json(self) -> requests:
        return self.get_live_data_response().json()

    def get_general_information_elements(self) -> dict:
        return self.get_general_information_json()["elements"]

    def get_general_information_events(self) -> dict:
        return self.get_general_information_json()["events"]

    def get_live_data_elements(self) -> list[dict]:
        return self.get_live_data_json()["elements"]

    def __get_current_gameweek(self) -> int:
        for dictionary in self.get_general_information_events():
            if dictionary["is_current"]:
                return dictionary["id"]
