import json

import ViNLP
from flask import Flask, request
from flask.templating import render_template
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/ws',  methods=['POST'])
def _ws():
    sent = request.form['sent']
    items = ViNLP.word_tokenize(sent)
    curr_len = 0
    entities = []
    text = ' '.join(items)
    for i, item in enumerate(items):
        entities.append([i, '', [[curr_len, curr_len + len(item)]]])
        curr_len += len(item) + 1
    resp = {
        'text': text,
        'entities': entities
    }
    return json.dumps(resp, ensure_ascii=False)

@app.route('/api/pos', methods=['POST'])
def _pos():
    sent = request.form['sent']
    items = ViNLP.pos_tag(sent)
    curr_len = 0
    entities = []
    text = ' '.join([item[0] for item in items])
    for i, item in enumerate(items):
        if item[-1] != 'X':
            entities.append([i, item[-1], [[curr_len, curr_len + len(item[0])]]])
        curr_len += len(item[0]) + 1
    resp = {
        'text': text,
        'entities': entities
    }
    return json.dumps(resp, ensure_ascii=False)

@app.route('/api/chunk', methods=['POST'])
def _chunk():
    sent = request.form['sent']
    items = ViNLP.chunk(sent)
    curr_len = 0
    entities = []
    text = ' '.join([item[0] for item in items])
    for i, item in enumerate(items):
        if item[-1] != 'O':
            entities.append([i, item[-1], [[curr_len, curr_len + len(item[0])]]])
        curr_len += len(item[0]) + 1
    resp = {
        'text': text,
        'entities': entities
    }
    return json.dumps(resp, ensure_ascii=False)

@app.route('/api/ner', methods=['POST'])
def _ner():
    sent = request.form['sent']
    items = ViNLP.ner(sent)
    curr_len = 0
    entities = []
    text = ' '.join([item[0] for item in items])
    for i, item in enumerate(items):
        if item[-1] != 'O':
            entities.append([i, item[-1], [[curr_len, curr_len + len(item[0])]]])
        curr_len += len(item[0]) + 1
    resp = {
        'text': text,
        'entities': entities
    }
    return json.dumps(resp, ensure_ascii=False)

app.run()
