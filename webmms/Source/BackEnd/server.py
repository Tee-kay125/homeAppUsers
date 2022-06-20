#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""This module is the WebMM process.

Description:

Server, it serves files to the browser

Company  : Reutech Radar Systems
Designer : T Ramukosi
Mentor   : J Taylor
Generated: 2018-08-30


Additional changes: Emile Rossouw

Example:
    To run this file do the following:

        $ export FLASK_APP=server.py
        $ flask run

    To set the host and port one can call:   Note!!! the shebang will be used to determine which python to use

        $ flask run --host=0.0.0.0 --port=5000

    If the shebang is to be ignored one can can say:

        $ python3.6 -m flask run --host=0.0.0.0 --port=5000

Debugging tips:

    One can debug this module in vscode by setting the lauch parameters to:

    "program": "",
    "args": ["-m", "flask","run","--host=0.0.0.0","--port=5000"],
    "cwd": "${workspaceRoot}/",

    The shebang is also important so that vscode knows which Python to call.

Todo:

"""


import sys, os, signal
import json
import urllib
import time
import platform
import logging
import queue
import threading

from Codegen.Codegen_Python import generate_Json
from Codegen.Codegen_Python import autogen_common_types
from Comms import Protocol_class as _Protocol_class
from Comms import zmq_manager as _zmq_manager
from Comms.Protocol_class import clsProcessing
from Comms.mqtt_manager import clsMqttManager
from Comms.comms_manager import clsCommsManager, clsMqttComms
from Comms.zmq_manager import clsZMQ_Manager
from Comms.auto_scripting import clsMessageObjects
from Comms.getIsDatabaseMessages import clsGetIsDatabaseMessages
import createCSV
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.datastructures import ImmutableMultiDict
from collections import OrderedDict
import clVariables
import copy
# Import the logger manager class so that we can create a logger
from Logging import logging_manager
from enum import Enum

app = Flask(__name__, static_url_path='/static')

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

dctMqttObj = {}
dctObjClsMqttComms = {}
dctFieldVal = {}
dctReceivedFieldVal = {}
G_dctZeroMQPubObjects = OrderedDict()
objMQTTQueue = queue.Queue()
G_dctActivePipes = OrderedDict()
G_dctChangedFields = OrderedDict()
G_dctDatabaseMessages = OrderedDict()

class E_WEBMM_PROCESSES(Enum):
    I_MAIN_PROCESS = 1
    I_AUTOSCRIPT_PROCESS = 2

@app.route("/")
def lstHome():
    '''
        This function is for home/default url, this function is called
        when you open a message manager and when you request a home url

        it read the SICD directory and return a list of xmls from the dir

        Args:

        Returns:
                xmlFiles (list) list of all xmls in the SICD directory
        Raises:
            Raises no exceptions
    '''
    xmlPath = os.path.join(os.path.dirname(__file__), "./SICD/")
    xmlFiles = os.listdir(xmlPath)
    lstXmls = []
    for i in range(len(xmlFiles)):
        if xmlFiles[i].endswith('.xml'):
            lstXmls.append(xmlFiles[i])

    return render_template('home.html', lstXmls=xmlFiles)

@app.route("/<name>")
def acViewMsg(name):
    '''
        this function takes the url name and return results according to the url name

        results returned are json files holding messages, pipes, fav messages etc.

        Args:

        Returns:
            (string)
        Raises:
            Raises no exceptions
    '''
    jsonPipes = OrderedDict()
    jsonXmls = list()
    jsonInterfaceXmls = list()
    dctCheckedMessages = OrderedDict()
    dctReceivedFieldVal = OrderedDict()
    dctRecordingMsgs = OrderedDict()
    dctRecordedMsgs = OrderedDict()
    global G_dctChangedFields

    if name == 'output.json':
        """
            This condition is called whenever a web interface is refreshed and the entire json has to be passed to the interface, and
            when a message is opened for iterating through structure when populating fields.
        """
        try:
            return json.dumps([_Protocol_class.G_dctJsonFileSender, _Protocol_class.G_dctJsonFile, _Protocol_class.G_dctJsonAutoScriptFile])
        except Exception as E:
            logging.error("Could not get json file, error -> %s", E)
            return "error"
    if name.startswith("fieldVals"):
        """
            This condition is True when you opened a message and field values have to be updated,
            it compares values existing with received values and return the difference.
        """
        try:
            dctFieldAndValTmp = copy.deepcopy(_Protocol_class.G_dctFieldAndVal) # variable described in protocol class
            dctFieldAndValReceivedTmp = copy.deepcopy(_Protocol_class.G_dctFieldAndValReceived) # variable described in protocol class

            setDctFieldAndValTmp = set(dctFieldAndValTmp.items())
            setDctFieldAndValReceivedTmp = set(dctFieldAndValReceivedTmp.items())

            dctChangedFields = OrderedDict(setDctFieldAndValReceivedTmp - setDctFieldAndValTmp)
            if dctChangedFields != {}:
                G_dctChangedFields = copy.deepcopy(dctChangedFields)

            _Protocol_class.G_dctFieldAndVal = copy.deepcopy(_Protocol_class.G_dctFieldAndValReceived)

        except Exception as E:
            return "error"
        
        try:
            return json.dumps(G_dctChangedFields)
        except Exception as E:
            logging.error("Could not get field values, error -> %s", E)
            return "error" 
    elif name == 'pipes.json':
        try:
            dctSavedPpes = OrderedDict()
            with open(os.path.join(os.path.dirname(__file__),"./Structure/pipes.json"), 'r') as f:
                dctSavedPpes = OrderedDict(json.load(f))
                f.close()
            return json.dumps(dctSavedPpes)
        except Exception as E:
            logging.error("Could not get pipes, error -> %s", E)
            return "error"
    elif name == "activePipe":
        try:
            jsonPipes = json.dumps(G_dctActivePipes)
            return jsonPipes
        except Exception as E:
            logging.error("Could not get pipes, error -> %s", E)
            return "error"
    elif name == 'xmls.json':
        try:
            jsonXmls = json.dumps(generate_Json.getXmls())
            return jsonXmls
        except Exception as E:
            logging.error("Could not get xmls, error -> %s", E)
            return "error"
    elif name == 'interface.json':
        try:
            jsonInterfaceXmls = json.dumps(generate_Json.getInterfaceXmls())
            return jsonInterfaceXmls
        except Exception as E:
            logging.error("Could not get the interface xmls, error -> %s", E)
            return "error"        
    elif name == 'dctReceivedMessages':
        try:
            dctReceivedMessages = json.dumps(clVariables.G_dctReceivedMessages)
            return dctReceivedMessages
        except Exception as E:
            logging.error("Could not get received messages, error -> %s", E)
            return "error"
    elif name == 'favMsgs.json':
        try:
            dctCheckedMessages = json.dumps(generate_Json.getCheckedMsgs())
            return dctCheckedMessages
        except Exception as E:
            logging.error("Could not get checked messages, error -> %s", E)
            return "error"        
    elif name == 'newTab':
        return render_template('newTab.html')
    elif name == 'databasePage':
        return render_template('database.html')
    elif name == 'getLog':
        try:
            MsgLog = generate_Json.getLog()
            return MsgLog
        except Exception as E:
            logging.error("Could not get log, error -> %s", E)
            return "error"
    elif name == 'getLog.txt':
        try:
            MsgLog = generate_Json.getLog()
            return MsgLog
        except Exception as E:
            logging.error("Could not get log, error -> %s", E)
            return "error"
    elif name == 'log':
        return render_template('log.html')
    elif name == 'dctFieldVal':
        try:
            dctReceivedFieldVal = json.dumps(generate_Json.getdctFieldVal())
            return dctReceivedFieldVal
        except Exception as E:
            logging.error("Could not get field values, error -> %s", E)
            return "error"
    elif name == 'getRecord':
        try:
            dctRecordingMsgs = json.dumps(generate_Json.getRecordingMsgs())
            return dctRecordingMsgs
        except Exception as E:
            logging.error("Could not get field recording messages, error -> %s", E)
            return "error"
    elif name == 'getRecordedMessages':
        try:
            dctRecordedMsgs = json.dumps(generate_Json.getRecordedMessages())
            return dctRecordedMsgs
        except Exception as E:
            logging.error("Could not get field recorded messages, error -> %s", E)
            return "error"     
    elif name[:8] == 'download':
        fileName = name[8:]
        msg = generate_Json.downloadFile(fileName)
        return msg
    elif name[:11] == 'csvDownload':
        fileName = name[11:]
        msg = generate_Json.downloadCsvFile(fileName)
        return msg
    elif name == 'recordIcon':
        return "static/images/Record.png"
    elif name == 'getCommonTypes':
        autogen_common_types.vGetCommonTypes()
        return json.dumps(autogen_common_types.G_dctADCS_common_types)

    return render_template('home.html')

def vReadDatabaseDirectory():
    """
        This function read database directory and assign all meessages from files to dictionary

        Args:
            
        Returns:
            
        Raises:
            Raises no exceptions
    """

    global G_dctDatabaseMessages

    G_dctDatabaseMessages = dict()

    acPathToDatabaseFolder = os.path.join(os.path.dirname(__file__), "databaseFiles/")
    lstFiles = os.listdir(acPathToDatabaseFolder)
    try:
        for i in range(len(lstFiles)):
            if lstFiles[i] != ".gitignore":
                with open(os.path.join(os.path.dirname(__file__),acPathToDatabaseFolder+"/"+lstFiles[i]), 'r') as f:
                    G_dctDatabaseMessages[lstFiles[i][:-5]] = OrderedDict(json.load(f))
                    f.close()
    except Exception as E:
        logging.info("Unable to open the database directory: %s", E)

@app.route("/reloadDatabaseImport", methods=['POST', 'GET'])
def vReloadDatabaseImport():
    """
        This function read database directory and assign all meessages from files to dictionary

        Args:
            
        Returns:
            (string): string message on complete
            
        Raises:
            Raises no exceptions
    """

    vReadDatabaseDirectory()
    
    return "done"

@app.route("/getDatabaseMessage", methods=['POST', 'GET'])
def dctGetDatabaseMessage():
    """
        return database messages on ajax get call

        Args:
            
        Returns:
            G_dctDatabaseMessages (dict): database messages
        Raises:
            Raises no exceptions
    """

    global G_dctDatabaseMessages
    return json.dumps(G_dctDatabaseMessages)

@app.route("/deleteFile", methods=['POST', 'GET'])
def vDeleteFile():
    """
        return database messages on ajax get call

        Args:
            
        Returns:
            (string): string message on complete
        Raises:
            Raises no exceptions
    """

    dctData = request.values
    dctData = ImmutableMultiDict(dctData).to_dict()
    acFileName = dctData["fileName"].split("__")[1]
    
    try:
        acPathToGenFolder = os.path.join(os.path.dirname(__file__), "./databaseFiles/")
        os.remove(acPathToGenFolder+acFileName+".json")
    except Exception as E:
        logging.error("Error deleting a file, error -> %s", E)

    vReadDatabaseDirectory()

    return "file Deleted"

@app.route("/updateDictionary", methods=['POST', 'GET'])
def acUpdateMessage():
    """
        This function update databse message values

        Args:
            
        Returns:
            (string): string message on complete
        Raises:
            Raises no exceptions
    """

    global G_dctDatabaseMessages

    dctData = request.values
    dctData = ImmutableMultiDict(dctData).to_dict()

    for acValuePath, actualValue in dctData.items():
        lstPathToValue = acValuePath.split("__")
        if len(lstPathToValue) == 5:
            G_dctDatabaseMessages[lstPathToValue[0]][lstPathToValue[1]][lstPathToValue[2]]["dctMessagePayload"]["Attr"][int(lstPathToValue[3])][lstPathToValue[4]] = actualValue
        elif len(lstPathToValue) == 6:
            G_dctDatabaseMessages[lstPathToValue[0]][lstPathToValue[1]][lstPathToValue[2]]["dctMessagePayload"]["Attr"][int(lstPathToValue[3])]["Attr"]["Attr"][int(lstPathToValue[4])][lstPathToValue[5]] = actualValue
        elif len(lstPathToValue) == 7:
            G_dctDatabaseMessages[lstPathToValue[0]][lstPathToValue[1]][lstPathToValue[2]]["dctMessagePayload"]["Attr"][int(lstPathToValue[3])]["Attr"]["Attr"][int(lstPathToValue[4])]["Attr"]["Attr"][int(lstPathToValue[5])][lstPathToValue[6]] = actualValue
        elif len(lstPathToValue) == 8:
            G_dctDatabaseMessages[lstPathToValue[0]][lstPathToValue[1]][lstPathToValue[2]]["dctMessagePayload"]["Attr"][int(lstPathToValue[3])]["Attr"]["Attr"][int(lstPathToValue[4])]["Attr"]["Attr"][int(lstPathToValue[5])]["Attr"]["Attr"][int(lstPathToValue[6])][lstPathToValue[7]] = actualValue
        elif len(lstPathToValue) == 9:
            G_dctDatabaseMessages[lstPathToValue[0]][lstPathToValue[1]][lstPathToValue[2]]["dctMessagePayload"]["Attr"][int(lstPathToValue[3])]["Attr"]["Attr"][int(lstPathToValue[4])]["Attr"]["Attr"][int(lstPathToValue[5])]["Attr"]["Attr"][int(lstPathToValue[6])]["Attr"]["Attr"][int(lstPathToValue[7])][lstPathToValue[8]] = actualValue
        elif len(lstPathToValue) == 10:
            G_dctDatabaseMessages[lstPathToValue[0]][lstPathToValue[1]][lstPathToValue[2]]["dctMessagePayload"]["Attr"][int(lstPathToValue[3])]["Attr"]["Attr"][int(lstPathToValue[4])]["Attr"]["Attr"][int(lstPathToValue[5])]["Attr"]["Attr"][int(lstPathToValue[6])]["Attr"]["Attr"][int(lstPathToValue[7])]["Attr"]["Attr"][int(lstPathToValue[8])][lstPathToValue[9]] = actualValue
        elif len(lstPathToValue) == 11:
            G_dctDatabaseMessages[lstPathToValue[0]][lstPathToValue[1]][lstPathToValue[2]]["dctMessagePayload"]["Attr"][int(lstPathToValue[3])]["Attr"]["Attr"][int(lstPathToValue[4])]["Attr"]["Attr"][int(lstPathToValue[5])]["Attr"]["Attr"][int(lstPathToValue[6])]["Attr"]["Attr"][int(lstPathToValue[7])]["Attr"]["Attr"][int(lstPathToValue[8])]["Attr"]["Attr"][int(lstPathToValue[9])][lstPathToValue[10]] = actualValue
        elif len(lstPathToValue) == 12:
            G_dctDatabaseMessages[lstPathToValue[0]][lstPathToValue[1]][lstPathToValue[2]]["dctMessagePayload"]["Attr"][int(lstPathToValue[3])]["Attr"]["Attr"][int(lstPathToValue[4])]["Attr"]["Attr"][int(lstPathToValue[5])]["Attr"]["Attr"][int(lstPathToValue[6])]["Attr"]["Attr"][int(lstPathToValue[7])]["Attr"]["Attr"][int(lstPathToValue[8])]["Attr"]["Attr"][int(lstPathToValue[9])]["Attr"]["Attr"][int(lstPathToValue[10])][lstPathToValue[11]] = actualValue
        elif len(lstPathToValue) == 13:
            G_dctDatabaseMessages[lstPathToValue[0]][lstPathToValue[1]][lstPathToValue[2]]["dctMessagePayload"]["Attr"][int(lstPathToValue[3])]["Attr"]["Attr"][int(lstPathToValue[4])]["Attr"]["Attr"][int(lstPathToValue[5])]["Attr"]["Attr"][int(lstPathToValue[6])]["Attr"]["Attr"][int(lstPathToValue[7])]["Attr"]["Attr"][int(lstPathToValue[8])]["Attr"]["Attr"][int(lstPathToValue[9])]["Attr"]["Attr"][int(lstPathToValue[10])]["Attr"]["Attr"][int(lstPathToValue[11])][lstPathToValue[12]] = actualValue
        
    return "done"

@app.route("/exportMessageBlock", methods=['POST', 'GET'])
def acExportMessageBlock():
    """
        This function saves message to file from memory

        Args:
            
        Returns:
            (string): string message on complete
        Raises:
            Raises no exceptions
    """

    global G_dctDatabaseMessages

    dctData = request.values
    dctData = ImmutableMultiDict(dctData).to_dict()
    acExportFileName = dctData["fileName"]
    
    acFilePath = "databaseFiles/"+acExportFileName+".json"
    try:
        with open(os.path.join(os.path.dirname(__file__), acFilePath), 'w') as f:
            f.write(json.dumps(G_dctDatabaseMessages[acExportFileName]))
            f.close()
    except Exception as E:
        logging.error("Unable to open the database file: %s", E)

    return "done"

@app.route("/CreateDatabase", methods=['POST', 'GET'])
def CreateDatabase():
    """
        This function saves message to file from memory

        Args:
            
        Returns:
            (string): string message on complete
        Raises:
            Raises no exceptions
    """
    dctData = request.values
    dctData = ImmutableMultiDict(dctData).to_dict()
    
    acDatabaseFileName = dctData["databaseFileName"]
    lstXmls = list()
    
    for key, value in dctData.items():
        if key != "databaseFileName":
            lstXmls.append(value)

    objGetIsDatabaseMessages = clsGetIsDatabaseMessages()
    objGetIsDatabaseMessages.vGetCommonTypes()
    objGetIsDatabaseMessages.vGetMessages(acDatabaseFileName, lstXmls)

    return "saved"

@app.route("/CreateDatabaseAll", methods=['POST', 'GET'])
def CreateDatabaseAll():
    """
        This function saves message to file from memory

        Args:
            
        Returns:
            (string): string message on complete
        Raises:
            Raises no exceptions
    """
    dctData = request.values
    dctData = ImmutableMultiDict(dctData).to_dict()
    
    acDatabaseFileName = dctData["databaseFileName"]

    objGetIsDatabaseMessages = clsGetIsDatabaseMessages()
    objGetIsDatabaseMessages.vGetCommonTypes()
    objGetIsDatabaseMessages.vGetAllMessages(acDatabaseFileName)

    return "saved"

@app.route("/pipes_config", methods=['POST', 'GET'])
def dctPipesConfig():
    """
        This function opens saved pipes directory and return files contained inside it.

        Args:

        Returns:
            dctSavedPipes (dict): saved pipes in json format.
        Raises:
            Raises no exceptions
    """
    acPathToGenFolder = os.path.join(os.path.dirname(__file__), "./pipes_config/")
    lstFiles = os.listdir(acPathToGenFolder)

    dctSavedPipes = OrderedDict()

    try:
        for i in range(len(lstFiles)):
            if lstFiles[i][-5:] == ".json":
                with open(os.path.join(os.path.dirname(__file__),acPathToGenFolder+"/"+lstFiles[i]), 'r') as f:
                    dctSavedPipes.update(OrderedDict(json.load(f)))
                    f.close()
    except Exception as E:
        logging.info("Unable to open the pipes config directory: %s", E)

    return json.dumps(dctSavedPipes)

@app.route("/connectPipe", methods=['POST', 'GET'])
def acConnectPipe():
    """
        This function is called everytime you connect a new pipe,
        It take textField values including xmls and pass them to autogen File to
        autogenerate the xmls, creating pipes and adding to main jsonFile

        Args:

        Returns:
            (string)
        Raises:
            Raises no exceptions
    """
    global G_dctZeroMQPubObjects
    acPathToGenFolder = os.path.join(os.path.dirname(__file__), "./Codegen/Codegen_Python/Generated_Python/")
    lstFiles = os.listdir(acPathToGenFolder)
    for i in range(len(lstFiles)):
        if lstFiles[i].endswith('MsgDef.py') or lstFiles[i].endswith('TypeDef.py'):
            os.remove(acPathToGenFolder+lstFiles[i])

    dctData = request.values
    dctData = ImmutableMultiDict(dctData).to_dict()
    acPipeName = str("")
    acMQTTRemoteIP = str("")
    acMQTTPort = str("")
    acZeroMQRemoteIP = str("")
    acZeroMQPort = str("")
    acZeroMQRemoteIPPub = str("")
    acZeroMQPortPub = str("")
    acPubSubTagSwap = str("")
    acPubSubTagSwapPipe = str("")
    acOld_xml_Schema = str("")
    lstXmlSchema = list()
    lstXmls = list()
    lstSystemName = list()
    lstDestination = list()
    lstSubTopic = list()
    lstInterfaceXmls = list()
    dctNewPipe = OrderedDict()
    
    for fieldname, val in dctData.items():
        if fieldname == 'pipe':
            acPipeName = val
        elif fieldname == 'MQTTRemoteIP':
            acMQTTRemoteIP = val
        elif fieldname == 'MQTTPort':
            acMQTTPort = val
        elif fieldname == 'ZeroMQRemoteIP':
            acZeroMQRemoteIP = val
        elif fieldname == 'ZeroMQPort':
            acZeroMQPort = val
        elif fieldname == 'ZeroMQRemoteIPPub':
            acZeroMQRemoteIPPub = val
        elif fieldname == 'ZeroMQPortPub':
            acZeroMQPortPub = val
        elif fieldname.startswith('schema'):	
            lstXmlSchema.append(val)
        elif fieldname.startswith('xml'):
            if val in lstXmls:
                logging.error("Can not add %s on webMM two times", val)
                return "Can not add "+val+" on webMM two times"
            else:
                lstXmls.append(val)
        elif fieldname.startswith('SystemName'):
            lstSystemName.append(val)
            lstSubTopic.append(val)
        elif fieldname.startswith('Destination'):
            lstDestination.append(val)
            lstSubTopic.append(val)
        elif fieldname.startswith('Interface'):
            lstInterfaceXmls.append(val)
        elif fieldname.startswith('pubSubTagSwap'):
            acPubSubTagSwap = val
        elif fieldname == 'acXmlSchema':
            acOld_xml_Schema = val
    
    for active_xml in _Protocol_class.G_dctJsonFileSender["xmls"]:
        tmpActiveXml = active_xml["Connection"]["xmlFile"][:-7] + ".xml"
        tmpPipeName = active_xml["Connection"]["PipeName"]
        if tmpActiveXml in lstXmls:
            logging.error(" %s is already active on webMM", tmpActiveXml)
            return "xml '"+ tmpActiveXml+"' is already connected on webMM"
        if tmpPipeName == acPipeName:
            logging.error(" %s is already active on webMM", tmpPipeName)
            return "Pipe name '"+ tmpPipeName+"' is already connected on webMM"

    if "pubSubTagSwap" in dctData:
        acPubSubTagSwapPipe = "on"
    else:
        acPubSubTagSwapPipe = "off"

    dctNewPipe.update({"swap_mic_pub_sub":acPubSubTagSwapPipe,"xml_schema":acOld_xml_Schema,"xmls":lstXmls,"mic":lstInterfaceXmls})

    if "useMQTT" in dctData:
        
        dctNewPipe.update({"mqtt_pub_sub":[acMQTTRemoteIP,acMQTTPort]})

        try:
            objMqtt = clsMqttManager(acMQTTRemoteIP,int(acMQTTPort)) # give publish topic to Comms
            bConnectStatus = objMqtt.G_bOnConnectFlag
            if bConnectStatus == True:
                objectKey = str(acMQTTRemoteIP)+'_'+str(acMQTTPort)
                _Protocol_class.G_dctMQTT_ZMQ_Objects.update({objectKey:objMqtt})
                logging.info("******************* Connected to the MQTT broker. *******************")
            else:
                logging.info("******************* Could not connect to the MQTT broker. *******************")
        except Exception as E:
            logging.error("******************* Could not create MQTT object error -> %s *******************", E)
            return "Could not create MQTT object"
    else: 
        acMQTTRemoteIP = str("")
        acMQTTPort = str("")
    try:
        generate_Json.generateJsonWithInterface(acPipeName,acMQTTRemoteIP, acMQTTPort, acZeroMQRemoteIP, acZeroMQPort, acZeroMQRemoteIPPub, acZeroMQPortPub, lstXmls, lstInterfaceXmls, acPubSubTagSwap, acOld_xml_Schema)
    except Exception as E:
        logging.error("******************* Could not call Generate_Json file -> %s *******************", E)
        return "Could not call Generate_Json file"
    

    if "useMQTT" in dctData:
        acBrokerName = str(acMQTTRemoteIP)+'/'+str(acMQTTPort)
        if acBrokerName in dctMqttObj:
            pass
        elif acBrokerName not in dctMqttObj:
            dctMqttObj.update({acBrokerName:objMqtt})
        
    # get key
    acXmlkey = ''
    lstxmlKeys = list()
    dctReceiverFile = copy.deepcopy(_Protocol_class.G_dctJsonFile)
    for xml in lstXmls:
        for Jxmls in dctReceiverFile['xmls']:
            if xml[:-4]+'_MsgDef' == Jxmls["Connection"]["xmlFile"]:
                for conMsg, msgInfo in Jxmls.items():
                    if conMsg == "Messages":
                        for key in msgInfo.items():
                            acXmlkey = key[0]
                            lstxmlKeys.append(acXmlkey)

    if "ZeroMQPub" in dctData:
        try:
            dctNewPipe.update({"zeromq_pub":[acZeroMQRemoteIPPub,acZeroMQPortPub]})
        except Exception as E:
            logging.error("Cant update zeroMQ pipe")
            return "Can't update zeroMQ pipe"
        try:
            acZMQ_Socket_Key = str(acZeroMQRemoteIPPub)+"_"+str(acZeroMQPortPub)
            G_dctZeroMQPubObjects[acZMQ_Socket_Key] = clsZMQ_Manager(acPipeName, acZMQ_Socket_Key, lstxmlKeys, "publish")
            _Protocol_class.G_dctMQTT_ZMQ_Objects.update({acZMQ_Socket_Key:G_dctZeroMQPubObjects[acZMQ_Socket_Key]})
        except Exception as E:
            logging.error("******************* Could not Connect to ZMQ *******************")
            return "Could not Connect to ZMQ"

    if "useZeroMQ" in dctData:
        try:
            dctNewPipe.update({"zeromq_sub":[acZeroMQRemoteIP,acZeroMQPort]})
        except Exception as E:
            logging.error("Cant update zeroMQ pipe")
            return "Can't update zeroMQ pipe"
        try:
            acZMQ_Socket_Key = str(acZeroMQRemoteIP)+"_"+str(acZeroMQPort)
            clsZMQ_Manager(acPipeName, acZMQ_Socket_Key, lstxmlKeys, "subscribe")
        except Exception as E:
            logging.error("******************* Could not subscribe to ZMQ *******************")
            return "Could not subscribe to ZMQ"

    for xml in lstXmls:
        for Jxmls in dctReceiverFile['xmls']:
            if xml[:-4]+'_MsgDef' == Jxmls["Connection"]["xmlFile"]:
                for conMsg, msgInfo in Jxmls.items():
                    if conMsg == "Messages":
                        for key in msgInfo.items():
                            acXmlkey = key[0]    
        if "useMQTT" in dctData:
            # Subscribe to MQTT Messages
            try:
                objClsMqttComms = clsMqttComms(dctMqttObj[acBrokerName], acXmlkey)
            except Exception as E:
                logging.error("******************* Could not create objClsMqttComms -> %s *******************", E)
                return "Could not create MQTT object for this pipe"
                
            try:
                dctObjClsMqttComms.update({acPipeName:objClsMqttComms})
            except Exception as E:
                logging.error("******************* Could not update dctObjClsMqttComms -> %s *******************", E)
                return "Could not update dictionary holding MQTT objects"

    G_dctActivePipes.update({acPipeName:dctNewPipe})


    _Protocol_class.G_dctFieldAndVal = OrderedDict()
    _Protocol_class.G_dctFieldAndValReceived = OrderedDict()
    lstMsgPayloadPayload = list()

    for xml in dctReceiverFile['xmls']:
        for conMsg, msgInfo in xml.items():
            if conMsg == "Messages":
                for key, values in msgInfo.items():
                    _Protocol_class.G_dctFieldAndVal = OrderedDict()
                    dctHoldData = OrderedDict()
                    for headerKey, headerVal in values["Header"].items():
                        _Protocol_class.G_dctFieldAndVal[key+'_'+headerKey] = headerVal
                    lstMsgPayloadPayload = values["Payload"]
                    vRecursiveGetFieldVals(key, lstMsgPayloadPayload, "", dctHoldData)

    _Protocol_class.G_dctFieldAndValReceived = copy.deepcopy(_Protocol_class.G_dctFieldAndVal)
    return 'connected'

def vRecursiveGetFieldVals(key, lstMsgPayloadPar, dctInnerStructurePar, dctHoldData):
    """
        This function recurse over the added xmls and create a {field:value} dictionary,
        for structured filed it will construct {'structure_structure_fieldName':'value'}, 
        this is to speed up the process when processing messages.

        Args:
            key (str): message key
            lstMsgPayloadPar (list): current message structure
            dctInnerStructurePar (dict): message structure to be recursed
            dctHoldData (dict): hold the key-value of all fields

        Returns:
            
        Raises:
            Raises no exceptions
    """
    for field in lstMsgPayloadPar:
        if ('enumType' not in field)  and ('value' not in field):
            try:
                acTmpStructureName = dctInnerStructurePar+field['name']
                vRecursiveGetFieldVals(key, field['members'], acTmpStructureName, dctHoldData)
            except Exception as E:
                logging.error("Could not recurse the structure %s", E)

        if ('enumType' not in field) and ('value'in field):
            try:
                if dctInnerStructurePar+field['name'] not in dctHoldData:
                    dctHoldData[dctInnerStructurePar+field['name']] = 0
                    tmpFiledName = key+'_'+dctInnerStructurePar+field['name']
                    _Protocol_class.G_dctFieldAndVal[tmpFiledName]=field['value']
                else:
                    dctHoldData[dctInnerStructurePar+field['name']] = int(dctHoldData[dctInnerStructurePar+field['name']]) + 1
                    tmpFiledName = key+'_'+dctInnerStructurePar+field['name']+ str(dctHoldData[dctInnerStructurePar+field['name']])
                    _Protocol_class.G_dctFieldAndVal[tmpFiledName]=field['value']
            except Exception as E:
                logging.error("Error gettig Field value")
                return "error"
        if ('enumType' in field ):
            try:
                if dctInnerStructurePar+field['name'] not in dctHoldData:
                    dctHoldData[dctInnerStructurePar+field['name']] = 0
                    tmpFiledName = key+'_'+dctInnerStructurePar+field['name']
                    _Protocol_class.G_dctFieldAndVal[tmpFiledName]=field['value']
                else:
                    dctHoldData[dctInnerStructurePar+field['name']] = int(dctHoldData[dctInnerStructurePar+field['name']]) + 1
                    tmpFiledName = key+'_'+dctInnerStructurePar+field['name'] + str(dctHoldData[dctInnerStructurePar+field['name']])
                    _Protocol_class.G_dctFieldAndVal[tmpFiledName]=field['value']
            except Exception as E:
                logging.error("Error gettig Enum value")
                return "error"

@app.route("/savePipe", methods=['POST', 'GET'])
def acSavePipe():
    """
        This function is called everytime you connect a new pipe,
        It take textField values including xmls and pass them to autogen File to
        autogenerate the xmls, creating pipes and adding to main jsonFile

        Args:

        Returns:
            string status on success.
        Raises:
            Raises no exceptions
        
    """
    dctData = request.values
    dctData = ImmutableMultiDict(dctData).to_dict()
    acPipeName = str("")
    acMQTTRemoteIP = str("")
    acMQTTPort = str("")
    acZeroMQRemoteIP = str("")
    acZeroMQPort = str("")
    acZeroMQRemoteIPPub = str("")
    acZeroMQPortPub = str("")
    acPubSubTagSwap = str("")
    acPubSubTagSwapPipe = str("")
    acOld_xml_Schema = str("")
    lstXmlSchema = list()
    lstXmls = list()
    lstSystemName = list()
    lstDestination = list()
    lstSubTopic = list()
    lstInterfaceXmls = list()
    dctNewPipe = OrderedDict()
    
    for fieldname, val in dctData.items():
        if fieldname == 'pipe':
            acPipeName = val
        elif fieldname == 'MQTTRemoteIP':
            acMQTTRemoteIP = val
        elif fieldname == 'MQTTPort':
            acMQTTPort = val
        elif fieldname == 'ZeroMQRemoteIP':
            acZeroMQRemoteIP = val
        elif fieldname == 'ZeroMQPort':
            acZeroMQPort = val
        elif fieldname == 'ZeroMQRemoteIPPub':
            acZeroMQRemoteIPPub = val
        elif fieldname == 'ZeroMQPortPub':
            acZeroMQPortPub = val
        elif fieldname.startswith('schema'):	
            lstXmlSchema.append(val)
        elif fieldname.startswith('xml'):
            if val in lstXmls:
                logging.error("Can not add %s on webMM two times", val)
                return "Can not add "+val+" on webMM two times"
            else:
                lstXmls.append(val)
        elif fieldname.startswith('SystemName'):
            lstSystemName.append(val)
            lstSubTopic.append(val)
        elif fieldname.startswith('Destination'):
            lstDestination.append(val)
            lstSubTopic.append(val)
        elif fieldname.startswith('Interface'):
            lstInterfaceXmls.append(val)
        elif fieldname.startswith('pubSubTagSwap'):
            acPubSubTagSwap = val
        elif fieldname == 'acXmlSchema':
            acOld_xml_Schema = val

    
    acPipeNameTmp = acPipeName.replace(" ","")
    if acPipeNameTmp == "":
        logging.error(" please provide pipe name")
        return "Please provide pipe name"

    if "pubSubTagSwap" in dctData:
        acPubSubTagSwapPipe = "on"
    else:
        acPubSubTagSwapPipe = "off"

    dctNewPipe.update({"swap_mic_pub_sub":acPubSubTagSwapPipe,"xml_schema":acOld_xml_Schema,"xmls":lstXmls,"mic":lstInterfaceXmls})

    if "useMQTT" in dctData:
        dctNewPipe.update({"mqtt_pub_sub":[acMQTTRemoteIP,acMQTTPort]})

    if "ZeroMQPub" in dctData:
        try:
            dctNewPipe.update({"zeromq_pub":[acZeroMQRemoteIPPub,acZeroMQPortPub]})
        except Exception as E:
            logging.error("Cant update zeroMQ pipe")
            return "Cant update zeroMQ pipe"
    if "useZeroMQ" in dctData:
        try:
            dctNewPipe.update({"zeromq_sub":[acZeroMQRemoteIP,acZeroMQPort]})
        except Exception as E:
            logging.error("Cant update zeroMQ pipe")
            return "Cant update zeroMQ pipe"

    with open(os.path.join(os.path.dirname(__file__),"./pipes_config/"+acPipeName+".json"), 'w') as f:
        f.write(json.dumps({acPipeName:dctNewPipe}))
        f.close()

    return 'saved'

@app.route("/disconnectPipe", methods=['POST', 'GET'])
def acDisconnectPipe():
    '''
        This function disconnect the pipe
        It remove the pipe from pipes file and remove its associated xmls from main jsonFile
        it also close the connection to the broker

        Args:

        Returns:
            (str): Html home page.
        Raises:
            Raises no exceptions
    '''
    dctData = request.values
    dctData = ImmutableMultiDict(dctData).to_dict()
    acPipeName   = dctData['pipeName'] 

    dctJsonPipes = generate_Json.getPipes()
    for modAdd, modAddVals in dctJsonPipes.items():
        if modAddVals['name'] == acPipeName:
            del dctJsonPipes[modAdd]
            break
    
    _Protocol_class.G_dctPipes = copy.deepcopy(dctJsonPipes)

    iXmlIndex = 0
    acXmlkey = ''
    acIp=""
    acPort=""
    lstXmlIndex = list()
    dctJsonStructure = copy.deepcopy(_Protocol_class.G_dctJsonFile)
    for xmls in dctJsonStructure['xmls']:
        for acConnnectionMsg, msgInfo in xmls.items():
            dctXmls = OrderedDict(xmls)
            dctMsgInfo = OrderedDict(msgInfo)
            if acConnnectionMsg == 'Connection':
                if dctMsgInfo['PipeName'] == acPipeName:
                    dctXmlkeys = OrderedDict(dctXmls['Messages'])
                    lstxmlkey = list(dctXmlkeys.keys())
                    acXmlkey = lstxmlkey[0]
                    acIp = dctMsgInfo['MQTTRemoteIP']
                    acPort = dctMsgInfo['MQTTPort']
                    lstXmlIndex.append(iXmlIndex)
                    break        
        iXmlIndex = iXmlIndex+1
    
    for xmlIndex in reversed(lstXmlIndex):
        del dctJsonStructure['xmls'][xmlIndex]
    acBrokerName = str(acIp)+'/'+str(acPort)

    objClsProcessing = clsProcessing(E_WEBMM_PROCESSES.I_MAIN_PROCESS.value)
    
    # unsubscribe list of topics from broker and removed them from dispatch dictionary
    dctMqttObj[acBrokerName].vUnsubscribe(objClsProcessing.lstGetSubMqttTopic(acXmlkey))

    _Protocol_class.G_dctJsonFileSender = copy.deepcopy(dctJsonStructure)
    _Protocol_class.G_dctJsonFile = copy.deepcopy(dctJsonStructure)

    return render_template('home.html')

@app.route("/deletPipe", methods=['POST', 'GET'])
def acDeletPipe():
    '''
        This function disconnect the pipe
        It remove the pipe from pipes file and remove its associated xmls from main jsonFile
        it also close the connection to the broker

        Args:

        Returns:
            (str): Html home page.
        Raises:
            Raises no exceptions
    '''
    dctData = request.values
    dctData = ImmutableMultiDict(dctData).to_dict()
    acPipeName   = dctData['pipeName'] 
    
    try:
        acPathToGenFolder = os.path.join(os.path.dirname(__file__), "./pipes_config/")
        os.remove(acPathToGenFolder+acPipeName+".json")
    except Exception as E:
        return "error"

    return render_template('home.html')

@app.route("/message", methods=['POST', 'GET'])
def acUpdateDct():
    

    '''
        This function is called whenever a textfield is changed before sending a message,
        it update the json file holding message velues

        Args:

        Returns:
            (str): Html home page.
        Raises:
            Raises no exceptions
    '''
    dctData = ImmutableMultiDict(request.values)
    dctData = ImmutableMultiDict(dctData).to_dict()
    acMsgKey = dctData['0']

    lstValues = list(dctData.values())
    lstPayLoadPath = lstValues[2:-1]
    actualValue = lstValues[-1]

    iXmlIndex = 0

    acConMsg = "Messages"
    acHeaderPayload = "Payload"
    for dctXmls in _Protocol_class.G_dctJsonFileSender["xmls"]:
        if acMsgKey in dctXmls["Messages"]:
            try:
                iStructureLength = len(lstPayLoadPath)
                if iStructureLength == 1:
                    _Protocol_class.G_dctJsonFileSender['xmls'][iXmlIndex][acConMsg][acMsgKey][acHeaderPayload][int(lstPayLoadPath[0])]['value'] = str(str(actualValue))
                elif iStructureLength == 2:
                    _Protocol_class.G_dctJsonFileSender['xmls'][iXmlIndex][acConMsg][acMsgKey][acHeaderPayload][int(lstPayLoadPath[0])]["members"][int(lstPayLoadPath[1])]['value'] = str(actualValue)
                elif iStructureLength == 3:
                    _Protocol_class.G_dctJsonFileSender['xmls'][iXmlIndex][acConMsg][acMsgKey][acHeaderPayload][int(lstPayLoadPath[0])]['members'][int(lstPayLoadPath[1])]['members'][int(lstPayLoadPath[2])]['value'] = str(actualValue)
                    
                elif iStructureLength == 4:
                    _Protocol_class.G_dctJsonFileSender['xmls'][iXmlIndex][acConMsg][acMsgKey][acHeaderPayload][int(lstPayLoadPath[0])]['members'][int(lstPayLoadPath[1])]['members'][int(lstPayLoadPath[2])]['members'][int(lstPayLoadPath[3])]['value'] = str(actualValue)
                    
                elif iStructureLength == 5:
                    _Protocol_class.G_dctJsonFileSender['xmls'][iXmlIndex][acConMsg][acMsgKey][acHeaderPayload][int(lstPayLoadPath[0])]['members'][int(lstPayLoadPath[1])]['members'][int(lstPayLoadPath[2])]['members'][int(lstPayLoadPath[3])]['members'][int(lstPayLoadPath[4])]['value'] = str(actualValue)
                elif iStructureLength == 6:
                    _Protocol_class.G_dctJsonFileSender['xmls'][iXmlIndex][acConMsg][acMsgKey][acHeaderPayload][int(lstPayLoadPath[0])]['members'][int(lstPayLoadPath[1])]['members'][int(lstPayLoadPath[2])]['members'][int(lstPayLoadPath[3])]['members'][int(lstPayLoadPath[4])]['members'][int(lstPayLoadPath[5])]['value'] = str(actualValue)
                elif iStructureLength == 7:
                    _Protocol_class.G_dctJsonFileSender['xmls'][iXmlIndex][acConMsg][acMsgKey][acHeaderPayload][int(lstPayLoadPath[0])]['members'][int(lstPayLoadPath[1])]['members'][int(lstPayLoadPath[2])]['members'][int(lstPayLoadPath[3])]['members'][int(lstPayLoadPath[4])]['members'][int(lstPayLoadPath[5])]['members'][int(lstPayLoadPath[6])]['value'] = str(actualValue)
                elif iStructureLength == 8:
                    _Protocol_class.G_dctJsonFileSender['xmls'][iXmlIndex][acConMsg][acMsgKey][acHeaderPayload][int(lstPayLoadPath[0])]['members'][int(lstPayLoadPath[1])]['members'][int(lstPayLoadPath[2])]['members'][int(lstPayLoadPath[3])]['members'][int(lstPayLoadPath[4])]['members'][int(lstPayLoadPath[5])]['members'][int(lstPayLoadPath[6])]['members'][int(lstPayLoadPath[7])]['value'] = str(actualValue)
                elif iStructureLength == 9:
                    _Protocol_class.G_dctJsonFileSender['xmls'][iXmlIndex][acConMsg][acMsgKey][acHeaderPayload][int(lstPayLoadPath[0])]['members'][int(lstPayLoadPath[1])]['members'][int(lstPayLoadPath[2])]['members'][int(lstPayLoadPath[3])]['members'][int(lstPayLoadPath[4])]['members'][int(lstPayLoadPath[5])]['members'][int(lstPayLoadPath[6])]['members'][int(lstPayLoadPath[7])]['members'][int(lstPayLoadPath[8])]['value'] = str(actualValue)
                elif iStructureLength == 10:
                    _Protocol_class.G_dctJsonFileSender['xmls'][iXmlIndex][acConMsg][acMsgKey][acHeaderPayload][int(lstPayLoadPath[0])]['members'][int(lstPayLoadPath[1])]['members'][int(lstPayLoadPath[2])]['members'][int(lstPayLoadPath[3])]['members'][int(lstPayLoadPath[4])]['members'][int(lstPayLoadPath[5])]['members'][int(lstPayLoadPath[6])]['members'][int(lstPayLoadPath[7])]['members'][int(lstPayLoadPath[8])]['members'][int(lstPayLoadPath[9])]['value'] = str(actualValue)
                elif iStructureLength == 11:
                    _Protocol_class.G_dctJsonFileSender['xmls'][iXmlIndex][acConMsg][acMsgKey][acHeaderPayload][int(lstPayLoadPath[0])]['members'][int(lstPayLoadPath[1])]['members'][int(lstPayLoadPath[2])]['members'][int(lstPayLoadPath[3])]['members'][int(lstPayLoadPath[4])]['members'][int(lstPayLoadPath[5])]['members'][int(lstPayLoadPath[6])]['members'][int(lstPayLoadPath[7])]['members'][int(lstPayLoadPath[8])]['members'][int(lstPayLoadPath[9])]['members'][int(lstPayLoadPath[10])]['value'] = str(actualValue)
            except Exception as E:
                logging.error("Error updating message Field value, error -> %s ", E)
            break
        iXmlIndex = iXmlIndex+1

    return render_template('home.html')

@app.route("/autoScriptMessage", methods=['POST', 'GET'])
def acAutoScriptMessage():

    '''
        This function is called whenever auto script textfield is changed before sending a message,
        it update the json file holding message velues

        Args:

        Returns:
            (str): Html home page.
        Raises:
            Raises no exceptions
    '''
    dctData = ImmutableMultiDict(request.values)
    dctData = ImmutableMultiDict(dctData).to_dict()
    acMsgKey = dctData['0']

    lstValues = list(dctData.values())
    lstPayLoadPath = lstValues[2:-1]
    actualValue = lstValues[-1]

    iXmlIndex = 0

    acConMsg = "Messages"
    acHeaderPayload = "Payload"
    for acScriptName, lstScriptInto in _Protocol_class.G_dctJsonAutoScriptFile.items():
        if acMsgKey in lstScriptInto:
            try:
                iStructureLength = len(lstPayLoadPath)
                if iStructureLength == 1:
                    _Protocol_class.G_dctJsonAutoScriptFile[acScriptName][acMsgKey][acHeaderPayload][int(lstPayLoadPath[0])]['value'] = str(str(actualValue))
                elif iStructureLength == 2:
                    _Protocol_class.G_dctJsonAutoScriptFile[acScriptName][acMsgKey][acHeaderPayload][int(lstPayLoadPath[0])]["members"][int(lstPayLoadPath[1])]['value'] = str(actualValue)
                elif iStructureLength == 3:
                    _Protocol_class.G_dctJsonAutoScriptFile[acScriptName][acMsgKey][acHeaderPayload][int(lstPayLoadPath[0])]['members'][int(lstPayLoadPath[1])]['members'][int(lstPayLoadPath[2])]['value'] = str(actualValue)
                    
                elif iStructureLength == 4:
                    _Protocol_class.G_dctJsonAutoScriptFile[acScriptName][acMsgKey][acHeaderPayload][int(lstPayLoadPath[0])]['members'][int(lstPayLoadPath[1])]['members'][int(lstPayLoadPath[2])]['members'][int(lstPayLoadPath[3])]['value'] = str(actualValue)
                    
                elif iStructureLength == 5:
                    _Protocol_class.G_dctJsonAutoScriptFile[acScriptName][acMsgKey][acHeaderPayload][int(lstPayLoadPath[0])]['members'][int(lstPayLoadPath[1])]['members'][int(lstPayLoadPath[2])]['members'][int(lstPayLoadPath[3])]['members'][int(lstPayLoadPath[4])]['value'] = str(actualValue)
                elif iStructureLength == 6:
                    _Protocol_class.G_dctJsonAutoScriptFile[acScriptName][acMsgKey][acHeaderPayload][int(lstPayLoadPath[0])]['members'][int(lstPayLoadPath[1])]['members'][int(lstPayLoadPath[2])]['members'][int(lstPayLoadPath[3])]['members'][int(lstPayLoadPath[4])]['members'][int(lstPayLoadPath[5])]['value'] = str(actualValue)
                elif iStructureLength == 7:
                    _Protocol_class.G_dctJsonAutoScriptFile[acScriptName][acMsgKey][acHeaderPayload][int(lstPayLoadPath[0])]['members'][int(lstPayLoadPath[1])]['members'][int(lstPayLoadPath[2])]['members'][int(lstPayLoadPath[3])]['members'][int(lstPayLoadPath[4])]['members'][int(lstPayLoadPath[5])]['members'][int(lstPayLoadPath[6])]['value'] = str(actualValue)
                elif iStructureLength == 8:
                    _Protocol_class.G_dctJsonAutoScriptFile[acScriptName][acMsgKey][acHeaderPayload][int(lstPayLoadPath[0])]['members'][int(lstPayLoadPath[1])]['members'][int(lstPayLoadPath[2])]['members'][int(lstPayLoadPath[3])]['members'][int(lstPayLoadPath[4])]['members'][int(lstPayLoadPath[5])]['members'][int(lstPayLoadPath[6])]['members'][int(lstPayLoadPath[7])]['value'] = str(actualValue)
                elif iStructureLength == 9:
                    _Protocol_class.G_dctJsonAutoScriptFile[acScriptName][acMsgKey][acHeaderPayload][int(lstPayLoadPath[0])]['members'][int(lstPayLoadPath[1])]['members'][int(lstPayLoadPath[2])]['members'][int(lstPayLoadPath[3])]['members'][int(lstPayLoadPath[4])]['members'][int(lstPayLoadPath[5])]['members'][int(lstPayLoadPath[6])]['members'][int(lstPayLoadPath[7])]['members'][int(lstPayLoadPath[8])]['value'] = str(actualValue)
                elif iStructureLength == 10:
                    _Protocol_class.G_dctJsonAutoScriptFile[acScriptName][acMsgKey][acHeaderPayload][int(lstPayLoadPath[0])]['members'][int(lstPayLoadPath[1])]['members'][int(lstPayLoadPath[2])]['members'][int(lstPayLoadPath[3])]['members'][int(lstPayLoadPath[4])]['members'][int(lstPayLoadPath[5])]['members'][int(lstPayLoadPath[6])]['members'][int(lstPayLoadPath[7])]['members'][int(lstPayLoadPath[8])]['members'][int(lstPayLoadPath[9])]['value'] = str(actualValue)
                elif iStructureLength == 11:
                    _Protocol_class.G_dctJsonAutoScriptFile[acScriptName][acMsgKey][acHeaderPayload][int(lstPayLoadPath[0])]['members'][int(lstPayLoadPath[1])]['members'][int(lstPayLoadPath[2])]['members'][int(lstPayLoadPath[3])]['members'][int(lstPayLoadPath[4])]['members'][int(lstPayLoadPath[5])]['members'][int(lstPayLoadPath[6])]['members'][int(lstPayLoadPath[7])]['members'][int(lstPayLoadPath[8])]['members'][int(lstPayLoadPath[9])]['members'][int(lstPayLoadPath[10])]['value'] = str(actualValue)
            except Exception as E:
                logging.error("Error updating message Field value, error -> %s ", E)
            break
        iXmlIndex = iXmlIndex+1

    try:
        with open(os.path.join(os.path.dirname(__file__),"scriptingFiles/"+acScriptName+".json"), 'w') as f:
            f.write(json.dumps(_Protocol_class.G_dctJsonAutoScriptFile[acScriptName]))
            f.close()
    except Exception as E:
        logging.error("unable to write to file, error -> %s", E)
        return 'error'

    return render_template('home.html')

@app.route("/updateValues", methods=['POST', 'GET'])
def acUpdateValues():
    """
        This function create a processing class object, get new packed bytes and
        update packed bytes from 'G_dctMQTT_ZeroMQ_Connections' dictionary

        Args:

        Returns:
            (str): Html home page.
        Raises:
            Raises no exceptions
    """
    dctData = ImmutableMultiDict(request.values)
    dctData = ImmutableMultiDict(dctData).to_dict()

    acMessageKey = dctData["msgID"]
    acXmlSchema = dctData["xmlSchema"]
    acScriptName = dctData["scriptName"]
    acProtocol = dctData["protocol"]
    
    #create processing objected and get new packed bytes
    objClsProcessing = clsProcessing(E_WEBMM_PROCESSES.I_AUTOSCRIPT_PROCESS.value)
    btaTmpMQTTZQMPackedMsg = objClsProcessing.btaGetPackedMessageAutoScripting(acMessageKey, acXmlSchema, acScriptName)

    #loop for message key and update index 1 which contains old packed bytes
    for acConnection, dctConnectionInfo in _Protocol_class.G_dctMQTT_ZeroMQ_Connections[acScriptName][acProtocol].items():
        if "MQTTMessages" in dctConnectionInfo:
            if acMessageKey in dctConnectionInfo["MQTTMessages"]:
                try:
                    _Protocol_class.G_dctMQTT_ZeroMQ_Connections[acScriptName][acProtocol][acConnection]["MQTTMessages"][acMessageKey][1] = btaTmpMQTTZQMPackedMsg
                except Exception as E:
                    logging.error("Could not update message, error-> %s", E)
                    return "Could not update message"
        if "ZMQMessages" in dctConnectionInfo:
            if acMessageKey in dctConnectionInfo["ZMQMessages"]:
                try:
                    _Protocol_class.G_dctMQTT_ZeroMQ_Connections[acScriptName][acProtocol][acConnection]["ZMQMessages"][acMessageKey][1] = btaTmpMQTTZQMPackedMsg
                except Exception as E:
                    logging.error("Could not update message, error-> %s", E)
                    return "Could not update message"

        
    return render_template('home.html')

@app.route("/editHeader", methods=['POST', 'GET'])
def acUpdateDctHeader():

    '''
        This function is called whenever a header textfield is changed,
        It copies the main json dictionary responsible for sending messages, and search for the right textfield
        and update it's value, then assign the resulting json to the main json

        Args:

        Returns:
            (str): Html home page.
        Raises:
            Raises no exceptions
    '''
    dctData = ImmutableMultiDict(request.values)
    dctData = ImmutableMultiDict(dctData).to_dict()

    acMsgKey = dctData['0']
    lstValues = list(dctData.values())
    acHeaderName = lstValues[1]
    actualValue = lstValues[2]
    dctJsonStructure = OrderedDict()

    try:
        dctJsonStructure = copy.deepcopy(_Protocol_class.G_dctJsonFileSender)
    except Exception as E:
        logging.error("Failed to fetch json file, Error -> %s", E)
    
    iXmlIndex = 0
    for dctXmls in dctJsonStructure['xmls']:
        for acConMsg, dctMsgInfo in dctXmls.items():
            if acConMsg == "Messages":
                if acMsgKey in dctMsgInfo:
                    for acKey, dctValues in dctMsgInfo.items():
                        if acKey == acMsgKey:
                            for acHeaderPayload, dctHeaderPayloadVal in dctValues.items():
                                if acHeaderPayload == "Header":
                                    dctJsonStructure['xmls'][iXmlIndex][acConMsg][acMsgKey][acHeaderPayload][acHeaderName] = str(actualValue)
        iXmlIndex = iXmlIndex+1

    _Protocol_class.G_dctJsonFileSender = copy.deepcopy(dctJsonStructure)
    return render_template('home.html')

@app.route("/editAutoScriptHeader", methods=['POST', 'GET'])
def acEditAutoScriptHeader():

    '''
        This function is called whenever an Autoscript header textfield is changed,
        It searches for the right textfield from Autoscript dictionary, update it's value,
        then write the resulting json to Autoscript json file

        Args:

        Returns:
            (str): Html home page.
        Raises:
            Raises no exceptions
    '''
    dctData = ImmutableMultiDict(request.values)
    dctData = ImmutableMultiDict(dctData).to_dict()

    acMsgKey = dctData['0']
    lstValues = list(dctData.values())
    acHeaderName = lstValues[1]
    actualValue = lstValues[2]
    
    for acScriptName, lstScriptInto in _Protocol_class.G_dctJsonAutoScriptFile.items():
        if acMsgKey in lstScriptInto:
            _Protocol_class.G_dctJsonAutoScriptFile[acScriptName][acMsgKey]["Header"][acHeaderName] = str(actualValue)

    try:
        with open(os.path.join(os.path.dirname(__file__),"scriptingFiles/"+acScriptName+".json"), 'w') as f:
            f.write(json.dumps(_Protocol_class.G_dctJsonAutoScriptFile[acScriptName]))
            f.close()
    except Exception as E:
        logging.error("unable to write to file, error -> %s", E)
        return 'error'

    return render_template('home.html')

@app.route("/sendMessage", methods=['POST', 'GET'])
def acSendMessage():
    '''
        This function is responsible for sending of messages

        Args:

        Returns:
            (str): Html home page.
        Raises:
            Raises no exceptions
    '''
    global G_dctZeroMQPubObjects
    dctData = ImmutableMultiDict(request.values)
    dctData = ImmutableMultiDict(dctData).to_dict()
    acMsgId   = dctData['_MsgId'] 
    acModAdd  = dctData['_ModuleAddress']
    acMsgType = dctData['_MsgType']
    acRoles   = dctData['Roles']
    acMsgKey  = str("")
    acPubSub_tag = str("")
    acZeroMQObjectKeyName = str("")
    acZeroMQRemoteIPPub = str("")
    acZeroMQPortPub = str("")
    acMsg_Topic = str("")

    if(acRoles == "NoRole"):
        acMsgKey = acMsgId+'_'+acModAdd+'_'+acMsgType
    else:
        acMsgKey = acMsgId+'_'+acModAdd+'_'+acMsgType+'_'+acRoles
    acPipeName = str("")
    acXmlSchema = str("")
    acIndividualMessageProtocol = str("")
    for dctXmls in _Protocol_class.G_dctJsonFile['xmls']:
        for acConMsg, dctMsgInfo in dctXmls.items():
            if acConMsg == "Messages":
                if acMsgKey in dctMsgInfo:
                    for acKey, dctValues in dctMsgInfo.items():
                        if acKey == acMsgKey:
                            acIndividualMessageProtocol = dctValues['Individual_Message_Protocol']
                            acPubSub_tag = dctValues['pubSub_tag']
                            acMsg_Topic = dctValues['Msg_Topic']
                            acPipeName = str(dctXmls['Connection']['PipeName'])
                            acXmlSchema = str(dctXmls['Connection']['xmlSchema'])
                            acZeroMQRemoteIPPub = str(dctXmls['Connection']['ZeroMQRemoteIPPub'])
                            acZeroMQPortPub = str(dctXmls['Connection']['ZeroMQPortPub'])
                            acZeroMQObjectKeyName = str(acZeroMQRemoteIPPub+"_"+acZeroMQPortPub)
                            break
    if acIndividualMessageProtocol == "MQTT":
        try:
            objClsMqttComms = dctObjClsMqttComms[acPipeName]
        except Exception as E:
            logging.error("Object for this key is not valid (check your key values -> MsgID_ModuleAddress_MsgType), error -> returned object %s ", E)
            return "error"
        try:
            objProtocol = _Protocol_class.RRS_MMI(objClsMqttComms) # give message of topic to Protocol
        except Exception as E:
            logging.error("Could not pass the object to protocol class, error -> %s ", E)
            return "error"
        
        try:
            objProtocol.vSend(acMsgKey, acXmlSchema) # publishes message
        except Exception as E:
            logging.error("Faild to send a message, error -> %s ", E)
            return "error"

    elif acIndividualMessageProtocol == "ZMQ":# and acPubSub_tag == "Publish":
        try:
            statusResponse = G_dctZeroMQPubObjects[acZeroMQObjectKeyName].vSendData(acZeroMQObjectKeyName,acMsgKey, acMsg_Topic, acXmlSchema)
            if statusResponse == "error":
                logging.error("Can not send ZeroMQ message")
                return "error"

        except Exception as E:
            logging.error("Could not send this message, this message is ZeroMQ, check if ZeroMQ connection was made, Error -> %s", E)
            return "error"
    return render_template('home.html')

@app.route("/startAutoscript", methods=['POST', 'GET'])
def acStartAutoscript():
    """
        This fuction create an autoscript object, unbind all zmq IP-port, put new IP and port of a selected protocol
        and make new connections.

        Args:

        Returns:
            string status on success.
        Raises:
            Raises no exceptions
    """

    dctData = ImmutableMultiDict(request.values)
    dctData = ImmutableMultiDict(dctData).to_dict()
    acConProtocol   = dctData['protocol'] 
    acConIp  = dctData['conIp']
    acConPort = dctData['conPort']

    try:
        objAutoScriptObject = clsMessageObjects()
        for acKeyName, objName in _Protocol_class.G_dctAutoScriptOnlyZMQ_Objects.items():
            objAutoScriptObject.vUnbindPubSoc(objName, acKeyName)

    except Exception as E:
        logging.error("can not unbind from this IP, error -> %s", E)

    acAutoScriptingPath = os.path.join(os.path.dirname(__file__), "./scriptingFiles/")
    acAutoScriptFiles = os.listdir(acAutoScriptingPath)
    for iIndex, acItem in enumerate(acAutoScriptFiles):
        if acItem[-5:] == ".json":
            acScriptFileName = acItem[:-5]
            try:
                with open(os.path.join(os.path.dirname(__file__), "./scriptingFiles/" + acItem), 'r') as f:
                    dctFileData = json.load(f)

                    
                    for messageKey, messageContent in dctFileData.items():
                        if acConProtocol == "MQTT":
                            dctFileData[messageKey]["Connection"].update({"Protocol": acConProtocol})
                            dctFileData[messageKey].update({"Individual_Message_Protocol": acConProtocol})
                            dctFileData[messageKey]["Connection"].update({"MQTTRemoteIP": acConIp})
                            dctFileData[messageKey]["Connection"].update({"MQTTPort": acConPort})
                        elif acConProtocol == "ZMQ":
                            dctFileData[messageKey]["Connection"].update({"Protocol": acConProtocol})
                            dctFileData[messageKey].update({"Individual_Message_Protocol": acConProtocol})
                            dctFileData[messageKey]["Connection"].update({"ZeroMQRemoteIPPub": acConIp})
                            dctFileData[messageKey]["Connection"].update({"ZeroMQPortPub": acConPort})
                        elif acConProtocol == "previous":
                            pass

                    _Protocol_class.G_dctJsonAutoScriptFile.update({acScriptFileName: dctFileData})
                    f.close()

            except Exception as E:
                logging.error("unable to write to file, error -> %s", E)
                return 'error'

            try:
                with open(os.path.join(os.path.dirname(__file__),"./scriptingFiles/"+acScriptFileName+".json"), 'w') as f:
                    f.write(json.dumps(_Protocol_class.G_dctJsonAutoScriptFile[acScriptFileName]))
                    f.close()
            except Exception as E:
                logging.error("unable to write to file, error -> %s", E)
                return 'error'

    objNewAutoScriptObject = clsMessageObjects()
    acConnectionMessage = objNewAutoScriptObject.vMakeConnection()

    if acConnectionMessage == "error":
        return "error"
    return 'Auto Script started'

@app.route("/restartAutoscript", methods=['POST', 'GET'])
def acRestartAutoscript():
    """
        restart autoscripting, unbind ZMQ and disconnect MQTT, empty all dictionaries and lists then restart connection.

        Args:

        Returns:
            string status on success.
        Raises:
            Raises no exceptions
    """
    _Protocol_class.G_stopThread = True
    time.sleep(2)
    objAutoScriptObject = clsMessageObjects()
    for acKeyName, objName in _Protocol_class.G_dctAutoScriptOnlyMQTT_ZMQ_Objects.items():
        if acKeyName in _Protocol_class.G_dctAutoScriptOnlyZMQ_Objects:
            objAutoScriptObject.vUnbindPubSoc(objName, acKeyName)
        else:
            try:
                objName.disconnect() # disconnect gracefully
                objName.loop_stop() # stops network loop
            except Exception as E:
                logging.error("Cannot stop thread, error-> %s", E)
    try:
        logging.info("empty dicts")
        _Protocol_class.G_dctJsonAutoScriptFile = OrderedDict()
        _Protocol_class.G_dctMQTT_ZeroMQ_Connections = OrderedDict()
        _Protocol_class.G_dctRepeatAutoscriptingParThread = OrderedDict()
        _Protocol_class.G_dctMQTT_ZMQ_Objects = OrderedDict()
        _Protocol_class.G_dctAutoScriptOnlyMQTT_ZMQ_Objects = OrderedDict()
        _Protocol_class.G_dctAutoScriptOnlyZMQ_Objects = OrderedDict()
        _Protocol_class.G_lstBusySendingScript = list()
    except Exception as E:
        logging.error("Cannot empty variables, error -> %s", E)

    try:
        objAutoScriptObject = clsMessageObjects()
        objAutoScriptObject.vMakeConnection()
    except Exception as E:
        logging.error("Error occures with the auto script object, error -> %s", E)

    return 'Auto Script restarted'

@app.route("/sendAutoScriptMessage", methods=['POST', 'GET'])
def btaSendAutoScriptMessage():
    """
     this fuction will check if a message has to repeat sending or it is only sending once.
     then send messages with their respective objects

     Args:

    Returns:
        acRepeatAutoscripting (bool): repeat publishing a message.
    Raises:
        Raises no exceptions
    """

    dctData = ImmutableMultiDict(request.values)
    dctData = ImmutableMultiDict(dctData).to_dict()

    _Protocol_class.G_stopThread = False
    acFileName = dctData["fileName"]
    acRepeatAutoscripting = dctData["repeatAutoscripting"]
    
    objAutoScriptObject = clsMessageObjects()
    
    if acFileName in _Protocol_class.G_dctRepeatAutoscriptingParThread:
        _Protocol_class.G_dctRepeatAutoscriptingParThread[acFileName].join()
        del _Protocol_class.G_dctRepeatAutoscriptingParThread[acFileName]

    if acRepeatAutoscripting == "false":
        objAutoScriptObject.vSendMessages(acFileName)
    
    elif acRepeatAutoscripting == "true":
        _Protocol_class.G_dctStopSingleThread.update({acFileName:objAutoScriptObject})
        _Protocol_class.G_dctRepeatAutoscriptingParThread[acFileName] = threading.Thread(target=objAutoScriptObject.vSendMessagesRepeat, args=(acFileName, ))
        _Protocol_class.G_dctRepeatAutoscriptingParThread[acFileName].daemon = True
        _Protocol_class.G_dctRepeatAutoscriptingParThread[acFileName].start()
        if acFileName not in _Protocol_class.G_lstBusySendingScript:
            _Protocol_class.G_lstBusySendingScript.append(acFileName)

    return acRepeatAutoscripting

@app.route("/stopAutoScriptMessage", methods=['POST', 'GET'])
def acStopAutoScriptMessage():
    """
        Stops the thread that is being used for sending messages.

        Args:

        Returns:
            String status on success
        Raises:
            Raises no exceptions
    """
    dctData = ImmutableMultiDict(request.values)
    dctData = ImmutableMultiDict(dctData).to_dict()
    acFileName = dctData["fileName"]
    try:
        _Protocol_class.G_dctStopSingleThread[acFileName].bStopSendingThread = True
    except Exception as E:
        logging.error("Failed to stop sending message")
    
    try:
        if acFileName in _Protocol_class.G_lstBusySendingScript:
            _Protocol_class.G_lstBusySendingScript.remove(acFileName)
    except Exception as E:
        logging.error("Unable to remove filename form busy sending script list, error -> %s", E)

    return "Message stopped sending"
    
@app.route("/getBusySendingAutoScripts", methods=['POST', 'GET'])
def lstBusySendingAutoScripts():
    """
        This functions returns a list of messages busy publishing via autoscripting

        Args:

        Returns:
            _Protocol_class.G_lstBusySendingScript (list): list of message busy publishing.
        Raises:
            Raises no exceptions
    """

    return json.dumps(_Protocol_class.G_lstBusySendingScript)

@app.route("/addMessageToScript", methods=['POST', 'GET'])
def acAddMessageToScript():
    '''
        This function received json/dictionary and add message to the autoscript file
        dictFormat: {"scriptType": "newScript", "scriptName": "OTT script", "delayInSecName": "3", "messageID": "50_2_4"}

        Args:

        Returns:
            String status on success.
        Raises:
            Raises no exceptions
    '''
    global G_dctZeroMQPubObjects
    dctData = ImmutableMultiDict(request.values)
    dctData = ImmutableMultiDict(dctData).to_dict()

    acScriptType   = dctData['scriptType'] 
    acScriptName  = dctData['scriptName']
    fDelayInSecName_sec = dctData['delayInSecName']
    acMessageID   = dctData['messageID']
    acMessageIDUnchanged   = dctData['messageID']
    dctExistingMessages = OrderedDict()

    if acScriptType == "existingScript":
        try:
            with open(os.path.join(os.path.dirname(__file__), "scriptingFiles/"+acScriptName+".json"), 'r') as f:
                dctExistingMessages = OrderedDict(json.load(f))
                f.close()
        except Exception as E:
            logging.error("unable fetch file, error -> %s", E)
            return 'error'
        if acMessageIDUnchanged in dctExistingMessages:
            iNumberOfMessages = len(dctExistingMessages.keys())
            acMessageID = acMessageID+"."+str(iNumberOfMessages)

    dctAutoScriptingMessage = dict()
    dctAutoScriptingMessage.update({acMessageID:dict()})

    for dctXmls in _Protocol_class.G_dctJsonFile['xmls']:
        for acConMsg, dctMsgInfo in dctXmls.items():
            if acConMsg == "Messages":
                if acMessageIDUnchanged in dctMsgInfo:
                    try:
                        dctAutoScriptingMessage[acMessageID].update(dctMsgInfo[acMessageIDUnchanged])
                        dctAutoScriptingMessage[acMessageID].update({"delayInSec":fDelayInSecName_sec})
                        dctAutoScriptingMessage[acMessageID].update({"Connection":dctXmls["Connection"]})

                    except Exception as E:
                        logging.error("unable to update dictionary, error -> %s", E)
    if acScriptType == "newScript":
        try:
            with open(os.path.join(os.path.dirname(__file__),"scriptingFiles/"+acScriptName+".json"), 'w') as f:
                f.write(json.dumps(dctAutoScriptingMessage))
                f.close()
        except Exception as E:
            logging.error("unable to write to file, error -> %s", E)
            return 'error'

        try:
            _Protocol_class.G_dctJsonAutoScriptFile.update({acScriptName:dctAutoScriptingMessage})
        except Exception as E:
            logging.error("unable to update dictionary, error -> %s", E)
            return 'error'

    elif acScriptType == "existingScript":
        try:
            dctExistingMessages.update(dctAutoScriptingMessage)
        except Exception as E:
            logging.error("unable to update dictionary, error -> %s", E)
            return 'error'
            
        try:
            with open(os.path.join(os.path.dirname(__file__),"scriptingFiles/"+acScriptName+".json"), 'w') as f:
                f.write(json.dumps(dctExistingMessages))
                f.close()
        except Exception as E:
            logging.error("unable to write to file, error -> %s", E)
            return 'error'

        try:
            _Protocol_class.G_dctJsonAutoScriptFile.update({acScriptName:dctExistingMessages})
        except Exception as E:
            logging.error("unable to update dictionary, error -> %s", E)
            return 'error'
    
    return 'saved'

def vReceivedMsg(acMsgKeyPar, dataPar):
    '''
        This function is called whenever a message is received.

        Args:
            acMsgKeyPar (str): message key
            dataPar (list) : message structure
        Returns:
            
        Raises:
            Raises no exceptions
    '''

    dctFieldVal.clear()
    lstMsgPay = list()
    acXmlSchemaPar = dataPar[1]
    data = list(dataPar[0])

    acMsgKey = acMsgKeyPar
    if acXmlSchemaPar == "BR12":
        lstMsgPay = data[5:]
        lstMsgHeader = data[:5]
    else:
        lstMsgPay = data[8:]
        lstMsgHeader = data[:8]

    acName = ""
    if int(data[1]) == 0 or int(data[1]) == 1 or int(data[1]) == 2 or int(data[1]) == 3 or int(data[1]) == 4:
        acMsgKeyForResp = acMsgKeyPar

        dctReceivedMessages = clVariables.G_dctReceivedMessages

        if acMsgKeyForResp in dctReceivedMessages:
            iOrigVal = dctReceivedMessages[acMsgKeyForResp]
            iNewVal  = int(iOrigVal) + 1
            dctReceivedMessages[acMsgKeyForResp] = iNewVal
        elif acMsgKeyForResp not in dctReceivedMessages:
            dctReceivedMessages.update({acMsgKeyForResp:1})

        clVariables.G_dctReceivedMessages = dctReceivedMessages
        iXmlIndex = 0
        for xmls in _Protocol_class.G_dctJsonFile['xmls']:
            for conMsg, msgInfo in xmls.items():
                if conMsg == "Connection":
                    acXmlFileName = msgInfo['xmlFile']
                if conMsg == "Messages":
                    if acMsgKey in msgInfo:
                        for key, dctValues in msgInfo.items():
                            if key == acMsgKey:
                                for payKey, headerPayload in dctValues.items():
                                    if payKey == "Name":
                                        acName = headerPayload
                                    if payKey == "Header":
                                        for fieldIndex, field in enumerate(headerPayload):
                                            fieldValue = lstMsgHeader[0]
                                            try:
                                                dctConvertToDict = OrderedDict(_Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey])
                                            except Exception as E:
                                                logging.error("Could not convert orderedDict ot dict, error -> %s", E)

                                            try:
                                                _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][field] = fieldValue

                                                tmpFieldName = field
                                                tmpKey = acMsgKeyPar +"_"+tmpFieldName
                                                _Protocol_class.G_dctFieldAndValReceived[tmpKey] = fieldValue

                                                
                                            except Exception as E:
                                                logging.error("Failed to update the dictionary header value, error -> %s", E)

                                            
                                            lstMsgHeader.pop(0)
                                    if payKey == "Payload":
                                        iRecurse_counter = 0
                                        iLevelField1 = 0
                                        iLevelField2 = 0
                                        iLevelField3 = 0
                                        iLevelField4 = 0
                                        iLevelField5 = 0

                                        dctHoldData = OrderedDict()
                                        def recurse_struceture(msgPayload, lstMsgPay, iRecurse_counter, dctHoldData, iLevelField1, iLevelField2, iLevelField3, iLevelField4, iLevelField5):
                                            for fieldIndex, field in enumerate(msgPayload):
                                                fieldValue = lstMsgPay[0]
                                                if type(fieldValue) == bytes:
                                                    fieldValue = fieldValue.decode("utf-8").strip("\x00")
                                                if "value" not in field:
                                                    iRecurse_counter = int(iRecurse_counter) + 1
                                                    if iRecurse_counter == 1:
                                                        iLevelField1 = fieldIndex
                                                    elif iRecurse_counter == 2:
                                                        iLevelField2 = fieldIndex
                                                    elif iRecurse_counter == 3:
                                                        iLevelField3 = fieldIndex
                                                    elif iRecurse_counter == 4:
                                                        iLevelField4 = fieldIndex
                                                    elif iRecurse_counter == 5:
                                                        iLevelField5 = fieldIndex
                                                    recurse_struceture(field['members'], lstMsgPay, iRecurse_counter, dctHoldData, iLevelField1, iLevelField2, iLevelField3, iLevelField4, iLevelField5)
                                                    iRecurse_counter = int(iRecurse_counter) - 1
                                                elif "value" in field and iRecurse_counter == 0:
                                                    _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][fieldIndex]['value'] = fieldValue
                                                    dctFieldVal.update({_Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][fieldIndex]['name']:fieldValue})
                                                    lstMsgPay.pop(0)
                                                    
                                                    tmpFieldName = _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][fieldIndex]['name']
                                                    tmpKey = acMsgKeyPar +"_"+tmpFieldName

                                                    if tmpKey not in dctHoldData:
                                                        dctHoldData[tmpKey] = 0
                                                        _Protocol_class.G_dctFieldAndValReceived[str(tmpKey)] = fieldValue
                                                    else:
                                                        dctHoldData[tmpKey] = int(dctHoldData[tmpKey]) + 1
                                                        _Protocol_class.G_dctFieldAndValReceived[str(tmpKey)+str(dctHoldData[tmpKey])] = fieldValue


                                                elif "value" in field and iRecurse_counter == 1:
                                                    _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][fieldIndex]['value'] = fieldValue
                                                    dctFieldVal.update({_Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][fieldIndex]['name']:fieldValue})
                                                    lstMsgPay.pop(0)

                                                    tmpFieldMember1 = _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['name']
                                                    tmpFieldName = _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][fieldIndex]['name']
                                                    tmpKey = acMsgKeyPar +"_"+tmpFieldMember1+tmpFieldName
                                                    if tmpKey not in dctHoldData:
                                                        dctHoldData[tmpKey] = 0
                                                        _Protocol_class.G_dctFieldAndValReceived[str(tmpKey)] = fieldValue
                                                    else:
                                                        dctHoldData[tmpKey] = int(dctHoldData[tmpKey]) + 1
                                                        _Protocol_class.G_dctFieldAndValReceived[str(tmpKey)+str(dctHoldData[tmpKey])] = fieldValue

                                                elif "value" in field and iRecurse_counter == 2:
                                                    _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][int(iLevelField2)]['members'][fieldIndex]['value'] = fieldValue
                                                    dctFieldVal.update({_Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][int(iLevelField2)]['members'][fieldIndex]['name']:fieldValue})
                                                    lstMsgPay.pop(0)

                                                    tmpFieldMember1 = _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['name']
                                                    tmpFieldMember2 = _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][int(iLevelField2)]['name']
                                                    tmpFieldName = _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][int(iLevelField2)]['members'][fieldIndex]['name']
                                                    tmpKey = acMsgKeyPar +"_"+tmpFieldMember1+tmpFieldMember2+tmpFieldName
                                                    if tmpKey not in dctHoldData:
                                                        dctHoldData[tmpKey] = 0
                                                        _Protocol_class.G_dctFieldAndValReceived[str(tmpKey)] = fieldValue
                                                    else:
                                                        dctHoldData[tmpKey] = int(dctHoldData[tmpKey]) + 1
                                                        _Protocol_class.G_dctFieldAndValReceived[str(tmpKey)+str(dctHoldData[tmpKey])] = fieldValue

                                                    
                                                elif "value" in field and iRecurse_counter == 3:
                                                    _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][int(iLevelField2)]['members'][int(iLevelField3)]['members'][fieldIndex]['value'] = fieldValue
                                                    dctFieldVal.update({_Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][int(iLevelField2)]['members'][int(iLevelField3)]['members'][fieldIndex]['name']:fieldValue})
                                                    lstMsgPay.pop(0)
                                                    
                                                    tmpFieldMember1 = _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['name']
                                                    tmpFieldMember2 = _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][int(iLevelField2)]['name']
                                                    tmpFieldMember3 = _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][int(iLevelField2)]['members'][int(iLevelField3)]['name']
                                                    tmpFieldName = _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][int(iLevelField2)]['members'][int(iLevelField3)]['members'][fieldIndex]['name']
                                                    tmpKey = acMsgKeyPar +"_"+tmpFieldMember1+tmpFieldMember2+tmpFieldMember3+tmpFieldName
                                                    if tmpKey not in dctHoldData:
                                                        dctHoldData[tmpKey] = 0
                                                        _Protocol_class.G_dctFieldAndValReceived[str(tmpKey)] = fieldValue
                                                    else:
                                                        dctHoldData[tmpKey] = int(dctHoldData[tmpKey]) + 1
                                                        _Protocol_class.G_dctFieldAndValReceived[str(tmpKey)+str(dctHoldData[tmpKey])] = fieldValue
                                                    
                                                    
                                                elif "value" in field and iRecurse_counter == 4:
                                                    _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][int(iLevelField2)]['members'][int(iLevelField3)]['members'][int(iLevelField4)]['members'][fieldIndex]['value'] = fieldValue
                                                    dctFieldVal.update({_Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][int(iLevelField2)]['members'][int(iLevelField3)]['members'][int(iLevelField4)]['members'][fieldIndex]['name']:fieldValue})
                                                    lstMsgPay.pop(0)

                                                    tmpFieldMember1 = _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['name']
                                                    tmpFieldMember2 = _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][int(iLevelField2)]['name']
                                                    tmpFieldMember3 = _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][int(iLevelField2)]['members'][int(iLevelField3)]['name']
                                                    tmpFieldMember4 = _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][int(iLevelField2)]['members'][int(iLevelField3)]['members'][int(iLevelField4)]['name']
                                                    tmpFieldName = _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][int(iLevelField2)]['members'][int(iLevelField3)]['members'][int(iLevelField4)]['members'][fieldIndex]['name']
                                                    tmpKey = acMsgKeyPar +"_"+tmpFieldMember1+tmpFieldMember2+tmpFieldMember3+tmpFieldMember4+tmpFieldName
                                                    if tmpKey not in dctHoldData:
                                                        dctHoldData[tmpKey] = 0
                                                        _Protocol_class.G_dctFieldAndValReceived[str(tmpKey)] = fieldValue
                                                    else:
                                                        dctHoldData[tmpKey] = int(dctHoldData[tmpKey]) + 1
                                                        _Protocol_class.G_dctFieldAndValReceived[str(tmpKey)+str(dctHoldData[tmpKey])] = fieldValue

                                                elif "value" in field and iRecurse_counter == 5:
                                                    _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][int(iLevelField2)]['members'][int(iLevelField3)]['members'][int(iLevelField4)]['members'][int(iLevelField5)]['members'][fieldIndex]['value'] = fieldValue
                                                    dctFieldVal.update({_Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][int(iLevelField2)]['members'][int(iLevelField3)]['members'][int(iLevelField4)]['members'][int(iLevelField5)]['members'][fieldIndex]['name']:fieldValue})
                                                    lstMsgPay.pop(0)

                                                    tmpFieldMember1 = _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['name']
                                                    tmpFieldMember2 = _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][int(iLevelField2)]['name']
                                                    tmpFieldMember3 = _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][int(iLevelField2)]['members'][int(iLevelField3)]['name']
                                                    tmpFieldMember4 = _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][int(iLevelField2)]['members'][int(iLevelField3)]['members'][int(iLevelField4)]['name']
                                                    tmpFieldMember5 = _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][int(iLevelField2)]['members'][int(iLevelField3)]['members'][int(iLevelField4)]['members'][int(iLevelField5)]['name']
                                                    tmpFieldName = _Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey][int(iLevelField1)]['members'][int(iLevelField2)]['members'][int(iLevelField3)]['members'][int(iLevelField4)]['members'][int(iLevelField5)]['members'][fieldIndex]['name']
                                                    tmpKey = acMsgKeyPar +"_"+tmpFieldMember1+tmpFieldMember2+tmpFieldMember3+tmpFieldMember4+tmpFieldMember5+tmpFieldName
                                                    if tmpKey not in dctHoldData:
                                                        dctHoldData[tmpFieldName] = 0
                                                        _Protocol_class.G_dctFieldAndValReceived[str(tmpKey)] = fieldValue
                                                    else:
                                                        dctHoldData[tmpFieldName] = int(dctHoldData[tmpFieldName]) + 1                                                    
                                                        _Protocol_class.G_dctFieldAndValReceived[str(tmpKey)+str(dctHoldData[tmpKey])] = fieldValue

                                            iRecurse_counter = 0
                                        recurse_struceture(headerPayload, lstMsgPay, iRecurse_counter, dctHoldData, iLevelField1, iLevelField2, iLevelField3, iLevelField4, iLevelField5)
                                        
                        dctRecordingMsgs = json.loads(generate_Json.getRecordingMsgs())

                        receivedKey = str(data[4])+'_'+str(data[3])+'_'+str(int(data[1] - 1))
                        if receivedKey in dctRecordingMsgs['msgs']:
                            dctRecordedMsgs = json.loads(generate_Json.getRecordedMessages())
                            currentTime = time.time()
                            if acMsgKey not in dctRecordedMsgs:
                                dctRecordedMsgs.update({acMsgKey:{"xmlName":acXmlFileName,"Name":acName,"Messages":{currentTime:_Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey]}}})
                            else:
                                dctRecordedMsgs[acMsgKey]["Messages"].update({currentTime:_Protocol_class.G_dctJsonFile['xmls'][iXmlIndex][conMsg][acMsgKey][payKey]})
                            with open(os.path.join(os.path.dirname(__file__),"Structure/recordedMessages.json"), 'w') as f:
                                f.write(json.dumps(dctRecordedMsgs))
                                f.close()

            iXmlIndex = iXmlIndex+1

@app.route("/editPipe", methods=['POST', 'GET'])
def acEditPipe():
    '''
        This function is called whenever you edit a pipe.

        Args:

        Returns:
            (str): Html home page.
        Raises:
            Raises no exceptions
    '''
    dctData = request.values
    dctData = ImmutableMultiDict(dctData).to_dict()
    acPipeName   = dctData['pipeName'] 
    acXmlName  = dctData['xmlName']

    dctJsonPipes = generate_Json.getPipes()
    for acModAdd, dctModAddVals in dctJsonPipes.items():
        if dctModAddVals['name'] == acPipeName:
            for acPipeXml in dctModAddVals['xmls']:
                if acPipeXml == acXmlName:
                    del dctJsonPipes[acModAdd]['xmls'][dctModAddVals['xmls'].index(acPipeXml)]

    _Protocol_class.G_dctPipes = copy.deepcopy(dctJsonPipes)

    iXmlIndex = 0
    dctJsonStructure = copy.deepcopy(_Protocol_class.G_dctJsonFileSender)
    for dctXmls in dctJsonStructure['xmls']:
        for acConMsg, dctMsgInfo in dctXmls.items():
            if acConMsg == "Connection":
                acTmpXMlName = dctMsgInfo['xmlFile'][:-9]+'sg.xml'
                if dctMsgInfo['PipeName'] == acPipeName and acTmpXMlName == acXmlName:
                    del dctJsonStructure['xmls'][iXmlIndex]
        iXmlIndex = iXmlIndex+1

    _Protocol_class.G_dctJsonFileSender = copy.deepcopy(dctJsonStructure)
    _Protocol_class.G_dctJsonFile = copy.deepcopy(dctJsonStructure)
    return render_template('home.html')

@app.route("/updateReceivedMessage", methods=['POST', 'GET'])
def acUpdateReceivedMessage():
    """
        This function is called whenever you want to see number of message received

    Args:

    Return:
        (str): Html home page.

    Exceptions:
        Throws no exceptions
    
    """
    dctData = request.values
    dctData = ImmutableMultiDict(dctData).to_dict()
    acViewedMsg   = dctData['MsgId']

    try:
        dctReceivedMessages = clVariables.G_dctReceivedMessages
    except Exception as E:
        logging.error("Could not get number of received messages, error -> %s ", E)
        return("")
        
    if acViewedMsg in dctReceivedMessages:
        try:
            del dctReceivedMessages[acViewedMsg]
        except Exception as E:
            logging.error("Could not empty number of message received error -> %s", E)

    clVariables.G_dctReceivedMessages = dctReceivedMessages

    return render_template('home.html')

@app.route("/editFavs", methods=['POST', 'GET'])
def acEditFavs():
    '''
        This function is called whenever you edit Favourite messages

        Args:

        Returns:
            (str): Html home page.
        Raises:
            Raises no exceptions
    '''
    dctData = request.values
    dctData = ImmutableMultiDict(dctData).to_dict()

    dctCheckedMessages = {}
    if 'value' in dctData:
        acCheckedMsg   = dctData['value']

        dctCheckedMessages = generate_Json.getCheckedMsgs()
        
        if acCheckedMsg in dctCheckedMessages["messages"]:
            indexOfChecked = dctCheckedMessages["messages"].index(acCheckedMsg)
            del dctCheckedMessages["messages"][indexOfChecked]
        elif acCheckedMsg not in dctCheckedMessages["messages"]:
            dctCheckedMessages["messages"].append(acCheckedMsg)

    elif 'value2' in dctData:
        acCheckedMsg   = dctData['value2']

        dctCheckedMessages = generate_Json.getCheckedMsgs()

        if acCheckedMsg in dctCheckedMessages["messages"]:
            indexOfChecked = dctCheckedMessages["messages"].index(acCheckedMsg)
            del dctCheckedMessages["messages"][indexOfChecked]
        
    elif 'valueFav' in dctData:
        acCheckedMsg   = dctData['valueFav']

        dctCheckedMessages = generate_Json.getCheckedMsgs()

        if acCheckedMsg in dctCheckedMessages["messages"]:
            indexOfChecked = dctCheckedMessages["messages"].index(acCheckedMsg)
            del dctCheckedMessages["messages"][indexOfChecked]

    _Protocol_class.G_dctFavourites = copy.deepcopy(dctCheckedMessages)

    return render_template('home.html')

@app.route("/reset", methods=['POST', 'GET'])
def acReset():

    """
        Restart message manager, this function emtry all instances created by message manager.

        Args:

        Returns:
            (str): Html home page.
        Raises:
            Raises no exceptions
    """
    global G_dctZeroMQPubObjects
    global dctMqttObj
    global dctObjClsMqttComms
    global dctFieldVal
    global dctReceivedFieldVal
    global objMQTTQueue
    global G_dctActivePipes
    _Protocol_class.G_stopThread = True
    time.sleep(2)

    dctFavMessages      = {"messages":[]}
    dctRecordMsgs       = {"msgs":[]}
    clVariables.G_dctReceivedMessages = {}
    dctJsonStructure       = {"xmls":[]}
    dctJsonPipes           = {}    

    with open(os.path.join(os.path.dirname(__file__),"Structure/messagesToRecord.json"), 'w') as f:
        f.write(json.dumps(dctRecordMsgs))
        f.close()

    objAutoScriptObject = clsMessageObjects()
    for acKeyName, objName in _Protocol_class.G_dctAutoScriptOnlyMQTT_ZMQ_Objects.items():
        if acKeyName in _Protocol_class.G_dctAutoScriptOnlyZMQ_Objects:
            objAutoScriptObject.vUnbindPubSoc(objName, acKeyName)
        else:
            try:
                objName.disconnect() # disconnect gracefully
                objName.loop_stop() # stops network loop
            except Exception as E:
                logging.error("Cannot stop thread, error-> %s", E)

    _Protocol_class.G_dctJsonFileSender = copy.deepcopy(dctJsonStructure)
    _Protocol_class.G_dctJsonFile = copy.deepcopy(dctJsonStructure)
    _Protocol_class.G_dctPipes = copy.deepcopy(dctJsonPipes)
    _Protocol_class.G_dctFavourites = copy.deepcopy(dctFavMessages)

    _Protocol_class.G_dctRecordedMessages = OrderedDict()
    _Protocol_class.G_dctFieldAndVal = OrderedDict()
    _Protocol_class.G_dctFieldAndValReceived = OrderedDict()
    _Protocol_class.G_dctJsonAutoScriptFile = OrderedDict()
    _Protocol_class.G_dctMQTT_ZeroMQ_Connections = OrderedDict()
    _Protocol_class.G_dctRepeatAutoscriptingParThread = OrderedDict()
    _Protocol_class.G_dctMQTT_ZMQ_Objects = OrderedDict()
    _Protocol_class.G_dctAutoScriptOnlyMQTT_ZMQ_Objects = OrderedDict()
    _Protocol_class.G_dctAutoScriptOnlyZMQ_Objects = OrderedDict()
    _Protocol_class.G_lstBusySendingScript = list()
    G_dctStopSingleThread = dict()

    
    acRecordPath = os.path.join(os.path.dirname(__file__), "record/json/")
    lstRecordFiles = os.listdir(acRecordPath)
    for i in range(len(lstRecordFiles)):
        if lstRecordFiles[i] != '.gitignore':
            os.remove(acRecordPath+lstRecordFiles[i])

    acRecordPath2 = os.path.join(os.path.dirname(__file__), "record/csv/")
    lstRecordFiles2 = os.listdir(acRecordPath2)
    for i in range(len(lstRecordFiles2)):
        if lstRecordFiles2[i] != '.gitignore':
            os.remove(acRecordPath2+lstRecordFiles2[i])

    #unbind zeroMQ
    for objKey, objVal in G_dctZeroMQPubObjects.items():
        objVal.vUnbindPubSoc(objKey)
    #disconnect MQTT
    for acBrokerName, brokerObject in dctMqttObj.items():
        brokerObject.vDisconnect()

    dctMqttObj = OrderedDict()
    dctObjClsMqttComms = OrderedDict()
    dctFieldVal = OrderedDict()
    dctReceivedFieldVal = OrderedDict()
    G_dctZeroMQPubObjects = OrderedDict()
    G_dctActivePipes = OrderedDict()
    objMQTTQueue = queue.Queue()
    try:
        for acFileName, objFile in _Protocol_class.G_dctStopSingleThread.items():
            objFile.bStopSendingThread = True
    except Exception as E:
        logging.error("Failed to stop sending message")

    return render_template('home.html')

@app.route("/record", methods=['POST', 'GET'])
def acRecord():
    """
        This methods records messages.

        Args:

        Returns:
            (str): Html home page.
        Raises:
    """
    dctData = ImmutableMultiDict(request.values)
    dctData = ImmutableMultiDict(dctData).to_dict()
    acReceivedKey = dctData["key"]

    lstRecordedMsgs = json.loads(generate_Json.getRecordingMsgs())

    if acReceivedKey in lstRecordedMsgs['msgs']:
        lstRecordedMsgs['msgs'].remove(acReceivedKey)
    else:
        lstRecordedMsgs['msgs'].append(acReceivedKey)

    with open(os.path.join(os.path.dirname(__file__),"Structure/messagesToRecord.json"), 'w') as f:
        f.write(json.dumps(lstRecordedMsgs))
        f.close()

    return json.dumps(lstRecordedMsgs)

@app.route("/saveMsgs", methods=['POST', 'GET'])
def acSaveMsgs():
    """
        This methods saves recorded messages.

        Args:

        Returns:
           acFileName (str): File name.
        Raises:
    """
    dctData = ImmutableMultiDict(request.values)
    dctData = ImmutableMultiDict(dctData).to_dict()

    dctRecordedMsgs = json.loads(generate_Json.getRecordedMessages())

    for acKey, dctVal in dctData.items():
        dctMsgToSave = dctRecordedMsgs[dctVal]
        acFileName = dctRecordedMsgs[dctVal]["Name"]
        with open(os.path.join(os.path.dirname(__file__),"record/json/"+acFileName+".json"), 'w') as f:
            f.write(json.dumps(dctMsgToSave))
            f.close()
    return acFileName

@app.route("/saveCsvMsgs", methods=['POST', 'GET'])
def acCreateCsv():
    """
        This methods creates a csv file.

        Args:

        Returns:
           acFileName (str): File name.
        Raises:
    """
    dctData = ImmutableMultiDict(request.values)
    dctData = ImmutableMultiDict(dctData).to_dict()

    dctRecordedMsgs = json.loads(generate_Json.getRecordedMessages())

    for acKey, dctVal in dctData.items():
        dctMsgToSave = dctRecordedMsgs[dctVal]
        acFileName = dctRecordedMsgs[dctVal]["Name"]
        with open(os.path.join(os.path.dirname(__file__),"record/json/"+acFileName+".json"), 'w') as f:
            f.write(json.dumps(dctMsgToSave))
            f.close()

    createCSV.main("record/json/"+acFileName+".json", "record/csv/")
    
    return acFileName

@app.route("/deleteMsgs", methods=['POST', 'GET'])
def acDeleteMsgs():
    """
        This methods saves recorded messages.

        Args:

        Returns:
           (str) function return status.
        Raises:
    """
    dctData = ImmutableMultiDict(request.values)
    dctData = ImmutableMultiDict(dctData).to_dict()

    dctRecordedMsgs = json.loads(generate_Json.getRecordedMessages())

    for acKey, dctVal in dctData.items():
        del dctRecordedMsgs[acKey]
        _Protocol_class.G_dctRecordedMessages = copy.deepcopy(dctRecordedMsgs)

    return "deleted"

@app.before_first_request
def vBeforeFirstRequest():
    """
        This methods resert webMM
        Args:

        Returns:

        Raises:
    """
    acReset()
    vReadDatabaseDirectory()

def handler(signal, frame):
    print("CTRL-C pressed!")
    sys.exit(0)

#==========================================
# GLOBAL SPACE
#==========================================
# Register a signal handler for SIGINT
signal.signal(signal.SIGINT, handler)

def vServerMainMethod():
    """ This is a public function is used as a constructor for the server.py module.

    Args:

    Returns:

    Raises:
        Raises no exceptions
    """

    # At this point we already have a refence to the Flask object called 'app'.
    # It was constructed at the beginning of this module (right at the top)

    # Create a new logger manager instance
    objClsLoggerManager = logging_manager.clsLoggingManager()
    objClsLoggerManager.vConfigureLogger()
    objRootLogger = objClsLoggerManager.objGetLoggerInstance()

    # Set the log level to INFO
    objRootLogger.setLevel(logging.INFO)

    # Indicate that the logging has started
    logging.info("======================================================")
    logging.info("= WEBMM FLASK PROCESS                                =")
    logging.info("= WEBMM VERSION -> V3.0.0                            =")
    logging.info("======================================================")
    logging.info("Process name %s: ",__name__)

    logging.info("Python version is [major] %d ", sys.version_info[0])
    logging.info("Python version is [minor] %d ", sys.version_info[1])

    # At this point we already have a refence to the Flask object called 'app'.
    # It was constructed at the beginning of this module (right at the top)

    logging.info("Flask app.jinja_env.auto_reload: %s", str(app.jinja_env.auto_reload))
    logging.info("Flask app.config['TEMPLATES_AUTO_RELOAD']: %s", str(app.config['TEMPLATES_AUTO_RELOAD']))

    autogen_common_types.vGetCommonTypes()
    return

if __name__ == "server":
    vServerMainMethod()

if __name__=='__main__':
    print("The WebMM should not be called using the the \"flask run\" command.")
    print("In this case it was run directly as \"python3.6 server.py\" which is not allowed")
    print("Exiting WebMM")
    sys.exit()
