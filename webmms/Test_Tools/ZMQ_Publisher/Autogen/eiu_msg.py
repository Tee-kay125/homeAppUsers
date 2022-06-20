#!/usr/bin/env python3.6
"""
    Autogen - Do not edit by hand!
    Autogen - Do not edit by hand!
    Autogen - Do not edit by hand!

    Generated using Python 3.6.9
    Rendered with Jinja2 2.11.1
    Generated on 2020-07-16 12:29:09 SAST
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

# IMPORT CODE START
from Autogen.mw_common_types import *
from Autogen.adcs_common_types import *
# IMPORT CODE END

# TYPEDEFS START
class sEIU_SENSOR_TRACK_INFO(clsAdcsStructType):
    """Public class definition of type sEIU_SENSOR_TRACK_INFO
    """
    def __init__(self, defaultValue=0):
        super().__init__("sEIU_SENSOR_TRACK_INFO")
        self.u4OriginTrackNumber = clsAdcsBaseType("U4", 0)
        self.vAddType("u4OriginTrackNumber")
        self.sKinematics = sADCS_SENSOR_TRACK_KINEMATICS()
        self.vAddType("sKinematics")
        self.sClassification = sADCS_CLASSIFICATION()
        self.vAddType("sClassification")
        self.sIdentification = sADCS_IDENTIFICATION()
        self.vAddType("sIdentification")
        self.sTrackQuality = sADCS_QVALUE()
        self.vAddType("sTrackQuality")


vAddClass("sEIU_SENSOR_TRACK_INFO",sEIU_SENSOR_TRACK_INFO)


# TYPEDEFS END

# MESSAGE HEADERS START
class sEIU_STATUS_REPORT_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sEIU_STATUS_REPORT_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_EIU)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0000)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sEIU_STATUS_REPORT_UNSOL_MESSAGE_HEADER", sEIU_STATUS_REPORT_UNSOL_MESSAGE_HEADER)


class sEIU_END_OF_SETUP_CMD_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sEIU_END_OF_SETUP_CMD
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_CMD)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_EIU)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0001)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sEIU_END_OF_SETUP_CMD_MESSAGE_HEADER", sEIU_END_OF_SETUP_CMD_MESSAGE_HEADER)


class sEIU_END_OF_SETUP_CMD_RSP_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sEIU_END_OF_SETUP_CMD_RSP
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_CMD_RSP)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_EIU)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0001)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sEIU_END_OF_SETUP_CMD_RSP_MESSAGE_HEADER", sEIU_END_OF_SETUP_CMD_RSP_MESSAGE_HEADER)


class sEIU_END_OF_READY_CMD_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sEIU_END_OF_READY_CMD
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_CMD)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_EIU)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0002)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sEIU_END_OF_READY_CMD_MESSAGE_HEADER", sEIU_END_OF_READY_CMD_MESSAGE_HEADER)


class sEIU_END_OF_READY_CMD_RSP_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sEIU_END_OF_READY_CMD_RSP
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_CMD_RSP)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_EIU)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0002)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sEIU_END_OF_READY_CMD_RSP_MESSAGE_HEADER", sEIU_END_OF_READY_CMD_RSP_MESSAGE_HEADER)


class sEIU_SHUTDOWN_CMD_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sEIU_SHUTDOWN_CMD
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_CMD)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_EIU)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0003)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sEIU_SHUTDOWN_CMD_MESSAGE_HEADER", sEIU_SHUTDOWN_CMD_MESSAGE_HEADER)


class sEIU_SHUTDOWN_CMD_RSP_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sEIU_SHUTDOWN_CMD_RSP
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_CMD_RSP)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_EIU)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0003)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sEIU_SHUTDOWN_CMD_RSP_MESSAGE_HEADER", sEIU_SHUTDOWN_CMD_RSP_MESSAGE_HEADER)


class sEIU_SENSOR_POINT_TRACK_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sEIU_SENSOR_POINT_TRACK_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_EIU)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0010)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sEIU_SENSOR_POINT_TRACK_UNSOL_MESSAGE_HEADER", sEIU_SENSOR_POINT_TRACK_UNSOL_MESSAGE_HEADER)


class sEIU_SENSOR_BEARING_TRACK_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sEIU_SENSOR_BEARING_TRACK_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_EIU)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0011)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sEIU_SENSOR_BEARING_TRACK_UNSOL_MESSAGE_HEADER", sEIU_SENSOR_BEARING_TRACK_UNSOL_MESSAGE_HEADER)


# MESSAGE HEADERS END

# PAYLOADS START
class sEIU_STATUS_REPORT_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sEIU_STATUS_REPORT_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.sModuleInfo = sADCS_MODULE_INFO()
        self.vAddType("sModuleInfo")
        self.sModuleState = sADCS_MODULE_STATE()
        self.vAddType("sModuleState")
        self.e1ConnectionStatus = E1_MW_BOOLEAN_ENUM(E1_MW_BOOLEAN_ENUM.MW_BOOLEAN_FALSE)
        self.vAddType("e1ConnectionStatus")
        self.u8TracksProcessedCounter = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TracksProcessedCounter")


vAddClass("sEIU_STATUS_REPORT_UNSOL_PL", sEIU_STATUS_REPORT_UNSOL_PL)


class sEIU_SENSOR_POINT_TRACK_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sEIU_SENSOR_POINT_TRACK_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.sTimestamp = sADCS_TIMESTAMP()
        self.vAddType("sTimestamp")
        self.u4TrackNumber = clsAdcsBaseType("U4", 0)
        self.vAddType("u4TrackNumber")
        self.sDescription = sADCS_STRING24()
        self.vAddType("sDescription")
        self.sTrackInfo = sEIU_SENSOR_TRACK_INFO()
        self.vAddType("sTrackInfo")
        self.e1Delete = E1_MW_BOOLEAN_ENUM(E1_MW_BOOLEAN_ENUM.MW_BOOLEAN_FALSE)
        self.vAddType("e1Delete")


vAddClass("sEIU_SENSOR_POINT_TRACK_UNSOL_PL", sEIU_SENSOR_POINT_TRACK_UNSOL_PL)


class sEIU_SENSOR_BEARING_TRACK_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sEIU_SENSOR_BEARING_TRACK_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.sTimestamp = sADCS_TIMESTAMP()
        self.vAddType("sTimestamp")
        self.u4TrackNumber = clsAdcsBaseType("U4", 0)
        self.vAddType("u4TrackNumber")
        self.sDescription = sADCS_STRING24()
        self.vAddType("sDescription")
        self.sTrackInfo = sEIU_SENSOR_TRACK_INFO()
        self.vAddType("sTrackInfo")
        self.e1Delete = E1_MW_BOOLEAN_ENUM(E1_MW_BOOLEAN_ENUM.MW_BOOLEAN_FALSE)
        self.vAddType("e1Delete")


vAddClass("sEIU_SENSOR_BEARING_TRACK_UNSOL_PL", sEIU_SENSOR_BEARING_TRACK_UNSOL_PL)


# PAYLOADS END

# MESSAGES START
class sEIU_STATUS_REPORT_UNSOL(clsAdcsMessageType):
    """Public class definition of type sEIU_STATUS_REPORT_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sEIU_STATUS_REPORT_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sEIU_STATUS_REPORT_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sEIU_STATUS_REPORT_UNSOL", sEIU_STATUS_REPORT_UNSOL)


