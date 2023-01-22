import paho.mqtt.client as mqtt 
import time

mqttBroker ="mqtt.eclipseprojects.io"
print("Connecting to broker: ", mqttBroker)

username = str(input("Masukkan nama anda: "))
client = mqtt.Client(username)

client.connect(mqttBroker) 

while True:
    message = input("Masukkan pesan anda: ")
    client.publish("CHATDEK!", message)
    print("Just published " + str(message) + " to topic CHATDEK!")
    time.sleep(1)