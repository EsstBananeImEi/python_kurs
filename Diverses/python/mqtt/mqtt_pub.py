import datetime
import json
import time

import paho.mqtt.client as mqtt

Temperatur = 30


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


def on_message(client, userdata, msg):
    json_payload = json.loads(msg.payload.decode("utf-8"))
    print(f"The temperature is {json_payload['data']}°C")
    decrease_temperature_by_one()
    print(f"Decreasing max temperature to {Temperatur}°C")


def decrease_temperature_by_one():
    global Temperatur
    Temperatur -= 1
    if Temperatur < 15:
        Temperatur = 15


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_start()

while True:
    time.sleep(5)
    now = datetime.datetime.now()
    client.subscribe("response/#")
    client.publish("Haus/EG/Wohnzimmer/Temperatur", str(Temperatur) + "°C", qos=1)
    # client.publish("Haus/EG/Wohnzimmer/Clock", now.strftime("%H:%M:%S"), qos=1)
    # client.publish("Haus/EG/Wohnzimmer/Temperatur", f"{str(randint(10, 24))}°C", qos=1)
    # client.publish(
    #     "Haus/EG/Schlafzimmer/Temperatur", f"{str(randint(10, 24))}°C", qos=1
    # )
    # client.publish("Haus/EG/Kueche/Temperatur", f"{str(randint(10, 24))}°C", qos=1)
    # client.publish(
    #     "Haus/EG/Kinderzimmer/Temperatur", f"{str(randint(10, 24))}°C", qos=1
    # )
    # client.publish("Haus/DG/Kueche/Clock", now.strftime("%H:%M:%S"), qos=1)
    # client.publish(
    #     "Haus/DG/Kinderzimmer/Temperatur", f"{str(randint(10, 24))}°C", qos=1
    # )
    # client.publish("Haus/EG/Kinderzimmer/Licht", f"Licht ist an", qos=1)
