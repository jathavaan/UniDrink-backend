class Country:
    def __init__(self, country_id: int, name: str, country_code: str, continent: str):
        self.__country_id = country_id
        self.__name = name
        self.__country_code = country_code
        self.__continent = continent

    def get_country_id(self) -> int:
        return self.__country_id

    def get_name(self) -> str:
        return self.__name

    def get_country_code(self) -> str:
        return self.__country_code

    def get_continent(self) -> str:
        return self.__continent
