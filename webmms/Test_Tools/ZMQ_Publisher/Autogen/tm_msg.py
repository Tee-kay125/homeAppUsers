#!/usr/bin/env python3.6
"""
    Autogen - Do not edit by hand!
    Autogen - Do not edit by hand!
    Autogen - Do not edit by hand!

    Generated using Python 3.6.9
    Rendered with Jinja2 2.11.1
    Generated on 2020-07-16 12:29:11 SAST
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
class E1_TM_OVERRIDE_CLASS(clsAdcsEnumType):
    """Public class definition of type E1_TM_OVERRIDE_CLASS
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    CLASS_NOT_OVERRIDEN = 0x00
    HOSTILITY = 0x01
    HOSTILITY_REFRESH = 0x02
    ENVIRONMENT = 0x03
    ENVIRONMENT_REFRESH = 0x04
    TYPE = 0x05
    TYPE_REFRESH = 0x06
    DESCRIPTION = 0x07
    DESCRIPTION_CLEAR = 0x08
    HEIGHT = 0x09
    HEIGHT_REFRESH = 0x0A


vAddEnum("E1_TM_OVERRIDE_CLASS", E1_TM_OVERRIDE_CLASS)


class E1_TM_MISMATCH(clsAdcsEnumType):
    """Public class definition of type E1_TM_MISMATCH
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    NO_MISMATCH = 0x00
    MISMATCH = 0x01


vAddEnum("E1_TM_MISMATCH", E1_TM_MISMATCH)


class E1_TM_MISMATCH_CLASS(clsAdcsEnumType):
    """Public class definition of type E1_TM_MISMATCH_CLASS
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    NO_CLASS_MISMATCH = 0x00
    CORRELATION_MISMATCH = 0x01
    DECORRELATION_MISMATCH = 0x02
    ASSOCIATION_MISMATCH = 0x03
    DISASSOCIATION_MISMATCH = 0x04


vAddEnum("E1_TM_MISMATCH_CLASS", E1_TM_MISMATCH_CLASS)


class sTM_TRACK_INFO(clsAdcsStructType):
    """Public class definition of type sTM_TRACK_INFO
    """
    def __init__(self, defaultValue=0):
        super().__init__("sTM_TRACK_INFO")
        self.sKinematics = sADCS_POINT_KINEMATICS()
        self.vAddType("sKinematics")
        self.sClassification = sADCS_CLASSIFICATION()
        self.vAddType("sClassification")
        self.sIdentification = sADCS_IDENTIFICATION()
        self.vAddType("sIdentification")
        self.sComposition = sADCS_COMPOSITION()
        self.vAddType("sComposition")
        self.sTrackQuality = sADCS_QVALUE()
        self.vAddType("sTrackQuality")


vAddClass("sTM_TRACK_INFO",sTM_TRACK_INFO)


# TYPEDEFS END

# MESSAGE HEADERS START
class sTM_STATUS_REPORT_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sTM_STATUS_REPORT_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_TM)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0000)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sTM_STATUS_REPORT_UNSOL_MESSAGE_HEADER", sTM_STATUS_REPORT_UNSOL_MESSAGE_HEADER)


class sTM_END_OF_SETUP_CMD_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sTM_END_OF_SETUP_CMD
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_CMD)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_TM)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0001)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sTM_END_OF_SETUP_CMD_MESSAGE_HEADER", sTM_END_OF_SETUP_CMD_MESSAGE_HEADER)


class sTM_END_OF_SETUP_CMD_RSP_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sTM_END_OF_SETUP_CMD_RSP
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_CMD_RSP)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_TM)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0001)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sTM_END_OF_SETUP_CMD_RSP_MESSAGE_HEADER", sTM_END_OF_SETUP_CMD_RSP_MESSAGE_HEADER)


class sTM_END_OF_READY_CMD_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sTM_END_OF_READY_CMD
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_CMD)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_TM)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0002)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sTM_END_OF_READY_CMD_MESSAGE_HEADER", sTM_END_OF_READY_CMD_MESSAGE_HEADER)


class sTM_END_OF_READY_CMD_RSP_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sTM_END_OF_READY_CMD_RSP
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_CMD_RSP)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_TM)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0002)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sTM_END_OF_READY_CMD_RSP_MESSAGE_HEADER", sTM_END_OF_READY_CMD_RSP_MESSAGE_HEADER)


