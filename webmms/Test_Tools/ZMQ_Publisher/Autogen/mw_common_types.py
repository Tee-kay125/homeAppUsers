#!/usr/bin/env python3.6
"""
    Autogen - Do not edit by hand!
    Autogen - Do not edit by hand!
    Autogen - Do not edit by hand!

    Generated using Python 3.6.9
    Rendered with Jinja2 2.11.1
    Generated on 2020-07-16 12:29:13 SAST
"""


from Autogen.adcs_base_types import clsAdcsBaseType
from Autogen.adcs_base_types import clsAdcsEnumType
from Autogen.adcs_base_types import clsAdcsEnumArrayType
from Autogen.adcs_base_types import clsAdcsStructType
from Autogen.adcs_base_types import clsAdcsStructArrayType
from Autogen.adcs_base_types import clsAdcsMessageType
from Autogen.adcs_base_types import vAddEnum
from Autogen.adcs_base_types import vAddClass
from Autogen.adcs_base_types import vAddMessage
from Autogen.adcs_base_types import clsAdcsHeaderStructType
from Autogen.adcs_base_types import clsAdcsMessageStructType


# TYPEDEFS START
class E2_MW_MESSAGE_TYPE(clsAdcsEnumType):
    """Public class definition of type E2_MW_MESSAGE_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U2", defaultValue)
    MW_MESSAGE_TYPE_CMD = 0x0000
    MW_MESSAGE_TYPE_CMD_RSP = 0x0001
    MW_MESSAGE_TYPE_REQ = 0x0002
    MW_MESSAGE_TYPE_REQ_RSP = 0x0003
    MW_MESSAGE_TYPE_UNSOL = 0x0004


vAddEnum("E2_MW_MESSAGE_TYPE", E2_MW_MESSAGE_TYPE)


class E2_MW_MESSAGE_STATUS(clsAdcsEnumType):
    """Public class definition of type E2_MW_MESSAGE_STATUS
    """
    def __init__(self, defaultValue=0):
        super().__init__("U2", defaultValue)
    MW_MESSAGE_STATUS_NORMAL = 0x0000
    MW_MESSAGE_STATUS_INVALID_FIELD = 0x0001
    MW_MESSAGE_STATUS_FIELD_MISSING = 0x0002
    MW_MESSAGE_STATUS_MODE_ERROR = 0x0003
    MW_MESSAGE_STATUS_HARDWARE_ERROR = 0x0004
    MW_MESSAGE_STATUS_UNDEF_MSG_ID = 0x0005
    MW_MESSAGE_STATUS_UNDEF_SUB_DEST = 0x0006
    MW_MESSAGE_STATUS_NOT_READY = 0x0007
    MW_MESSAGE_STATUS_TIMEOUT = 0x0008
    MW_MESSAGE_STATUS_SOFTWARE_ERROR = 0x0009
    MW_MESSAGE_STATUS_INVALID_MSG_TYPE = 0x000A
    MW_MESSAGE_STATUS_IN_PROGRESS = 0x000B
    MW_MESSAGE_STATUS_INVALID_MSG_FIELD = 0x000C


vAddEnum("E2_MW_MESSAGE_STATUS", E2_MW_MESSAGE_STATUS)


class E2_MW_MODULE_ADDRESS(clsAdcsEnumType):
    """Public class definition of type E2_MW_MODULE_ADDRESS
    """
    def __init__(self, defaultValue=0):
        super().__init__("U2", defaultValue)
    MW_MODULE_ADDRESS_RESERVED = 0x0000
    MW_MODULE_ADDRESS_TEWA = 0x0001
    MW_MODULE_ADDRESS_TM = 0x0002
    MW_MODULE_ADDRESS_PDBP = 0x0003
    MW_MODULE_ADDRESS_OLHM = 0x0004
    MW_MODULE_ADDRESS_DR = 0x0005
    MW_MODULE_ADDRESS_EIU = 0x0006
    MW_MODULE_ADDRESS_HMI = 0x0007
    MW_MODULE_ADDRESS_DSF = 0x0008
    MW_MODULE_ADDRESS_ACI = 0x0009
    MW_MODULE_ADDRESS_GATEWAY = 0x000a
    MW_MODULE_ADDRESS_SF1 = 0x000b
    MW_MODULE_ADDRESS_SF2 = 0x000c
    MW_MODULE_ADDRESS_SF3 = 0x000d
    MW_MODULE_ADDRESS_TEST = 0x00ff
    MW_MODULE_ADDRESS_MGB = 0x0100
    MW_MODULE_ADDRESS_ISG = 0x0200
    MW_MODULE_ADDRESS_MMS = 0x0300
    MW_MODULE_ADDRESS_UNKNOWN = 0xFFFF


vAddEnum("E2_MW_MODULE_ADDRESS", E2_MW_MODULE_ADDRESS)


class E1_MW_BOOLEAN_ENUM(clsAdcsEnumType):
    """Public class definition of type E1_MW_BOOLEAN_ENUM
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    MW_BOOLEAN_FALSE = 0x00
    MW_BOOLEAN_TRUE = 0x01


vAddEnum("E1_MW_BOOLEAN_ENUM", E1_MW_BOOLEAN_ENUM)


# TYPEDEFS END







