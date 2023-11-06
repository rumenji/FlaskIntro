# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

calcs = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<calc>')
def routes(calc):
    a = request.args['a']
    b = request.args['b']
    result = calcs[calc](int(a), int(b))
    return f'{result}'