class sTM_SHUTDOWN_CMD_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sTM_SHUTDOWN_CMD
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_CMD)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_TM)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0003)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sTM_SHUTDOWN_CMD_MESSAGE_HEADER", sTM_SHUTDOWN_CMD_MESSAGE_HEADER)


class sTM_SHUTDOWN_CMD_RSP_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sTM_SHUTDOWN_CMD_RSP
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_CMD_RSP)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_TM)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0003)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sTM_SHUTDOWN_CMD_RSP_MESSAGE_HEADER", sTM_SHUTDOWN_CMD_RSP_MESSAGE_HEADER)


class sTM_SYSTEM_POINT_TRACK_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sTM_SYSTEM_POINT_TRACK_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_TM)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0010)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sTM_SYSTEM_POINT_TRACK_UNSOL_MESSAGE_HEADER", sTM_SYSTEM_POINT_TRACK_UNSOL_MESSAGE_HEADER)


class sTM_SYSTEM_BEARING_TRACK_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sTM_SYSTEM_BEARING_TRACK_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_TM)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0011)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sTM_SYSTEM_BEARING_TRACK_UNSOL_MESSAGE_HEADER", sTM_SYSTEM_BEARING_TRACK_UNSOL_MESSAGE_HEADER)


class sTM_PROPOSED_FLAG_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sTM_PROPOSED_FLAG_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_TM)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0020)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sTM_PROPOSED_FLAG_UNSOL_MESSAGE_HEADER", sTM_PROPOSED_FLAG_UNSOL_MESSAGE_HEADER)


class sTM_MISMATCH_FLAG_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sTM_MISMATCH_FLAG_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_TM)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0021)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sTM_MISMATCH_FLAG_UNSOL_MESSAGE_HEADER", sTM_MISMATCH_FLAG_UNSOL_MESSAGE_HEADER)


class sTM_OVERRIDE_FAIL_FLAG_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sTM_OVERRIDE_FAIL_FLAG_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_TM)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0022)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sTM_OVERRIDE_FAIL_FLAG_UNSOL_MESSAGE_HEADER", sTM_OVERRIDE_FAIL_FLAG_UNSOL_MESSAGE_HEADER)


class sTM_CORRELATION_ENGINEERING_DATA_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sTM_CORRELATION_ENGINEERING_DATA_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_TM)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0030)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sTM_CORRELATION_ENGINEERING_DATA_UNSOL_MESSAGE_HEADER", sTM_CORRELATION_ENGINEERING_DATA_UNSOL_MESSAGE_HEADER)


class sTM_DECORRELATION_ENGINEERING_DATA_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sTM_DECORRELATION_ENGINEERING_DATA_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_TM)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0031)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sTM_DECORRELATION_ENGINEERING_DATA_UNSOL_MESSAGE_HEADER", sTM_DECORRELATION_ENGINEERING_DATA_UNSOL_MESSAGE_HEADER)


class sTM_ASSOCIATION_ENGINEERING_DATA_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sTM_ASSOCIATION_ENGINEERING_DATA_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_TM)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0032)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sTM_ASSOCIATION_ENGINEERING_DATA_UNSOL_MESSAGE_HEADER", sTM_ASSOCIATION_ENGINEERING_DATA_UNSOL_MESSAGE_HEADER)


class sTM_DISSOCIATION_ENGINEERING_DATA_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sTM_DISSOCIATION_ENGINEERING_DATA_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_TM)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0033)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sTM_DISSOCIATION_ENGINEERING_DATA_UNSOL_MESSAGE_HEADER", sTM_DISSOCIATION_ENGINEERING_DATA_UNSOL_MESSAGE_HEADER)


class sTM_THC_ENGINEERING_DATA_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sTM_THC_ENGINEERING_DATA_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_TM)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0034)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sTM_THC_ENGINEERING_DATA_UNSOL_MESSAGE_HEADER", sTM_THC_ENGINEERING_DATA_UNSOL_MESSAGE_HEADER)


class sTM_TYPE_CLASSIFICATION_ENGINEERING_DATA_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sTM_TYPE_CLASSIFICATION_ENGINEERING_DATA_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_TM)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0035)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sTM_TYPE_CLASSIFICATION_ENGINEERING_DATA_UNSOL_MESSAGE_HEADER", sTM_TYPE_CLASSIFICATION_ENGINEERING_DATA_UNSOL_MESSAGE_HEADER)


