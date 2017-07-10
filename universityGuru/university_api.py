import xml.etree.ElementTree as ET
import requests


class UniversityNews(object):

    def __init__(self):
        pass

    @staticmethod
    def get_university(university_name, country):
        url = 'http://universities.hipolabs.com/search?name={}&country={}'.format(university_name, country)
        response = requests.get(url)
        return response.json()
