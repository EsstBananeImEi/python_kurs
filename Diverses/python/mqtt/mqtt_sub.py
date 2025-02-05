import json

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe("Haus/EG/Wohnzimmer/#")
    # client.subscribe("Haus/EG/+/Temperatur")
    # client.subscribe("Haus/EG/Kinderzimmer/#")


def on_message(client, userdata, msg):
    temperature = 0
    print(msg.topic + " " + str(msg.payload.decode("utf-8")))
    if msg.topic == "Haus/EG/Wohnzimmer/Temperatur":
        temperature = int(msg.payload.decode("utf-8")[:-2])
        if temperature > 20:
            print("Temperatur ist zu hoch")
            client.publish(
                "response/Haus/EG/Wohnzimmer/Temperatur",
                json.dumps({"msg": "Too Hot", "data": temperature}),
                qos=1,
            )


def on_publish(client, userdata, mid):
    print("Message published")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect("localhost", 1883, 60)

client.loop_forever()
