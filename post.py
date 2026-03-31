from atproto import Client, client_utils

import json
import datetime

def main():
    with open('credentials.json', 'r') as f:
        credentials = json.loads(f.read())

    client = Client()
    profile = client.login(credentials['username'], credentials['password'])

    target = datetime.datetime(2026, 10, 22, 10)
    today = datetime.datetime.now()
    diff = target - today

    text = client_utils.TextBuilder().text(f'It is {diff.days} days until ').link('Spiel 2026', 'https://www.spiel-essen.de/').text(' (starts 22 Oct 2026)!')
    post = client.send_post(text)

if __name__ == '__main__':
    main()

