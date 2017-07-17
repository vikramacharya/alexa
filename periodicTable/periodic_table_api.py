import xml.etree.ElementTree as ET
import requests
import json

class PeriodicTable(object):

    def __init__(self):
        pass

    @staticmethod
    def get_Element(name):
		url = 'http://54.172.80.183/api/pt.php?mode=names,numbers&elements={}'.format(name)
		response = requests.get(url)
		return response.json()