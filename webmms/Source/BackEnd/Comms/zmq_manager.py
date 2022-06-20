import logging
import copy
import sys
import threading
import time

from collections import OrderedDict
import zmq
from Comms import Protocol_class
from Comms.processing import clsProcessing
from enum import Enum

G_ZMQ_Sockets = OrderedDict()
G_ZMQ_Sockets_Thread = OrderedDict()
G_ZMQ_Available_Sockets = list()

class E_WEBMM_PROCESSES(Enum):
    I_MAIN_PROCESS = 1
    I_AUTOSCRIPT_PROCESS = 2


class clsZMQ_Manager:
    """
        ZMQ class that manages connections and sending of messages
    """

    def __init__(self, acPipeNamePar, acZMQSocketKeyPar, lstxmlKeysPar, acPubSubTag):
        """
            This is a public function is used as a constructor for the server.py module.

            Args:
            acPipeNamePar (str): name of the pipe used during connection
            acZMQSocketKeyPar (str): IP and Port used for connection
            lstxmlKeysPar (list): list of xml key
            acPubSubTag (str) : checks if a message is publishing or subscribing

            Returns:

            Raises:
                Raises no exceptions
        """
        self.lstxmlKeysPar = lstxmlKeysPar
        self.acPipeNamePar = acPipeNamePar
        self.acZMQSocketKeyPar = acZMQSocketKeyPar
        self.objClsProcessing = clsProcessing(E_WEBMM_PROCESSES.I_MAIN_PROCESS.value)
        # Get the IP and Port to connect/bind to socket
        try:
            self.acSocketIP, self.acSockerPort = self.acZMQSocketKeyPar.split("_")
        except Exception as E:
            logging.error(" unable to get IP and Port, Error -> %s", E)

        # check if its publish or subscribe (connect for subscribe and bind for publish)
        if acPubSubTag == "publish":
            try:
                self.vZeroMQPublisher()
            except Exception as E:
                logging.error("unable to connect to publisher, error -> %s", E)

        elif acPubSubTag == "subscribe":
            # get all topics for subscribing from processing class
            for acXmlKey in self.lstxmlKeysPar:
                try:
                    self.lstZMQTopics = self.objClsProcessing.lstGetSubZMQTopic(acXmlKey)
                except Exception as E:
                    logging.error("Unable to get ZMQ topics, error -> %s ", E)

            # subscribe and use the topic as topic filters
            try:
                self.vZeroMQSubscriber()
            except Exception as E:
                logging.error("unable to subcribe, error -> %s", E)

    def vZeroMQPublisher(self):
        """
            bind the socket, if it returns a zero, the connection for this port is already made
            Args:

            Returns:

            Raises:
                Raises no exceptions
        """
        try:
            objTmpSocket = self.objBindPubSoc()
            if objTmpSocket == "error":
                sys.exit()
            else:
                G_ZMQ_Sockets[self.acZMQSocketKeyPar] = objTmpSocket

        except Exception as E:
            logging.error(" unable to bind the socket, Error -> %s", E)

    def vZeroMQSubscriber(self):
        """
            connect to the socket

            Args:

            Returns:

            Raises:
                Raises no exceptions
        """
        try:
            socket = self.objBindSoc()
        except Exception as E:
            logging.error(" unable to bind the socket, Error -> %s", E)

        # run a subscriber thread for that socket
        try:
            G_ZMQ_Sockets_Thread[self.acZMQSocketKeyPar] = threading.Thread(target=self.vRecvData, args=(socket,))
            G_ZMQ_Sockets_Thread[self.acZMQSocketKeyPar].daemon = True
            G_ZMQ_Sockets_Thread[self.acZMQSocketKeyPar].start()
        except Exception as E:
            logging.info("Unable to start a thread for this connection, Error -> %s", E)

    def objBindPubSoc(self):
        """
            Bind the socker for publishing, if the connection is successful, return the object

            Args:
            socket (obj): zmq client connection object

            Returns:

            Raises:
                Raises no exceptions
        """
        try:
            context = zmq.Context()
            objSocket = context.socket(zmq.PUB)
            objSocket.bind("tcp://%s:%s" % (self.acSocketIP, int(self.acSockerPort)))
        except Exception as E:
            logging.error("Cannot make the ZMQ connection, Error -> %s", E)

            # remove the xml that refused to connect (get the module of the xml)
            dctLoadedData = copy.deepcopy(Protocol_class.G_dctJsonFileSender)

            for xmlNum, xml in enumerate(dctLoadedData["xmls"]):
                if self.acPipeNamePar == xml["Connection"]["PipeName"]:
                    del dctLoadedData["xmls"][xmlNum]

            # after deleting, update the json file, the main dictionary and return error
            Protocol_class.G_dctJsonFileSender = copy.deepcopy(dctLoadedData)
            Protocol_class.G_dctJsonFile = copy.deepcopy(dctLoadedData)

        return objSocket

    def vUnbindPubSoc(self, ipPortKeyPar):
        """
            unbind the socket when this function is called and retun nothing

            Args:
                ipPortKeyPar (str): IP and Port of the connection

            Returns:

            Raises:
                Raises no exceptions
        """
        acUrlIP, acUrlPort = ipPortKeyPar.split("_")
        urlString = "tcp://" + acUrlIP + ":" + acUrlPort
        G_ZMQ_Sockets[ipPortKeyPar].unbind(urlString)

    def objBindSoc(self):
        """
            bind the socket for subscription

            Args:

            Returns:
                socket (obj): zmq client connection object

            Raises:
                Raises no exceptions
        """
        try:
            context = zmq.Context()
            objSocket = context.socket(zmq.SUB)
            objSocket.connect("tcp://%s:%s" % (self.acSocketIP, int(self.acSockerPort)))
        except Exception as E:
            logging.error("Cannot make the ZMQ connection, Error -> %s", E)
            return "error"
        # use the topics as topic filter
        for acTopicFilter in self.lstZMQTopics:
            objSocket.setsockopt_string(zmq.SUBSCRIBE, acTopicFilter)

        return objSocket

    def vSendData(self, acZeroMQObjectKeyNamePar, acMsgKeyPar, acMsgTopicPar, acXmlSchemaPar):
        """
            method to send zmq autoscript messages

            Args:
                acZeroMQObjectKeyNamePar (str): instance name
                acMsgKeyPar (str): message key
                acMsgTopicPar (str): message topic
                acXmlSchemaPar (str): xml schema

            Returns:

            Raises:
                Raises no exceptions
        """
        btaTopic = acMsgTopicPar.encode('utf-8')
        btaMessageData = self.objClsProcessing.btaGetPackedMessage(acMsgKeyPar, acXmlSchemaPar)
        if btaMessageData == "error":
            logging.error("failed to pack data, please check you data types")

        try:
            G_ZMQ_Sockets[acZeroMQObjectKeyNamePar].send_multipart([btaTopic, btaMessageData], flags=0, copy=True, track=False)
        except Exception as E:
            logging.error("Can not send ZeroMQ message, error -> %s", E)

    def vSendZmqDataMainThread(self, acZeroMQObjectKeyNamePar, acMsgTopicPar, btaMessageDataPar):
        """
            method to send messages

            Args:
                acZeroMQObjectKeyNamePar (str): instance name
                acMsgTopicPar (str): message topic
                btaMessageDataPar (bytes): message data to be published

            Returns:

            Raises:
                Raises no exceptions
        """
        btaTopic = acMsgTopicPar.encode('utf-8')
        try:
            G_ZMQ_Sockets[acZeroMQObjectKeyNamePar].send_multipart([btaTopic, btaMessageDataPar], flags=0, copy=True, track=False)
        except Exception as E:
            logging.error("Can not send ZeroMQ message, error -> %s", E)

    def vRecvData(self, socketPar):
        """
            method to send messages

            Args:
                socketPar (object): zmq connection object for receiving messages

            Returns:

            Raises:
                Raises no exceptions
        """
        while True:
            try:
                lstReceivedData = socketPar.recv_multipart(flags=0, copy=True, track=False)
            except Exception as E:
                logging.error("Cannot receive the message, Error -> %s", E)
            try:
                acTopic = lstReceivedData[0].decode("utf-8")
            except Exception as E:
                logging.error("Error decoding the topic, Error -> %s", E)

            try:
                btaMessage = lstReceivedData[1]
            except Exception as E:
                logging.error("Cannot retrieve the byte message from the received message list, Error -> %s", E)

            try:
                protocolObj = Protocol_class.RRS_MMI("")
                protocolObj.vReceive(acTopic, btaMessage)
            except Exception as E:
                logging.error("Cannot unpack the received message, Error -> %s", E)

            time.sleep(0.01)
