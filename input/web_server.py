import json
from flask import Flask
app = Flask(__name__)



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
def message_drone():
    return json.dumps(load_user_msg())


if __name__=="__main__":
	app.run(debug=True, port="24474")
