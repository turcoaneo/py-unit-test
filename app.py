import json

import spacy
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin

from ner_client import NamedEntityClient

app = Flask(__name__)

model = spacy.load("en_core_web_sm")
ner = NamedEntityClient(model)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ner', methods=['POST'])
@cross_origin(CORS(app))
def get_named_ents():
    data = request.get_json()
    result = ner.get_entities(data['sentence'])
    response = {"entities": result.get("ents"), "html": result.get("html")}
    dumps = json.dumps(response)
    return dumps


if __name__ == '__main__':
    app.run(debug=True)
