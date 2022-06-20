import paho.mqtt.client as mqtt
import threading, sys, os, struct, json, time, signal

G_dctMqttMain = {}
lstClients = []
iNoOfClient = 1
info = [["127.0.0.1",1883,"#"]]
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK Returned code=",rc)
        topic = userdata
        client.subscribe(topic)

        thread_publishUnsol = threading.Thread(target=publishUnsol, args=(client, True))
        thread_publishUnsol.start()
    else:
        print("Bad connection Returned code=",rc)
        sys.exit()

def on_message(client, userdata, msg):
    try:
        if msg.topic.endswith("Unsol"):
            pass
        else:
            data = struct.unpack(G_dctMqttMain[msg.topic][0],msg.payload)
            print("Received message -> ",msg.topic)
            try:
                for key, val in G_dctMqttMain.items():
                    if key == msg.topic+"Rsp":
                        
                        RespMessage = struct.pack(G_dctMqttMain[key][0],*G_dctMqttMain[key][1])
                        client.publish(key, RespMessage)
            except Exception as E:
                print("Error publishing the message, Exception ->  %s", E)
    except Exception as E:
        print(E)

def publishUnsol(client, flag=True):
    unsolCounter = 0
    while True:
        for key, value in G_dctMqttMain.items():
            if key.endswith("Unsol"):
                packedData = struct.pack(value[0],*value[1])
                client.publish(key, packedData)
                sys.stdout.write("\rpublishing unsol messages -> %d"%unsolCounter)
                sys.stdout.flush()
                unsolCounter+=1
        time.sleep(1)

def multi_loop(client, flag=True):
    while flag:
        client.loop(0.1)

def getGlobalDict(G_dctMain):
    global G_dctMqttMain
    G_dctMqttMain = G_dctMain

def mqttFunctions(G_dctMain):
    getGlobalDict(G_dctMain)
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
        
        try:
            client.connect(broker, port)
        except Exception as E:
            print("Error connecting to brocker, Exception: {}".format(E))
        
        thread_multi_loop = threading.Thread(target=multi_loop, args=(client, True))
        thread_multi_loop.start()