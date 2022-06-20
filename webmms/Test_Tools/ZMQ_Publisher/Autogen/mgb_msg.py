#!/usr/bin/env python3.6
"""
    Autogen - Do not edit by hand!
    Autogen - Do not edit by hand!
    Autogen - Do not edit by hand!

    Generated using Python 3.6.9
    Rendered with Jinja2 2.11.1
    Generated on 2020-07-16 12:29:02 SAST
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
from Autogen.cnis_secb_chap2_common_types import *
from Autogen.res_eiu_temp_types import *
from Autogen.mw_common_types import *
# IMPORT CODE END


# MESSAGE HEADERS START
class sLZA_C01_AIR_TRACK_REPORT_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sLZA_C01_AIR_TRACK_REPORT_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_MGB)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x6500)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sLZA_C01_AIR_TRACK_REPORT_UNSOL_MESSAGE_HEADER", sLZA_C01_AIR_TRACK_REPORT_UNSOL_MESSAGE_HEADER)


class sLZA_C02_SURFACE_TRACK_REPORT_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sLZA_C02_SURFACE_TRACK_REPORT_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_MGB)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x6600)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sLZA_C02_SURFACE_TRACK_REPORT_UNSOL_MESSAGE_HEADER", sLZA_C02_SURFACE_TRACK_REPORT_UNSOL_MESSAGE_HEADER)


class sLZA_C04_BEARING_TRACK_REPORT_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sLZA_C04_BEARING_TRACK_REPORT_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_MGB)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x6800)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sLZA_C04_BEARING_TRACK_REPORT_UNSOL_MESSAGE_HEADER", sLZA_C04_BEARING_TRACK_REPORT_UNSOL_MESSAGE_HEADER)


class sLZA_L06_OWN_POSITION_REPORT_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sLZA_L06_OWN_POSITION_REPORT_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_MGB)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x9200)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sLZA_L06_OWN_POSITION_REPORT_UNSOL_MESSAGE_HEADER", sLZA_L06_OWN_POSITION_REPORT_UNSOL_MESSAGE_HEADER)


class sLZA_T10_Q_AIR_RAID_WARNING_STATE_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sLZA_T10_Q_AIR_RAID_WARNING_STATE_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_MGB)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x0A11)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sLZA_T10_Q_AIR_RAID_WARNING_STATE_UNSOL_MESSAGE_HEADER", sLZA_T10_Q_AIR_RAID_WARNING_STATE_UNSOL_MESSAGE_HEADER)


class sLZA_T61_G_AIR_DEFENCE_READINESS_STATE_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sLZA_T61_G_AIR_DEFENCE_READINESS_STATE_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_MGB)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x3D07)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sLZA_T61_G_AIR_DEFENCE_READINESS_STATE_UNSOL_MESSAGE_HEADER", sLZA_T61_G_AIR_DEFENCE_READINESS_STATE_UNSOL_MESSAGE_HEADER)


class sLZA_T61_J_WEAPON_CONTROL_ORDER_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sLZA_T61_J_WEAPON_CONTROL_ORDER_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_MGB)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x3D0A)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sLZA_T61_J_WEAPON_CONTROL_ORDER_UNSOL_MESSAGE_HEADER", sLZA_T61_J_WEAPON_CONTROL_ORDER_UNSOL_MESSAGE_HEADER)


class sLZA_T63_A_ENGAGEMENT_COMPLIANCE_REPORT_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sLZA_T63_A_ENGAGEMENT_COMPLIANCE_REPORT_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_MGB)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x3F01)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sLZA_T63_A_ENGAGEMENT_COMPLIANCE_REPORT_UNSOL_MESSAGE_HEADER", sLZA_T63_A_ENGAGEMENT_COMPLIANCE_REPORT_UNSOL_MESSAGE_HEADER)


class sLZA_T63_B_ENGAGEMENT_CONTROL_STATE_REPORT_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sLZA_T63_B_ENGAGEMENT_CONTROL_STATE_REPORT_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_MGB)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x3F02)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sLZA_T63_B_ENGAGEMENT_CONTROL_STATE_REPORT_UNSOL_MESSAGE_HEADER", sLZA_T63_B_ENGAGEMENT_CONTROL_STATE_REPORT_UNSOL_MESSAGE_HEADER)


class sLZA_T63_C_ENGAGEMENT_ACTION_STATUS_REPORT_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sLZA_T63_C_ENGAGEMENT_ACTION_STATUS_REPORT_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_MGB)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x3F03)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sLZA_T63_C_ENGAGEMENT_ACTION_STATUS_REPORT_UNSOL_MESSAGE_HEADER", sLZA_T63_C_ENGAGEMENT_ACTION_STATUS_REPORT_UNSOL_MESSAGE_HEADER)


class sLZA_T63_D_ENGAGEMENT_OUTCOME_REPORT_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sLZA_T63_D_ENGAGEMENT_OUTCOME_REPORT_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_MGB)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x3F04)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sLZA_T63_D_ENGAGEMENT_OUTCOME_REPORT_UNSOL_MESSAGE_HEADER", sLZA_T63_D_ENGAGEMENT_OUTCOME_REPORT_UNSOL_MESSAGE_HEADER)


class sLZA_T63_H_ACTION_STATUS_REPORT_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sLZA_T63_H_ACTION_STATUS_REPORT_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_MGB)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x3F08)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sLZA_T63_H_ACTION_STATUS_REPORT_UNSOL_MESSAGE_HEADER", sLZA_T63_H_ACTION_STATUS_REPORT_UNSOL_MESSAGE_HEADER)


class sLZA_T63_L_WEAPON_SYSTEM_STATUS_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sLZA_T63_L_WEAPON_SYSTEM_STATUS_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_MGB)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x3F0C)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sLZA_T63_L_WEAPON_SYSTEM_STATUS_UNSOL_MESSAGE_HEADER", sLZA_T63_L_WEAPON_SYSTEM_STATUS_UNSOL_MESSAGE_HEADER)


class sLZA_T61_H_LOCAL_WARNING_ORDER_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sLZA_T61_H_LOCAL_WARNING_ORDER_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_MGB)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x3D08)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sLZA_T61_H_LOCAL_WARNING_ORDER_UNSOL_MESSAGE_HEADER", sLZA_T61_H_LOCAL_WARNING_ORDER_UNSOL_MESSAGE_HEADER)


class sLZA_T61_I_ENGAGEMENT_ORDER_UNSOL_MESSAGE_HEADER(clsAdcsHeaderStructType):
    """Public class definition of type sLZA_T61_I_ENGAGEMENT_ORDER_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.u2MsgLength = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgLength")
        self.e2MsgType = E2_MW_MESSAGE_TYPE(E2_MW_MESSAGE_TYPE.MW_MESSAGE_TYPE_UNSOL)
        self.vAddType("e2MsgType")
        self.e2MsgStatus = E2_MW_MESSAGE_STATUS(E2_MW_MESSAGE_STATUS.MW_MESSAGE_STATUS_NORMAL)
        self.vAddType("e2MsgStatus")
        self.e2ModuleAddress = E2_MW_MODULE_ADDRESS(E2_MW_MODULE_ADDRESS.MW_MODULE_ADDRESS_MGB)
        self.vAddType("e2ModuleAddress")
        self.u2MsgId = clsAdcsBaseType("U2", 0x3D09)
        self.vAddType("u2MsgId")
        self.u2MsgCount = clsAdcsBaseType("U2", 0)
        self.vAddType("u2MsgCount")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")
        self.u2ProcessStartCnt = clsAdcsBaseType("U2", 0xFFFF)
        self.vAddType("u2ProcessStartCnt")


