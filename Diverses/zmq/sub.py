import json

import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://127.0.0.1:2000')
socket.setsockopt_string(zmq.SUBSCRIBE, 'ASCII')

while True:
    message = socket.recv_json()
    print(message.get("CurrentMessage"))
    if message.get("CurrentMessage") is not None:
        print(message)

# TODO: MQTT Informationen Hinzufügen!!
# TODO: ZMQ vollenden !!!
