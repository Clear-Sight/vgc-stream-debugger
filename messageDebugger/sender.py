import json
import base64
import zmq

"""
send phi, theata and lockon:bool
"""
msg = {
    "phi":0.0,
    "theta":0.0,
    "lockon":False
}


DOMAIN = "localhost"
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect(f'tcp:/{DOMAIN}/:7777')

socket.send(json.dumps(msg))