vAddClass("sLZA_T61_I_ENGAGEMENT_ORDER_UNSOL_MESSAGE_HEADER", sLZA_T61_I_ENGAGEMENT_ORDER_UNSOL_MESSAGE_HEADER)


# MESSAGE HEADERS END

# PAYLOADS START
class sLZA_C01_AIR_TRACK_REPORT_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sLZA_C01_AIR_TRACK_REPORT_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.e1MessageTypeNumber = E1_LZA_MESSAGE_TYPE(E1_LZA_MESSAGE_TYPE.LZA_MESSAGE_TYPE_C01)
        self.vAddType("e1MessageTypeNumber")
        self.sOrigin = sLZA_HEADER_ORIGIN()
        self.vAddType("sOrigin")
        self.u1NetIdentifier = clsAdcsBaseType("U1", 255)
        self.u1NetIdentifier.vSetMin(0)
        self.u1NetIdentifier.vSetMax(255)
        self.vAddType("u1NetIdentifier")
        self.e1PrecedenceLevel = E1_LZA_PRECEDENCE_LEVEL(E1_LZA_PRECEDENCE_LEVEL.LZA_PRECEDENCE_LEVEL_IMMEDIATE)
        self.vAddType("e1PrecedenceLevel")
        self.u1ExpiryTimeLza15Second = clsAdcsBaseType("U1", 1)
        self.u1ExpiryTimeLza15Second.vSetMin(0)
        self.u1ExpiryTimeLza15Second.vSetMax(255)
        self.vAddType("u1ExpiryTimeLza15Second")
        self.u2Date = clsAdcsBaseType("U2", 1)
        self.u2Date.vSetMin(1)
        self.u2Date.vSetMax(366)
        self.vAddType("u2Date")
        self.sTransmissionTime = sLZA_HEADER_TIME()
        self.vAddType("sTransmissionTime")
        self.u2SerialNumber = clsAdcsBaseType("U2", 1)
        self.u2SerialNumber.vSetMin(1)
        self.u2SerialNumber.vSetMax(65535)
        self.vAddType("u2SerialNumber")
        self.u1NumberOfDestinations = clsAdcsBaseType("U1", 1)
        self.u1NumberOfDestinations.vSetMin(0)
        self.u1NumberOfDestinations.vSetMax(8)
        self.vAddType("u1NumberOfDestinations")
        self.asDestinations = clsAdcsStructArrayType("sLZA_HEADER_DESTINATION:8")
        self.vAddType("asDestinations")
        self.u1NumberOfTracks = clsAdcsBaseType("U1", 1)
        self.u1NumberOfTracks.vSetMin(1)
        self.u1NumberOfTracks.vSetMax(16)
        self.vAddType("u1NumberOfTracks")
        self.asAirTrack = clsAdcsStructArrayType("sLZA_AIR_TRACK:16")
        self.vAddType("asAirTrack")


vAddClass("sLZA_C01_AIR_TRACK_REPORT_UNSOL_PL", sLZA_C01_AIR_TRACK_REPORT_UNSOL_PL)


class sLZA_C02_SURFACE_TRACK_REPORT_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sLZA_C02_SURFACE_TRACK_REPORT_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.e1MessageTypeNumber = E1_LZA_MESSAGE_TYPE(E1_LZA_MESSAGE_TYPE.LZA_MESSAGE_TYPE_C02)
        self.vAddType("e1MessageTypeNumber")
        self.sOrigin = sLZA_HEADER_ORIGIN()
        self.vAddType("sOrigin")
        self.u1NetIdentifier = clsAdcsBaseType("U1", 255)
        self.u1NetIdentifier.vSetMin(0)
        self.u1NetIdentifier.vSetMax(255)
        self.vAddType("u1NetIdentifier")
        self.e1PrecedenceLevel = E1_LZA_PRECEDENCE_LEVEL(E1_LZA_PRECEDENCE_LEVEL.LZA_PRECEDENCE_LEVEL_ROUTINE)
        self.vAddType("e1PrecedenceLevel")
        self.u1ExpiryTimeLza15Second = clsAdcsBaseType("U1", 1)
        self.u1ExpiryTimeLza15Second.vSetMin(0)
        self.u1ExpiryTimeLza15Second.vSetMax(255)
        self.vAddType("u1ExpiryTimeLza15Second")
        self.u2Date = clsAdcsBaseType("U2", 1)
        self.u2Date.vSetMin(1)
        self.u2Date.vSetMax(366)
        self.vAddType("u2Date")
        self.sTransmissionTime = sLZA_HEADER_TIME()
        self.vAddType("sTransmissionTime")
        self.u2SerialNumber = clsAdcsBaseType("U2", 1)
        self.u2SerialNumber.vSetMin(1)
        self.u2SerialNumber.vSetMax(65535)
        self.vAddType("u2SerialNumber")
        self.u1NumberOfDestinations = clsAdcsBaseType("U1", 1)
        self.u1NumberOfDestinations.vSetMin(0)
        self.u1NumberOfDestinations.vSetMax(8)
        self.vAddType("u1NumberOfDestinations")
        self.asDestinations = clsAdcsStructArrayType("sLZA_HEADER_DESTINATION:8")
        self.vAddType("asDestinations")
        self.u1NumberOfTracks = clsAdcsBaseType("U1", 1)
        self.u1NumberOfTracks.vSetMin(1)
        self.u1NumberOfTracks.vSetMax(16)
        self.vAddType("u1NumberOfTracks")
        self.asSurfaceTrack = clsAdcsStructArrayType("sLZA_SURFACE_TRACK:16")
        self.vAddType("asSurfaceTrack")


vAddClass("sLZA_C02_SURFACE_TRACK_REPORT_UNSOL_PL", sLZA_C02_SURFACE_TRACK_REPORT_UNSOL_PL)


class sLZA_C04_BEARING_TRACK_REPORT_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sLZA_C04_BEARING_TRACK_REPORT_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.e1MessageTypeNumber = E1_LZA_MESSAGE_TYPE(E1_LZA_MESSAGE_TYPE.LZA_MESSAGE_TYPE_C04)
        self.vAddType("e1MessageTypeNumber")
        self.sOrigin = sLZA_HEADER_ORIGIN()
        self.vAddType("sOrigin")
        self.u1NetIdentifier = clsAdcsBaseType("U1", 255)
        self.u1NetIdentifier.vSetMin(0)
        self.u1NetIdentifier.vSetMax(255)
        self.vAddType("u1NetIdentifier")
        self.e1PrecedenceLevel = E1_LZA_PRECEDENCE_LEVEL(E1_LZA_PRECEDENCE_LEVEL.LZA_PRECEDENCE_LEVEL_IMMEDIATE)
        self.vAddType("e1PrecedenceLevel")
        self.u1ExpiryTimeLza15Second = clsAdcsBaseType("U1", 1)
        self.u1ExpiryTimeLza15Second.vSetMin(0)
        self.u1ExpiryTimeLza15Second.vSetMax(255)
        self.vAddType("u1ExpiryTimeLza15Second")
        self.u2Date = clsAdcsBaseType("U2", 1)
        self.u2Date.vSetMin(1)
        self.u2Date.vSetMax(366)
        self.vAddType("u2Date")
        self.sTransmissionTime = sLZA_HEADER_TIME()
        self.vAddType("sTransmissionTime")
        self.u2SerialNumber = clsAdcsBaseType("U2", 1)
        self.u2SerialNumber.vSetMin(1)
        self.u2SerialNumber.vSetMax(65535)
        self.vAddType("u2SerialNumber")
        self.u1NumberOfDestinations = clsAdcsBaseType("U1", 1)
        self.u1NumberOfDestinations.vSetMin(0)
        self.u1NumberOfDestinations.vSetMax(8)
        self.vAddType("u1NumberOfDestinations")
        self.asDestinations = clsAdcsStructArrayType("sLZA_HEADER_DESTINATION:8")
        self.vAddType("asDestinations")
        self.u1NumberOfTracks = clsAdcsBaseType("U1", 1)
        self.u1NumberOfTracks.vSetMin(1)
        self.u1NumberOfTracks.vSetMax(16)
        self.vAddType("u1NumberOfTracks")
        self.asBearingTrack = clsAdcsStructArrayType("sLZA_BEARING_TRACK:16")
        self.vAddType("asBearingTrack")


