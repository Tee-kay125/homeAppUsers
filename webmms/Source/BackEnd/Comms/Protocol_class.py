'''
This script generates a Protocol base class (interface) 
which can be inherited by different protocol types

Created on 26/09/2018 

Written by X Frantz
'''
import logging
import socket
import struct
import sys
import os
import glob
import time
from Comms.processing import clsProcessing
import server
from collections import OrderedDict
import json
from logging import handlers
from logging.handlers import RotatingFileHandler
import copy
from enum import Enum

class E_WEBMM_PROCESSES(Enum):
    I_MAIN_PROCESS = 1
    I_AUTOSCRIPT_PROCESS = 2

G_dctJsonFileSender = OrderedDict({"xmls": []})
G_dctJsonFile = OrderedDict({"xmls": []})
G_dctPipes = OrderedDict()
G_dctFavourites = {"messages": []}
G_dctRecordedMessages = OrderedDict()
G_dctFieldAndVal = OrderedDict()  # contains a dictionary of field_name (as key) and  - value (created when adding a pipe)
G_dctFieldAndValReceived = OrderedDict()  # contains a dictionary of field_name (as key) and  - value of received values
G_dctJsonAutoScriptFile = OrderedDict()
G_dctMQTT_ZeroMQ_Connections = OrderedDict() # OrderedDict([('eiuScript', {'MQTT': {'127.0.0.1_1883': {'MQTTObject': <paho.mqtt.client.Client object at 0x7fa916d0ca20>, 'MQTTMessages': {'2_6_1': ['ADCS/EIU/EiuEndOfReadyCmdRsp', b'\x14\x00', '1'], '2_6_1.1': ['ADCS/EIU/EiuEndOfReadyCmdRsp', b'\x14\x00', '1'], '0_6_4': ['ADCS/EIU/EiuStatusReportUnsol', b'\xad\x00\x04\x00', '1']}}}, 'ZMQ': {}})])
G_dctRepeatAutoscriptingParThread = OrderedDict()  # OrderedDict([('127.0.0.1_1883', <paho.mqtt.client.Client object at 0x7fa916d0ca20>)])
G_dctMQTT_ZMQ_Objects = OrderedDict()  # OrderedDict([('127.0.0.1_1883', <paho.mqtt.client.Client object at 0x7fa916d0ca20>)])
G_dctAutoScriptOnlyMQTT_ZMQ_Objects = OrderedDict()  # holds ZMQ and MQTT objects for auto scripting only
G_dctAutoScriptOnlyZMQ_Objects = OrderedDict()  # hold ZMQ objects only
G_stopThread = False
G_lstBusySendingScript = list()  # list of all scripts busy sending
G_dctStopSingleThread = dict()

