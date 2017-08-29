from flask import Flask
from flask_ask import Ask, statement, question, session
from star_wars_api import StarWarsCharacter

app = Flask(__name__)
ask = Ask(app, "/")


@ask.launch
def new_game():
	session.attributes['last_intent'] = 'Launch'
	return question(
		'You can get the star wars character detail by their name. Tell me the name of character.')


@ask.intent('ListCharacterIntent', mapping={'character_name': 'character_name'})
def starwars_app(character_name):
	print
	character_name
	try:
		starwars_characters = StarWarsCharacter().get_character_details(character_name)
		starwars_character_list = starwars_characters.get('results')
	except Exception as e:
		starwars_character_list = []
	
	if not starwars_character_list:
		return statement('Sorry. Could not find any details for %s' % (character_name))
		
	speech = '{} records found. '.format(len(starwars_character_list))
	
	for title in starwars_character_list:
		character_name = title.get('name')
		character_height = title.get('height')
		character_mass = title.get('mass')
		character_skin_color = title.get('skin_color')
		character_birth_year = title.get('birth_year')
		character_gender = title.get('gender')
		if character_gender == 'male':
			prefix = 'He'
		else:
			prefix = "She"
			
		speech += '{} is {} with height {} and mass {}. '.format(character_name, character_gender, character_height, character_mass)
		speech += '{} has {} skin color. '.format(prefix, character_skin_color)
		speech += '{} birth year is {}'.format(character_name, character_birth_year)
	return statement(speech)


@ask.intent('AMAZON.HelpIntent')
def get_help():
	if session.attributes.get('last_intent') == 'Launch':
		return question('I can provide you with the character details of the star wars. '
						'Just tell me the name of the character and '
						'i will give detail to you. '
						'So which character you want to know about ?')


@ask.intent('AMAZON.CancelIntent')
def cancel_request():
	return statement('Thank you for using the app. Have a good day')


@ask.intent('AMAZON.StopIntent')
def stop_app():
	return statement('Thank you for using the app. Have a good day')


if __name__ == '__main__':
	app.run(debug=True)


#starwars_app('Darth Vaderw   ')