vAddClass("sLZA_C04_BEARING_TRACK_REPORT_UNSOL_PL", sLZA_C04_BEARING_TRACK_REPORT_UNSOL_PL)


class sLZA_L06_OWN_POSITION_REPORT_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sLZA_L06_OWN_POSITION_REPORT_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.e1MessageTypeNumber = E1_LZA_MESSAGE_TYPE(E1_LZA_MESSAGE_TYPE.LZA_MESSAGE_TYPE_L06)
        self.vAddType("e1MessageTypeNumber")
        self.sOrigin = sLZA_HEADER_ORIGIN()
        self.vAddType("sOrigin")
        self.u1NetIdentifier = clsAdcsBaseType("U1", 255)
        self.u1NetIdentifier.vSetMin(0)
        self.u1NetIdentifier.vSetMax(255)
        self.vAddType("u1NetIdentifier")
        self.e1PrecedenceLevel = E1_LZA_PRECEDENCE_LEVEL(E1_LZA_PRECEDENCE_LEVEL.LZA_PRECEDENCE_LEVEL_ROUTINE)
        self.vAddType("e1PrecedenceLevel")
        self.u1ExpiryTimeLza15Second = clsAdcsBaseType("U1", 1)
        self.u1ExpiryTimeLza15Second.vSetMin(0)
        self.u1ExpiryTimeLza15Second.vSetMax(255)
        self.vAddType("u1ExpiryTimeLza15Second")
        self.u2Date = clsAdcsBaseType("U2", 1)
        self.u2Date.vSetMin(1)
        self.u2Date.vSetMax(366)
        self.vAddType("u2Date")
        self.sTransmissionTime = sLZA_HEADER_TIME()
        self.vAddType("sTransmissionTime")
        self.u2SerialNumber = clsAdcsBaseType("U2", 1)
        self.u2SerialNumber.vSetMin(1)
        self.u2SerialNumber.vSetMax(65535)
        self.vAddType("u2SerialNumber")
        self.u1NumberOfDestinations = clsAdcsBaseType("U1", 1)
        self.u1NumberOfDestinations.vSetMin(0)
        self.u1NumberOfDestinations.vSetMax(8)
        self.vAddType("u1NumberOfDestinations")
        self.asDestinations = clsAdcsStructArrayType("sLZA_HEADER_DESTINATION:8")
        self.vAddType("asDestinations")
        self.sOwnPositionTrack = sLZA_OWN_POSITION_TRACK()
        self.vAddType("sOwnPositionTrack")


vAddClass("sLZA_L06_OWN_POSITION_REPORT_UNSOL_PL", sLZA_L06_OWN_POSITION_REPORT_UNSOL_PL)


class sLZA_T10_Q_AIR_RAID_WARNING_STATE_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sLZA_T10_Q_AIR_RAID_WARNING_STATE_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.e1MessageTypeNumber = E1_LZA_MESSAGE_TYPE(E1_LZA_MESSAGE_TYPE.LZA_MESSAGE_TYPE_T10)
        self.vAddType("e1MessageTypeNumber")
        self.sOrigin = sLZA_HEADER_ORIGIN()
        self.vAddType("sOrigin")
        self.u1NetIdentifier = clsAdcsBaseType("U1", 255)
        self.u1NetIdentifier.vSetMin(0)
        self.u1NetIdentifier.vSetMax(255)
        self.vAddType("u1NetIdentifier")
        self.e1PrecedenceLevel = E1_LZA_PRECEDENCE_LEVEL(E1_LZA_PRECEDENCE_LEVEL.LZA_PRECEDENCE_LEVEL_FLASH_OVERRIDE)
        self.vAddType("e1PrecedenceLevel")
        self.u1ExpiryTimeLza15Second = clsAdcsBaseType("U1", 1)
        self.u1ExpiryTimeLza15Second.vSetMin(0)
        self.u1ExpiryTimeLza15Second.vSetMax(255)
        self.vAddType("u1ExpiryTimeLza15Second")
        self.u2Date = clsAdcsBaseType("U2", 1)
        self.u2Date.vSetMin(1)
        self.u2Date.vSetMax(366)
        self.vAddType("u2Date")
        self.sTransmissionTime = sLZA_HEADER_TIME()
        self.vAddType("sTransmissionTime")
        self.u2SerialNumber = clsAdcsBaseType("U2", 1)
        self.u2SerialNumber.vSetMin(1)
        self.u2SerialNumber.vSetMax(65535)
        self.vAddType("u2SerialNumber")
        self.u1NumberOfDestinations = clsAdcsBaseType("U1", 1)
        self.u1NumberOfDestinations.vSetMin(0)
        self.u1NumberOfDestinations.vSetMax(8)
        self.vAddType("u1NumberOfDestinations")
        self.asDestinations = clsAdcsStructArrayType("sLZA_HEADER_DESTINATION:8")
        self.vAddType("asDestinations")
        self.e1TemplateCode = E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE(E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE.LINK_ZA_MSG_TEMPLATE_CODE_Q)
        self.vAddType("e1TemplateCode")
        self.sDateOrigin = sCSIU_DATE_JULIAN()
        self.vAddType("sDateOrigin")
        self.sTimeOrigin = sCSIU_TIME_HMS()
        self.vAddType("sTimeOrigin")
        self.e1Arws = E1_CSIU_ARWS_TYPE(E1_CSIU_ARWS_TYPE.CSIU_ARWS_YELLOW)
        self.vAddType("e1Arws")


vAddClass("sLZA_T10_Q_AIR_RAID_WARNING_STATE_UNSOL_PL", sLZA_T10_Q_AIR_RAID_WARNING_STATE_UNSOL_PL)


