from datetime import datetime
from flask import Flask, request, abort
import time


app = Flask(__name__)

database = [
    {'name': 'Jone',
     'text': 'Привет всем!',
     'time': time.time()
    },
    {'name': 'Mary',
     'text': 'Привет, Jone',
     'time': time.time()
     }
]

@app.route("/")
def hello():
    return f"Hello, Skillbox! <a href='/status'>Статус кво</a>"

@app.route('/status')
def status():
    return {
        'status': True,
        'name': 'Ihor',
        'time': time.time(),
        'time2': time.asctime(),
        'time3': datetime.now(),
        'time4': datetime.now().isoformat(),
        'time5': datetime.now().strftime("%H:%M-%S")
    }

@app.route("/send", methods=['POST'])
def send_message():
    data = request.json

    if not isinstance(data, dict):
        return abort(400)
    if 'name' not in data or 'text' not in data:
        return abort(400)

    name = data['name']
    text = data['text']

    if not isinstance(name, str) or not isinstance(text, str):
        return abort(400)
    if not (0 < len(name) <= 128):
        return abort(400)
    if not (0 < len(text) < 1000):
        return abort(400)

    message = {
        'name': name,
        'text': text,
        'time': time.time()
    }

    database.append(message)

    return {'ok': True}


@app.route("/messages")
def get_messages():

    try:
        after = float(request.args['after'])
    except:
        return abort(400)


    messages = []
    for message in database:
        if message['time'] > after:
            messages.append(message)

    return {'messages': messages[:50]}

app.run()
