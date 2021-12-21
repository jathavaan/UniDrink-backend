from flask import Flask
from api import API

from sample.UniDrink_game.game_user import User

app = Flask(__name__)


@app.route('/')
def home():
    api = API()
    return str(api.get_leagues())


if __name__ == '__main__':
    app.run()