class sLZA_T61_G_AIR_DEFENCE_READINESS_STATE_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sLZA_T61_G_AIR_DEFENCE_READINESS_STATE_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.e1MessageTypeNumber = E1_LZA_MESSAGE_TYPE(E1_LZA_MESSAGE_TYPE.LZA_MESSAGE_TYPE_T61)
        self.vAddType("e1MessageTypeNumber")
        self.sOrigin = sLZA_HEADER_ORIGIN()
        self.vAddType("sOrigin")
        self.u1NetIdentifier = clsAdcsBaseType("U1", 255)
        self.u1NetIdentifier.vSetMin(0)
        self.u1NetIdentifier.vSetMax(255)
        self.vAddType("u1NetIdentifier")
        self.e1PrecedenceLevel = E1_LZA_PRECEDENCE_LEVEL(E1_LZA_PRECEDENCE_LEVEL.LZA_PRECEDENCE_LEVEL_FLASH_OVERRIDE)
        self.vAddType("e1PrecedenceLevel")
        self.u1ExpiryTimeLza15Second = clsAdcsBaseType("U1", 1)
        self.u1ExpiryTimeLza15Second.vSetMin(0)
        self.u1ExpiryTimeLza15Second.vSetMax(255)
        self.vAddType("u1ExpiryTimeLza15Second")
        self.u2Date = clsAdcsBaseType("U2", 1)
        self.u2Date.vSetMin(1)
        self.u2Date.vSetMax(366)
        self.vAddType("u2Date")
        self.sTransmissionTime = sLZA_HEADER_TIME()
        self.vAddType("sTransmissionTime")
        self.u2SerialNumber = clsAdcsBaseType("U2", 1)
        self.u2SerialNumber.vSetMin(1)
        self.u2SerialNumber.vSetMax(65535)
        self.vAddType("u2SerialNumber")
        self.u1NumberOfDestinations = clsAdcsBaseType("U1", 1)
        self.u1NumberOfDestinations.vSetMin(0)
        self.u1NumberOfDestinations.vSetMax(8)
        self.vAddType("u1NumberOfDestinations")
        self.asDestinations = clsAdcsStructArrayType("sLZA_HEADER_DESTINATION:8")
        self.vAddType("asDestinations")
        self.e1TemplateCode = E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE(E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE.LINK_ZA_MSG_TEMPLATE_CODE_G)
        self.vAddType("e1TemplateCode")
        self.sDateOrigin = sCSIU_DATE_JULIAN()
        self.vAddType("sDateOrigin")
        self.sTimeOrigin = sCSIU_TIME_HMS()
        self.vAddType("sTimeOrigin")
        self.e1Adrs = E1_CSIU_ADRS_TYPE(E1_CSIU_ADRS_TYPE.CSIU_ADRS_MEDIUM)
        self.vAddType("e1Adrs")


vAddClass("sLZA_T61_G_AIR_DEFENCE_READINESS_STATE_UNSOL_PL", sLZA_T61_G_AIR_DEFENCE_READINESS_STATE_UNSOL_PL)


class sLZA_T61_J_WEAPON_CONTROL_ORDER_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sLZA_T61_J_WEAPON_CONTROL_ORDER_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.e1MessageTypeNumber = E1_LZA_MESSAGE_TYPE(E1_LZA_MESSAGE_TYPE.LZA_MESSAGE_TYPE_T61)
        self.vAddType("e1MessageTypeNumber")
        self.sOrigin = sLZA_HEADER_ORIGIN()
        self.vAddType("sOrigin")
        self.u1NetIdentifier = clsAdcsBaseType("U1", 255)
        self.u1NetIdentifier.vSetMin(0)
        self.u1NetIdentifier.vSetMax(255)
        self.vAddType("u1NetIdentifier")
        self.e1PrecedenceLevel = E1_LZA_PRECEDENCE_LEVEL(E1_LZA_PRECEDENCE_LEVEL.LZA_PRECEDENCE_LEVEL_FLASH_OVERRIDE)
        self.vAddType("e1PrecedenceLevel")
        self.u1ExpiryTimeLza15Second = clsAdcsBaseType("U1", 1)
        self.u1ExpiryTimeLza15Second.vSetMin(0)
        self.u1ExpiryTimeLza15Second.vSetMax(255)
        self.vAddType("u1ExpiryTimeLza15Second")
        self.u2Date = clsAdcsBaseType("U2", 1)
        self.u2Date.vSetMin(1)
        self.u2Date.vSetMax(366)
        self.vAddType("u2Date")
        self.sTransmissionTime = sLZA_HEADER_TIME()
        self.vAddType("sTransmissionTime")
        self.u2SerialNumber = clsAdcsBaseType("U2", 1)
        self.u2SerialNumber.vSetMin(1)
        self.u2SerialNumber.vSetMax(65535)
        self.vAddType("u2SerialNumber")
        self.u1NumberOfDestinations = clsAdcsBaseType("U1", 1)
        self.u1NumberOfDestinations.vSetMin(0)
        self.u1NumberOfDestinations.vSetMax(8)
        self.vAddType("u1NumberOfDestinations")
        self.asDestinations = clsAdcsStructArrayType("sLZA_HEADER_DESTINATION:8")
        self.vAddType("asDestinations")
        self.e1TemplateCode = E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE(E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE.LINK_ZA_MSG_TEMPLATE_CODE_J)
        self.vAddType("e1TemplateCode")
        self.sDateOrigin = sCSIU_DATE_JULIAN()
        self.vAddType("sDateOrigin")
        self.sTimeOrigin = sCSIU_TIME_HMS()
        self.vAddType("sTimeOrigin")
        self.e1Wco = E1_CSIU_WCO_TYPE(E1_CSIU_WCO_TYPE.CSIU_WCO_WEAPONS_UNDER_CONTROL)
        self.vAddType("e1Wco")


vAddClass("sLZA_T61_J_WEAPON_CONTROL_ORDER_UNSOL_PL", sLZA_T61_J_WEAPON_CONTROL_ORDER_UNSOL_PL)


class sLZA_T63_A_ENGAGEMENT_COMPLIANCE_REPORT_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sLZA_T63_A_ENGAGEMENT_COMPLIANCE_REPORT_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.e1MessageTypeNumber = E1_LZA_MESSAGE_TYPE(E1_LZA_MESSAGE_TYPE.LZA_MESSAGE_TYPE_T63)
        self.vAddType("e1MessageTypeNumber")
        self.sOrigin = sLZA_HEADER_ORIGIN()
        self.vAddType("sOrigin")
        self.u1NetIdentifier = clsAdcsBaseType("U1", 255)
        self.u1NetIdentifier.vSetMin(0)
        self.u1NetIdentifier.vSetMax(255)
        self.vAddType("u1NetIdentifier")
        self.e1PrecedenceLevel = E1_LZA_PRECEDENCE_LEVEL(E1_LZA_PRECEDENCE_LEVEL.LZA_PRECEDENCE_LEVEL_FLASH)
        self.vAddType("e1PrecedenceLevel")
        self.u1ExpiryTimeLza15Second = clsAdcsBaseType("U1", 1)
        self.u1ExpiryTimeLza15Second.vSetMin(0)
        self.u1ExpiryTimeLza15Second.vSetMax(255)
        self.vAddType("u1ExpiryTimeLza15Second")
        self.u2Date = clsAdcsBaseType("U2", 1)
        self.u2Date.vSetMin(1)
        self.u2Date.vSetMax(366)
        self.vAddType("u2Date")
        self.sTransmissionTime = sLZA_HEADER_TIME()
        self.vAddType("sTransmissionTime")
        self.u2SerialNumber = clsAdcsBaseType("U2", 1)
        self.u2SerialNumber.vSetMin(1)
        self.u2SerialNumber.vSetMax(65535)
        self.vAddType("u2SerialNumber")
        self.u1NumberOfDestinations = clsAdcsBaseType("U1", 1)
        self.u1NumberOfDestinations.vSetMin(0)
        self.u1NumberOfDestinations.vSetMax(8)
        self.vAddType("u1NumberOfDestinations")
        self.asDestinations = clsAdcsStructArrayType("sLZA_HEADER_DESTINATION:8")
        self.vAddType("asDestinations")
        self.e1TemplateCode = E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE(E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE.LINK_ZA_MSG_TEMPLATE_CODE_A)
        self.vAddType("e1TemplateCode")
        self.u2EngagementSerialNumber = clsAdcsBaseType("U2", 0)
        self.vAddType("u2EngagementSerialNumber")
        self.e1ComplianceIndicator = E1_CSIU_CANTCO_WILCO_TYPE(E1_CSIU_CANTCO_WILCO_TYPE.CSIU_CANTCO)
        self.vAddType("e1ComplianceIndicator")


vAddClass("sLZA_T63_A_ENGAGEMENT_COMPLIANCE_REPORT_UNSOL_PL", sLZA_T63_A_ENGAGEMENT_COMPLIANCE_REPORT_UNSOL_PL)


