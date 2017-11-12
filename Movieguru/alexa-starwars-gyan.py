import requests
from flask import Flask
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")


def getCharacters(character_count):
	result = requests.get("http://swapi.co/api/people/").json()
	characters = result.get("results")
	return map(lambda x: x.get('name'), characters)[:character_count]

@ask.launch
def introduction():
	session.attributes['last_intent'] = 'Launch'
	return question('I will tell you about the major characters of star wars. How many characters do you want me to share?')

@ask.intent('ListCharacterIntent', mapping={'character_count': 'character_count'})
def list_charcaters(character_count):
	print(character_count)
	speech = 'Following are the {} major character of star wars. '.format(character_count)
	characters = getCharacters(character_count)
	speech += ','.join(characters)
	return statement(speech)


@ask.intent('AMAZON.HelpIntent')
def get_help():
    if session.attributes.get('last_intent') == 'Launch':
        return question('I can provide you with the list of characters in the movie Star Wars. How many characters should I say?')


@ask.intent('AMAZON.CancelIntent')
def cancel_request():
    return statement('Thank you for using the app. Have a good day')


@ask.intent('AMAZON.StopIntent')
def stop_app():
    return statement('Thank you for using the app. Have a good day')


if __name__ == '__main__':
    app.run(debug=True)
