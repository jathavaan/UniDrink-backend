import datetime
import re


class User:
    def __init__(self, first_name: str, surname: str, date_of_birth: datetime.datetime, username: str, password: str):
        """Creates a new instance of User"""
        if not isinstance(first_name, str):
            raise TypeError

        if not isinstance(surname, str):
            raise TypeError

        if not isinstance(date_of_birth, datetime.datetime):
            raise TypeError

        if not isinstance(username, str):
            raise TypeError

        if not isinstance(password, str):
            raise TypeError

        self.set_first_name(first_name)
        self.set_surname(surname)
        self.set_date_of_birth(date_of_birth)
        self.set_username(username)
        self.set_password(password)

    # Getters and setters

    def get_first_name(self) -> str:
        return self.__first_name

    def set_first_name(self, first_name: str):
        if not isinstance(first_name, str):
            raise TypeError

        if not self.__valid_string(first_name):
            raise ValueError("First name cannot be empty")

        if not self.__name_validation(first_name):
            raise ValueError("Invalid first name. It can only contain letters, spaces, hyphens and apostrophes")

        self.__first_name = first_name

    def get_surname(self) -> str:
        return self.__surname

    def set_surname(self, surname: str):
        if not isinstance(surname, str):
            raise TypeError

        if not self.__valid_string(surname):
            raise ValueError("Surname cannot be empty")

        if not self.__name_validation(surname):
            raise ValueError("Invalid surname. It can only contain letters, spaces, hyphens and apostrophes")

        self.__surname = surname

    def get_date_of_birth(self) -> datetime:
        return self.__date_of_birth

    def set_date_of_birth(self, date_of_birth: datetime.datetime):
        if not isinstance(date_of_birth, datetime.datetime):
            raise TypeError

        self.__date_of_birth_validation(date_of_birth)

        self.__date_of_birth = date_of_birth

    def get_username(self):
        return self.__username

    def set_username(self, username: str):
        if not isinstance(username, str):
            raise TypeError

        if not self.__valid_string(username):
            raise ValueError('Username cannot be empty')

        self.__username_validation(username)
        self.__username = username

    def get_password(self) -> str:
        return self.__password

    def set_password(self, password: str):
        if not isinstance(password, str):
            raise TypeError

        if not self.__valid_string(password):
            raise ValueError("Password cannot be empty")

        self.__password_validation(password)
        self.__password = password

    # Validation methods

    def __valid_string(self, string: str) -> bool:
        """Checks if string is empty or None"""
        if not isinstance(string, str):
            raise TypeError

        return string and string is not None

    def __name_validation(self, name: str) -> bool:
        """Checks if name contains valid characters"""
        if not isinstance(name, str):
            raise TypeError

        pattern = re.compile("^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$")
        return pattern.match(name)

    def __date_of_birth_validation(self, date_of_birth: datetime.datetime):
        if not isinstance(date_of_birth, datetime.datetime):
            raise TypeError

        if date_of_birth is None:
            raise ValueError("Date of birth cannot be empty")

        if not self.__age_check(date_of_birth):
            raise ValueError("You are not old enough. You need to be at least 18 years of age to create an account")

    def __age_check(self, date_of_birth: datetime.datetime) -> bool:
        """Checks if user is at least 18 years of age"""
        if not isinstance(date_of_birth, datetime.datetime):
            raise TypeError

        current_date = datetime.datetime.today()
        current_year = current_date.year
        current_month = current_date.month
        current_day = current_date.day
        min_age = datetime.datetime(current_year - 18, current_month, current_day)

        return not date_of_birth > min_age

    def __username_validation(self, username: str):
        if not isinstance(username, str):
            raise TypeError

        pattern = re.compile("^[a-zA-Z0-9._-]{3,}$")
        if not pattern.match(username):
            raise ValueError(
                "Invalid username. Username has to meet the following requirements:" +
                "\n\t=> At least 3 characters long" +
                "\n\t=> Can contain upper- and lowercase letters from the English alphabet" +
                "\n\t=> Can contain the numbers from 0 to 9" +
                "\n\t=> Can contain dashes and underscores"
            )

    def __password_validation(self, password: str):
        if not isinstance(password, str):
            raise TypeError

        pattern = re.compile("^(?=.*\\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%]).{8,20}$")
        if not pattern.match(password):
            raise ValueError(
                "Password is not strong enough. Please ensure that the following requirements are fulfilled:" +
                "\n\t=> Between 8 and 20 character" +
                "\n\t=> At least one numeric character" +
                "\n\t=> At least one lowercase character" +
                "\n\t=> At least one lowercase character" +
                "\n\t=> At least one of the following symbols: \"@, #, $, %\""
            )

    def to_string(self) -> str:
        """To string method that gives the user object a string representation"""
        return f"Name: {self.get_first_name()} {self.get_surname()}\n" \
               f"Date of birth [yyyy-MM-dd hh:mm:ss]: {self.get_date_of_birth()}\n" \
               f"Username: {self.get_username()}\n" \
               f"Password: {self.get_password()}"
