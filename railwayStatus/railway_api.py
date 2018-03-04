import xml.etree.ElementTree as ET
import requests
import json
from pprint import pprint

class RailwayNews(object):

    def __init__(self):
        pass

    @staticmethod
    def get_pnr_details(pnr):
        url = 'https://api.railwayapi.com/v2/pnr-status/pnr/{}/apikey/{}'.format(pnr, 'uf0ni07b37')
        response = requests.get(url)
        return response.json()
        #result = {u'doj': u'03-02-2017', u'to_station': {u'lat': None, u'lng': None, u'code': u'DBG', u'name': u'DARBHANGA JN'}, u'total_passengers': 2, u'chart_prepared': False, u'passengers': [{u'booking_status': u'CNF/S11/34/GN', u'current_status': u'CNF/-/0/GN', u'no': 1}, {u'booking_status': u'CNF/S11/37/GN', u'current_status': u'CNF/-/0/GN', u'no': 2}], u'response_code': 200, u'pnr': u'8420803198', u'reservation_upto': {u'lat': None, u'lng': None, u'code': u'DBG', u'name': u'DARBHANGA JN'}, u'train': {u'classes': [], u'number': u'11061', u'name': u'DARBHANGA EXP', u'days': []}, u'from_station': {u'lat': None, u'lng': None, u'code': u'LTT', u'name': u'LOKMANYATILAK'}, u'debit': 3, u'journey_class': {u'code': u'SL', u'name': None}, u'boarding_point': {u'lat': None, u'lng': None, u'code': u'LTT', u'name': u'LOKMANYATILAK'}}
        #result = {u'doj': u'14-02-2017', u'to_station': {u'lat': None, u'lng': None, u'code': u'LTT', u'name': u'LOKMANYATILAK'}, u'total_passengers': 2, u'chart_prepared': False, u'passengers': [{u'booking_status': u'CNF/S3/33/SS', u'current_status': u'CAN/-/0/SS', u'no': 1}, {u'booking_status': u'CNF/S3/36/SS', u'current_status': u'CAN/-/0/SS', u'no': 2}], u'response_code': 200, u'pnr': u'6309015112', u'reservation_upto': {u'lat': None, u'lng': None, u'code': u'LTT', u'name': u'LOKMANYATILAK'}, u'train': {u'classes': [], u'number': u'11062', u'name': u'DBG LTT EXPRESS', u'days': []}, u'from_station': {u'lat': None, u'lng': None, u'code': u'DBG', u'name': u'DARBHANGA JN'}, u'debit': 3, u'journey_class': {u'code': u'SL', u'name': None}, u'boarding_point': {u'lat': None, u'lng': None, u'code': u'DBG', u'name': u'DARBHANGA JN'}}
        #return result
    
# railway = RailwayNews()
# speech = ''
# ApiResult = railway.get_pnr_details(6309015112)
# #print(ApiResult)
# speech_output = "Welcome to the Alexa Indian Railway PNR Status skill. "
# doj = ApiResult['doj']
# pnr = ApiResult['pnr']
# reservation_upto = ApiResult['reservation_upto']['name']
# to_station = ApiResult['to_station']['name']
# train_number = ApiResult['train']['number']
# train_name = ApiResult['train']['name']
#
# speech += "Reservation status for "
# current_status_speech = "Current status for "
# total_passengers = ApiResult['total_passengers']
# chart_prepared = ApiResult['chart_prepared']
# response_code = ApiResult['response_code']
# boarding_point = ApiResult['boarding_point']['name']
# journey_class = ApiResult['journey_class']['code']
# passengers = ApiResult['passengers']
# for x in passengers:
# 	booking_status = x['booking_status']
# 	current_status = x['current_status']
# 	passanger_number = x['no']
# 	current_status_value = current_status.split('/')
# 	current_status_data = current_status_value[0]
# 	if current_status_data == 'CAN':
# 		latest_status = 'Cancelled'
# 	elif current_status_data == 'CNF':
# 		latest_status = 'Confirmed'
# 	else:
# 		latest_status = 'Chart Not Prepared'
# 	speech += "passenger {} is {} with current status {}".format(passanger_number, booking_status, latest_status)
# 	if passanger_number!= total_passengers:
# 		speech += ' and '
# 	else:
# 		speech += '.'
#
# speech_output += "PNR "+pnr+" is for train "+train_number+" "+train_name+". "
# if chart_prepared:
# 	speech_output += "Chart for PNR {} is prepared.".format(pnr)
# else:
# 	speech_output += "Chart for PNR {} is not prepared yet.".format(pnr)
# speech_output += " Your Boarding point is "+boarding_point+ " on "+ doj+" and destination is "+reservation_upto+"."
# speech_output += " You have booked ticker for " +str(total_passengers)+ " people. "
# speech_output += speech
#
# print(speech_output)

	