class sEIU_END_OF_SETUP_CMD(clsAdcsMessageType):
    """Public class definition of type sEIU_END_OF_SETUP_CMD
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sEIU_END_OF_SETUP_CMD_MESSAGE_HEADER()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sEIU_END_OF_SETUP_CMD", sEIU_END_OF_SETUP_CMD)


class sEIU_END_OF_SETUP_CMD_RSP(clsAdcsMessageType):
    """Public class definition of type sEIU_END_OF_SETUP_CMD_RSP
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sEIU_END_OF_SETUP_CMD_RSP_MESSAGE_HEADER()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sEIU_END_OF_SETUP_CMD_RSP", sEIU_END_OF_SETUP_CMD_RSP)


class sEIU_END_OF_READY_CMD(clsAdcsMessageType):
    """Public class definition of type sEIU_END_OF_READY_CMD
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sEIU_END_OF_READY_CMD_MESSAGE_HEADER()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sEIU_END_OF_READY_CMD", sEIU_END_OF_READY_CMD)


class sEIU_END_OF_READY_CMD_RSP(clsAdcsMessageType):
    """Public class definition of type sEIU_END_OF_READY_CMD_RSP
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sEIU_END_OF_READY_CMD_RSP_MESSAGE_HEADER()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sEIU_END_OF_READY_CMD_RSP", sEIU_END_OF_READY_CMD_RSP)


class sEIU_SHUTDOWN_CMD(clsAdcsMessageType):
    """Public class definition of type sEIU_SHUTDOWN_CMD
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sEIU_SHUTDOWN_CMD_MESSAGE_HEADER()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sEIU_SHUTDOWN_CMD", sEIU_SHUTDOWN_CMD)


class sEIU_SHUTDOWN_CMD_RSP(clsAdcsMessageType):
    """Public class definition of type sEIU_SHUTDOWN_CMD_RSP
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sEIU_SHUTDOWN_CMD_RSP_MESSAGE_HEADER()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sEIU_SHUTDOWN_CMD_RSP", sEIU_SHUTDOWN_CMD_RSP)


class sEIU_SENSOR_POINT_TRACK_UNSOL(clsAdcsMessageType):
    """Public class definition of type sEIU_SENSOR_POINT_TRACK_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sEIU_SENSOR_POINT_TRACK_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sEIU_SENSOR_POINT_TRACK_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sEIU_SENSOR_POINT_TRACK_UNSOL", sEIU_SENSOR_POINT_TRACK_UNSOL)


class sEIU_SENSOR_BEARING_TRACK_UNSOL(clsAdcsMessageType):
    """Public class definition of type sEIU_SENSOR_BEARING_TRACK_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sEIU_SENSOR_BEARING_TRACK_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sEIU_SENSOR_BEARING_TRACK_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sEIU_SENSOR_BEARING_TRACK_UNSOL", sEIU_SENSOR_BEARING_TRACK_UNSOL)


# MESSAGES END




