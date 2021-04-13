import json
import zmq
import time

"""
send phi, theata and lockon:bool
"""
msg = {
    "phi":0.0,
    "theta":0.0,
    "lockon":False
}

host = "178.174.148.6"
port = "7777"

# Creates a socket instance
context = zmq.Context()
socket = context.socket(zmq.PUB)

# Binds the socket to a predefined port on a host.
socket.connect(f"tcp://{host}:{port}")

# Sleeps to give time to setup the connection.
time.sleep(1)

# Sends the instruction JSON.
socket.send_json(msg)
