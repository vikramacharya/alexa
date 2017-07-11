from flask import Flask
from flask_ask import Ask, statement, question, session
from university_api import UniversityNews

app = Flask(__name__)
ask = Ask(app, "/")


@ask.launch
def new_game():
    session.attributes['last_intent'] = 'Launch'
    return question('You can get the university domain detail by name of university and country. Tell me the name of University and Country.')


@ask.intent('UniversityNewsIntent', mapping={'name': 'name', 'country': 'country'})
def university_app(name,country):
    try:
        university_title_list = UniversityNews().get_university(name, country)
    except Exception as e:
        university_title_list = []

    if not university_title_list:
        return statement('Sorry. Could not find any details for %s in %s' % name % country)
    speech = '{} records found'.format(len(university_title_list))
    
    for title in university_title_list:
        university_name = title.get('name')
        university_domain = title.get('web_page')
        speech += 'The domain for {} is {}.'.format(university_name,university_domain)
    return statement(speech)


@ask.intent('AMAZON.HelpIntent')
def get_help():
    if session.attributes.get('last_intent') == 'Launch':
        return question('I can provide you with the domain detail for the given university of provided country. '
                        'Just tell me the name of the university along with country and '
						'i will read the domain detail to you. '
						'So which University you want to know about ?')


@ask.intent('AMAZON.CancelIntent')
def cancel_request():
    return statement('Thank you for using the app. Have a good day')


@ask.intent('AMAZON.StopIntent')
def stop_app():
    return statement('Thank you for using the app. Have a good day')


if __name__ == '__main__':
    app.run(debug=True)