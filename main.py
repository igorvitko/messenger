import datetime
import time


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

def send_message(name, text):
    message = {
        'name': name,
        'text': text,
        'time': time.time()
    }

    database.append(message)


send_message('admin', 'Щас заблочу!')
send_message('Jone', 'Нет, не надо!')


def print_messages(messages):
    for message in messages:
        dt = datetime.datetime.fromtimestamp(message['time'])
        print(dt, message['name'])
        print(message['text'])
        print()


def get_messages(after):
    messages = []
    for message in database:
        if message['time'] > after:
            messages.append(message)

    return messages

print_messages(get_messages(0))
