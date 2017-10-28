#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request

from AlgebraicParser import AlgebraicParser

from random import randint

from BingImagesAPI import BingImageSearch
import json

app = Flask(__name__)

AP = AlgebraicParser()

# Set of phrases for Learny to say
yesResults = ["Yes!", "You're right!", "That's Correct!", "Emoji_100"]
noResults = ["No.", "Not quite.", "Nope.", "Emoji_Poop"]

# Main Parsing Function
def Parse(input):

    # (1) Empty input
    if input == '' or input.isspace():
        return "You didn't ask me anything!"


    # (2) TODO: Write logic for parsing English statements
    if '=' not in input:
        return "IDK"


    # (3) Mathematical Evaluations
    equations = input.split('=')
    evaluations = []

    for e in equations:
        if e == '' or e.isspace():
            continue

        try:
            evaluations.append(AP.eval(e))
        except:
            return "That doesn't make sense!"

    if len(evaluations) < 2:
        return "That doesn't make sense!"

    left = 0
    right = 0

    for i in range(len(evaluations) - 1):
        left = evaluations[i]
        right = evaluations[i+1]

        if(left != right):
            return 'No'

    return 'Yes'



# 404 Handler
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# POST statement
@app.route('/learny/api/v1.0/eval', methods=['POST'])
def eval():
    if not request.json or not 'statement' in request.json:
        abort(400)

    result = Parse(request.json['statement'])

    if result == 'Yes':
        r = randint(0, len(yesResults) - 1)
        result = yesResults[r]
    elif result == 'No':
        r = randint(0, len(noResults) - 1)
        result = noResults[r]
    elif result == 'IDK':

        headers, result = BingImageSearch(request.json['statement'])
        resultDict = json.loads(result)

        imageURL = resultDict["value"][0]["thumbnailUrl"]

        return jsonify({'result':  "I don't know, but here's a picture!",
                        'url': imageURL}), 201

    return jsonify({'result':  result}), 201

def runLocalServer():
    app.run(debug=True)
