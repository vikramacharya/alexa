from flask import Flask
from flask_ask import Ask, statement, question, session
from periodic_table_api import PeriodicTable

app = Flask(__name__)
ask = Ask(app, "/")


@ask.launch
def new_game():
	session.attributes['last_intent'] = 'Launch'
	return question(
		'You can get the name and atomic number of the element by its symbol. Tell me the the symbol.')


@ask.intent('PeriodicIntent', mapping={'name': 'name'})
def periodic_app(name):
	try:
		periodic_title_list = PeriodicTable().get_Element(name)
	except Exception as e:
		periodic_title_list = []
	
	if not periodic_title_list:
		return statement('Sorry. Could not find any details for %s' % name)
	
	element_data = periodic_title_list['names'][name]
	speech = ''
	if element_data == 'Invalid element!':
		speech += '{} is Invalid element!'.format(name)
	else:
		atomic_data = periodic_title_list['numbers'][name]['atomic']
		# print(atomic_data)
		speech += 'The element name for {} is {} and its atomic number is {}.'.format(name, element_data,
																					atomic_data)
	return statement(speech)


@ask.intent('AMAZON.HelpIntent')
def get_help():
	if session.attributes.get('last_intent') == 'Launch':
		return question('I can provide you with the element detail for the any given symbol. '
						'Just tell me the symbol and '
						'i will read the element details for you. '
						'So which symbol you want to know about ?')


@ask.intent('AMAZON.CancelIntent')
def cancel_request():
	return statement('Thank you for using the app. Have a good day')


@ask.intent('AMAZON.StopIntent')
def stop_app():
	return statement('Thank you for using the app. Have a good day')


if __name__ == '__main__':
	app.run(debug=True)