# MESSAGE HEADERS END

# PAYLOADS START
class sTM_STATUS_REPORT_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sTM_STATUS_REPORT_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.sModuleInfo = sADCS_MODULE_INFO()
        self.vAddType("sModuleInfo")
        self.sModuleState = sADCS_MODULE_STATE()
        self.vAddType("sModuleState")


vAddClass("sTM_STATUS_REPORT_UNSOL_PL", sTM_STATUS_REPORT_UNSOL_PL)


class sTM_SYSTEM_POINT_TRACK_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sTM_SYSTEM_POINT_TRACK_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.sTimestamp = sADCS_TIMESTAMP()
        self.vAddType("sTimestamp")
        self.u4TrackNumber = clsAdcsBaseType("U4", 0)
        self.vAddType("u4TrackNumber")
        self.sDescription = sADCS_STRING24()
        self.vAddType("sDescription")
        self.sLocalTrackInfo = sTM_TRACK_INFO()
        self.vAddType("sLocalTrackInfo")
        self.sIntegratedTrackInfo = sTM_TRACK_INFO()
        self.vAddType("sIntegratedTrackInfo")
        self.e1Delete = E1_MW_BOOLEAN_ENUM(E1_MW_BOOLEAN_ENUM.MW_BOOLEAN_FALSE)
        self.vAddType("e1Delete")


vAddClass("sTM_SYSTEM_POINT_TRACK_UNSOL_PL", sTM_SYSTEM_POINT_TRACK_UNSOL_PL)


class sTM_SYSTEM_BEARING_TRACK_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sTM_SYSTEM_BEARING_TRACK_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.sTimestamp = sADCS_TIMESTAMP()
        self.vAddType("sTimestamp")
        self.u4TrackNumber = clsAdcsBaseType("U4", 0)
        self.vAddType("u4TrackNumber")
        self.sDescription = sADCS_STRING24()
        self.vAddType("sDescription")
        self.sTrackInfo = sTM_TRACK_INFO()
        self.vAddType("sTrackInfo")
        self.e1Delete = E1_MW_BOOLEAN_ENUM(E1_MW_BOOLEAN_ENUM.MW_BOOLEAN_FALSE)
        self.vAddType("e1Delete")


vAddClass("sTM_SYSTEM_BEARING_TRACK_UNSOL_PL", sTM_SYSTEM_BEARING_TRACK_UNSOL_PL)


class sTM_PROPOSED_FLAG_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sTM_PROPOSED_FLAG_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.sTimestamp = sADCS_TIMESTAMP()
        self.vAddType("sTimestamp")
        self.au4TrackNumbers = clsAdcsBaseType("U4:2", 0)
        self.vAddType("au4TrackNumbers")
        self.e1EnvironmentMismatch = E1_TM_MISMATCH(E1_TM_MISMATCH.NO_MISMATCH)
        self.vAddType("e1EnvironmentMismatch")
        self.e1TypeMismatch = E1_TM_MISMATCH(E1_TM_MISMATCH.NO_MISMATCH)
        self.vAddType("e1TypeMismatch")
        self.e1HostilityMismatch = E1_TM_MISMATCH(E1_TM_MISMATCH.NO_MISMATCH)
        self.vAddType("e1HostilityMismatch")


vAddClass("sTM_PROPOSED_FLAG_UNSOL_PL", sTM_PROPOSED_FLAG_UNSOL_PL)


class sTM_MISMATCH_FLAG_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sTM_MISMATCH_FLAG_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.sTimestamp = sADCS_TIMESTAMP()
        self.vAddType("sTimestamp")
        self.e1Class = E1_TM_MISMATCH_CLASS(E1_TM_MISMATCH_CLASS.NO_CLASS_MISMATCH)
        self.vAddType("e1Class")
        self.au4TrackNumbers = clsAdcsBaseType("U4:2", 0)
        self.vAddType("au4TrackNumbers")
        self.e1EnvironmentMismatch = E1_TM_MISMATCH(E1_TM_MISMATCH.NO_MISMATCH)
        self.vAddType("e1EnvironmentMismatch")
        self.e1TypeMismatch = E1_TM_MISMATCH(E1_TM_MISMATCH.NO_MISMATCH)
        self.vAddType("e1TypeMismatch")
        self.e1HostilityMismatch = E1_TM_MISMATCH(E1_TM_MISMATCH.NO_MISMATCH)
        self.vAddType("e1HostilityMismatch")


