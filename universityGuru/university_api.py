import xml.etree.ElementTree as ET
import requests


class UniversityNews(object):

    def __init__(self):
        pass

    @staticmethod
    def get_url(university_name, country):
        return 'http://universities.hipolabs.com/search?name=%s%s&university,country'
        #return 'https://news.google.com/news/section?geo=%s&output=rss' \
              # % ('+'.join(pnr.split()))

    @staticmethod
    def get_rss_xml(url):
        return requests.get(url).text

    @staticmethod
    def get_news_title(rss_xml):
        root = ET.fromstring(rss_xml)
        return [item.find('title').text for item in root.iter('item')][:5]

    def main(self, university_name, country):
        url = self.get_url(university_name, country)
        #rss_xml = self.get_rss_xml(url).encode('utf-8')
        #return self.get_news_title(rss_xml)
        return url