from atproto import Client, client_utils

import json
import datetime

def main():
    target = datetime.datetime(2027, 10, 21, 10)
    
    with open('credentials.json', 'r') as f:
        credentials = json.loads(f.read())

    client = Client()
    profile = client.login(credentials['username'], credentials['password'])

    today = datetime.datetime.now()
    print(f'{today}')
    diff = target - today

    text = client_utils.TextBuilder().text(f'It is {diff.days} days until ').link('Spiel ' + datetime.strftime(target, '%Y'), 'https://www.spiel-essen.de/').text(' (' + datetime.strftime(target, '%d %B %Y') +')!')
    post = client.send_post(text)

if __name__ == '__main__':
    main()

