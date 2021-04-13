import zmq
import base64
import numpy as np
import json

def recive():
    host = "*"
    port = "7777"

    # Creates a socket instance
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.bind(f"tcp://{host}:{port}")

    socket.subscribe("")
    while True:
        msg = socket.recv_json()

recive()