vAddClass("sTM_MISMATCH_FLAG_UNSOL_PL", sTM_MISMATCH_FLAG_UNSOL_PL)


class sTM_OVERRIDE_FAIL_FLAG_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sTM_OVERRIDE_FAIL_FLAG_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.sTimestamp = sADCS_TIMESTAMP()
        self.vAddType("sTimestamp")
        self.e1OverrideClass = E1_TM_OVERRIDE_CLASS(E1_TM_OVERRIDE_CLASS.CLASS_NOT_OVERRIDEN)
        self.vAddType("e1OverrideClass")
        self.u4TrackNumber = clsAdcsBaseType("U4", 0)
        self.vAddType("u4TrackNumber")


vAddClass("sTM_OVERRIDE_FAIL_FLAG_UNSOL_PL", sTM_OVERRIDE_FAIL_FLAG_UNSOL_PL)


class sTM_CORRELATION_ENGINEERING_DATA_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sTM_CORRELATION_ENGINEERING_DATA_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.sTimestamp = sADCS_TIMESTAMP()
        self.vAddType("sTimestamp")
        self.e1CorrelationResult = E1_MW_BOOLEAN_ENUM(E1_MW_BOOLEAN_ENUM.MW_BOOLEAN_FALSE)
        self.vAddType("e1CorrelationResult")
        self.au4TrackNumbers = clsAdcsBaseType("U4:2", 0)
        self.vAddType("au4TrackNumbers")
        self.sCorrelationDelta = sADCS_ECEF()
        self.vAddType("sCorrelationDelta")
        self.e1HasTrackFromSensor = E1_MW_BOOLEAN_ENUM(E1_MW_BOOLEAN_ENUM.MW_BOOLEAN_FALSE)
        self.vAddType("e1HasTrackFromSensor")
        self.e1EnvironmentMismatch = E1_TM_MISMATCH(E1_TM_MISMATCH.NO_MISMATCH)
        self.vAddType("e1EnvironmentMismatch")
        self.e1TypeMismatch = E1_TM_MISMATCH(E1_TM_MISMATCH.NO_MISMATCH)
        self.vAddType("e1TypeMismatch")
        self.e1HostilityMismatch = E1_TM_MISMATCH(E1_TM_MISMATCH.NO_MISMATCH)
        self.vAddType("e1HostilityMismatch")


vAddClass("sTM_CORRELATION_ENGINEERING_DATA_UNSOL_PL", sTM_CORRELATION_ENGINEERING_DATA_UNSOL_PL)


class sTM_DECORRELATION_ENGINEERING_DATA_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sTM_DECORRELATION_ENGINEERING_DATA_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.sTimestamp = sADCS_TIMESTAMP()
        self.vAddType("sTimestamp")
        self.e1DeCorrelationResult = E1_MW_BOOLEAN_ENUM(E1_MW_BOOLEAN_ENUM.MW_BOOLEAN_FALSE)
        self.vAddType("e1DeCorrelationResult")
        self.au4TrackNumbers = clsAdcsBaseType("U4:2", 0)
        self.vAddType("au4TrackNumbers")
        self.sDeCorrelationDelta = sADCS_ECEF()
        self.vAddType("sDeCorrelationDelta")
        self.e1EnvironmentMismatch = E1_TM_MISMATCH(E1_TM_MISMATCH.NO_MISMATCH)
        self.vAddType("e1EnvironmentMismatch")
        self.e1TypeMismatch = E1_TM_MISMATCH(E1_TM_MISMATCH.NO_MISMATCH)
        self.vAddType("e1TypeMismatch")
        self.e1HostilityMismatch = E1_TM_MISMATCH(E1_TM_MISMATCH.NO_MISMATCH)
        self.vAddType("e1HostilityMismatch")


vAddClass("sTM_DECORRELATION_ENGINEERING_DATA_UNSOL_PL", sTM_DECORRELATION_ENGINEERING_DATA_UNSOL_PL)


