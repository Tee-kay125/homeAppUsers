import logging
from Comms.mqtt_manager import clsMqttManager
from Comms.processing import clsProcessing
from Comms import Protocol_class
import copy
from enum import Enum

class E_WEBMM_PROCESSES(Enum):
    I_MAIN_PROCESS = 1
    I_AUTOSCRIPT_PROCESS = 2


class clsCommsManager:
    """This is a class is used as a base class

    Args:

    """

    def __init__(self):
        pass

    def vSend(self, acTopicPar, lstPayloadPar):
        raise NotImplementedError("Subclass must implement abstract method")

    def vReceive(self, acTopicPar, btaDataPar):
        raise NotImplementedError("Subclass must implement abstract method")


class clsMqttComms(clsCommsManager):
    """This is a class is used for MQTT comms and inherits from the clsCommsManager

    Args:
        objClsMqttManagerPar (mqtt class object):
        acMsgKeyPar (string): any message key from the xml

    """

    def __init__(self, objClsMqttManagerPar, acMsgKeyPar):
        """
            Constructor: get all message topics of the xml and subscribe.
        """
        self.objClsMqttManager = objClsMqttManagerPar
        self.objClsProcessing = clsProcessing(E_WEBMM_PROCESSES.I_MAIN_PROCESS.value)
        self.objClsMqttManager.vSubscribe(self.objClsProcessing.lstGetSubMqttTopic(acMsgKeyPar), self)

    def vSend(self, acTopicPar, lstPayloadPar):
        """ This method is called when sending data.

        Args:
            topic (string: message topic.
            lstPayloadPar (list): message payload, only values.

        Returns:

        Raises:
            Raises no exceptions
        """
        try:
            self.objClsMqttManager.vSend(acTopicPar, lstPayloadPar)
        except Exception as E:
            logging.error("Could not send message error -> %s", E)

    def vReceive(self, acTopicPar, btaDataPar):
        """ This is method is called when data is received.

        Args:
            data (bytes): The first parameter. The received data.

        Returns:

        Raises:
            Raises no exceptions
        """
        try:
            objProtocol = Protocol_class.RRS_MMI(self.objClsMqttManager)
            objProtocol.vReceive(acTopicPar, btaDataPar)
        except Exception as E:
            logging.error("Could not pass received data to protocol class -> %s", E)