class clsProtocol:
    def vSend(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def vReceive(self,topicPar, data):
        raise NotImplementedError("Subclass must implement abstract method")

############################ Start of RRS_MMI class ############################
class RRS_MMI(clsProtocol):
    def __init__(self, objClsMqttComms):
        """ 
            Constructor: Instantiate ClsMqttComms objects and clsProcessing object

        Args:
            lstSubscribeTopic (list) : list of message topic.

        Returns:

        Raises:
        """
        self.objClsMqttComms = objClsMqttComms
        self.objClsProcessing = clsProcessing(E_WEBMM_PROCESSES.I_MAIN_PROCESS.value)
        self.lstOfMsgValues = list()    # Holds the payload of the message with a given key
        self.acTypesOfMsgValues = str("") # Holds the pack formart of the message, used for packing data
        self.publishedTopic = str("") # Topic to publish the message to
        self.messageInBytes = str("") #Packed data, ready to send to a node
        self.acHeaderStructUnpackSyntax = "=5H"  # 5 x U2 native standard none
        self.tplResponseMessageHeader = ()
        self.acMsgKey = str("")
        self.tplResponseMessage = tuple()
        self.acXmlSchemaForReceivedMessage = str("")


    def vSend(self, messageKey, acXmlSchemaPar):      

        """ 
            This message uses the message key to get the topic and payload to send data to the node

        Args:
            messageKey (string) : message key
            acXmlSchemaPar (string): xml schema being used

        Returns:

        Raises:
        """
        # Get the payload of the message with a given key
        self.lstOfMsgValues = self.objClsProcessing.lstGetMessageValues(messageKey)
        # Get the pack formart of the message, used for packing data
        self.acTypesOfMsgValues = self.objClsProcessing.acFormatSring(messageKey, acXmlSchemaPar)
        # Get the topic to publish the message to
        self.publishedTopic = self.objClsProcessing.acGetMqttTopic(messageKey)
        # Converts list of values to correct form, ie, string to byte array etc
        self.lstOfMsgValues = self.lstCorrectValues(self.lstOfMsgValues)
        # pack message into bytes
        try:
            self.messageInBytes = struct.pack(self.acTypesOfMsgValues, *self.lstOfMsgValues)
        except Exception as E:
            logging.info("Could not pack message values, error -> %s ", E)

        # vSend to CommsClass
        self.objClsMqttComms.vSend(self.publishedTopic, self.messageInBytes)

    def getLstOfMsgValues(self, messageKey):
        # Get the payload of the message with a given key
        self.lstOfMsgValues = self.objClsProcessing.lstGetMessageValues(messageKey)
        # Converts list of values to correct form, ie, string to byte array etc
        self.lstOfMsgValues = self.lstCorrectValues(self.lstOfMsgValues)
        return self.lstOfMsgValues

    def getPackFormat(self, messageKey, acXmlSchemaPar):
        # Get the pack formart of the message, used for packing data
        self.acTypesOfMsgValues = self.objClsProcessing.acFormatSring(messageKey, acXmlSchemaPar)
        return self.acTypesOfMsgValues

    def vReceive(self, topicPar, data):
        """ This public class method processes the received data into the header tuple and message key.
        It then also gets the response message.

        Args:
            acXmlPathPar (str): Path to the current xml file to be parsed.

        Returns:

        Raises:
            Raises no exceptions
        """

        if (not data):
            logging.error("Parameter data is invalid")
            return

        if (len(data) < 10):
            logging.error("Parameter data is not long enough to at least contain a header")
            return

        # Unpack the header into a tuple
        try:
            self.tplResponseMessageHeader = struct.unpack(self.acHeaderStructUnpackSyntax, data[:10])
        except Exception as E:
            logging.error("Could not unpack header - Exception %s", str(E))
            return

        try:
            if len(topicPar.split("/")) > 3:
                acTopicParRole = "_".join(topicPar.split("/")[3:])
                self.acMsgKey = str(self.tplResponseMessageHeader[4])+'_'+str(self.tplResponseMessageHeader[3])+'_'+str(int(self.tplResponseMessageHeader[1]))+'_'+str(acTopicParRole)
            else:
                self.acMsgKey = str(self.tplResponseMessageHeader[4])+'_'+str(self.tplResponseMessageHeader[3])+'_'+str(int(self.tplResponseMessageHeader[1]))
        except Exception as E:
            logging.error("Could not build up acMsgKey - Exception %s", str(E))
            return
        # Receiving the bytes and then unpacking the data
        try:
            self.tplResponseMessage = self.objClsProcessing.lstGetResponseValues(self.acMsgKey, data)
            if len(self.tplResponseMessage) == 0:
                return
        except Exception as e:
            logging.error("Could not successfully call getResponseValues() - acMsgKey %s - Exception %s", self.acMsgKey, str(e))
            return

        # give all unpacked data to server
        try:
            server.vReceivedMsg(self.acMsgKey, self.tplResponseMessage)
        except Exception as E:
            logging.error("Could not give unpacked data to server, received message %s- Exception %s", str(self.tplResponseMessage), str(E))
            return
        
            
    def lstCorrectValues(self, lstMsgValues):
        """ 
            Takes the list of values from the send function and puts it into the correct format for packing.

        Args:
            lstMsgValues (list) : list of message values.

        Returns:
            lstMsgValues (list)
        Raises:
            Raises no exceptions
        """

        for i in range(len(lstMsgValues)):
            # checks if value in the list is a string
            if isinstance(lstMsgValues[i], str):
                # check if it contains '0x'
                if '0x' in lstMsgValues[i]:
                    new = int(lstMsgValues[i],16)
                    lstMsgValues[i] = new
                try:
                    lstMsgValues[i] = int(lstMsgValues[i])
                except:
                    # converts string to byte array
                    lstMsgValues[i] = (bytes(lstMsgValues[i],'utf-8'))
        return lstMsgValues