class sTM_ASSOCIATION_ENGINEERING_DATA_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sTM_ASSOCIATION_ENGINEERING_DATA_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.sTimestamp = sADCS_TIMESTAMP()
        self.vAddType("sTimestamp")
        self.e1AssociationResult = E1_MW_BOOLEAN_ENUM(E1_MW_BOOLEAN_ENUM.MW_BOOLEAN_FALSE)
        self.vAddType("e1AssociationResult")
        self.au4TrackNumbers = clsAdcsBaseType("U4:2", 0)
        self.vAddType("au4TrackNumbers")
        self.f8AssociationDelta = clsAdcsBaseType("F8", 0.0)
        self.vAddType("f8AssociationDelta")
        self.e1IsAssociated = E1_MW_BOOLEAN_ENUM(E1_MW_BOOLEAN_ENUM.MW_BOOLEAN_FALSE)
        self.vAddType("e1IsAssociated")
        self.e1EnvironmentMismatch = E1_TM_MISMATCH(E1_TM_MISMATCH.NO_MISMATCH)
        self.vAddType("e1EnvironmentMismatch")
        self.e1TypeMismatch = E1_TM_MISMATCH(E1_TM_MISMATCH.NO_MISMATCH)
        self.vAddType("e1TypeMismatch")
        self.e1HostilityMismatch = E1_TM_MISMATCH(E1_TM_MISMATCH.NO_MISMATCH)
        self.vAddType("e1HostilityMismatch")


vAddClass("sTM_ASSOCIATION_ENGINEERING_DATA_UNSOL_PL", sTM_ASSOCIATION_ENGINEERING_DATA_UNSOL_PL)


class sTM_DISSOCIATION_ENGINEERING_DATA_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sTM_DISSOCIATION_ENGINEERING_DATA_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.sTimestamp = sADCS_TIMESTAMP()
        self.vAddType("sTimestamp")
        self.e1DissociationResult = E1_MW_BOOLEAN_ENUM(E1_MW_BOOLEAN_ENUM.MW_BOOLEAN_FALSE)
        self.vAddType("e1DissociationResult")
        self.au4TrackNumbers = clsAdcsBaseType("U4:2", 0)
        self.vAddType("au4TrackNumbers")
        self.f8DissociationDelta = clsAdcsBaseType("F8", 0.0)
        self.vAddType("f8DissociationDelta")
        self.e1IsAssociated = E1_MW_BOOLEAN_ENUM(E1_MW_BOOLEAN_ENUM.MW_BOOLEAN_FALSE)
        self.vAddType("e1IsAssociated")
        self.e1EnvironmentMismatch = E1_TM_MISMATCH(E1_TM_MISMATCH.NO_MISMATCH)
        self.vAddType("e1EnvironmentMismatch")
        self.e1TypeMismatch = E1_TM_MISMATCH(E1_TM_MISMATCH.NO_MISMATCH)
        self.vAddType("e1TypeMismatch")
        self.e1HostilityMismatch = E1_TM_MISMATCH(E1_TM_MISMATCH.NO_MISMATCH)
        self.vAddType("e1HostilityMismatch")


vAddClass("sTM_DISSOCIATION_ENGINEERING_DATA_UNSOL_PL", sTM_DISSOCIATION_ENGINEERING_DATA_UNSOL_PL)


class sTM_THC_ENGINEERING_DATA_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sTM_THC_ENGINEERING_DATA_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.sTimestamp = sADCS_TIMESTAMP()
        self.vAddType("sTimestamp")
        self.u4TrackNumber = clsAdcsBaseType("U4", 0)
        self.vAddType("u4TrackNumber")
        self.u1CurrentThc = clsAdcsBaseType("U1", 0)
        self.vAddType("u1CurrentThc")
        self.u1AutoThc = clsAdcsBaseType("U1", 0)
        self.vAddType("u1AutoThc")
        self.u1OperatorThc = clsAdcsBaseType("U1", 0)
        self.vAddType("u1OperatorThc")
        self.u1ProposedThc = clsAdcsBaseType("U1", 0)
        self.vAddType("u1ProposedThc")
        self.u1AirLaneThc = clsAdcsBaseType("U1", 0)
        self.vAddType("u1AirLaneThc")
        self.u1AirZoneThc = clsAdcsBaseType("U1", 0)
        self.vAddType("u1AirZoneThc")
        self.u1IffThc = clsAdcsBaseType("U1", 0)
        self.vAddType("u1IffThc")
        self.u1SensorThc = clsAdcsBaseType("U1", 0)
        self.vAddType("u1SensorThc")


