import json
from flask import Flask
app = Flask(__name__)

usr_msg = {
    "compass":0,
    "angle":0,
    "zoom":2,
    "lock_on": False
}

def add_to_usr_msg():
    degree = 0.5
    if usr_msg["compass"] < 360:
        usr_msg["compass"] += degree
    else:
        usr_msg["compass"] = 0
    if usr_msg["angle"] < 90:
        usr_msg["angle"] += degree
    else:
        usr_msg["angle"] = 0
    if usr_msg["zoom"] < 10:
        usr_msg["zoom"] += degree
    else:
        usr_msg["zoom"] = 0
    return usr_msg

def load_user_msg():
    """ returns a dict of the config from config.json """
    FILE = "./usr_msg.json"
    with open(FILE, 'r') as file:
        f = json.load(file)
    return f

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/drone/user/fetch')
@app.route('/drone/user/fetch/')
def message_drone():
    return json.dumps(add_to_usr_msg())
    # return json.dumps(load_user_msg())


if __name__=="__main__":
	app.run(debug=True, port="24474")