class sLZA_T63_B_ENGAGEMENT_CONTROL_STATE_REPORT_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sLZA_T63_B_ENGAGEMENT_CONTROL_STATE_REPORT_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.e1MessageTypeNumber = E1_LZA_MESSAGE_TYPE(E1_LZA_MESSAGE_TYPE.LZA_MESSAGE_TYPE_T63)
        self.vAddType("e1MessageTypeNumber")
        self.sOrigin = sLZA_HEADER_ORIGIN()
        self.vAddType("sOrigin")
        self.u1NetIdentifier = clsAdcsBaseType("U1", 255)
        self.u1NetIdentifier.vSetMin(0)
        self.u1NetIdentifier.vSetMax(255)
        self.vAddType("u1NetIdentifier")
        self.e1PrecedenceLevel = E1_LZA_PRECEDENCE_LEVEL(E1_LZA_PRECEDENCE_LEVEL.LZA_PRECEDENCE_LEVEL_IMMEDIATE)
        self.vAddType("e1PrecedenceLevel")
        self.u1ExpiryTimeLza15Second = clsAdcsBaseType("U1", 1)
        self.u1ExpiryTimeLza15Second.vSetMin(0)
        self.u1ExpiryTimeLza15Second.vSetMax(255)
        self.vAddType("u1ExpiryTimeLza15Second")
        self.u2Date = clsAdcsBaseType("U2", 1)
        self.u2Date.vSetMin(1)
        self.u2Date.vSetMax(366)
        self.vAddType("u2Date")
        self.sTransmissionTime = sLZA_HEADER_TIME()
        self.vAddType("sTransmissionTime")
        self.u2SerialNumber = clsAdcsBaseType("U2", 1)
        self.u2SerialNumber.vSetMin(1)
        self.u2SerialNumber.vSetMax(65535)
        self.vAddType("u2SerialNumber")
        self.u1NumberOfDestinations = clsAdcsBaseType("U1", 1)
        self.u1NumberOfDestinations.vSetMin(0)
        self.u1NumberOfDestinations.vSetMax(8)
        self.vAddType("u1NumberOfDestinations")
        self.asDestinations = clsAdcsStructArrayType("sLZA_HEADER_DESTINATION:8")
        self.vAddType("asDestinations")
        self.e1TemplateCode = E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE(E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE.LINK_ZA_MSG_TEMPLATE_CODE_B)
        self.vAddType("e1TemplateCode")
        self.u2EngagementSerialNumber = clsAdcsBaseType("U2", 0)
        self.vAddType("u2EngagementSerialNumber")
        self.e1EngagementState = E1_CSIU_ENGAGEMENT_STATE_TYPE(E1_CSIU_ENGAGEMENT_STATE_TYPE.CSIU_ENGAGEMENT_STATE_PENDING)
        self.vAddType("e1EngagementState")


vAddClass("sLZA_T63_B_ENGAGEMENT_CONTROL_STATE_REPORT_UNSOL_PL", sLZA_T63_B_ENGAGEMENT_CONTROL_STATE_REPORT_UNSOL_PL)


class sLZA_T63_C_ENGAGEMENT_ACTION_STATUS_REPORT_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sLZA_T63_C_ENGAGEMENT_ACTION_STATUS_REPORT_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.e1MessageTypeNumber = E1_LZA_MESSAGE_TYPE(E1_LZA_MESSAGE_TYPE.LZA_MESSAGE_TYPE_T63)
        self.vAddType("e1MessageTypeNumber")
        self.sOrigin = sLZA_HEADER_ORIGIN()
        self.vAddType("sOrigin")
        self.u1NetIdentifier = clsAdcsBaseType("U1", 255)
        self.u1NetIdentifier.vSetMin(0)
        self.u1NetIdentifier.vSetMax(255)
        self.vAddType("u1NetIdentifier")
        self.e1PrecedenceLevel = E1_LZA_PRECEDENCE_LEVEL(E1_LZA_PRECEDENCE_LEVEL.LZA_PRECEDENCE_LEVEL_IMMEDIATE)
        self.vAddType("e1PrecedenceLevel")
        self.u1ExpiryTimeLza15Second = clsAdcsBaseType("U1", 1)
        self.u1ExpiryTimeLza15Second.vSetMin(0)
        self.u1ExpiryTimeLza15Second.vSetMax(255)
        self.vAddType("u1ExpiryTimeLza15Second")
        self.u2Date = clsAdcsBaseType("U2", 1)
        self.u2Date.vSetMin(1)
        self.u2Date.vSetMax(366)
        self.vAddType("u2Date")
        self.sTransmissionTime = sLZA_HEADER_TIME()
        self.vAddType("sTransmissionTime")
        self.u2SerialNumber = clsAdcsBaseType("U2", 1)
        self.u2SerialNumber.vSetMin(1)
        self.u2SerialNumber.vSetMax(65535)
        self.vAddType("u2SerialNumber")
        self.u1NumberOfDestinations = clsAdcsBaseType("U1", 1)
        self.u1NumberOfDestinations.vSetMin(0)
        self.u1NumberOfDestinations.vSetMax(8)
        self.vAddType("u1NumberOfDestinations")
        self.asDestinations = clsAdcsStructArrayType("sLZA_HEADER_DESTINATION:8")
        self.vAddType("asDestinations")
        self.e1TemplateCode = E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE(E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE.LINK_ZA_MSG_TEMPLATE_CODE_C)
        self.vAddType("e1TemplateCode")
        self.u2EngagementSerialNumber = clsAdcsBaseType("U2", 1)
        self.vAddType("u2EngagementSerialNumber")
        self.e1EngagementActionStatus = E1_CSIU_ENGAGEMENT_ACTION_STATUS_TYPE(E1_CSIU_ENGAGEMENT_ACTION_STATUS_TYPE.CSIU_ENGAGEMENT_ACTION_STATUS_NO_TRACKING)
        self.vAddType("e1EngagementActionStatus")


vAddClass("sLZA_T63_C_ENGAGEMENT_ACTION_STATUS_REPORT_UNSOL_PL", sLZA_T63_C_ENGAGEMENT_ACTION_STATUS_REPORT_UNSOL_PL)