vAddClass("sTM_THC_ENGINEERING_DATA_UNSOL_PL", sTM_THC_ENGINEERING_DATA_UNSOL_PL)


class sTM_TYPE_CLASSIFICATION_ENGINEERING_DATA_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sTM_TYPE_CLASSIFICATION_ENGINEERING_DATA_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.sTimestamp = sADCS_TIMESTAMP()
        self.vAddType("sTimestamp")
        self.u4TrackNumber = clsAdcsBaseType("U4", 0)
        self.vAddType("u4TrackNumber")
        self.u1CurrentType = clsAdcsBaseType("U1", 0)
        self.vAddType("u1CurrentType")
        self.u1HigherOrderEchelonType = clsAdcsBaseType("U1", 0)
        self.vAddType("u1HigherOrderEchelonType")
        self.u1OperatorType = clsAdcsBaseType("U1", 0)
        self.vAddType("u1OperatorType")
        self.u1ProposedType = clsAdcsBaseType("U1", 0)
        self.vAddType("u1ProposedType")
        self.u1SensorType = clsAdcsBaseType("U1", 0)
        self.vAddType("u1SensorType")


vAddClass("sTM_TYPE_CLASSIFICATION_ENGINEERING_DATA_UNSOL_PL", sTM_TYPE_CLASSIFICATION_ENGINEERING_DATA_UNSOL_PL)


# PAYLOADS END

# MESSAGES START
class sTM_STATUS_REPORT_UNSOL(clsAdcsMessageType):
    """Public class definition of type sTM_STATUS_REPORT_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sTM_STATUS_REPORT_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sTM_STATUS_REPORT_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sTM_STATUS_REPORT_UNSOL", sTM_STATUS_REPORT_UNSOL)


class sTM_END_OF_SETUP_CMD(clsAdcsMessageType):
    """Public class definition of type sTM_END_OF_SETUP_CMD
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sTM_END_OF_SETUP_CMD_MESSAGE_HEADER()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sTM_END_OF_SETUP_CMD", sTM_END_OF_SETUP_CMD)


class sTM_END_OF_SETUP_CMD_RSP(clsAdcsMessageType):
    """Public class definition of type sTM_END_OF_SETUP_CMD_RSP
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sTM_END_OF_SETUP_CMD_RSP_MESSAGE_HEADER()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sTM_END_OF_SETUP_CMD_RSP", sTM_END_OF_SETUP_CMD_RSP)


class sTM_END_OF_READY_CMD(clsAdcsMessageType):
    """Public class definition of type sTM_END_OF_READY_CMD
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sTM_END_OF_READY_CMD_MESSAGE_HEADER()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sTM_END_OF_READY_CMD", sTM_END_OF_READY_CMD)


class sTM_END_OF_READY_CMD_RSP(clsAdcsMessageType):
    """Public class definition of type sTM_END_OF_READY_CMD_RSP
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sTM_END_OF_READY_CMD_RSP_MESSAGE_HEADER()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sTM_END_OF_READY_CMD_RSP", sTM_END_OF_READY_CMD_RSP)


class sTM_SHUTDOWN_CMD(clsAdcsMessageType):
    """Public class definition of type sTM_SHUTDOWN_CMD
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sTM_SHUTDOWN_CMD_MESSAGE_HEADER()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sTM_SHUTDOWN_CMD", sTM_SHUTDOWN_CMD)


class sTM_SHUTDOWN_CMD_RSP(clsAdcsMessageType):
    """Public class definition of type sTM_SHUTDOWN_CMD_RSP
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sTM_SHUTDOWN_CMD_RSP_MESSAGE_HEADER()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sTM_SHUTDOWN_CMD_RSP", sTM_SHUTDOWN_CMD_RSP)


class sTM_SYSTEM_POINT_TRACK_UNSOL(clsAdcsMessageType):
    """Public class definition of type sTM_SYSTEM_POINT_TRACK_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sTM_SYSTEM_POINT_TRACK_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sTM_SYSTEM_POINT_TRACK_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sTM_SYSTEM_POINT_TRACK_UNSOL", sTM_SYSTEM_POINT_TRACK_UNSOL)


