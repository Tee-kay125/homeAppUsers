import paho.mqtt.client as mqtt
import threading, sys, os, struct, json
lstClients = []
iNoOfClient = 1
info = [["10.2.5.13",1883,"#"]]

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK Returned code=",rc)
        topic = userdata
        print(topic)
        client.subscribe(topic)
    else:
        print("Bad connection Returned code=",rc)
        sys.exit()

def on_message(client, userdata, msg):
    try:
        data = struct.unpack("=6HQH8I2iIB2H24s",msg.payload)
        print("0 -> topic: {} - Payload: {}".format(msg.topic, data))
    except Exception:
        pass

    try:
        data = struct.unpack("=6HQH",msg.payload)
        print("1 -> topic: {} - Payload CMD: {}".format(msg.topic, data))
        # lstData = list(data)
        # message = struct.pack("=6HQH",*lstData)
        # print(message)
        # client.publish(msg.topic, message)
    except Exception:
        pass

    print("2 -> topic: {} - Payload: {}".format(msg.topic, msg.payload))

def multi_loop(client, flag=True):
    while flag:
        client.loop(0.1)

def main():
    for i in range(iNoOfClient):
        client_name  = "client_"+str(i)
        topic       = info[i][2]
        client      = mqtt.Client(client_name, userdata=topic)
        client.on_connect = on_connect
        client.on_message = on_message
        lstClients.append(client)

    clients_count = 0
    for client in lstClients:
        broker  = info[clients_count][0]
        port    = info[clients_count][1]
        clients_count = clients_count + 1
        
        #try catch
        client.connect(broker, port)
        t = threading.Thread(target=multi_loop, args=(client, True))
        t.start()

if __name__== "__main__":
    main()