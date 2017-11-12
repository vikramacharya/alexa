import xml.etree.ElementTree as ET
import requests


class PeriodicTable(object):

    def __init__(self):
        pass

    @staticmethod
    def get_element(symbol_name):
		url = 'http://54.172.80.183/api/pt.php?mode=names,numbers&elements={}'.format(symbol_name)
		response = requests.get(url)
		return response.json()