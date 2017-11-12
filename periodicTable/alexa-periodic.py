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


@ask.intent('PeriodicIntent', mapping={'symbol_name': 'symbol_name'})
def periodic_app(symbol_name):
	
	try:
		print('symbol provided : {} '.format(symbol_name))
		if not symbol_name:
			return question("You haven't provided any symbol yet. Please provide a symbol name.")
		symbol_name = symbol_name.title()
		print('symbol provided : {} '.format(symbol_name))
		periodic_title_list = PeriodicTable().get_element(symbol_name)
		print(periodic_title_list)
	except Exception as e:
		periodic_title_list = []
	
	if not periodic_title_list:
		return statement('Sorry. Could not find any details for %s' % symbol_name)
	
	element_data = periodic_title_list['names']
	symbol = element_data.get(symbol_name)
	
	speech = ''
	if symbol == 'Invalid element!':
		speech += 'Sorry! No such element found'
	else:
		atomic_data = periodic_title_list['numbers']
		atomic_data_value = atomic_data.get(symbol_name,{})
		if atomic_data_value:
			atomic_number = atomic_data_value.get('atomic')
			print(atomic_number)
			speech += 'The element name for {} is {} and its atomic number is {}.'.format(symbol_name, symbol, atomic_number)
		else:
			speech += 'Sorry! No such element found'
			
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