from flask import Flask
from flask_restful import Api
from resources.megasena import Megasena

app = Flask(__name__)

api = Api(app)

api.add_resource(Megasena, '/megasena', '/megasena/jogos/<int:quantity>')


if __name__ == '__main__':
    app.run(debug=True)
