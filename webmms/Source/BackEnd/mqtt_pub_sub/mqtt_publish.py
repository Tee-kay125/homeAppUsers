import paho.mqtt.client as mqtt
import time, struct

broker  = "127.0.0.1"
port    = 1883



def on_publish(client, userdata, results):
    print("{} Data published \n".format(results))
    pass

def main():
    client = mqtt.Client()
    client.on_publish = on_publish
    client.connect(broker, port)   

    while True:
        # c1 = c1+0.0001
        # dctData = [0, 4, 0, 6, 0, 0, 0, 65535, 2019, 11, 5, 14, 26, 58, 11, 18, 23, 45, 52, 2, 8, 98, b'Testing ADCS EIU']
        # message = struct.pack("=6HQH8I2iIB2H24s",*dctData)
        # client.publish("ADCS/EIU/EiuStatusReportUnsol", message)

        dctData2 = [0, 1, 0, 6, 1, 0, 0, 65535]
        message2 = struct.pack("=6HQH",*dctData2)
        client.publish("ADCS/EIU/EiuEndOfSetupCmdRsp", message2)

        time.sleep(1)


if __name__ == "__main__":
    main()