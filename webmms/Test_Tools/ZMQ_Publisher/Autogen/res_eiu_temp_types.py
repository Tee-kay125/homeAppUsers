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


# TYPEDEFS START
class E1_CSIU_ARWS_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_CSIU_ARWS_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    CSIU_ARWS_WHITE = 0x00
    CSIU_ARWS_YELLOW = 0x01
    CSIU_ARWS_RED = 0x02


vAddEnum("E1_CSIU_ARWS_TYPE", E1_CSIU_ARWS_TYPE)


class E1_CSIU_ADRS_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_CSIU_ADRS_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    CSIU_ADRS_LOW = 0x00
    CSIU_ADRS_MEDIUM = 0x01
    CSIU_ADRS_HIGH = 0x02


vAddEnum("E1_CSIU_ADRS_TYPE", E1_CSIU_ADRS_TYPE)


class E1_CSIU_WCO_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_CSIU_WCO_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    CSIU_WCO_WEAPONS_FREE = 0x00
    CSIU_WCO_WEAPONS_UNDER_CONTROL = 0x01
    CSIU_WCO_WEAPONS_HOLD_FIRE = 0x02


vAddEnum("E1_CSIU_WCO_TYPE", E1_CSIU_WCO_TYPE)


class E1_CSIU_NO_YES_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_CSIU_NO_YES_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    CSIU_NO = 0x00
    CSIU_YES = 0x01


vAddEnum("E1_CSIU_NO_YES_TYPE", E1_CSIU_NO_YES_TYPE)


class E1_CSIU_ACTION_STATE_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_CSIU_ACTION_STATE_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    CSIU_ACTION_STATE_OUT_OF_ACTION = 0x00
    CSIU_ACTION_STATE_READY_FOR_ACTION = 0x01
    CSIU_ACTION_STATE_IN_ACTION = 0x02


vAddEnum("E1_CSIU_ACTION_STATE_TYPE", E1_CSIU_ACTION_STATE_TYPE)


class E1_CSIU_CANTCO_WILCO_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_CSIU_CANTCO_WILCO_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    CSIU_CANTCO = 0x00
    CSIU_WILCO = 0x01


vAddEnum("E1_CSIU_CANTCO_WILCO_TYPE", E1_CSIU_CANTCO_WILCO_TYPE)


class E1_CSIU_ENGAGEMENT_STATE_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_CSIU_ENGAGEMENT_STATE_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    CSIU_ENGAGEMENT_STATE_PENDING = 0x00
    CSIU_ENGAGEMENT_STATE_INITIATED = 0x01
    CSIU_ENGAGEMENT_STATE_STOP_FIRE = 0x02
    CSIU_ENGAGEMENT_STATE_HOLD_FIRE = 0x03


vAddEnum("E1_CSIU_ENGAGEMENT_STATE_TYPE", E1_CSIU_ENGAGEMENT_STATE_TYPE)


class E1_CSIU_ENGAGEMENT_ACTION_STATUS_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_CSIU_ENGAGEMENT_ACTION_STATUS_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    CSIU_ENGAGEMENT_ACTION_STATUS_NO_TRACKING = 0x00
    CSIU_ENGAGEMENT_ACTION_STATUS_TRACKING = 0x01
    CSIU_ENGAGEMENT_ACTION_STATUS_FIRED = 0x02


vAddEnum("E1_CSIU_ENGAGEMENT_ACTION_STATUS_TYPE", E1_CSIU_ENGAGEMENT_ACTION_STATUS_TYPE)


class E1_CSIU_ENGAGEMENT_WEAPON_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_CSIU_ENGAGEMENT_WEAPON_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    CSIU_ENGAGEMENT_WEAPON_MISSILE_VSHORAD = 0x00
    CSIU_ENGAGEMENT_WEAPON_MISSILE_SHORAD = 0x01
    CSIU_ENGAGEMENT_WEAPON_MISSILE_ESHORAD = 0x02
    CSIU_ENGAGEMENT_WEAPON_MISSILE_MRAD = 0x03
    CSIU_ENGAGEMENT_WEAPON_GUNS_35_STD = 0x04
    CSIU_ENGAGEMENT_WEAPON_GUNS_35_AHEAD = 0x05
    CSIU_ENGAGEMENT_WEAPON_MISSILES_AND_GUNS = 0x06


