import requests

from flask import Flask
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")


def get_news():
    result = requests.get(
        "https://newsapi.org/v1/articles?source=the-hindu&sortBy=latest&apiKey=98a2baf72f5b4565960077ac7ced4f80").json()
    articles = result.get("articles")
    # articles = news_list.get("articles")
    return map(lambda x: (x.get('title'), x.get('author')), articles)[:10]


@ask.launch
def introduction():
    session.attributes['last_intent'] = 'Launch'
    return question('I will tell you about the major news of India.')


@ask.intent('ListCharacterIntent')
def list_news():
    speech = 'Following are the major news of India. '
    news = get_news()
    output_data = ''
    for item in news:
        title, author = item
        content = title + " by " + author + ". "
        output_data += content
    return statement(output_data)


@ask.intent('AMAZON.HelpIntent')
def get_help():
    if session.attributes.get('last_intent') == 'Launch':
        return question('I can provide you with the latest news of India ')


@ask.intent('AMAZON.CancelIntent')
def cancel_request():
    return statement('Thank you for using the app. Have a good day')


@ask.intent('AMAZON.StopIntent')
def stop_app():
    return statement('Thank you for using the app. Have a good day')


if __name__ == '__main__':
    app.run(debug=True)

    
