#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import json
import time
import paho.mqtt.client as mqtt
import logging
import zmq
from Comms.processing import clsProcessing
from Comms import Protocol_class as _Protocol_class
from enum import Enum

class E_WEBMM_PROCESSES(Enum):
    I_MAIN_PROCESS = 1
    I_AUTOSCRIPT_PROCESS = 2


class clsAutoScripting:
    """
        This class declares all functions that will be used for auto Scripting
        Args:

    """
    def __init__(self):
        pass

    def vGetFileContent(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def vMakeConnection(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def objCreateMQTTObject(self, acIpAddressPar, iPortPar):
        raise NotImplementedError("Subclass must implement abstract method")

    def vOnConnect(self, objClientPar, userDataPar, flags, rc):
        raise NotImplementedError("Subclass must implement abstract method")

    def vSendMessages(self, acScriptNamePar):
        raise NotImplementedError("Subclass must implement abstract method")

    def vSendMessagesRepeat(self, acScriptNamePar):
        raise NotImplementedError("Subclass must implement abstract method")

    def objBindZMQPubSoc(self, acIpAddressPar, iPortPar):
        raise NotImplementedError("Subclass must implement abstract method")

    def vSendZmqData(self, objBrockerObjectPar, acMsgTopicPar, bMessageDataPar):
        raise NotImplementedError("Subclass must implement abstract method")

    def vUnbindPubSoc(self,ZMQSocket, acIpPortKeyPar):
        raise NotImplementedError("Subclass must implement abstract method")


class clsMessageObjects(clsAutoScripting):
    """
        This class inherits and defines all classes declared on the parent class

        Args:

    """
    def __init__(self):
        """
            Scripting files are called whenevE_WEBMM_PROCESSES(er a new instance is created
        """
        self.vGetFileContent()
        self.objClsProcessing = clsProcessing(E_WEBMM_PROCESSES.I_AUTOSCRIPT_PROCESS.value)
        self.bStopSendingThread = False

    def vGetFileContent(self):

        """
            Read auto script directory and get all files content

            Args:

            Returns:

            Raises:
                Raises no exceptions
        """
        acAutoScriptingPath = os.path.join(os.path.dirname(__file__), "../scriptingFiles/")
        acAutoScriptFiles = os.listdir(acAutoScriptingPath)
        for iIndex, acItem in enumerate(acAutoScriptFiles):
            if acItem[-5:] == ".json":
                with open(os.path.join(os.path.dirname(__file__), "../scriptingFiles/" + acItem), 'r') as f:
                    acScriptFileName = acItem[:-5]
                    _Protocol_class.G_dctJsonAutoScriptFile.update({acScriptFileName: json.load(f)})
                    f.close()

    def vMakeConnection(self):
        """
            This function get all MQTT and ZeroMQ IP and port from script files and make connections

            Args:

            Returns: string : string message if MQTT object was not created successfully

            Raises:
                Raises no exceptions
        """
        for acScriptName, dctScriptInfo in _Protocol_class.G_dctJsonAutoScriptFile.items():
            _Protocol_class.G_dctMQTT_ZeroMQ_Connections.update({acScriptName: {}})
            _Protocol_class.G_dctMQTT_ZeroMQ_Connections[acScriptName].update({"MQTT": {}})
            _Protocol_class.G_dctMQTT_ZeroMQ_Connections[acScriptName].update({"ZMQ": {}})
            dctTmpMQTTMessages = dict()
            dctTmpZMQMessages = dict()
            for acMessageKey, dctMessageInfo in dctScriptInfo.items():
                acIP = str()
                iPort = int()
                acTmpMsgProtocol = str()
                acIpPort = str()
                acPubSub = str()
                acTmpMsgProtocol = dctMessageInfo["Individual_Message_Protocol"]
                acPubSub = dctMessageInfo["pubSub_tag"]
                acMsgTopic = dctMessageInfo["Msg_Topic"]
                acDelayInSec = dctMessageInfo["delayInSec"]

                # Check if message is MQTT or ZeroMQ and make proper connection
                if acTmpMsgProtocol == "MQTT":
                    acIP = dctMessageInfo["Connection"]["MQTTRemoteIP"]
                    iPort = dctMessageInfo["Connection"]["MQTTPort"]
                    acXmlSchema = dctMessageInfo["Connection"]["xmlSchema"]
                    acIpPort = str(acIP) + "_" + str(iPort)

                    """
                        If connection to given IP and port is already made, simply add the messages, if connection is not yet made
                        create the connection and save the object to a class variable
                    """

                    try:
                        if acIpPort not in _Protocol_class.G_dctMQTT_ZeroMQ_Connections[acScriptName]["MQTT"]:
                            if acIpPort in _Protocol_class.G_dctMQTT_ZMQ_Objects:
                                try:
                                    _Protocol_class.G_dctMQTT_ZeroMQ_Connections[acScriptName]["MQTT"].update({acIpPort: {"MQTTObject": _Protocol_class.G_dctMQTT_ZMQ_Objects[acIpPort]}})
                                except Exception as E:
                                    logging.error("Unable to add message to this connection")
                            else:
                                if self.objCreateMQTTObject(acIP, int(iPort)) is None:
                                    return "error"
                                
                                objMqtt = self.objCreateMQTTObject(acIP, int(iPort))  # give publish topic to Comms
                                _Protocol_class.G_dctMQTT_ZeroMQ_Connections[acScriptName]["MQTT"].update({acIpPort: {"MQTTObject": objMqtt}})
                                _Protocol_class.G_dctMQTT_ZMQ_Objects.update({acIpPort: objMqtt})
                                _Protocol_class.G_dctAutoScriptOnlyMQTT_ZMQ_Objects.update({acIpPort: objMqtt})
                    except Exception as E:
                        logging.info("Cant create MQTT object, roor -> %s", E)
                        return "error"

                    bTmpMQTTPackedMsg = self.objClsProcessing.btaGetPackedMessageAutoScripting(acMessageKey, acXmlSchema, acScriptName)
                    dctTmpMQTTMessages.update({acMessageKey: [acMsgTopic, bTmpMQTTPackedMsg, acDelayInSec]})

                    try:
                        _Protocol_class.G_dctMQTT_ZeroMQ_Connections[acScriptName]["MQTT"][acIpPort].update({"MQTTMessages": dctTmpMQTTMessages})
                    except Exception as E:
                        logging.info("Can't append MQTT message, %s", E)
                        return "error"

                elif acTmpMsgProtocol == "ZMQ" and acPubSub == "Publish":
                    acIP = dctMessageInfo["Connection"]["ZeroMQRemoteIPPub"]
                    iPort = dctMessageInfo["Connection"]["ZeroMQPortPub"]
                    acXmlSchema = dctMessageInfo["Connection"]["xmlSchema"]
                    acIpPort = str(acIP) + "_" + str(iPort)

                    """
                        If connection to given IP and port is already made, simply add the messages, if connection is not yet made
                        create the connection and save the object to a class variable
                    """
                    try:
                        if acIpPort not in _Protocol_class.G_dctMQTT_ZeroMQ_Connections[acScriptName]["ZMQ"]:
                            if acIpPort in _Protocol_class.G_dctMQTT_ZMQ_Objects:
                                try:
                                    _Protocol_class.G_dctMQTT_ZeroMQ_Connections[acScriptName]["ZMQ"].update({acIpPort: {"ZMQObject": _Protocol_class.G_dctMQTT_ZMQ_Objects[acIpPort]}})
                                except Exception as E:
                                    logging.error("Unable to add message to this connection")
                                    return "error"
                            else:
                                objZMQ = self.objBindZMQPubSoc(acIP, int(iPort))  # get a zmqObject
                                _Protocol_class.G_dctMQTT_ZeroMQ_Connections[acScriptName]["ZMQ"].update({acIpPort: {"ZMQObject": objZMQ}})
                                _Protocol_class.G_dctMQTT_ZMQ_Objects.update({acIpPort: objZMQ})
                                _Protocol_class.G_dctAutoScriptOnlyMQTT_ZMQ_Objects.update({acIpPort: objZMQ})
                                _Protocol_class.G_dctAutoScriptOnlyZMQ_Objects.update({acIpPort: objZMQ})

                    except Exception as E:
                        logging.info("Cant create ZMQ object, roor -> %s", E)
                        return "error"

                    bTmpZMQPackedMsg = self.objClsProcessing.btaGetPackedMessageAutoScripting(acMessageKey, acXmlSchema, acScriptName)
                    dctTmpZMQMessages.update({acMessageKey: [acMsgTopic, bTmpZMQPackedMsg, acDelayInSec]})

                    try:
                        _Protocol_class.G_dctMQTT_ZeroMQ_Connections[acScriptName]["ZMQ"][acIpPort].update({"ZMQMessages": dctTmpZMQMessages})
                    except Exception as E:
                        logging.info("Can't append ZMQ message, %s", E)
                        return "error"
        return "object created"

    def objCreateMQTTObject(self, acIpAddressPar, iPortPar):
        """
            This methid creates an MQTT object using passed IP and Port and return

            Args:
                acIpAddressPar (str): MQTT IP address
                iPortPar (int): MQTT port number

            Returns:
                objClient (obj): MQTT object
            Raises:
                Raises no exceptions
        """
        # creating Mqtt client
        objClient = mqtt.Client("auto scripting")

        # Assign event\link to CALLBACKS
        objClient.on_connect = self.vOnConnect
        try:
            objClient.connect(acIpAddressPar, iPortPar)
        except Exception as E:
            logging.info("Not connected to broker error -> %s", E)
            return None

        # Start the client loop
        objClient.loop_start()
        logging.info("Sleeping for 4 seconds")
        time.sleep(4)  # wait for connection to happen
        return objClient

    def vOnConnect(self, objClientPar, userDataPar, acFlagsPar, iRcPar):
        """

            Args:
                objClientPar (obj): The client is a client object.
                userDataPar: The private user data as set in Client()
                acFlagsPar (str): response flags sent by the broker
                iRcPar (int): is used for checking that the connection was established
        """
        if(iRcPar == 0):
            logging.info("vOnConnect success")
        else:
            logging.info("vOnConnect failed")
            objClientPar.loop_stop()
            logging.info("Stopping MQTT thread loop")

    def vSendMessages(self, acScriptNamePar):
        """
            functions takes one argument (script name) and send every message inside the file, it uses saved objects
            to send all messages to their respective destination.

            Args:
                acScriptNamePar (str): Name of the file

            Returns:

            Raises:
                Raises no exceptions
        """

        for acBroker, dctBrokerInfo in _Protocol_class.G_dctMQTT_ZeroMQ_Connections[acScriptNamePar].items():
            for acConnection, dctConnectionInfo in dctBrokerInfo.items():
                if acBroker == "MQTT":
                    objBrockerObject = dctConnectionInfo["MQTTObject"]
                    for acMessageKey, dctMessageInfo in dctConnectionInfo["MQTTMessages"].items():
                        acMessageTopic = dctMessageInfo[0]
                        bMessageValues = dctMessageInfo[1]
                        acDelayInSec = dctMessageInfo[2]
                        if acDelayInSec:
                            try:
                                time.sleep(float(acDelayInSec))
                            except Exception as E:
                                logging.error("Error with time delay. error -> %s", E)
                        if acConnection in _Protocol_class.G_dctAutoScriptOnlyMQTT_ZMQ_Objects:
                            try:
                                objBrockerObject.publish(acMessageTopic, bMessageValues)
                            except Exception as E:
                                logging.info("Error sending a message, error -> %s", E)
                        else:
                            try:
                                objBrockerObject.vSend(acMessageTopic, bMessageValues)
                            except Exception as E:
                                logging.error("Error sending this message, error -> %s", E)
                elif acBroker == "ZMQ":
                    objBrockerObject = dctConnectionInfo["ZMQObject"]
                    for acMessageKey, dctMessageInfo in dctConnectionInfo["ZMQMessages"].items():
                        acMessageTopic = dctMessageInfo[0]
                        bMessageValues = dctMessageInfo[1]
                        acDelayInSec = dctMessageInfo[2]
                        if acDelayInSec:
                            try:
                                time.sleep(float(acDelayInSec))
                            except Exception as E:
                                logging.error("Error with time delay. error -> %s", E)
                        if acConnection in _Protocol_class.G_dctAutoScriptOnlyMQTT_ZMQ_Objects:
                            try:
                                self.vSendZmqData(objBrockerObject, acMessageTopic, bMessageValues)
                            except Exception as E:
                                logging.info("Error sending ZMQ a message, error -> %s", E)
                        else:
                            try:
                                objBrockerObject.vSendZmqDataMainThread(acConnection, acMessageTopic, bMessageValues)
                            except Exception as E:
                                logging.error("Error sending ZMQ message, error -> %s", E)

    def vSendMessagesRepeat(self, acScriptNamePar):
        """
            functions sends every message inside the file, it uses saved objects
            to send all messages to their respective destination.

            Args:
                acScriptNamePar (str): Name of the file

            Returns:

            Raises:
                Raises no exceptions
        """
        while True:
            if _Protocol_class.G_stopThread:
                break
            if self.bStopSendingThread:
                break
            for acBroker, dctBrokerInfo in _Protocol_class.G_dctMQTT_ZeroMQ_Connections[acScriptNamePar].items():
                for acConnection, dctConnectionInfo in dctBrokerInfo.items():
                    if acBroker == "MQTT":
                        objBrockerObject = dctConnectionInfo["MQTTObject"]
                        for acMessageKey, dctMessageInfo in dctConnectionInfo["MQTTMessages"].items():
                            if not _Protocol_class.G_stopThread and not self.bStopSendingThread:
                                acMessageTopic = dctMessageInfo[0]
                                bMessageValues = dctMessageInfo[1]
                                acDelayInSec = dctMessageInfo[2]
                                if acDelayInSec:
                                    try:
                                        time.sleep(float(acDelayInSec))
                                        if _Protocol_class.G_stopThread:
                                            break
                                    except Exception as E:
                                        logging.error("Error with time delay. error -> %s", E)
                                if acConnection in _Protocol_class.G_dctAutoScriptOnlyMQTT_ZMQ_Objects:
                                    try:
                                        objBrockerObject.publish(acMessageTopic, bMessageValues)
                                    except Exception as E:
                                        logging.info("Error sending a message, error -> %s", E)
                                else:
                                    try:
                                        objBrockerObject.vSend(acMessageTopic, bMessageValues)
                                    except Exception as E:
                                        logging.error("Error sending this message, error -> %s", E)
                    elif acBroker == "ZMQ":
                        objBrockerObject = dctConnectionInfo["ZMQObject"]
                        for acMessageKey, dctMessageInfo in dctConnectionInfo["ZMQMessages"].items():
                            if not _Protocol_class.G_stopThread and not self.bStopSendingThread:
                                acMessageTopic = dctMessageInfo[0]
                                bMessageValues = dctMessageInfo[1]
                                acDelayInSec = dctMessageInfo[2]
                                if acDelayInSec:
                                    try:
                                        time.sleep(float(acDelayInSec))
                                        if _Protocol_class.G_stopThread:
                                            break
                                    except Exception as E:
                                        logging.error("Error with time delay. error -> %s", E)
                                if acConnection in _Protocol_class.G_dctAutoScriptOnlyMQTT_ZMQ_Objects:
                                    try:
                                        self.vSendZmqData(objBrockerObject, acMessageTopic, bMessageValues)
                                    except Exception as E:
                                        logging.info("Error sending ZMQ a message, error -> %s", E)
                                else:
                                    try:
                                        objBrockerObject.vSendZmqDataMainThread(acConnection, acMessageTopic, bMessageValues)
                                    except Exception as E:
                                        logging.error("Error sending ZMQ message, error -> %s", E)
            time.sleep(0.1)

    def objBindZMQPubSoc(self, acIpAddressPar, iPortPar):
    
        """
            Sends zmq message when called.

            Args:
                objBrockerObjectPar (obj): broker object
                acMsgTopicPar (str): message topic

            Returns:

            Raises:
                Raises no exceptions
        """
        objSocket = None
        try:
            objContext = zmq.Context()
            objSocket = objContext.socket(zmq.PUB)
            objSocket.bind("tcp://%s:%s" % (acIpAddressPar, int(iPortPar)))
            return objSocket
        except Exception as E:
            logging.error("Cannot make the ZMQ connection, Error -> %s", E)

        return objSocket

    def vSendZmqData(self, objBrockerObjectPar, acMsgTopicPar, bMessageDataPar):
        """
            Sends zmq message when called.

            Args:
                objBrockerObjectPar (obj): broker object
                acMsgTopicPar (str): message topic
                bMessageDataPar (bytes): message data

            Returns:

            Raises:
                Raises no exceptions
        """
        bTopic = acMsgTopicPar.encode('utf-8')
        if bMessageDataPar == "error":
            logging.error("failed to pack data, please check you data types")
        try:
            objBrockerObjectPar.send_multipart([bTopic, bMessageDataPar], flags=0, copy=True, track=False)
        except Exception as E:
            logging.error("Can not send ZeroMQ message, error -> %s", E)

    def vUnbindPubSoc(self, objZMQSocket, acIpPortKeyPar):
        """
            unbind the socket when this function is called and retun nothing.

            Args:
                objZMQSocket (obj): ZMQ object
                acIpPortKeyPar (str): ZMQ IP and Port

            Returns:

            Raises:
                Raises no exceptions
        """
        acUrlIP, acUrlPort = acIpPortKeyPar.split("_")
        acUrlString = "tcp://" + acUrlIP + ":" + acUrlPort
        objZMQSocket.unbind(acUrlString)
