from flask import Flask
from flask_ask import Ask, statement, question, session
from railway_api import RailwayNews

app = Flask(__name__)
ask = Ask(app, "/")


@ask.launch
def new_game():
    session.attributes['last_intent'] = 'Launch'
    return question('You can get the latest status of the railway by PNR. Which PNR will it be ?')


@ask.intent('RailwayNewsIntent', mapping={'pnr': 'pnr'})
def railway_news_app(pnr):
    try:
        railway_news_title_list = RailwayNews().main(pnr)
    except Exception as e:
        railway_news_title_list = []

    if not railway_news_title_list:
        return statement('Sorry. Could not find any update for %s' % pnr)
    speech = ''
    for title in railway_news_title_list:
        title, source = title.rsplit('-', 1)
        speech += 'According to %s %s.' % (source, title)
    return statement(speech)


@ask.intent('AMAZON.HelpIntent')
def get_help():
    if session.attributes.get('last_intent') == 'Launch':
        return question('I can provide you with the latest status for any railway PNR you ask me about. '
                        'Just tell me the PNR of the railway and i will read the status to you. '
                        'So which pnr do you want to know about ?')


@ask.intent('AMAZON.CancelIntent')
def cancel_request():
    return statement('Thank you for using the app. Have a good day')


@ask.intent('AMAZON.StopIntent')
def stop_app():
    return statement('Thank you for using the app. Have a good day')


if __name__ == '__main__':
    app.run(debug=True)