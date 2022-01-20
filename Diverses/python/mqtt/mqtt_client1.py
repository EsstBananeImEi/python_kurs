import json

import paho.mqtt.client as mqtt
import time, random, threading
import multiprocessing

serverUrl = "localhost"
clientId = "thermostat1"
device_name = "My Thermostat"

task_queue = multiprocessing.Queue()


def on_message(client, userdata, message):
    payload = json.loads(message.payload)
    print(" < received message " + str(payload))
    if payload.get("error"):
        task_queue.put(perform_restart)


def perform_restart():
    print("Simulating device restart...")
    message = json.dumps({"temp": "thermostat 1",
                          "value": "Restarting"})
    publish("send/temperature", message, wait_for_ack=True)

    print("...restarting...")
    time.sleep(1)
    print("...restart completed")
    message = json.dumps({"temp": "thermostat 1",
                          "value": "restart Finished"})
    publish("send/temperature", message, wait_for_ack=True)


def send_measurement():
    print("Sending temperature measurement...")
    temperature = random.randint(1, 5)
    message = json.dumps({"temp": "thermostat 1",
                          "value": temperature})
    publish("send/temperature", message)


def publish(topic, message, wait_for_ack=False):
    QoS = 2 if wait_for_ack else 0
    message_info = client.publish(topic, message, QoS)
    if wait_for_ack:
        print(" > awaiting ACK for {}".format(message_info.mid))
        message_info.wait_for_publish()
        print(" < received ACK for {}".format(message_info.mid))


def on_publish(client, userdata, mid):
    print(" > published message: {}".format(mid))


def device_loop():
    while True:
        task_queue.put(send_measurement)
        time.sleep(2)


client = mqtt.Client(clientId)
client.on_message = on_message
client.on_publish = on_publish

client.connect(serverUrl)
client.loop_start()
print("Device registered successfully!")

client.subscribe("/temperature/response")

device_loop_thread = threading.Thread(target=device_loop)
device_loop_thread.daemon = True
device_loop_thread.start()

# process all tasks on queue
try:
    while True:
        task = task_queue.get()
        task()
except (KeyboardInterrupt, SystemExit):
    print("Received keyboard interrupt, quitting ...")
    exit(0)