class sLZA_T63_D_ENGAGEMENT_OUTCOME_REPORT_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sLZA_T63_D_ENGAGEMENT_OUTCOME_REPORT_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.e1MessageTypeNumber = E1_LZA_MESSAGE_TYPE(E1_LZA_MESSAGE_TYPE.LZA_MESSAGE_TYPE_T63)
        self.vAddType("e1MessageTypeNumber")
        self.sOrigin = sLZA_HEADER_ORIGIN()
        self.vAddType("sOrigin")
        self.u1NetIdentifier = clsAdcsBaseType("U1", 255)
        self.u1NetIdentifier.vSetMin(0)
        self.u1NetIdentifier.vSetMax(255)
        self.vAddType("u1NetIdentifier")
        self.e1PrecedenceLevel = E1_LZA_PRECEDENCE_LEVEL(E1_LZA_PRECEDENCE_LEVEL.LZA_PRECEDENCE_LEVEL_FLASH)
        self.vAddType("e1PrecedenceLevel")
        self.u1ExpiryTimeLza15Second = clsAdcsBaseType("U1", 1)
        self.u1ExpiryTimeLza15Second.vSetMin(0)
        self.u1ExpiryTimeLza15Second.vSetMax(255)
        self.vAddType("u1ExpiryTimeLza15Second")
        self.u2Date = clsAdcsBaseType("U2", 1)
        self.u2Date.vSetMin(1)
        self.u2Date.vSetMax(366)
        self.vAddType("u2Date")
        self.sTransmissionTime = sLZA_HEADER_TIME()
        self.vAddType("sTransmissionTime")
        self.u2SerialNumber = clsAdcsBaseType("U2", 1)
        self.u2SerialNumber.vSetMin(1)
        self.u2SerialNumber.vSetMax(65535)
        self.vAddType("u2SerialNumber")
        self.u1NumberOfDestinations = clsAdcsBaseType("U1", 1)
        self.u1NumberOfDestinations.vSetMin(0)
        self.u1NumberOfDestinations.vSetMax(8)
        self.vAddType("u1NumberOfDestinations")
        self.asDestinations = clsAdcsStructArrayType("sLZA_HEADER_DESTINATION:8")
        self.vAddType("asDestinations")
        self.e1TemplateCode = E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE(E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE.LINK_ZA_MSG_TEMPLATE_CODE_D)
        self.vAddType("e1TemplateCode")
        self.u2EngagementSerialNumber = clsAdcsBaseType("U2", 0)
        self.vAddType("u2EngagementSerialNumber")
        self.e1WeaponsUsed = E1_CSIU_ENGAGEMENT_WEAPON_TYPE(E1_CSIU_ENGAGEMENT_WEAPON_TYPE.CSIU_ENGAGEMENT_WEAPON_MISSILE_VSHORAD)
        self.vAddType("e1WeaponsUsed")
        self.e1EngagementSuccess = E1_CSIU_NO_YES_TYPE(E1_CSIU_NO_YES_TYPE.CSIU_NO)
        self.vAddType("e1EngagementSuccess")


vAddClass("sLZA_T63_D_ENGAGEMENT_OUTCOME_REPORT_UNSOL_PL", sLZA_T63_D_ENGAGEMENT_OUTCOME_REPORT_UNSOL_PL)


class sLZA_T63_H_ACTION_STATUS_REPORT_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sLZA_T63_H_ACTION_STATUS_REPORT_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.e1MessageTypeNumber = E1_LZA_MESSAGE_TYPE(E1_LZA_MESSAGE_TYPE.LZA_MESSAGE_TYPE_T63)
        self.vAddType("e1MessageTypeNumber")
        self.sOrigin = sLZA_HEADER_ORIGIN()
        self.vAddType("sOrigin")
        self.u1NetIdentifier = clsAdcsBaseType("U1", 255)
        self.u1NetIdentifier.vSetMin(0)
        self.u1NetIdentifier.vSetMax(255)
        self.vAddType("u1NetIdentifier")
        self.e1PrecedenceLevel = E1_LZA_PRECEDENCE_LEVEL(E1_LZA_PRECEDENCE_LEVEL.LZA_PRECEDENCE_LEVEL_PRIORITY)
        self.vAddType("e1PrecedenceLevel")
        self.u1ExpiryTimeLza15Second = clsAdcsBaseType("U1", 1)
        self.u1ExpiryTimeLza15Second.vSetMin(0)
        self.u1ExpiryTimeLza15Second.vSetMax(255)
        self.vAddType("u1ExpiryTimeLza15Second")
        self.u2Date = clsAdcsBaseType("U2", 1)
        self.u2Date.vSetMin(1)
        self.u2Date.vSetMax(366)
        self.vAddType("u2Date")
        self.sTransmissionTime = sLZA_HEADER_TIME()
        self.vAddType("sTransmissionTime")
        self.u2SerialNumber = clsAdcsBaseType("U2", 1)
        self.u2SerialNumber.vSetMin(1)
        self.u2SerialNumber.vSetMax(65535)
        self.vAddType("u2SerialNumber")
        self.u1NumberOfDestinations = clsAdcsBaseType("U1", 1)
        self.u1NumberOfDestinations.vSetMin(0)
        self.u1NumberOfDestinations.vSetMax(8)
        self.vAddType("u1NumberOfDestinations")
        self.asDestinations = clsAdcsStructArrayType("sLZA_HEADER_DESTINATION:8")
        self.vAddType("asDestinations")
        self.e1TemplateCode = E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE(E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE.LINK_ZA_MSG_TEMPLATE_CODE_H)
        self.vAddType("e1TemplateCode")
        self.e1ActionState = E1_CSIU_ACTION_STATE_TYPE(E1_CSIU_ACTION_STATE_TYPE.CSIU_ACTION_STATE_OUT_OF_ACTION)
        self.vAddType("e1ActionState")


vAddClass("sLZA_T63_H_ACTION_STATUS_REPORT_UNSOL_PL", sLZA_T63_H_ACTION_STATUS_REPORT_UNSOL_PL)


class sLZA_T63_L_WEAPON_SYSTEM_STATUS_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sLZA_T63_L_WEAPON_SYSTEM_STATUS_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.e1MessageTypeNumber = E1_LZA_MESSAGE_TYPE(E1_LZA_MESSAGE_TYPE.LZA_MESSAGE_TYPE_T63)
        self.vAddType("e1MessageTypeNumber")
        self.sOrigin = sLZA_HEADER_ORIGIN()
        self.vAddType("sOrigin")
        self.u1NetIdentifier = clsAdcsBaseType("U1", 255)
        self.u1NetIdentifier.vSetMin(0)
        self.u1NetIdentifier.vSetMax(255)
        self.vAddType("u1NetIdentifier")
        self.e1PrecedenceLevel = E1_LZA_PRECEDENCE_LEVEL(E1_LZA_PRECEDENCE_LEVEL.LZA_PRECEDENCE_LEVEL_IMMEDIATE)
        self.vAddType("e1PrecedenceLevel")
        self.u1ExpiryTimeLza15Second = clsAdcsBaseType("U1", 1)
        self.u1ExpiryTimeLza15Second.vSetMin(0)
        self.u1ExpiryTimeLza15Second.vSetMax(255)
        self.vAddType("u1ExpiryTimeLza15Second")
        self.u2Date = clsAdcsBaseType("U2", 1)
        self.u2Date.vSetMin(1)
        self.u2Date.vSetMax(366)
        self.vAddType("u2Date")
        self.sTransmissionTime = sLZA_HEADER_TIME()
        self.vAddType("sTransmissionTime")
        self.u2SerialNumber = clsAdcsBaseType("U2", 1)
        self.u2SerialNumber.vSetMin(1)
        self.u2SerialNumber.vSetMax(65535)
        self.vAddType("u2SerialNumber")
        self.u1NumberOfDestinations = clsAdcsBaseType("U1", 1)
        self.u1NumberOfDestinations.vSetMin(0)
        self.u1NumberOfDestinations.vSetMax(8)
        self.vAddType("u1NumberOfDestinations")
        self.asDestinations = clsAdcsStructArrayType("sLZA_HEADER_DESTINATION:8")
        self.vAddType("asDestinations")
        self.e1TemplateCode = E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE(E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE.LINK_ZA_MSG_TEMPLATE_CODE_L)
        self.vAddType("e1TemplateCode")
        self.u2WsTrackNumber = clsAdcsBaseType("U2", 1)
        self.u2WsTrackNumber.vSetMin(0)
        self.u2WsTrackNumber.vSetMax(16383)
        self.vAddType("u2WsTrackNumber")
        self.e1WsState = E1_CSIU_WS_STATE(E1_CSIU_WS_STATE.CSIU_WS_STATE_NOT_AVAILABLE)
        self.vAddType("e1WsState")
        self.u1NumberOfFireChannelsAvailable = clsAdcsBaseType("U1", 1)
        self.u1NumberOfFireChannelsAvailable.vSetMin(0)
        self.u1NumberOfFireChannelsAvailable.vSetMax(31)
        self.vAddType("u1NumberOfFireChannelsAvailable")
        self.u1NumberOfFireChannelsUsed = clsAdcsBaseType("U1", 0)
        self.vAddType("u1NumberOfFireChannelsUsed")
        self.u1NumberOfAmmoTypes = clsAdcsBaseType("U1", 1)
        self.u1NumberOfAmmoTypes.vSetMin(1)
        self.u1NumberOfAmmoTypes.vSetMax(10)
        self.vAddType("u1NumberOfAmmoTypes")
        self.sAmmoStatus = sCSIU_STATUS_AMMO_TYPE()
        self.vAddType("sAmmoStatus")


