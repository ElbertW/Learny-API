#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request

from AlgebraicParser import AlgebraicParser

app = Flask(__name__)

AP = AlgebraicParser()

# Main Parsing Function
def Parse(input):
    if '=' not in input:
        return 'maybe'

    equations = input.split('=')

    evaluations = []

    for e in equations:
        evaluations.append(AP.eval(e))

    left = 0
    right = 0

    for i in range(len(evaluations) - 1):
        left = evaluations[i]
        right = evaluations[i+1]

        if(left != right):
            return 'no'

    return 'yes'


# 404 Handler
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# POST statement
@app.route('/learny/api/v1.0/eval', methods=['POST'])
def eval():
    if not request.json or not 'statement' in request.json:
        abort(400)

    return jsonify({'result': Parse(request.json['statement']) }), 201


# if __name__ == '__main__':
#     app.run(debug=True)