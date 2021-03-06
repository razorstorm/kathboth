# coding=utf-8
import json
import random

import markovify
import numpy as np

import requests
from flask import request, Flask

app = Flask(__name__)

token = 'EAAXSUovhrQkBAJfw0cqLd1bZCpZBn9564eLqucEuJPPyZC1Gqy0AQvx6F0twfcnjtG4ZC5Ui9CFLj33cVJeS6ih86gVFYFtuzWzyGBf7SSvSO7oQHef86YMbZASBmDsPROqOktQciCs0UNfCmIFDkiseWmLM5PzHZAUhU95zx2dQZDZD'  # noqa
ARI_TEXT_AVERAGE_LENGTH = 22

text = None


@app.route('/receive', methods=['GET'])
def serve():
    if (
        request.args.get('hub.mode') == 'subscribe' and
        request.args.get('hub.verify_token') == 'kath'
    ):
        return request.args.get('hub.challenge')
    return 'kath'


def generate_kath_speech():
    # Get raw text as string.
    global text
    if not text:
        with open("kath_parsed_text.txt") as f:
            text = f.read()

    text_models = []
    for i in range(6):
        # Build the models
        text_models.append(markovify.Text(text, state_size=i))

    # Use a random distribution to figure out how many sentences to generate
    num_sentences = max(1, int(round(np.random.normal(1, 0.5, 1)[0], 0)))

    sentences = []
    for i in range(num_sentences):
        # Make a random choice on which model to use
        chosen_text_model = text_models[random.randint(0, 5)]
        # Generate sentences certain length
        sentences.append(chosen_text_model.make_short_sentence(max_chars=ARI_TEXT_AVERAGE_LENGTH*7, min_chars=ARI_TEXT_AVERAGE_LENGTH/3, tries=1000))

    sentences = " ".join(sentences)

    return sentences


@app.route('/receive', methods=['POST'])
def receive():
    print(request.data)
    data = json.loads(request.data)

    sentences = generate_kath_speech()

    try:
        for entry in data['entry']:
            for message in entry['messaging']:
                sender = message['sender']['id']

                resp_msg = {
                    'recipient': {
                        'id': sender,
                    },
                    'message': {
                        'text': sentences,
                    },
                }

                response = requests.post(
                    'https://graph.facebook.com/v2.6/me/messages',
                    params={'access_token': token},
                    json=resp_msg,
                )
                print('Sent requests %s' % json.dumps(resp_msg))
                print('Received response %s' % response.text)
    except Exception as e:
        print(e)
        return 'not handled'

    return 'success'
