from flask import Flask
from flask_ask import Ask, statement, question, session
from railway_api import RailwayNews

app = Flask(__name__)
ask = Ask(app, "/")


@ask.launch
def new_game():
    session.attributes['last_intent'] = 'Launch'
    return question('I can provide you with the latest status for any railway PNR you ask me about. '
                        'Just tell me the PNR of the railway and i will read the status to you. '
                        'So which pnr do you want to know about ?')

@ask.intent('RailwayNewsIntent', mapping={'pnr': 'pnr'})
def railway_news_app(pnr):
    try:
        ApiResult = RailwayNews().get_pnr_details(pnr)
    except Exception as e:
        ApiResult = []

    if not ApiResult:
        return statement('Sorry. Could not find any update for %s' % pnr)
    speech = ''
    
    #ApiResult = railway.get_pnr_details(6309015112)
    # print(ApiResult)
    speech_output = "Welcome to the Alexa Indian Railway PNR Status skill. "
    doj = ApiResult['doj']
    pnr = ApiResult['pnr']
    reservation_upto = ApiResult['reservation_upto']['name']
    to_station = ApiResult['to_station']['name']
    train_number = ApiResult['train']['number']
    train_name = ApiResult['train']['name']

    speech += "Reservation status for "
    total_passengers = ApiResult['total_passengers']
    chart_prepared = ApiResult['chart_prepared']
    response_code = ApiResult['response_code']
    boarding_point = ApiResult['boarding_point']['name']
    journey_class = ApiResult['journey_class']['code']
    passengers = ApiResult['passengers']
    for x in passengers:
        booking_status = x['booking_status']
        current_status = x['current_status']
        passenger_number = x['no']
        current_status_value = current_status.split('/')
        current_status_data = current_status_value[0]
        if current_status_data == 'CAN':
            latest_status = 'Cancelled'
        elif current_status_data == 'CNF':
            latest_status = 'Confirmed'
        else:
            latest_status = 'Chart Not Prepared'
        speech += "passenger {} is {} with current status {}".format(passenger_number, booking_status, latest_status)
        if passenger_number != total_passengers:
            speech += ' and '
        else:
            speech += '.'

    speech_output += "PNR " + pnr + " is for train " + train_number + " " + train_name + ". "
    if chart_prepared:
        speech_output += "Chart for PNR {} is prepared.".format(pnr)
    else:
        speech_output += "Chart for PNR {} is not prepared yet.".format(pnr)
    speech_output += " Your Boarding point is " + boarding_point + " on " + doj + " and destination is " + reservation_upto + "."
    speech_output += " You have booked ticker for " + str(total_passengers) + " people. "
    speech_output += speech

    return statement(speech_output)

speech_output = "Welcome to the Alexa Indian Railway PNR Status Skill. " \
					"You can ask me for your PNR status for any Indian Railway, " \
					"and I will provide you with the details on the same."

@ask.intent('AMAZON.HelpIntent')
def get_help():
    if session.attributes.get('last_intent') == 'Launch':
        return question('I can provide you with the latest status for any railway PNR you ask me about. '
                        'Just tell me the PNR of the railway and i will read the status to you. '
                        'So which pnr do you want to know about ?')


@ask.intent('AMAZON.CancelIntent')
def cancel_request():
    return statement('Thank you for using the Alexa Indian Railway PNR Status Skill. See you next time!')


@ask.intent('AMAZON.StopIntent')
def stop_app():
    return statement('Thank you for using the Alexa Indian Railway PNR Status Skill. See you next time!')


if __name__ == '__main__':
    app.run(debug=True)