"""-----------------------------------------------------------------------------

Company  : Reutech Radar Systems
Designer : T Ramukosi and X Frantz
Mentor   : J Taylor
Generated: 26/09/2018
--------------------------------------------------------------------------------

Description:

This script extracts various information from the JSON file with the message key
-----------------------------------------------------------------------------"""

import json
import socket
import sys, os
import struct
from random import randint
from collections import OrderedDict
import logging
from Comms import Protocol_class
import copy
from enum import Enum

class E_WEBMM_PROCESSES(Enum):
    I_MAIN_PROCESS = 1
    I_AUTOSCRIPT_PROCESS = 2

class clsProcessing:
    """
        Class to process message data
        Args:
            acProcessTypePar (str): autoscripting and main processes

    """
    def __init__(self, acProcessTypePar):
        self.lstMessageTypes = []
        self.actualLst = []
        self.acFormatString = str("")
        self.iMsgLength = 0
        self.acMsgHeader = str("")
        self.acMqttTopic = str("")
        self.acPayload = str("")
        self.lstMessageValues = list()
        self.lstHeaderValues = list()
        self.dctData = OrderedDict()
        self.dctMsgs = OrderedDict()
        self.acNumberAndType = str()
        self.iNumber = int()
        self.acType = str("")
        self.iNewNumber = int()
        self.acNewValue = str("")
        self.lstSubTopics = list()
        self.lstMsgValues = list()
        self.acTypesOfMsgValues = str("")
        self.btaMessage = bytes()

        self.TypeDict = {
            'ST': 's',
            'CH': 's',
            'I1': 'b',
            'I2': 'h',
            'I4': 'i',
            'I8': 'q',
            'U1': 'B',
            'U2': 'H',
            'U4': 'I',
            'U8': 'Q',
            'F4': 'f',
            'F8': 'd'
        }

        if acProcessTypePar == E_WEBMM_PROCESSES.I_MAIN_PROCESS.value:
            self.dctData = Protocol_class.G_dctJsonFile
            for dctXml in self.dctData['xmls']:
                self.dctMsgs.update(dctXml['Messages'])
        elif acProcessTypePar == E_WEBMM_PROCESSES.I_AUTOSCRIPT_PROCESS.value:
            self.dctData = Protocol_class.G_dctJsonAutoScriptFile
            self.dctMsgs.update(self.dctData)
        
    def btaGetPackedMessage(self, acMessageKeyPar, acXmlSchemaPar):
        """ this method packs message data and return the bytes.

            Args:
                acMessageKeyPar (str): message key
                acXmlSchemaPar (str): xml schema being used

            Returns:
                self.btaMessage (bytes): packed message
            Raises:
                Raises no exceptions
        """

        self.acFormatString = str("")
        self.lstMessageTypes = list()
        self.lstHeaderValues = list()
        self.lstMessageValues = list()
        # Get the payload of the message with a given key
        self.lstMsgValues = self.lstGetMessageValues(acMessageKeyPar)
        # Converts list of values to correct form, ie, string to byte array etc
        self.lstMsgValues = self.lstCorrectValues(self.lstMsgValues)
        # Get the pack formart of the message, used for packing data
        self.acTypesOfMsgValues = self.acFormatSring(acMessageKeyPar, acXmlSchemaPar)
        # pack message into bytes
        try:
            self.btaMessage = struct.pack(self.acTypesOfMsgValues, *self.lstMsgValues)
        except Exception as E:
            logging.error("Could not pack message values, error -> %s ", E)

        return self.btaMessage

    def btaGetPackedMessageAutoScripting(self, acMessageKeyPar, acXmlSchemaPar, acScriptNamePar):
        """ this method packs message data for auto scripting and return the bytes.

            Args:
                acMessageKeyPar (str): message key
                acXmlSchemaPar (str): xml schema being used
                acScriptNamePar (str): script name

            Returns:
                self.btaMessage (bytes): packed message
            Raises:
                Raises no exceptions
        """
        self.acFormatString = str("")
        self.lstMessageTypes = list()
        self.lstHeaderValues = list()
        self.lstMessageValues = list()
        # Get the payload of the message with a given key
        self.lstMsgValues = self.lstGetMessageValuesAutoScripting(acMessageKeyPar, acScriptNamePar)
        # Converts list of values to correct form, ie, string to byte array etc
        self.lstMsgValues = self.lstCorrectValues(self.lstMsgValues)
        # Get the pack formart of the message, used for packing data
        self.acTypesOfMsgValues = self.acFormatStringAutoScripting(acMessageKeyPar, acXmlSchemaPar, acScriptNamePar)
        # pack message into bytes
        try:
            self.btaMessage = struct.pack(self.acTypesOfMsgValues, *self.lstMsgValues)
        except Exception as E:
            logging.error("Could not pack message values, error -> %s ", E)

        return self.btaMessage

    def lstCorrectValues(self, lstMsgValuesPar):
        """ this method converts hex to decimal values.

            Args:
                lstMsgValuesPar (list): message list

            Returns:
                lstMsgValuesPar (list): packed message
            Raises:
                Raises no exceptions
        """
        for i in range(len(lstMsgValuesPar)):
            # checks if value in the list is a string
            if isinstance(lstMsgValuesPar[i], str):
                # check if it contains '0x'
                if '0x' in lstMsgValuesPar[i]:
                    new = int(lstMsgValuesPar[i],16)
                    lstMsgValuesPar[i] = new
                try:
                    lstMsgValuesPar[i] = int(lstMsgValuesPar[i])
                except:
                    # converts string to byte array
                    lstMsgValuesPar[i] = (bytes(lstMsgValuesPar[i],'utf-8'))
        return lstMsgValuesPar

    def acFormatSring(self, acMessageKeyPar, acXmlSchemaPar):
        """ this method gets the list of all fields types on a message and join them to make a
            pack format.

            Args:
                acMessageKeyPar (str): message key
                acXmlSchemaPar (str): xml schema being used

            Returns:
                string of pack format
            Raises:
                Raises no exceptions
        """

        # lstMsgPayload = list()
        for acMsg in self.dctMsgs:
            if acMsg == acMessageKeyPar:
                try:
                    self.acFormatString = self.dctMsgs[acMsg]['payloadtypes']
                except Exception as E:
                    logging.error("Could not Join the pack format, error -> %s", E)
        if(acXmlSchemaPar == "BR12"):
            return "=5H" + self.acFormatString
        else:
            return "=6HQH" + self.acFormatString
    
    def acFormatStringAutoScripting(self, acMessageKeyPar, acXmlSchemaPar, acScriptNamePar):
        """ this method gets the list of all fields types on a message and join them to make a
            pack format.

            Args:
                acMessageKeyPar (str): message key
                acXmlSchemaPar (str): xml schema being used
                acScriptNamePar (str): script name

            Returns:
                string of pack format
            Raises:
                Raises no exceptions
        """
        for acScriptName, dctScriptInfo in self.dctMsgs.items():
            if acScriptName == acScriptNamePar:
                for acMsg, dctMsgInfo in dctScriptInfo.items():
                    if acMsg == acMessageKeyPar:
                        try:
                            self.acFormatString = self.dctMsgs[acScriptName][acMsg]['payloadtypes']
                        except Exception as E:
                            logging.error("Could not Join the pack format, error -> %s", E)
        if(acXmlSchemaPar == "BR12"):
            return "=5H" + self.acFormatString
        else:
            return "=6HQH" + self.acFormatString

    def lstGetSubMqttTopic(self, acMessageKeyPar):
        """ this method compares the module address passed and that of messages on the xml,
            and subscribe to all messages with  the same midule address as the message key passed

            Args:
                acMessageKeyPar (str): message key
            Returns:
                self.lstSubTopics (list): list of messgae topics to subscribe to
            Raises:
                Raises no exceptions
        """
        acModuleAddress = str("")
        acModAdd = str("")
        acMqttTopic = str("")
        acModuleAddress = acMessageKeyPar.split('_')[1]

        # Check for the module address we are interested in the dict       
        for acMsg in self.dctMsgs:
            acModAdd = acMsg.split('_')[1]
            if acModuleAddress == acModAdd:
                if self.dctMsgs[acMsg]['Individual_Message_Protocol'] == "MQTT" and self.dctMsgs[acMsg]['pubSub_tag_Sub'] == "Subscribe":
                    acMqttTopic = self.dctMsgs[acMsg]['Msg_Topic_Sub']
                    self.lstSubTopics.append(acMqttTopic)
        return self.lstSubTopics

    def lstGetSubZMQTopic(self, acMessageKeyPar):
        """ this method compares the module address passed and that of messages on the xml,
            and subscribe to all messages with  the same midule address as the message key passed

            Args:
                acMessageKeyPar (str): message key
            Returns:
                self.lstSubTopics (ist): list of messgae topics to subscribe to
            Raises:
                Raises no exceptions
        """
        acModuleAddress = str("")
        acModAdd = str("")
        acZMQTopic = str("")
        acModuleAddress = acMessageKeyPar.split('_')[1]

        # Check for the module address we are interested in the dict       
        for acMsg in self.dctMsgs:
            acModAdd = acMsg.split('_')[1]
            if acModuleAddress == acModAdd:
                if self.dctMsgs[acMsg]['Individual_Message_Protocol'] == "ZMQ" and self.dctMsgs[acMsg]['pubSub_tag_Sub'] == "Subscribe":
                    acZMQTopic = self.dctMsgs[acMsg]['Msg_Topic_Sub']
                    if acZMQTopic in self.lstSubTopics:
                        pass
                    else:
                        self.lstSubTopics.append(acZMQTopic)
        return self.lstSubTopics

    def acGetMqttTopic(self, acMessageKeyPar):
        """ this method return the topic to publish the message to

            Args:
                acMessageKeyPar (str): message key
            Returns:
                self.acMqttTopic (str): mqtt message topic
            Raises:
                Raises no exceptions
        """
        for acMsg in self.dctMsgs:
            if acMsg == acMessageKeyPar:
                self.acMqttTopic = self.dctMsgs[acMsg]['Msg_Topic']            
        return self.acMqttTopic

    def lstRecursiveGetPayloadValues(self, lstPayloadPar):
        """ this method is used to recursively get values of all fields in the payload

            Args:
                lstPayloadPar (list) = message payload

            Returns:
                self.lstMessageValues (list): values of a payload
            Raises:
                This function throw an exception
        """

        if type(lstPayloadPar) == list:
            for field in lstPayloadPar:
                if 'enumType' not in field and 'value' not in field:
                    self.lstRecursiveGetPayloadValues((field['members']))
                elif 'enumType' not in field and 'value' in field:
                    if field['type'] == 'ST':
                        self.lstMessageValues.append(str(field['value']).encode('utf-8'))
                    elif field['type'] == 'CH':
                        self.lstMessageValues.append(str(field['value']).encode('utf-8'))
                    elif field['type'] == 'F4':
                        self.lstMessageValues.append(float(field['value']))
                    elif field['type'] == 'F8':
                        self.lstMessageValues.append(float(field['value']))
                    else:
                        self.lstMessageValues.append(int(field['value']))
                elif 'enumType' in field:
                    if field['type'] == 'ST':
                        self.lstMessageValues.append(str(field['value']).encode('utf-8'))
                    elif field['type'] == 'CH':
                        self.lstMessageValues.append(str(field['value']).encode('utf-8'))
                    elif field['type'] == 'F4':
                        self.lstMessageValues.append(float(field['value']))
                    elif field['type'] == 'F8':
                        self.lstMessageValues.append(float(field['value']))
                    else:
                        self.lstMessageValues.append(int(field['value']))

        return self.lstMessageValues

    def lstGetHeaderValues(self, dctMsgHeaderPar):
        """ this method is used to get the values of the header

            Args:
                dctMsgHeaderPar (dict) = message header

            Returns:
                self.lstHeaderValues (list): values of a header
            Raises:
                Raises no exceptions
        """
        for acKey, iVal in dctMsgHeaderPar.items():
            try:
                self.lstHeaderValues.append(int(iVal))
            except Exception as E:
                logging.error("Could not append field value to a lstHeaderValues, error -> %s", E)           
        return self.lstHeaderValues        

    def lstGetMessageValues(self, acMessageKeyPar):
        """ this method gets the values of the message, header + payload

            Args:
                acMessageKeyPar (str) = message key

            Returns:
                lstMessageValues (list) : list of values (message header + payload)
            Raises:
                Raises no exceptions
        """
        lstMessageValues = list()
        fileData = OrderedDict()
        dctMsgs = OrderedDict()
        dctMsgHeader = OrderedDict()
        dctPayload = OrderedDict()
        fileData = OrderedDict()

        fileData = copy.deepcopy(Protocol_class.G_dctJsonFileSender)

        for xml in fileData['xmls']:
            dctMsgs.update(xml['Messages'])

        for keyMsg, ValMsg in dctMsgs.items():
            if keyMsg == acMessageKeyPar:
                dctMsgHeader = ValMsg['Header']
                dctPayload = ValMsg['Payload']
        try:
            lstMessageValues = self.lstGetHeaderValues(dctMsgHeader) + self.lstRecursiveGetPayloadValues(dctPayload)
        except Exception as E:
            logging.error("Couldn't join the header and payload values, error -> %s",E)

        return lstMessageValues

    def lstGetMessageValuesAutoScripting(self, acMessageKeyPar, acScriptNamePar):
        """ this method gets the values of the message, header + payload

            Args:
                acMessageKeyPar (str): message key
                acScriptNamePar (str): Script name

            Returns:
                lstMessageValues (list) : list of values (message header + payload)
            Raises:
                Raises no exceptions
        """
        lstMessageValues = list()
        dctMsgs = OrderedDict()
        dctMsgHeader = OrderedDict()
        dctPayload = OrderedDict()

        dctMsgs = copy.deepcopy(Protocol_class.G_dctJsonAutoScriptFile)

        for acScriptName, scriptInfo in dctMsgs.items():
            if acScriptName == acScriptNamePar:
                for acKeyMsg, ValMsg in scriptInfo.items():
                    if acKeyMsg == acMessageKeyPar:
                        dctMsgHeader = ValMsg['Header']
                        dctPayload = ValMsg['Payload']
        try:
            lstMessageValues = self.lstGetHeaderValues(dctMsgHeader) + self.lstRecursiveGetPayloadValues(dctPayload)
        except Exception as E:
            logging.error("Couldn't join the header and payload values, error -> %s", E)

        return lstMessageValues

    def lstGetResponseValues(self, acMsgKey, btaDataPar):

        """ this method unpack the bytes received

            Args:
                acMsgKey (str) = message key
                btaDataPar (bytes)    = received data

            Returns:
                [tplResponseMessage,acXmlSchema] (list) : list of values (message header + payload) and xmlSChema
            Raises:
                Raises no exceptions
        """

        lstMessageTypes = list()
        lstJsonStructure = Protocol_class.G_dctJsonFile

        acMsgTypes = str("")
        acMsgTypesPack = str("")
        acXmlSchema = str("")
        tplResponseMessage = tuple()
        bMsgKeyCounter = False
        for iXmlIndex, dctXmls in enumerate(lstJsonStructure['xmls']):
            for acConnectionMessage, dctMsgInfo in dctXmls.items():
                if acConnectionMessage == "Messages":
                    if acMsgKey in dctMsgInfo:
                        for acMessageKey, dctMessageValues in dctMsgInfo.items():
                            if acMessageKey == acMsgKey:
                                bMsgKeyCounter = True
                                acXmlSchema = lstJsonStructure['xmls'][iXmlIndex]['Connection']['xmlSchema']
                                lstMessageTypes = dctMsgInfo[acMsgKey]['payloadtypes']
                                break

        acMsgTypes = ''.join(lstMessageTypes)

        if bMsgKeyCounter == False:
            return list()
        if(acXmlSchema == "BR12"):
            acMsgTypesPack = '=5H'+acMsgTypes
        else:
            acMsgTypesPack = '=6HQH'+acMsgTypes
        try:
            tplResponseMessage = struct.unpack(acMsgTypesPack, btaDataPar)
        except Exception as E:
            logging.error("Cant unpack data, error -> %s, given %s", E,len(btaDataPar))

        return [tplResponseMessage,acXmlSchema]