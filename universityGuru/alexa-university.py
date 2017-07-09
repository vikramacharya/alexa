from flask import Flask
from flask_ask import Ask, statement, question, session
from university_api import UniversityNews

app = Flask(__name__)
ask = Ask(app, "/")


@ask.launch
def new_game():
    session.attributes['last_intent'] = 'Launch'
    return question('You can get the university detail by name of country. Which PNR will it be ?')


@ask.intent('UniversityNewsIntent', mapping={'name': 'name', 'country': 'country'})
def university_app(name,country):
    try:
        university_title_list = UniversityNews().main(name, country)
    except Exception as e:
        university_title_list = []

    if not university_title_list:
        return statement('Sorry. Could not find any update for %s in %s' % name % country)
    speech = ''
    for title in university_title_list:
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