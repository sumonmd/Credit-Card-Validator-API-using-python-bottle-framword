from bottle import route, run, template, request,view,response

from card_validator.validator import card_validator


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)
@route('/')
@view('index')
def home_index():
    return {
        "message": request.query.get("message", "Welcome to Card Check Point")
    }
@route('/validate')
def validator():
    card_number = request.query.get('cardNumber')
    if card_number:
        try:
            issuer = card_validator(card_number)
        except ValueError:
            response.status = 400
            return {
                "result": 'This is not a valid card number'
            }
        return {
            "issue": issuer,
            "result": "It is a {} card".format(issuer)
        }
    else:
        return {"result": "Please give your card number as a query parameter"}

run(host='localhost', port=8080)