vAddEnum("E1_CSIU_ENGAGEMENT_WEAPON_TYPE", E1_CSIU_ENGAGEMENT_WEAPON_TYPE)


class E1_CSIU_AMMO_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_CSIU_AMMO_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    CSIU_AMMO_35_AHEAD = 0x00
    CSIU_AMMO_35_STD = 0x01
    CSIU_AMMO_VSHORAD = 0x02
    CSIU_AMMO_SHORAD = 0x03
    CSIU_AMMO_ESHORAD = 0x04
    CSIU_AMMO_MRAD = 0x05


vAddEnum("E1_CSIU_AMMO_TYPE", E1_CSIU_AMMO_TYPE)


class E1_CSIU_WS_STATE(clsAdcsEnumType):
    """Public class definition of type E1_CSIU_WS_STATE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    CSIU_WS_STATE_NOT_AVAILABLE = 0x00
    CSIU_WS_STATE_AVAILABLE = 0x01


vAddEnum("E1_CSIU_WS_STATE", E1_CSIU_WS_STATE)


class E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE(clsAdcsEnumType):
    """Public class definition of type E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    LINK_ZA_MSG_TEMPLATE_CODE_B = 0x02
    LINK_ZA_MSG_TEMPLATE_CODE_A = 0x01
    LINK_ZA_MSG_TEMPLATE_CODE_C = 0x03
    LINK_ZA_MSG_TEMPLATE_CODE_D = 0x04
    LINK_ZA_MSG_TEMPLATE_CODE_E = 0x05
    LINK_ZA_MSG_TEMPLATE_CODE_F = 0x06
    LINK_ZA_MSG_TEMPLATE_CODE_G = 0x07
    LINK_ZA_MSG_TEMPLATE_CODE_H = 0x08
    LINK_ZA_MSG_TEMPLATE_CODE_I = 0x09
    LINK_ZA_MSG_TEMPLATE_CODE_J = 0x0A
    LINK_ZA_MSG_TEMPLATE_CODE_K = 0x0B
    LINK_ZA_MSG_TEMPLATE_CODE_L = 0x0C
    LINK_ZA_MSG_TEMPLATE_CODE_M = 0x0D
    LINK_ZA_MSG_TEMPLATE_CODE_N = 0x0E
    LINK_ZA_MSG_TEMPLATE_CODE_O = 0x0F
    LINK_ZA_MSG_TEMPLATE_CODE_P = 0x10
    LINK_ZA_MSG_TEMPLATE_CODE_Q = 0x11
    LINK_ZA_MSG_TEMPLATE_CODE_R = 0x12
    LINK_ZA_MSG_TEMPLATE_CODE_S = 0x13
    LINK_ZA_MSG_TEMPLATE_CODE_T = 0x14
    LINK_ZA_MSG_TEMPLATE_CODE_U = 0x15
    LINK_ZA_MSG_TEMPLATE_CODE_V = 0x16
    LINK_ZA_MSG_TEMPLATE_CODE_W = 0x17
    LINK_ZA_MSG_TEMPLATE_CODE_X = 0x18
    LINK_ZA_MSG_TEMPLATE_CODE_Y = 0x19
    LINK_ZA_MSG_TEMPLATE_CODE_Z = 0x1A


vAddEnum("E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE", E1_CSIU_LINK_ZA_MSG_TEMPLATE_CODE)


class E1_CSIU_ENGAGE_ORDER_MSG_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_CSIU_ENGAGE_ORDER_MSG_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    CSIU_ENGAGE_MSG_ORDER = 0x00
    CSIU_ENGAGE_MSG_CANCEL = 0x01
    CSIU_ENGAGE_MSG_STOP = 0x02
    CSIU_ENGAGE_MSG_HOLD = 0x03


vAddEnum("E1_CSIU_ENGAGE_ORDER_MSG_TYPE", E1_CSIU_ENGAGE_ORDER_MSG_TYPE)


class E1_CSIU_LW_ORDER_MSG_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_CSIU_LW_ORDER_MSG_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    CSIU_LW_ORDER_MSG_CANCEL = 0x01
    CSIU_LW_ORDER_MSG_ORDER = 0x00


vAddEnum("E1_CSIU_LW_ORDER_MSG_TYPE", E1_CSIU_LW_ORDER_MSG_TYPE)


