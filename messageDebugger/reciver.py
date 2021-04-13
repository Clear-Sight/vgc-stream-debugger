import zmq
import base64
import numpy as np

def recive():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.bind('tcp://*:7777')
    socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))
    while True:
        msg_string = socket.recv_string()
        msg = json.loads(msg_string)
        if msg:
            print(msg)