vAddClass("sLZA_T63_L_WEAPON_SYSTEM_STATUS_UNSOL_PL", sLZA_T63_L_WEAPON_SYSTEM_STATUS_UNSOL_PL)


class sLZA_T61_H_LOCAL_WARNING_ORDER_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sLZA_T61_H_LOCAL_WARNING_ORDER_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.e1MessageTypeNumber = E1_LZA_MESSAGE_TYPE(E1_LZA_MESSAGE_TYPE.LZA_MESSAGE_TYPE_T61)
        self.vAddType("e1MessageTypeNumber")
        self.sOrigin = sLZA_HEADER_ORIGIN()
        self.vAddType("sOrigin")
        self.u1NetIdentifier = clsAdcsBaseType("U1", 255)
        self.u1NetIdentifier.vSetMin(0)
        self.u1NetIdentifier.vSetMax(255)
        self.vAddType("u1NetIdentifier")
        self.e1PrecedenceLevel = E1_LZA_PRECEDENCE_LEVEL(E1_LZA_PRECEDENCE_LEVEL.LZA_PRECEDENCE_LEVEL_FLASH)
        self.vAddType("e1PrecedenceLevel")
        self.u1ExpiryTimeLza15Second = clsAdcsBaseType("U1", 1)
        self.u1ExpiryTimeLza15Second.vSetMin(0)
        self.u1ExpiryTimeLza15Second.vSetMax(255)
        self.vAddType("u1ExpiryTimeLza15Second")
        self.u2Date = clsAdcsBaseType("U2", 1)
        self.u2Date.vSetMin(1)
        self.u2Date.vSetMax(366)
        self.vAddType("u2Date")
        self.sTransmissionTime = sLZA_HEADER_TIME()
        self.vAddType("sTransmissionTime")
        self.u2SerialNumber = clsAdcsBaseType("U2", 1)
        self.u2SerialNumber.vSetMin(1)
        self.u2SerialNumber.vSetMax(65535)
        self.vAddType("u2SerialNumber")
        self.u1NumberOfDestinations = clsAdcsBaseType("U1", 1)
        self.u1NumberOfDestinations.vSetMin(0)
        self.u1NumberOfDestinations.vSetMax(8)
        self.vAddType("u1NumberOfDestinations")
        self.asDestinations = clsAdcsStructArrayType("sLZA_HEADER_DESTINATION:8")
        self.vAddType("asDestinations")
        self.e1TemplateCode = E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE(E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE.LINK_ZA_MSG_TEMPLATE_CODE_H)
        self.vAddType("e1TemplateCode")
        self.u1NrOfLocalWarningOrders = clsAdcsBaseType("U1", 1)
        self.u1NrOfLocalWarningOrders.vSetMin(1)
        self.u1NrOfLocalWarningOrders.vSetMax(31)
        self.vAddType("u1NrOfLocalWarningOrders")
        self.asLocalWarningOrders = clsAdcsStructArrayType("sCSIU_AIR_TRACK_ALLOCATION_RECORD:31")
        self.vAddType("asLocalWarningOrders")


vAddClass("sLZA_T61_H_LOCAL_WARNING_ORDER_UNSOL_PL", sLZA_T61_H_LOCAL_WARNING_ORDER_UNSOL_PL)


class sLZA_T61_I_ENGAGEMENT_ORDER_UNSOL_PL(clsAdcsMessageStructType):
    """Public class definition of type sLZA_T61_I_ENGAGEMENT_ORDER_UNSOL_PL
    """
    def __init__(self, formatType=None):
        super().__init__(formatType)
        self.e1MessageTypeNumber = E1_LZA_MESSAGE_TYPE(E1_LZA_MESSAGE_TYPE.LZA_MESSAGE_TYPE_T61)
        self.vAddType("e1MessageTypeNumber")
        self.sOrigin = sLZA_HEADER_ORIGIN()
        self.vAddType("sOrigin")
        self.u1NetIdentifier = clsAdcsBaseType("U1", 255)
        self.u1NetIdentifier.vSetMin(0)
        self.u1NetIdentifier.vSetMax(255)
        self.vAddType("u1NetIdentifier")
        self.e1PrecedenceLevel = E1_LZA_PRECEDENCE_LEVEL(E1_LZA_PRECEDENCE_LEVEL.LZA_PRECEDENCE_LEVEL_FLASH)
        self.vAddType("e1PrecedenceLevel")
        self.u1ExpiryTimeLza15Second = clsAdcsBaseType("U1", 1)
        self.u1ExpiryTimeLza15Second.vSetMin(0)
        self.u1ExpiryTimeLza15Second.vSetMax(255)
        self.vAddType("u1ExpiryTimeLza15Second")
        self.u2Date = clsAdcsBaseType("U2", 1)
        self.u2Date.vSetMin(1)
        self.u2Date.vSetMax(366)
        self.vAddType("u2Date")
        self.sTransmissionTime = sLZA_HEADER_TIME()
        self.vAddType("sTransmissionTime")
        self.u2SerialNumber = clsAdcsBaseType("U2", 1)
        self.u2SerialNumber.vSetMin(1)
        self.u2SerialNumber.vSetMax(65535)
        self.vAddType("u2SerialNumber")
        self.u1NumberOfDestinations = clsAdcsBaseType("U1", 1)
        self.u1NumberOfDestinations.vSetMin(0)
        self.u1NumberOfDestinations.vSetMax(8)
        self.vAddType("u1NumberOfDestinations")
        self.asDestinations = clsAdcsStructArrayType("sLZA_HEADER_DESTINATION:8")
        self.vAddType("asDestinations")
        self.e1TemplateCode = E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE(E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE.LINK_ZA_MSG_TEMPLATE_CODE_I)
        self.vAddType("e1TemplateCode")
        self.u1NrOfEngagementOrders = clsAdcsBaseType("U1", 1)
        self.u1NrOfEngagementOrders.vSetMin(1)
        self.u1NrOfEngagementOrders.vSetMax(31)
        self.vAddType("u1NrOfEngagementOrders")
        self.asEngagementOrders = clsAdcsStructArrayType("sCSIU_ENGAGEMENT_ORDER_RECORD:31")
        self.vAddType("asEngagementOrders")


vAddClass("sLZA_T61_I_ENGAGEMENT_ORDER_UNSOL_PL", sLZA_T61_I_ENGAGEMENT_ORDER_UNSOL_PL)


# PAYLOADS END

# MESSAGES START
class sLZA_C01_AIR_TRACK_REPORT_UNSOL(clsAdcsMessageType):
    """Public class definition of type sLZA_C01_AIR_TRACK_REPORT_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sLZA_C01_AIR_TRACK_REPORT_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sLZA_C01_AIR_TRACK_REPORT_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sLZA_C01_AIR_TRACK_REPORT_UNSOL", sLZA_C01_AIR_TRACK_REPORT_UNSOL)


class sLZA_C02_SURFACE_TRACK_REPORT_UNSOL(clsAdcsMessageType):
    """Public class definition of type sLZA_C02_SURFACE_TRACK_REPORT_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sLZA_C02_SURFACE_TRACK_REPORT_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sLZA_C02_SURFACE_TRACK_REPORT_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sLZA_C02_SURFACE_TRACK_REPORT_UNSOL", sLZA_C02_SURFACE_TRACK_REPORT_UNSOL)


