import datetime
import time
from random import randint
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


client = mqtt.Client()
client.on_connect = on_connect

client.connect("broker.emqx.io", 1883, 60)

client.loop_start()

while True:
    time.sleep(5)
    now = datetime.datetime.now()
    client.publish("Haus/EG/Wohnzimmer/Clock", now.strftime("%H:%M:%S"), qos=1)
    client.publish("Haus/EG/Wohnzimmer/Temperatur", f"{str(randint(10, 24))}°C", qos=1)
    client.publish("Haus/EG/Schlafzimmer/Temperatur", f"{str(randint(10, 24))}°C", qos=1)
    client.publish("Haus/EG/Kueche/Temperatur", f"{str(randint(10, 24))}°C", qos=1)
    client.publish("Haus/EG/Kinderzimmer/Temperatur", f"{str(randint(10, 24))}°C", qos=1)
    client.publish("Haus/DG/Kueche/Clock", now.strftime("%H:%M:%S"), qos=1)
    client.publish("Haus/DG/Kinderzimmer/Temperatur", f"{str(randint(10, 24))}°C", qos=1)
    client.publish("Haus/EG/Kinderzimmer/Licht", f"Licht ist an", qos=1)