class E1_CSIU_LINK_ZA_VMF_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_CSIU_LINK_ZA_VMF_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    CSIU_LINK_ZA_VMF_ABSENT = 0x00
    CSIU_LINK_ZA_VMF_PRESENT = 0x01


vAddEnum("E1_CSIU_LINK_ZA_VMF_TYPE", E1_CSIU_LINK_ZA_VMF_TYPE)


class sCSIU_STATUS_AMMO_TYPE(clsAdcsStructType):
    """Public class definition of type sCSIU_STATUS_AMMO_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("sCSIU_STATUS_AMMO_TYPE")
        self.e1AmmoType = E1_CSIU_AMMO_TYPE(E1_CSIU_AMMO_TYPE.CSIU_AMMO_VSHORAD)
        self.vAddType("e1AmmoType")
        self.u2AmmoAvailable1stLineOnRamp = clsAdcsBaseType("U2", 0)
        self.u2AmmoAvailable1stLineOnRamp.vSetMin(0)
        self.u2AmmoAvailable1stLineOnRamp.vSetMax(4094)
        self.vAddType("u2AmmoAvailable1stLineOnRamp")
        self.u2AmmoAvailable1stLineStandby = clsAdcsBaseType("U2", 0)
        self.u2AmmoAvailable1stLineStandby.vSetMin(0)
        self.u2AmmoAvailable1stLineStandby.vSetMax(4094)
        self.vAddType("u2AmmoAvailable1stLineStandby")


vAddClass("sCSIU_STATUS_AMMO_TYPE",sCSIU_STATUS_AMMO_TYPE)


class sCSIU_TIME_HMS(clsAdcsStructType):
    """Public class definition of type sCSIU_TIME_HMS
    """
    def __init__(self, defaultValue=0):
        super().__init__("sCSIU_TIME_HMS")
        self.u1SS = clsAdcsBaseType("U1", 0)
        self.u1SS.vSetMin(0)
        self.u1SS.vSetMax(59)
        self.vAddType("u1SS")
        self.u1MM = clsAdcsBaseType("U1", 0)
        self.u1MM.vSetMin(0)
        self.u1MM.vSetMax(59)
        self.vAddType("u1MM")
        self.u1HH = clsAdcsBaseType("U1", 0)
        self.u1HH.vSetMin(0)
        self.u1HH.vSetMax(23)
        self.vAddType("u1HH")


vAddClass("sCSIU_TIME_HMS",sCSIU_TIME_HMS)


class sCSIU_DATE_JULIAN(clsAdcsStructType):
    """Public class definition of type sCSIU_DATE_JULIAN
    """
    def __init__(self, defaultValue=0):
        super().__init__("sCSIU_DATE_JULIAN")
        self.u2Date = clsAdcsBaseType("U2", 255)
        self.u2Date.vSetMin(1)
        self.u2Date.vSetMax(366)
        self.vAddType("u2Date")


vAddClass("sCSIU_DATE_JULIAN",sCSIU_DATE_JULIAN)


class sCSIU_AIR_TRACK_ALLOCATION_RECORD(clsAdcsStructType):
    """Public class definition of type sCSIU_AIR_TRACK_ALLOCATION_RECORD
    """
    def __init__(self, defaultValue=0):
        super().__init__("sCSIU_AIR_TRACK_ALLOCATION_RECORD")
        self.u2OrderSerialNumber = clsAdcsBaseType("U2", 0)
        self.vAddType("u2OrderSerialNumber")
        self.e1OrderType = E1_CSIU_LW_ORDER_MSG_TYPE(E1_CSIU_LW_ORDER_MSG_TYPE.CSIU_LW_ORDER_MSG_ORDER)
        self.vAddType("e1OrderType")
        self.e1DataPresent = E1_CSIU_LINK_ZA_VMF_TYPE(E1_CSIU_LINK_ZA_VMF_TYPE.CSIU_LINK_ZA_VMF_PRESENT)
        self.vAddType("e1DataPresent")
        self.u2FireUnitOrWsTrackNumber = clsAdcsBaseType("U2", 1)
        self.u2FireUnitOrWsTrackNumber.vSetMin(0)
        self.u2FireUnitOrWsTrackNumber.vSetMax(16383)
        self.vAddType("u2FireUnitOrWsTrackNumber")
        self.u2AirTrackNumber = clsAdcsBaseType("U2", 1)
        self.u2AirTrackNumber.vSetMin(0)
        self.u2AirTrackNumber.vSetMax(16383)
        self.vAddType("u2AirTrackNumber")
        self.u1ThreatValueForTrack = clsAdcsBaseType("U1", 1)
        self.u1ThreatValueForTrack.vSetMin(1)
        self.u1ThreatValueForTrack.vSetMax(100)
        self.vAddType("u1ThreatValueForTrack")
        self.e1WcoForTrack = E1_CSIU_WCO_TYPE(E1_CSIU_WCO_TYPE.CSIU_WCO_WEAPONS_UNDER_CONTROL)
        self.vAddType("e1WcoForTrack")


vAddClass("sCSIU_AIR_TRACK_ALLOCATION_RECORD",sCSIU_AIR_TRACK_ALLOCATION_RECORD)


class sCSIU_ENGAGEMENT_ORDER_RECORD(clsAdcsStructType):
    """Public class definition of type sCSIU_ENGAGEMENT_ORDER_RECORD
    """
    def __init__(self, defaultValue=0):
        super().__init__("sCSIU_ENGAGEMENT_ORDER_RECORD")
        self.u2OrderSerialNumber = clsAdcsBaseType("U2", 0)
        self.vAddType("u2OrderSerialNumber")
        self.e1OrderType = E1_CSIU_ENGAGE_ORDER_MSG_TYPE(E1_CSIU_ENGAGE_ORDER_MSG_TYPE.CSIU_ENGAGE_MSG_ORDER)
        self.vAddType("e1OrderType")
        self.e1DataPresent = E1_CSIU_LINK_ZA_VMF_TYPE(E1_CSIU_LINK_ZA_VMF_TYPE.CSIU_LINK_ZA_VMF_PRESENT)
        self.vAddType("e1DataPresent")
        self.u2FireUnitOrWsTrackNumber = clsAdcsBaseType("U2", 1)
        self.u2FireUnitOrWsTrackNumber.vSetMin(0)
        self.u2FireUnitOrWsTrackNumber.vSetMax(16383)
        self.vAddType("u2FireUnitOrWsTrackNumber")
        self.u2AirTrackNumber = clsAdcsBaseType("U2", 1)
        self.u2AirTrackNumber.vSetMin(0)
        self.u2AirTrackNumber.vSetMax(16383)
        self.vAddType("u2AirTrackNumber")
        self.u1ThreatValueForTrack = clsAdcsBaseType("U1", 1)
        self.u1ThreatValueForTrack.vSetMin(1)
        self.u1ThreatValueForTrack.vSetMax(100)
        self.vAddType("u1ThreatValueForTrack")
        self.e1WcoForTrack = E1_CSIU_WCO_TYPE(E1_CSIU_WCO_TYPE.CSIU_WCO_WEAPONS_UNDER_CONTROL)
        self.vAddType("e1WcoForTrack")
        self.e1EngageDetailsPresent = E1_CSIU_LINK_ZA_VMF_TYPE(E1_CSIU_LINK_ZA_VMF_TYPE.CSIU_LINK_ZA_VMF_PRESENT)
        self.vAddType("e1EngageDetailsPresent")
        self.e1AmmoType = E1_CSIU_AMMO_TYPE(E1_CSIU_AMMO_TYPE.CSIU_AMMO_VSHORAD)
        self.vAddType("e1AmmoType")
        self.u2SalvoSize = clsAdcsBaseType("U2", 1)
        self.u2SalvoSize.vSetMin(1)
        self.u2SalvoSize.vSetMax(4095)
        self.vAddType("u2SalvoSize")
        self.sFirstTimeToFire = sCSIU_TIME_HMS()
        self.vAddType("sFirstTimeToFire")
        self.sLastTimeToFire = sCSIU_TIME_HMS()
        self.vAddType("sLastTimeToFire")
        self.sRecommendedTimeToFire = sCSIU_TIME_HMS()
        self.vAddType("sRecommendedTimeToFire")


vAddClass("sCSIU_ENGAGEMENT_ORDER_RECORD",sCSIU_ENGAGEMENT_ORDER_RECORD)


# TYPEDEFS END