class sLZA_C04_BEARING_TRACK_REPORT_UNSOL(clsAdcsMessageType):
    """Public class definition of type sLZA_C04_BEARING_TRACK_REPORT_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sLZA_C04_BEARING_TRACK_REPORT_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sLZA_C04_BEARING_TRACK_REPORT_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sLZA_C04_BEARING_TRACK_REPORT_UNSOL", sLZA_C04_BEARING_TRACK_REPORT_UNSOL)


class sLZA_L06_OWN_POSITION_REPORT_UNSOL(clsAdcsMessageType):
    """Public class definition of type sLZA_L06_OWN_POSITION_REPORT_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sLZA_L06_OWN_POSITION_REPORT_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sLZA_L06_OWN_POSITION_REPORT_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sLZA_L06_OWN_POSITION_REPORT_UNSOL", sLZA_L06_OWN_POSITION_REPORT_UNSOL)


class sLZA_T10_Q_AIR_RAID_WARNING_STATE_UNSOL(clsAdcsMessageType):
    """Public class definition of type sLZA_T10_Q_AIR_RAID_WARNING_STATE_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sLZA_T10_Q_AIR_RAID_WARNING_STATE_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sLZA_T10_Q_AIR_RAID_WARNING_STATE_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sLZA_T10_Q_AIR_RAID_WARNING_STATE_UNSOL", sLZA_T10_Q_AIR_RAID_WARNING_STATE_UNSOL)


class sLZA_T61_G_AIR_DEFENCE_READINESS_STATE_UNSOL(clsAdcsMessageType):
    """Public class definition of type sLZA_T61_G_AIR_DEFENCE_READINESS_STATE_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sLZA_T61_G_AIR_DEFENCE_READINESS_STATE_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sLZA_T61_G_AIR_DEFENCE_READINESS_STATE_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sLZA_T61_G_AIR_DEFENCE_READINESS_STATE_UNSOL", sLZA_T61_G_AIR_DEFENCE_READINESS_STATE_UNSOL)


class sLZA_T61_J_WEAPON_CONTROL_ORDER_UNSOL(clsAdcsMessageType):
    """Public class definition of type sLZA_T61_J_WEAPON_CONTROL_ORDER_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sLZA_T61_J_WEAPON_CONTROL_ORDER_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sLZA_T61_J_WEAPON_CONTROL_ORDER_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sLZA_T61_J_WEAPON_CONTROL_ORDER_UNSOL", sLZA_T61_J_WEAPON_CONTROL_ORDER_UNSOL)


class sLZA_T63_A_ENGAGEMENT_COMPLIANCE_REPORT_UNSOL(clsAdcsMessageType):
    """Public class definition of type sLZA_T63_A_ENGAGEMENT_COMPLIANCE_REPORT_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sLZA_T63_A_ENGAGEMENT_COMPLIANCE_REPORT_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sLZA_T63_A_ENGAGEMENT_COMPLIANCE_REPORT_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sLZA_T63_A_ENGAGEMENT_COMPLIANCE_REPORT_UNSOL", sLZA_T63_A_ENGAGEMENT_COMPLIANCE_REPORT_UNSOL)


class sLZA_T63_B_ENGAGEMENT_CONTROL_STATE_REPORT_UNSOL(clsAdcsMessageType):
    """Public class definition of type sLZA_T63_B_ENGAGEMENT_CONTROL_STATE_REPORT_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sLZA_T63_B_ENGAGEMENT_CONTROL_STATE_REPORT_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sLZA_T63_B_ENGAGEMENT_CONTROL_STATE_REPORT_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sLZA_T63_B_ENGAGEMENT_CONTROL_STATE_REPORT_UNSOL", sLZA_T63_B_ENGAGEMENT_CONTROL_STATE_REPORT_UNSOL)


class sLZA_T63_C_ENGAGEMENT_ACTION_STATUS_REPORT_UNSOL(clsAdcsMessageType):
    """Public class definition of type sLZA_T63_C_ENGAGEMENT_ACTION_STATUS_REPORT_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sLZA_T63_C_ENGAGEMENT_ACTION_STATUS_REPORT_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sLZA_T63_C_ENGAGEMENT_ACTION_STATUS_REPORT_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sLZA_T63_C_ENGAGEMENT_ACTION_STATUS_REPORT_UNSOL", sLZA_T63_C_ENGAGEMENT_ACTION_STATUS_REPORT_UNSOL)


class sLZA_T63_D_ENGAGEMENT_OUTCOME_REPORT_UNSOL(clsAdcsMessageType):
    """Public class definition of type sLZA_T63_D_ENGAGEMENT_OUTCOME_REPORT_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sLZA_T63_D_ENGAGEMENT_OUTCOME_REPORT_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sLZA_T63_D_ENGAGEMENT_OUTCOME_REPORT_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sLZA_T63_D_ENGAGEMENT_OUTCOME_REPORT_UNSOL", sLZA_T63_D_ENGAGEMENT_OUTCOME_REPORT_UNSOL)


class sLZA_T63_H_ACTION_STATUS_REPORT_UNSOL(clsAdcsMessageType):
    """Public class definition of type sLZA_T63_H_ACTION_STATUS_REPORT_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sLZA_T63_H_ACTION_STATUS_REPORT_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sLZA_T63_H_ACTION_STATUS_REPORT_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sLZA_T63_H_ACTION_STATUS_REPORT_UNSOL", sLZA_T63_H_ACTION_STATUS_REPORT_UNSOL)


class sLZA_T63_L_WEAPON_SYSTEM_STATUS_UNSOL(clsAdcsMessageType):
    """Public class definition of type sLZA_T63_L_WEAPON_SYSTEM_STATUS_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sLZA_T63_L_WEAPON_SYSTEM_STATUS_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sLZA_T63_L_WEAPON_SYSTEM_STATUS_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sLZA_T63_L_WEAPON_SYSTEM_STATUS_UNSOL", sLZA_T63_L_WEAPON_SYSTEM_STATUS_UNSOL)


class sLZA_T61_H_LOCAL_WARNING_ORDER_UNSOL(clsAdcsMessageType):
    """Public class definition of type sLZA_T61_H_LOCAL_WARNING_ORDER_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sLZA_T61_H_LOCAL_WARNING_ORDER_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sLZA_T61_H_LOCAL_WARNING_ORDER_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sLZA_T61_H_LOCAL_WARNING_ORDER_UNSOL", sLZA_T61_H_LOCAL_WARNING_ORDER_UNSOL)


class sLZA_T61_I_ENGAGEMENT_ORDER_UNSOL(clsAdcsMessageType):
    """Public class definition of type sLZA_T61_I_ENGAGEMENT_ORDER_UNSOL
    """
    def __init__(self):
        super().__init__()
        self.sMsgHeader = sLZA_T61_I_ENGAGEMENT_ORDER_UNSOL_MESSAGE_HEADER()
        self.sMsgPayload = sLZA_T61_I_ENGAGEMENT_ORDER_UNSOL_PL()
        self.sMsgHeader.u2MsgLength.Value = self.iSizeBytes() - 2

        return


vAddMessage("sLZA_T61_I_ENGAGEMENT_ORDER_UNSOL", sLZA_T61_I_ENGAGEMENT_ORDER_UNSOL)


# MESSAGES END




