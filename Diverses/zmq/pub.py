import zmq
from time import sleep

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://127.0.0.1:2000')

messages = [1, 2, 3, 5, 8, 13]

current_Message = 0

while True:
    sleep(1)
    socket.send_json({"CurrentMessage:": messages[current_Message]})
    if current_Message == 2:
        current_Message = 0
    else:
        current_Message += 1
