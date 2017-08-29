import xml.etree.ElementTree as ET
import requests


class StarWarsCharacter(object):

    def __init__(self):
        pass

    @staticmethod
    def get_character_details(character_name):
        url = 'https://swapi.co/api/people/?search={}'.format(character_name)
        response = requests.get(url)
        return response.json()