class sTM_SYSTEM_BEARING_TRACK_UNSOL(clsAdcsMessageType):
    """Public class definition of type sTM_SYSTEM_BEARING_TRACK_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sTM_SYSTEM_BEARING_TRACK_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sTM_SYSTEM_BEARING_TRACK_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sTM_SYSTEM_BEARING_TRACK_UNSOL", sTM_SYSTEM_BEARING_TRACK_UNSOL)


class sTM_PROPOSED_FLAG_UNSOL(clsAdcsMessageType):
    """Public class definition of type sTM_PROPOSED_FLAG_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sTM_PROPOSED_FLAG_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sTM_PROPOSED_FLAG_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sTM_PROPOSED_FLAG_UNSOL", sTM_PROPOSED_FLAG_UNSOL)


class sTM_MISMATCH_FLAG_UNSOL(clsAdcsMessageType):
    """Public class definition of type sTM_MISMATCH_FLAG_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sTM_MISMATCH_FLAG_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sTM_MISMATCH_FLAG_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sTM_MISMATCH_FLAG_UNSOL", sTM_MISMATCH_FLAG_UNSOL)


class sTM_OVERRIDE_FAIL_FLAG_UNSOL(clsAdcsMessageType):
    """Public class definition of type sTM_OVERRIDE_FAIL_FLAG_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sTM_OVERRIDE_FAIL_FLAG_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sTM_OVERRIDE_FAIL_FLAG_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sTM_OVERRIDE_FAIL_FLAG_UNSOL", sTM_OVERRIDE_FAIL_FLAG_UNSOL)


class sTM_CORRELATION_ENGINEERING_DATA_UNSOL(clsAdcsMessageType):
    """Public class definition of type sTM_CORRELATION_ENGINEERING_DATA_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sTM_CORRELATION_ENGINEERING_DATA_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sTM_CORRELATION_ENGINEERING_DATA_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sTM_CORRELATION_ENGINEERING_DATA_UNSOL", sTM_CORRELATION_ENGINEERING_DATA_UNSOL)


class sTM_DECORRELATION_ENGINEERING_DATA_UNSOL(clsAdcsMessageType):
    """Public class definition of type sTM_DECORRELATION_ENGINEERING_DATA_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sTM_DECORRELATION_ENGINEERING_DATA_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sTM_DECORRELATION_ENGINEERING_DATA_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sTM_DECORRELATION_ENGINEERING_DATA_UNSOL", sTM_DECORRELATION_ENGINEERING_DATA_UNSOL)


class sTM_ASSOCIATION_ENGINEERING_DATA_UNSOL(clsAdcsMessageType):
    """Public class definition of type sTM_ASSOCIATION_ENGINEERING_DATA_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sTM_ASSOCIATION_ENGINEERING_DATA_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sTM_ASSOCIATION_ENGINEERING_DATA_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sTM_ASSOCIATION_ENGINEERING_DATA_UNSOL", sTM_ASSOCIATION_ENGINEERING_DATA_UNSOL)


class sTM_DISSOCIATION_ENGINEERING_DATA_UNSOL(clsAdcsMessageType):
    """Public class definition of type sTM_DISSOCIATION_ENGINEERING_DATA_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sTM_DISSOCIATION_ENGINEERING_DATA_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sTM_DISSOCIATION_ENGINEERING_DATA_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sTM_DISSOCIATION_ENGINEERING_DATA_UNSOL", sTM_DISSOCIATION_ENGINEERING_DATA_UNSOL)


class sTM_THC_ENGINEERING_DATA_UNSOL(clsAdcsMessageType):
    """Public class definition of type sTM_THC_ENGINEERING_DATA_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sTM_THC_ENGINEERING_DATA_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sTM_THC_ENGINEERING_DATA_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sTM_THC_ENGINEERING_DATA_UNSOL", sTM_THC_ENGINEERING_DATA_UNSOL)


class sTM_TYPE_CLASSIFICATION_ENGINEERING_DATA_UNSOL(clsAdcsMessageType):
    """Public class definition of type sTM_TYPE_CLASSIFICATION_ENGINEERING_DATA_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sTM_TYPE_CLASSIFICATION_ENGINEERING_DATA_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sTM_TYPE_CLASSIFICATION_ENGINEERING_DATA_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sTM_TYPE_CLASSIFICATION_ENGINEERING_DATA_UNSOL", sTM_TYPE_CLASSIFICATION_ENGINEERING_DATA_UNSOL)


# MESSAGES END




