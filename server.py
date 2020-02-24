from flask import Flask
from flask import Response
from flask import json
from flask import request

app = Flask(__name__)

RESERVATIONS = {}
for hour in ["10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm", "6pm", "7pm", "8pm", "9pm", "10pm"]:
    RESERVATIONS[hour] = {
    "available": True,
    "player": None
}

@app.route("/")
def index():
    return "Welcome to tennis reservations"

@app.route('/reservations', methods = ['GET', 'POST'])
def api_reservations():
    if request.method == 'GET':
        if request.args.get('hour'):
            playtime = request.args.get('hour')
            js = json.dumps(RESERVATIONS[playtime])
            resp = Response(js, status=200, mimetype='application/json')
            return resp
        else:
            js = json.dumps(RESERVATIONS)
            resp = Response(js, status=200, mimetype='application/json')
            return resp

    elif request.method == 'POST':
        payload = request.get_json()
        RESERVATIONS[payload['hour']] = {'available': False, 'player': payload['player']}
        js = json.dumps(payload)
        resp = Response(js, status=201, mimetype='application/json')
        return resp
    else:
        return "415 Unsupported Media Type ;)"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
