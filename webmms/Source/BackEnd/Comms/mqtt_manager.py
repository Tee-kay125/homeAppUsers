import sys
import time
import logging
import paho.mqtt.client as mqtt
import server
import threading
import copy

G_boolMQTTMsgThread = False
class clsMqttManager():
    """ This is mqtt class, it connect, sends and receives data from the node

        args:
    """

    def __init__(self, acIpAddress, iPort):
        """
            Constructor: accept IP and Port and connect to the Node.
            Args:
                acIpAddress (String) : Node Ip address
                iPort (int)          : Node Port
        """
        self.acIpAddress = acIpAddress
        self.iPort = iPort

        self.G_dispatch_dict = {}   #Hold all topics and comms object, used to pass data to comms when receiving messages
        self.G_bOnConnectFlag = False

        # creating Mqtt client
        self.client = mqtt.Client()

        # Assign event\link to CALLBACKS
        self.client.on_connect = self.vOnConnect
        self.client.on_message = self.vReceive

        # Connect to broker
        try:
            self.client.connect(self.acIpAddress, self.iPort)
            # logging.info("Connected to MQTT broker with IP %s and port %s", self.acIpAddress, str(self.iPort))
        except Exception as E:
            self.G_bOnConnectFlag = False
            logging.error("Not connected to broker error -> %s", E)

        # Start the client loop
        self.client.loop_start()
        logging.info("Sleeping for 4 seconds")
        time.sleep(4)  # wait for connection to happen

    def vOnLog(self, client, userdata, level, buf):
        pass

    def vSubscribe(self, lstSubscribeTopic, commsObj):
        """ This method subscribe to a list of message topics passed
            and add the topic with its object to global dictionary G_dispatch_dict.

        Args:
            lstSubscribeTopic (list) : list of message topic.
            commsObj (object): object of a comms class.

        Returns:

        Raises:
            Raises no exceptions
        """
        for topic in lstSubscribeTopic:
            try:
                self.G_dispatch_dict.update({topic:commsObj})
            except Exception as E:
                logging.error("Could not update global dictionary G_dispatch_dict, error -> %s", E)

            try:
                self.client.subscribe(topic)
            except Exception as E:
                logging.error("Could not subscribe to topic, error -> %s", E)

            
            
    def vUnsubscribe(self, lstSubscribeTopic):
        """ This method unsubscribe to a list of message topics passed
            and remove the topic with its object from global dictionary G_dispatch_dict.

        Args:
            lstSubscribeTopic (list) : list of message topic.

        Returns:

        Raises:
            Raises no exceptions
        """
        for topic in lstSubscribeTopic:
            try:
                self.client.unsubscribe(topic)
            except Exception as E:
                logging.error("Could not unsubscribe to topic, error -> %s", E)

            try:
                del self.G_dispatch_dict[topic]  
            except Exception as E:
                logging.error("Could not Delete message topic from G_dispatch_dict, error -> %s", E)
 
    def vOnConnect(self, client, userdata, flags, rc):

        if(rc == 0):
            self.G_bOnConnectFlag = True
            logging.info("vOnConnect success")
        else:
            self.G_bOnConnectFlag = False
            logging.error("vOnConnect failed")
            self.client.loop_stop()
            logging.error("Stopping MQTT thread loop")

    def vDisconnect(self):
        self.G_bOnConnectFlag = False
        self.client.loop_stop()

    def vSend(self, topic, payload):
        """ This method sends data to the node

        Args:
            topic (string) : message topic.
            payload (list) : message payload

        Returns:

        Raises:
            Raises no exceptions
        """

        try:
            self.client.publish(topic, payload) 
        except Exception as E:
            logging.error("Could not publish messages to this pipe, error -> %s", E)

        time.sleep(2)

    def vReceive(self, client, userdata, msg):
        """ This method receives data and use the comms object stored in G_dispatch_dict
            to send data to comms class

        Args:
            client : mqtt client.
            userdata : mtqq userdata
            msg : mqtt msg, containes topic and payload

        Returns:

        Raises:
            Raises no exceptions
        """

        self.G_bOnConnectFlag = True
        global G_boolMQTTMsgThread
        try:
            objClsMqttComms = self.G_dispatch_dict[msg.topic]

            lstMsg = [objClsMqttComms, msg]
            server.objMQTTQueue.put(lstMsg)
        except Exception as E:
            logging.error("could not put messages on queue -> %s", E)
        
        if G_boolMQTTMsgThread == False:
            threading.Thread(target=self.getMQTTMsgs, daemon=True).start()
            G_boolMQTTMsgThread = True

    def getMQTTMsgs(self):
        while True:
            if server.objMQTTQueue.qsize() > 0:
                try:
                    lstMsg = server.objMQTTQueue.get()
                    objClsMqttComms = lstMsg[0]
                    msg = lstMsg[1]
                    if(objClsMqttComms):
                        objClsMqttComms.vReceive(msg.topic, msg.payload)
                except Exception as E:
                    logging.error("Could not find comms object exception -> %s", E)
            time.sleep(0.01)
            