import paho.mqtt.client as mqtt
import time

mqttBroker ="mqtt.eclipseprojects.io"
print("Connecting to broker: ", mqttBroker)

mqttBroker ="mqtt.eclipseprojects.io"

client = mqtt.Client("Pemilih")
client.connect(mqttBroker) 

client.loop_start()

def on_message(client, userdata, message):
    print("pesan dari pemilih: ", str(message.payload.decode("utf-8")))

client.subscribe("CHATDEK!")
client.on_message=on_message 

time.sleep(30)
client.loop_stop()