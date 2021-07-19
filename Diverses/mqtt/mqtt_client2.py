import json

import paho.mqtt.client as mqtt
import time, random, threading
import multiprocessing

serverUrl = "localhost"
clientId = "pc1"
device_name = "My pc1"

task_queue = multiprocessing.Queue()


# display all incoming messages
def on_message(client, userdata, message):
    payload = json.loads(message.payload.decode("utf-8"))
    print(message.payload)
    print(" < received message " + str(payload))
    if payload.get("value") == 5:
        task_queue.put(shutdown)


def shutdown():
    message = json.dumps({"error": 1})
    publish("/temperature/response", message)


# publish a message
def publish(topic, message, wait_for_ack=False):
    QoS = 2 if wait_for_ack else 0
    message_info = client.publish(topic, message, QoS)
    if wait_for_ack:
        print(" > awaiting ACK for {}".format(message_info.mid))
        message_info.wait_for_publish()
        print(" < received ACK for {}".format(message_info.mid))


# display all outgoing messages
def on_publish(client, userdata, mid):
    print(" > published message: {}".format(mid))


# connect the client to Cumulocity IoT and register a device
client = mqtt.Client(clientId)
client.on_message = on_message
client.on_publish = on_publish

client.connect(serverUrl)
client.loop_start()
print("Device registered successfully!")

client.subscribe("send/temperature")

# process all tasks on queue
try:
    while True:
        task = task_queue.get()
        task()
except (KeyboardInterrupt, SystemExit):
    print("Received keyboard interrupt, quitting ...")
    exit(0)
