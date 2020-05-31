from loteria import megasena, multiple_luckynumbers
from flask_restful import Resource


class Megasena(Resource):

    def get(self, quantity=None):
        if quantity:
            return {'Jogos': multiple_luckynumbers(quantity)}
        game = megasena()
        return [
            {'jogo': game},
            {   
                'posicao_um': game[0],
                'posicao_dois': game[1],
                'posicao_tres': game[2],
                'posicao_quatro': game[3],
                'posicao_quinto': game[4],
                'posicao_seis': game[5]
            }
        ]
