#!/usr/bin/env python3.6
"""
    Autogen - Do not edit by hand!
    Autogen - Do not edit by hand!
    Autogen - Do not edit by hand!

    Generated using Python 3.6.9
    Rendered with Jinja2 2.11.1
    Generated on 2020-07-16 12:29:12 SAST
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
class E1_ADCS_BOOLEAN(clsAdcsEnumType):
    """Public class definition of type E1_ADCS_BOOLEAN
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    ADCS_BOOLEAN_FALSE = 0x00
    ADCS_BOOLEAN_TRUE = 0x01


vAddEnum("E1_ADCS_BOOLEAN", E1_ADCS_BOOLEAN)


class E1_ADCS_OVERRIDE(clsAdcsEnumType):
    """Public class definition of type E1_ADCS_OVERRIDE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    NOT_OVERRIDDEN = 0x00
    OVERRIDEN = 0x01


vAddEnum("E1_ADCS_OVERRIDE", E1_ADCS_OVERRIDE)


class E1_ADCS_SYSTEM_STATE(clsAdcsEnumType):
    """Public class definition of type E1_ADCS_SYSTEM_STATE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    SYSTEM_STATE_UNKNOWN = 0x00
    SYSTEM_STATE_OFFLINE = 0x01
    SYSTEM_STATE_INITIALISE = 0x02
    SYSTEM_STATE_READY = 0x03
    SYSTEM_STATE_OPERATIONAL = 0x04
    SYSTEM_STATE_SHUTDOWN = 0x05
    SYSTEM_STATE_FAILED = 0x06


vAddEnum("E1_ADCS_SYSTEM_STATE", E1_ADCS_SYSTEM_STATE)


class E1_ADCS_AVAILABILITY_STATE(clsAdcsEnumType):
    """Public class definition of type E1_ADCS_AVAILABILITY_STATE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    AVAILABILITY_STATE_OPERATIONAL = 0x00
    AVAILABILITY_STATE_NO_COMMS = 0x01
    AVAILABILITY_STATE_DEGRADED = 0x02
    AVAILABILITY_STATE_UNAVAILABLE = 0x03


vAddEnum("E1_ADCS_AVAILABILITY_STATE", E1_ADCS_AVAILABILITY_STATE)


class E1_ADCS_SCHEDULED_STATE(clsAdcsEnumType):
    """Public class definition of type E1_ADCS_SCHEDULED_STATE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    SCHEDULED = 0x00
    ACTIVE = 0x01


vAddEnum("E1_ADCS_SCHEDULED_STATE", E1_ADCS_SCHEDULED_STATE)


class E1_ADCS_AIR_ZONE_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_ADCS_AIR_ZONE_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    RESTRICTED_AIR_ZONE = 0x00
    PROHIBITED_AIR_ZONE = 0x01
    AREA_SAFE_FLYING = 0x02
    ZONE_APPROACH = 0x03
    ZONE_ASSET_DEFENCE = 0x04
    ZONE_OUTSIDE = 0x05


vAddEnum("E1_ADCS_AIR_ZONE_TYPE", E1_ADCS_AIR_ZONE_TYPE)


class E1_ADCS_AIR_LANE_ENTRY_METHOD(clsAdcsEnumType):
    """Public class definition of type E1_ADCS_AIR_LANE_ENTRY_METHOD
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    COORD_POINT_CENTRE_LINE = 0x00
    COORD_POINT_OUTLINE = 0x01


vAddEnum("E1_ADCS_AIR_LANE_ENTRY_METHOD", E1_ADCS_AIR_LANE_ENTRY_METHOD)


class E1_ADCS_AIR_LANE_DIRECTION_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_ADCS_AIR_LANE_DIRECTION_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    DIRECTION_BOTH_WAYS = 0x00
    DIRECTION_FROM_WAYPOINT_1 = 0x01
    DIRECTION_TOWARDS_WAYPOINT_1 = 0x02


vAddEnum("E1_ADCS_AIR_LANE_DIRECTION_TYPE", E1_ADCS_AIR_LANE_DIRECTION_TYPE)


class E1_ADCS_AIR_LANE_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_ADCS_AIR_LANE_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    FLIGHT_LANE = 0x00
    SAFE_FLYING_TUNNEL = 0x01
    SAFE_FLYING_LANE = 0x02


vAddEnum("E1_ADCS_AIR_LANE_TYPE", E1_ADCS_AIR_LANE_TYPE)


class E1_ADCS_RAID_SIZE_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_ADCS_RAID_SIZE_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    RAID_SIZE_UNKNOWN_UNITS = 0x00
    RAID_SIZE_ONE_UNIT = 0x01
    RAID_SIZE_TWO_UNITS = 0x02
    RAID_SIZE_THREE_UNITS = 0x03
    RAID_SIZE_FOUR_UNITS = 0x04
    RAID_SIZE_FIVE_UNITS = 0x05
    RAID_SIZE_SIX_UNITS = 0x06
    RAID_SIZE_SEVEN_UNITS = 0x07
    RAID_SIZE_EIGHT_UNIT = 0x08
    RAID_SIZE_NINE_UNITS = 0x09
    RAID_SIZE_TEN_UNITS = 0x0A
    RAID_SIZE_ELEVEN_UNITS = 0x0B
    RAID_SIZE_TWO_TO_SEVEN_UNITS = 0x0C
    RAID_SIZE_MORE_THAN_SEVEN_UNITS = 0x0D
    RAID_SIZE_MORE_THAN_TWELVE_UNITS = 0x0E


vAddEnum("E1_ADCS_RAID_SIZE_TYPE", E1_ADCS_RAID_SIZE_TYPE)


class E1_ADCS_POSITION_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_ADCS_POSITION_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    NO_POSITION_TYPE = 0x00
    ECEF = 0x01
    LAT_LONG = 0x02
    LAT_LONG_HEIGHT = 0x03
    SENSOR_LAT_LONG_HEIGHT_AND_RANGE_BEARING = 0x04
    SENSOR_LAT_LONG_HEIGHT_AND_RANGE_BEARING_HEIGHT = 0x05
    SENSOR_LAT_LONG_HEIGHT_AND_RANGE_BEARING_ELEVATION = 0x06
    SENSOR_LAT_LONG_HEIGHT_AND_BEARING_RANGE = 0x07
    SENSOR_LAT_LONG_HEIGHT_AND_BEARING = 0x08
    SENSOR_LAT_LONG_HEIGHT_AND_BEARING_ELEVATION = 0x09
    SENSOR_LAT_LONG_HEIGHT_AND_BEARING_ELEVATION_RANGE = 0x0A


vAddEnum("E1_ADCS_POSITION_TYPE", E1_ADCS_POSITION_TYPE)


class E1_ADCS_IFF_SECURE_MODE_RESPONSE_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_ADCS_IFF_SECURE_MODE_RESPONSE_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    NO_INTERROGATION = 0x00
    NO_RESPONSE = 0x01
    FRIEND_RESPONSE = 0x02


vAddEnum("E1_ADCS_IFF_SECURE_MODE_RESPONSE_TYPE", E1_ADCS_IFF_SECURE_MODE_RESPONSE_TYPE)


class E1_ADCS_HOSTILITY_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_ADCS_HOSTILITY_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    UNKNOWN_HOSTILITY = 0x00
    FRIEND = 0x01
    NEAR_FRIEND = 0x02
    NEUTRAL = 0x03
    NEAR_ENEMY = 0x04
    ENEMY = 0x05


vAddEnum("E1_ADCS_HOSTILITY_TYPE", E1_ADCS_HOSTILITY_TYPE)


class E1_ADCS_ENVIRONMENT_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_ADCS_ENVIRONMENT_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    UNKNOWN_ENVIRONMENT = 0x00
    AIR = 0x01
    LAND = 0x02
    SURFACE = 0x03
    SUBSURFACE = 0x04
    SPACE = 0x05


vAddEnum("E1_ADCS_ENVIRONMENT_TYPE", E1_ADCS_ENVIRONMENT_TYPE)


class E1_ADCS_ENGAGEMENT_STATUS(clsAdcsEnumType):
    """Public class definition of type E1_ADCS_ENGAGEMENT_STATUS
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    UNKNOWN_ES = 0x00
    ENGAGE_ES = 0x01
    STOP_ES = 0x02
    HOLD_ES = 0x03


vAddEnum("E1_ADCS_ENGAGEMENT_STATUS", E1_ADCS_ENGAGEMENT_STATUS)


class E1_ADCS_ENGAGEMENT_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_ADCS_ENGAGEMENT_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    PROPOSED_ET = 0x00
    PLANNED_ET = 0x01
    ACTIVE_ET = 0x02


vAddEnum("E1_ADCS_ENGAGEMENT_TYPE", E1_ADCS_ENGAGEMENT_TYPE)


class E1_ADCS_FEEDBACK_STATUS(clsAdcsEnumType):
    """Public class definition of type E1_ADCS_FEEDBACK_STATUS
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    NOFEEDBACK_FB = 0x00
    WILCO_FB = 0x01
    CANTCO_FB = 0x02
    TRACKING_FB = 0x03
    FIRING_FB = 0x04
    SUCCESS_FB = 0x05
    NOSUCCESS_FB = 0x06
    CEASEDFIRE_FB = 0x07
    HELDFIRE_FB = 0x08


vAddEnum("E1_ADCS_FEEDBACK_STATUS", E1_ADCS_FEEDBACK_STATUS)


class E1_ADCS_WCO_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_ADCS_WCO_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    WCO_WEAPONS_FREE = 0x00
    WCO_WEAPONS_UNDER_CONTROL = 0x01
    WCO_WEAPONS_HOLD_FIRE = 0x02


vAddEnum("E1_ADCS_WCO_TYPE", E1_ADCS_WCO_TYPE)


class E1_ADCS_ADRS_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_ADCS_ADRS_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    ADRS_HIGH = 0x00
    ADRS_MEDIUM = 0x01
    ADRS_LOW = 0x02


vAddEnum("E1_ADCS_ADRS_TYPE", E1_ADCS_ADRS_TYPE)


class E1_ADCS_ARWS_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_ADCS_ARWS_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    ARWS_RED = 0x00
    ARWS_YELLOW = 0x01
    ARWS_WHITE = 0x02


vAddEnum("E1_ADCS_ARWS_TYPE", E1_ADCS_ARWS_TYPE)


class sADCS_TIMESTAMP(clsAdcsStructType):
    """Public class definition of type sADCS_TIMESTAMP
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_TIMESTAMP")
        self.u4Year = clsAdcsBaseType("U4", 0)
        self.vAddType("u4Year")
        self.u4Month = clsAdcsBaseType("U4", 0)
        self.vAddType("u4Month")
        self.u4MonthDay = clsAdcsBaseType("U4", 0)
        self.vAddType("u4MonthDay")
        self.u4WeekDay = clsAdcsBaseType("U4", 0)
        self.vAddType("u4WeekDay")
        self.u4Hour = clsAdcsBaseType("U4", 0)
        self.vAddType("u4Hour")
        self.u4Minute = clsAdcsBaseType("U4", 0)
        self.vAddType("u4Minute")
        self.u4Second = clsAdcsBaseType("U4", 0)
        self.vAddType("u4Second")
        self.u4MilliSecond = clsAdcsBaseType("U4", 0)
        self.vAddType("u4MilliSecond")


vAddClass("sADCS_TIMESTAMP",sADCS_TIMESTAMP)


class sADCS_STRING8(clsAdcsStructType):
    """Public class definition of type sADCS_STRING8
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_STRING8")
        self.acString8 = clsAdcsBaseType("CH:8", "")
        self.vAddType("acString8")


vAddClass("sADCS_STRING8",sADCS_STRING8)


class sADCS_STRING24(clsAdcsStructType):
    """Public class definition of type sADCS_STRING24
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_STRING24")
        self.acString24 = clsAdcsBaseType("CH:24", "")
        self.vAddType("acString24")


vAddClass("sADCS_STRING24",sADCS_STRING24)


class sADCS_STRING512(clsAdcsStructType):
    """Public class definition of type sADCS_STRING512
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_STRING512")
        self.acString512 = clsAdcsBaseType("CH:512", "")
        self.vAddType("acString512")


vAddClass("sADCS_STRING512",sADCS_STRING512)


class sADCS_STRING1024(clsAdcsStructType):
    """Public class definition of type sADCS_STRING1024
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_STRING1024")
        self.acString1024 = clsAdcsBaseType("CH:1024", "")
        self.vAddType("acString1024")


vAddClass("sADCS_STRING1024",sADCS_STRING1024)


class sADCS_STRING128(clsAdcsStructType):
    """Public class definition of type sADCS_STRING128
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_STRING128")
        self.acString128 = clsAdcsBaseType("CH:128", "")
        self.vAddType("acString128")


vAddClass("sADCS_STRING128",sADCS_STRING128)


class sADCS_QVALUE(clsAdcsStructType):
    """Public class definition of type sADCS_QVALUE
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_QVALUE")
        self.f8Value = clsAdcsBaseType("F8", 0.0)
        self.vAddType("f8Value")
        self.f8Error = clsAdcsBaseType("F8", 0.0)
        self.vAddType("f8Error")


vAddClass("sADCS_QVALUE",sADCS_QVALUE)


class sADCS_ECEF(clsAdcsStructType):
    """Public class definition of type sADCS_ECEF
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_ECEF")
        self.sXDimM = sADCS_QVALUE()
        self.vAddType("sXDimM")
        self.sYDimM = sADCS_QVALUE()
        self.vAddType("sYDimM")
        self.sZDimM = sADCS_QVALUE()
        self.vAddType("sZDimM")


vAddClass("sADCS_ECEF",sADCS_ECEF)


class sADCS_AOR_CENTRE(clsAdcsStructType):
    """Public class definition of type sADCS_AOR_CENTRE
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_AOR_CENTRE")
        self.sPosition = sADCS_ECEF()
        self.vAddType("sPosition")
        self.u4Aor = clsAdcsBaseType("U4", 0)
        self.vAddType("u4Aor")


vAddClass("sADCS_AOR_CENTRE",sADCS_AOR_CENTRE)


class sADCS_RBE(clsAdcsStructType):
    """Public class definition of type sADCS_RBE
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_RBE")
        self.sRangeM = sADCS_QVALUE()
        self.vAddType("sRangeM")
        self.sBearingRad = sADCS_QVALUE()
        self.vAddType("sBearingRad")
        self.sElevationRad = sADCS_QVALUE()
        self.vAddType("sElevationRad")


vAddClass("sADCS_RBE",sADCS_RBE)


class sADCS_GEOMETRY(clsAdcsStructType):
    """Public class definition of type sADCS_GEOMETRY
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_GEOMETRY")
        self.sLengthM = sADCS_QVALUE()
        self.vAddType("sLengthM")
        self.sWidthM = sADCS_QVALUE()
        self.vAddType("sWidthM")
        self.f8AltitudeM = clsAdcsBaseType("F8", 0.0)
        self.vAddType("f8AltitudeM")


vAddClass("sADCS_GEOMETRY",sADCS_GEOMETRY)


class sADCS_PHYSICS(clsAdcsStructType):
    """Public class definition of type sADCS_PHYSICS
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_PHYSICS")
        self.sGeometry = sADCS_GEOMETRY()
        self.vAddType("sGeometry")
        self.u4Composition = clsAdcsBaseType("U4", 0)
        self.vAddType("u4Composition")
        self.f4Orientation = clsAdcsBaseType("F4", 0.0)
        self.vAddType("f4Orientation")


vAddClass("sADCS_PHYSICS",sADCS_PHYSICS)


class sADCS_WCO(clsAdcsStructType):
    """Public class definition of type sADCS_WCO
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_WCO")
        self.e1Wco = E1_ADCS_WCO_TYPE(E1_ADCS_WCO_TYPE.WCO_WEAPONS_UNDER_CONTROL)
        self.vAddType("e1Wco")
        self.sOriginDateTime = sADCS_TIMESTAMP()
        self.vAddType("sOriginDateTime")


vAddClass("sADCS_WCO",sADCS_WCO)


class sADCS_ADRS(clsAdcsStructType):
    """Public class definition of type sADCS_ADRS
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_ADRS")
        self.e1Adrs = E1_ADCS_ADRS_TYPE(E1_ADCS_ADRS_TYPE.ADRS_HIGH)
        self.vAddType("e1Adrs")
        self.sOriginDateTime = sADCS_TIMESTAMP()
        self.vAddType("sOriginDateTime")


vAddClass("sADCS_ADRS",sADCS_ADRS)


class sADCS_ARWS(clsAdcsStructType):
    """Public class definition of type sADCS_ARWS
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_ARWS")
        self.e1Arws = E1_ADCS_ARWS_TYPE(E1_ADCS_ARWS_TYPE.ARWS_RED)
        self.vAddType("e1Arws")
        self.sOriginDateTime = sADCS_TIMESTAMP()
        self.vAddType("sOriginDateTime")


vAddClass("sADCS_ARWS",sADCS_ARWS)


class sADCS_MODULE_STATE(clsAdcsStructType):
    """Public class definition of type sADCS_MODULE_STATE
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_MODULE_STATE")
        self.e1SystemState = E1_ADCS_SYSTEM_STATE(E1_ADCS_SYSTEM_STATE.SYSTEM_STATE_UNKNOWN)
        self.vAddType("e1SystemState")


vAddClass("sADCS_MODULE_STATE",sADCS_MODULE_STATE)


class sADCS_MODULE_INFO(clsAdcsStructType):
    """Public class definition of type sADCS_MODULE_INFO
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_MODULE_INFO")
        self.acGitShortHash = clsAdcsBaseType("CH:7", "")
        self.vAddType("acGitShortHash")
        self.acModuleName = clsAdcsBaseType("CH:32", "")
        self.vAddType("acModuleName")
        self.acCsciNumber = clsAdcsBaseType("CH:64", "")
        self.vAddType("acCsciNumber")
        self.acModuleRevision = clsAdcsBaseType("CH:32", "")
        self.vAddType("acModuleRevision")


vAddClass("sADCS_MODULE_INFO",sADCS_MODULE_INFO)


class sADCS_IDENTIFICATION(clsAdcsStructType):
    """Public class definition of type sADCS_IDENTIFICATION
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_IDENTIFICATION")
        self.e1IFFSecureModeResponse = E1_ADCS_IFF_SECURE_MODE_RESPONSE_TYPE(E1_ADCS_IFF_SECURE_MODE_RESPONSE_TYPE.NO_INTERROGATION)
        self.vAddType("e1IFFSecureModeResponse")
        self.sSquawkCode = sADCS_STRING24()
        self.vAddType("sSquawkCode")
        self.sCallsign = sADCS_STRING24()
        self.vAddType("sCallsign")


vAddClass("sADCS_IDENTIFICATION",sADCS_IDENTIFICATION)


class sADCS_SENSOR_TRACK_POSITION(clsAdcsStructType):
    """Public class definition of type sADCS_SENSOR_TRACK_POSITION
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_SENSOR_TRACK_POSITION")
        self.e1PositionType = E1_ADCS_POSITION_TYPE(E1_ADCS_POSITION_TYPE.NO_POSITION_TYPE)
        self.vAddType("e1PositionType")
        self.sPosECEF = sADCS_ECEF()
        self.vAddType("sPosECEF")
        self.sPosRBE = sADCS_RBE()
        self.vAddType("sPosRBE")
        self.e1AltitudeOverride = E1_ADCS_OVERRIDE(E1_ADCS_OVERRIDE.NOT_OVERRIDDEN)
        self.vAddType("e1AltitudeOverride")
        self.f8AltitudeM = clsAdcsBaseType("F8", 0.0)
        self.vAddType("f8AltitudeM")


vAddClass("sADCS_SENSOR_TRACK_POSITION",sADCS_SENSOR_TRACK_POSITION)


class sADCS_POINT_POSITION(clsAdcsStructType):
    """Public class definition of type sADCS_POINT_POSITION
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_POINT_POSITION")
        self.sPosECEF = sADCS_ECEF()
        self.vAddType("sPosECEF")
        self.e1AltitudeOverride = E1_ADCS_OVERRIDE(E1_ADCS_OVERRIDE.NOT_OVERRIDDEN)
        self.vAddType("e1AltitudeOverride")
        self.f8AltitudeM = clsAdcsBaseType("F8", 0.0)
        self.vAddType("f8AltitudeM")


vAddClass("sADCS_POINT_POSITION",sADCS_POINT_POSITION)


class sADCS_VELOCITY(clsAdcsStructType):
    """Public class definition of type sADCS_VELOCITY
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_VELOCITY")
        self.sVelECEF = sADCS_ECEF()
        self.vAddType("sVelECEF")


vAddClass("sADCS_VELOCITY",sADCS_VELOCITY)


class sADCS_SENSOR_TRACK_KINEMATICS(clsAdcsStructType):
    """Public class definition of type sADCS_SENSOR_TRACK_KINEMATICS
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_SENSOR_TRACK_KINEMATICS")
        self.sPosition = sADCS_SENSOR_TRACK_POSITION()
        self.vAddType("sPosition")
        self.sOrigin = sADCS_POINT_POSITION()
        self.vAddType("sOrigin")
        self.sVelocity = sADCS_VELOCITY()
        self.vAddType("sVelocity")


vAddClass("sADCS_SENSOR_TRACK_KINEMATICS",sADCS_SENSOR_TRACK_KINEMATICS)


class sADCS_SPECIFIC(clsAdcsStructType):
    """Public class definition of type sADCS_SPECIFIC
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_SPECIFIC")
        self.u4Category = clsAdcsBaseType("U4", 0)
        self.vAddType("u4Category")
        self.u4Specific = clsAdcsBaseType("U4", 0)
        self.vAddType("u4Specific")


vAddClass("sADCS_SPECIFIC",sADCS_SPECIFIC)


class sADCS_CLASSIFICATION(clsAdcsStructType):
    """Public class definition of type sADCS_CLASSIFICATION
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_CLASSIFICATION")
        self.e1Environment = E1_ADCS_ENVIRONMENT_TYPE(E1_ADCS_ENVIRONMENT_TYPE.UNKNOWN_ENVIRONMENT)
        self.vAddType("e1Environment")
        self.e1Hostility = E1_ADCS_HOSTILITY_TYPE(E1_ADCS_HOSTILITY_TYPE.UNKNOWN_HOSTILITY)
        self.vAddType("e1Hostility")
        self.sType = sADCS_SPECIFIC()
        self.vAddType("sType")
        self.sTechnique = sADCS_SPECIFIC()
        self.vAddType("sTechnique")
        self.e1RaidSize = E1_ADCS_RAID_SIZE_TYPE(E1_ADCS_RAID_SIZE_TYPE.RAID_SIZE_ONE_UNIT)
        self.vAddType("e1RaidSize")


vAddClass("sADCS_CLASSIFICATION",sADCS_CLASSIFICATION)


class sADCS_EXCLUSION_BOUNDARIES(clsAdcsStructType):
    """Public class definition of type sADCS_EXCLUSION_BOUNDARIES
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_EXCLUSION_BOUNDARIES")
        self.sThreatType = sADCS_SPECIFIC()
        self.vAddType("sThreatType")
        self.f8Range = clsAdcsBaseType("F8", 0.0)
        self.vAddType("f8Range")


vAddClass("sADCS_EXCLUSION_BOUNDARIES",sADCS_EXCLUSION_BOUNDARIES)


class sADCS_COMPOSITION(clsAdcsStructType):
    """Public class definition of type sADCS_COMPOSITION
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_COMPOSITION")
        self.u4SensorTrackCount = clsAdcsBaseType("U4", 0)
        self.u4SensorTrackCount.vSetMax(10)
        self.vAddType("u4SensorTrackCount")
        self.au4SensorTrackNumber = clsAdcsBaseType("U4:10", 0)
        self.vAddType("au4SensorTrackNumber")
        self.au4SensorID = clsAdcsBaseType("U4:10", 0)
        self.vAddType("au4SensorID")
        self.u4PreferredSensor = clsAdcsBaseType("U4", 0)
        self.vAddType("u4PreferredSensor")


vAddClass("sADCS_COMPOSITION",sADCS_COMPOSITION)


class sADCS_AMMO_AVAILABLE(clsAdcsStructType):
    """Public class definition of type sADCS_AMMO_AVAILABLE
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_AMMO_AVAILABLE")
        self.u4Quantity = clsAdcsBaseType("U4", 0)
        self.vAddType("u4Quantity")
        self.u4Type = clsAdcsBaseType("U4", 0)
        self.vAddType("u4Type")


vAddClass("sADCS_AMMO_AVAILABLE",sADCS_AMMO_AVAILABLE)


class sADCS_ARC(clsAdcsStructType):
    """Public class definition of type sADCS_ARC
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_ARC")
        self.u4StartAzimuthRad = clsAdcsBaseType("U4", 0)
        self.vAddType("u4StartAzimuthRad")
        self.u4EndAzimuthRad = clsAdcsBaseType("U4", 0)
        self.vAddType("u4EndAzimuthRad")
        self.u4InnerRangeM = clsAdcsBaseType("U4", 0)
        self.vAddType("u4InnerRangeM")
        self.u4OuterRangeM = clsAdcsBaseType("U4", 0)
        self.vAddType("u4OuterRangeM")


vAddClass("sADCS_ARC",sADCS_ARC)


class sADCS_AMMO(clsAdcsStructType):
    """Public class definition of type sADCS_AMMO
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_AMMO")
        self.sOnRamp = sADCS_AMMO_AVAILABLE()
        self.vAddType("sOnRamp")
        self.sStandby = sADCS_AMMO_AVAILABLE()
        self.vAddType("sStandby")


vAddClass("sADCS_AMMO",sADCS_AMMO)


class sADCS_ANGULAR_POSITION(clsAdcsStructType):
    """Public class definition of type sADCS_ANGULAR_POSITION
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_ANGULAR_POSITION")
        self.sPosRBE = sADCS_RBE()
        self.vAddType("sPosRBE")
        self.e1AltitudeOverride = E1_ADCS_OVERRIDE(E1_ADCS_OVERRIDE.NOT_OVERRIDDEN)
        self.vAddType("e1AltitudeOverride")
        self.f8AltitudeM = clsAdcsBaseType("F8", 0.0)
        self.vAddType("f8AltitudeM")


vAddClass("sADCS_ANGULAR_POSITION",sADCS_ANGULAR_POSITION)


class sADCS_ANGULAR_KINEMATICS(clsAdcsStructType):
    """Public class definition of type sADCS_ANGULAR_KINEMATICS
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_ANGULAR_KINEMATICS")
        self.sPosition = sADCS_ANGULAR_POSITION()
        self.vAddType("sPosition")
        self.sOrigin = sADCS_POINT_POSITION()
        self.vAddType("sOrigin")
        self.sVelocity = sADCS_VELOCITY()
        self.vAddType("sVelocity")


vAddClass("sADCS_ANGULAR_KINEMATICS",sADCS_ANGULAR_KINEMATICS)


class sADCS_POINT_KINEMATICS(clsAdcsStructType):
    """Public class definition of type sADCS_POINT_KINEMATICS
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_POINT_KINEMATICS")
        self.sPosition = sADCS_POINT_POSITION()
        self.vAddType("sPosition")
        self.sVelocity = sADCS_VELOCITY()
        self.vAddType("sVelocity")


vAddClass("sADCS_POINT_KINEMATICS",sADCS_POINT_KINEMATICS)


class sADCS_THREATINFO(clsAdcsStructType):
    """Public class definition of type sADCS_THREATINFO
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_THREATINFO")
        self.u4TrackNumber = clsAdcsBaseType("U4", 0)
        self.vAddType("u4TrackNumber")
        self.u4ThreatValue = clsAdcsBaseType("U4", 0)
        self.vAddType("u4ThreatValue")


vAddClass("sADCS_THREATINFO",sADCS_THREATINFO)


class sADCS_SCHEDULED_INFO(clsAdcsStructType):
    """Public class definition of type sADCS_SCHEDULED_INFO
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_SCHEDULED_INFO")
        self.u8StartTimeMsEp = clsAdcsBaseType("U8", 0)
        self.vAddType("u8StartTimeMsEp")
        self.u8EndTimeMsEp = clsAdcsBaseType("U8", 0)
        self.vAddType("u8EndTimeMsEp")
        self.e1State = E1_ADCS_SCHEDULED_STATE(E1_ADCS_SCHEDULED_STATE.SCHEDULED)
        self.vAddType("e1State")


vAddClass("sADCS_SCHEDULED_INFO",sADCS_SCHEDULED_INFO)


class sADCS_AIR_ZONE_CIRCULAR(clsAdcsStructType):
    """Public class definition of type sADCS_AIR_ZONE_CIRCULAR
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_AIR_ZONE_CIRCULAR")
        self.u4AirZoneID = clsAdcsBaseType("U4", 0)
        self.vAddType("u4AirZoneID")
        self.e1AirZoneType = E1_ADCS_AIR_ZONE_TYPE(E1_ADCS_AIR_ZONE_TYPE.RESTRICTED_AIR_ZONE)
        self.vAddType("e1AirZoneType")
        self.sCallsign = sADCS_STRING8()
        self.vAddType("sCallsign")
        self.sDescription = sADCS_STRING24()
        self.vAddType("sDescription")
        self.sCenterECEF = sADCS_ECEF()
        self.vAddType("sCenterECEF")
        self.u4RadiusM = clsAdcsBaseType("U4", 0)
        self.vAddType("u4RadiusM")
        self.f8AltitudeLowerLimitM = clsAdcsBaseType("F8", 0.0)
        self.vAddType("f8AltitudeLowerLimitM")
        self.f8AltitudeUpperLimitM = clsAdcsBaseType("F8", 0.0)
        self.vAddType("f8AltitudeUpperLimitM")
        self.sScheduled = sADCS_SCHEDULED_INFO()
        self.vAddType("sScheduled")
        self.e1Delete = E1_ADCS_BOOLEAN(E1_ADCS_BOOLEAN.ADCS_BOOLEAN_FALSE)
        self.vAddType("e1Delete")


vAddClass("sADCS_AIR_ZONE_CIRCULAR",sADCS_AIR_ZONE_CIRCULAR)


class sADCS_AIR_ZONE_POLYGON(clsAdcsStructType):
    """Public class definition of type sADCS_AIR_ZONE_POLYGON
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_AIR_ZONE_POLYGON")
        self.u4AirZoneID = clsAdcsBaseType("U4", 0)
        self.vAddType("u4AirZoneID")
        self.e1AirZoneType = E1_ADCS_AIR_ZONE_TYPE(E1_ADCS_AIR_ZONE_TYPE.RESTRICTED_AIR_ZONE)
        self.vAddType("e1AirZoneType")
        self.sCallsign = sADCS_STRING8()
        self.vAddType("sCallsign")
        self.sDescription = sADCS_STRING24()
        self.vAddType("sDescription")
        self.f8AltitudeLowerLimitM = clsAdcsBaseType("F8", 0.0)
        self.vAddType("f8AltitudeLowerLimitM")
        self.f8AltitudeUpperLimitM = clsAdcsBaseType("F8", 0.0)
        self.vAddType("f8AltitudeUpperLimitM")
        self.sScheduled = sADCS_SCHEDULED_INFO()
        self.vAddType("sScheduled")
        self.u4AnchorPointCount = clsAdcsBaseType("U4", 0)
        self.u4AnchorPointCount.vSetMin(2)
        self.u4AnchorPointCount.vSetMax(10)
        self.vAddType("u4AnchorPointCount")
        self.asPolyPoints = clsAdcsStructArrayType("sADCS_ECEF:10")
        self.vAddType("asPolyPoints")
        self.e1Delete = E1_ADCS_BOOLEAN(E1_ADCS_BOOLEAN.ADCS_BOOLEAN_FALSE)
        self.vAddType("e1Delete")


vAddClass("sADCS_AIR_ZONE_POLYGON",sADCS_AIR_ZONE_POLYGON)


class sADCS_AIR_LANE_POINT(clsAdcsStructType):
    """Public class definition of type sADCS_AIR_LANE_POINT
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_AIR_LANE_POINT")
        self.sPosECEF = sADCS_ECEF()
        self.vAddType("sPosECEF")
        self.f8WidthM = clsAdcsBaseType("F8", 0.0)
        self.vAddType("f8WidthM")


vAddClass("sADCS_AIR_LANE_POINT",sADCS_AIR_LANE_POINT)


class sADCS_AIR_LANE(clsAdcsStructType):
    """Public class definition of type sADCS_AIR_LANE
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_AIR_LANE")
        self.u4AirLaneID = clsAdcsBaseType("U4", 0)
        self.vAddType("u4AirLaneID")
        self.e1AirLaneType = E1_ADCS_AIR_LANE_TYPE(E1_ADCS_AIR_LANE_TYPE.FLIGHT_LANE)
        self.vAddType("e1AirLaneType")
        self.u4ParentAirZoneID = clsAdcsBaseType("U4", 0)
        self.vAddType("u4ParentAirZoneID")
        self.sCallsign = sADCS_STRING24()
        self.vAddType("sCallsign")
        self.sDescription = sADCS_STRING24()
        self.vAddType("sDescription")
        self.u4TemplateCode = clsAdcsBaseType("U4", 0x01)
        self.vAddType("u4TemplateCode")
        self.f8AltitudeLowerLimitM = clsAdcsBaseType("F8", 0.0)
        self.vAddType("f8AltitudeLowerLimitM")
        self.f8AltitudeUpperLimitM = clsAdcsBaseType("F8", 0.0)
        self.vAddType("f8AltitudeUpperLimitM")
        self.u4SpeedMps = clsAdcsBaseType("U4", 0)
        self.vAddType("u4SpeedMps")
        self.e1Direction = E1_ADCS_AIR_LANE_DIRECTION_TYPE(E1_ADCS_AIR_LANE_DIRECTION_TYPE.DIRECTION_FROM_WAYPOINT_1)
        self.vAddType("e1Direction")
        self.sScheduled = sADCS_SCHEDULED_INFO()
        self.vAddType("sScheduled")
        self.e1EntryMethod = E1_ADCS_AIR_LANE_ENTRY_METHOD(E1_ADCS_AIR_LANE_ENTRY_METHOD.COORD_POINT_CENTRE_LINE)
        self.vAddType("e1EntryMethod")
        self.u4AirLanePointCount = clsAdcsBaseType("U4", 0)
        self.u4AirLanePointCount.vSetMin(2)
        self.u4AirLanePointCount.vSetMax(10)
        self.vAddType("u4AirLanePointCount")
        self.asAirLanePoints = clsAdcsStructArrayType("sADCS_AIR_LANE_POINT:10")
        self.vAddType("asAirLanePoints")
        self.e1Delete = E1_ADCS_BOOLEAN(E1_ADCS_BOOLEAN.ADCS_BOOLEAN_FALSE)
        self.vAddType("e1Delete")


vAddClass("sADCS_AIR_LANE",sADCS_AIR_LANE)


class sADCS_IFF_LINE(clsAdcsStructType):
    """Public class definition of type sADCS_IFF_LINE
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_IFF_LINE")
        self.u4IffLineID = clsAdcsBaseType("U4", 0)
        self.vAddType("u4IffLineID")
        self.f8Interval = clsAdcsBaseType("F8", 0.0)
        self.vAddType("f8Interval")
        self.sIdentification = sADCS_IDENTIFICATION()
        self.vAddType("sIdentification")
        self.sScheduled = sADCS_SCHEDULED_INFO()
        self.vAddType("sScheduled")
        self.u4LinePointCount = clsAdcsBaseType("U4", 0)
        self.u4LinePointCount.vSetMin(2)
        self.u4LinePointCount.vSetMax(10)
        self.vAddType("u4LinePointCount")
        self.asLinePoints = clsAdcsStructArrayType("sADCS_ECEF:10")
        self.vAddType("asLinePoints")
        self.e1Delete = E1_ADCS_BOOLEAN(E1_ADCS_BOOLEAN.ADCS_BOOLEAN_FALSE)
        self.vAddType("e1Delete")


vAddClass("sADCS_IFF_LINE",sADCS_IFF_LINE)


class sADCS_FLIGHT_PLAN_WAYPOINT(clsAdcsStructType):
    """Public class definition of type sADCS_FLIGHT_PLAN_WAYPOINT
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_FLIGHT_PLAN_WAYPOINT")
        self.sPosECEF = sADCS_ECEF()
        self.vAddType("sPosECEF")
        self.u4AltitudeM = clsAdcsBaseType("U4", 0)
        self.vAddType("u4AltitudeM")
        self.u4SpeedMpS = clsAdcsBaseType("U4", 0)
        self.vAddType("u4SpeedMpS")
        self.u8TimeStampMs = clsAdcsBaseType("U8", 0)
        self.vAddType("u8TimeStampMs")


vAddClass("sADCS_FLIGHT_PLAN_WAYPOINT",sADCS_FLIGHT_PLAN_WAYPOINT)


class sADCS_FLIGHT_PLAN(clsAdcsStructType):
    """Public class definition of type sADCS_FLIGHT_PLAN
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_FLIGHT_PLAN")
        self.u4TrackNumber = clsAdcsBaseType("U4", 0)
        self.vAddType("u4TrackNumber")
        self.sClassification = sADCS_CLASSIFICATION()
        self.vAddType("sClassification")
        self.sIdentification = sADCS_IDENTIFICATION()
        self.vAddType("sIdentification")
        self.sTailNumber = sADCS_STRING24()
        self.vAddType("sTailNumber")
        self.sCommsFreq = sADCS_STRING24()
        self.vAddType("sCommsFreq")
        self.sScheduled = sADCS_SCHEDULED_INFO()
        self.vAddType("sScheduled")
        self.u4WaypointCount = clsAdcsBaseType("U4", 0)
        self.u4WaypointCount.vSetMin(2)
        self.u4WaypointCount.vSetMax(10)
        self.vAddType("u4WaypointCount")
        self.asWaypoints = clsAdcsStructArrayType("sADCS_FLIGHT_PLAN_WAYPOINT:10")
        self.vAddType("asWaypoints")
        self.e1Delete = E1_ADCS_BOOLEAN(E1_ADCS_BOOLEAN.ADCS_BOOLEAN_FALSE)
        self.vAddType("e1Delete")


vAddClass("sADCS_FLIGHT_PLAN",sADCS_FLIGHT_PLAN)


class sADCS_EFFECTOR(clsAdcsStructType):
    """Public class definition of type sADCS_EFFECTOR
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_EFFECTOR")
        self.u4TrackNumber = clsAdcsBaseType("U4", 0)
        self.vAddType("u4TrackNumber")
        self.u4PeTrackNumber = clsAdcsBaseType("U4", 0)
        self.vAddType("u4PeTrackNumber")
        self.u1EffectorType = clsAdcsBaseType("U1", 0)
        self.vAddType("u1EffectorType")
        self.sCallsign = sADCS_STRING24()
        self.vAddType("sCallsign")
        self.sDescription = sADCS_STRING24()
        self.vAddType("sDescription")
        self.u1Grouping = clsAdcsBaseType("U1", 0)
        self.vAddType("u1Grouping")
        self.sKinematics = sADCS_POINT_KINEMATICS()
        self.vAddType("sKinematics")
        self.u4Aor = clsAdcsBaseType("U4", 0)
        self.vAddType("u4Aor")
        self.u4Layer = clsAdcsBaseType("U4", 0)
        self.vAddType("u4Layer")
        self.sAmmunition = sADCS_AMMO()
        self.vAddType("sAmmunition")
        self.sPrimaryFireArc = sADCS_ARC()
        self.vAddType("sPrimaryFireArc")
        self.u4NoFireArcCount = clsAdcsBaseType("U4", 0)
        self.u4NoFireArcCount.vSetMax(10)
        self.vAddType("u4NoFireArcCount")
        self.asNoFireArcs = clsAdcsStructArrayType("sADCS_ARC:10")
        self.vAddType("asNoFireArcs")
        self.u4SurveillanceArcCount = clsAdcsBaseType("U4", 0)
        self.u4SurveillanceArcCount.vSetMax(10)
        self.vAddType("u4SurveillanceArcCount")
        self.asSurveillanceFireArcs = clsAdcsStructArrayType("sADCS_ARC:10")
        self.vAddType("asSurveillanceFireArcs")
        self.e1Availability = E1_ADCS_AVAILABILITY_STATE(E1_ADCS_AVAILABILITY_STATE.AVAILABILITY_STATE_OPERATIONAL)
        self.vAddType("e1Availability")


vAddClass("sADCS_EFFECTOR",sADCS_EFFECTOR)


class sADCS_ASSET(clsAdcsStructType):
    """Public class definition of type sADCS_ASSET
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_ASSET")
        self.u4TrackNumber = clsAdcsBaseType("U4", 0)
        self.vAddType("u4TrackNumber")
        self.u4PeTrackNumber = clsAdcsBaseType("U4", 0)
        self.vAddType("u4PeTrackNumber")
        self.sDescription = sADCS_STRING24()
        self.vAddType("sDescription")
        self.u4RadiusM = clsAdcsBaseType("U4", 0)
        self.vAddType("u4RadiusM")
        self.sKinematics = sADCS_POINT_KINEMATICS()
        self.vAddType("sKinematics")
        self.sPhysics = sADCS_PHYSICS()
        self.vAddType("sPhysics")
        self.f8AssetValue = clsAdcsBaseType("F8", 2)
        self.f8AssetValue.vSetMin(2)
        self.f8AssetValue.vSetMax(14)
        self.vAddType("f8AssetValue")
        self.e1Availability = E1_ADCS_AVAILABILITY_STATE(E1_ADCS_AVAILABILITY_STATE.AVAILABILITY_STATE_OPERATIONAL)
        self.vAddType("e1Availability")


vAddClass("sADCS_ASSET",sADCS_ASSET)


class sADCS_SENSOR(clsAdcsStructType):
    """Public class definition of type sADCS_SENSOR
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_SENSOR")
        self.u4TrackNumber = clsAdcsBaseType("U4", 0)
        self.vAddType("u4TrackNumber")
        self.u4PeTrackNumber = clsAdcsBaseType("U4", 0)
        self.vAddType("u4PeTrackNumber")
        self.sDescription = sADCS_STRING24()
        self.vAddType("sDescription")
        self.sKinematics = sADCS_POINT_KINEMATICS()
        self.vAddType("sKinematics")
        self.sClassification = sADCS_CLASSIFICATION()
        self.vAddType("sClassification")
        self.sIdentification = sADCS_IDENTIFICATION()
        self.vAddType("sIdentification")
        self.u4Range = clsAdcsBaseType("U4", 0)
        self.vAddType("u4Range")
        self.e1Availability = E1_ADCS_AVAILABILITY_STATE(E1_ADCS_AVAILABILITY_STATE.AVAILABILITY_STATE_OPERATIONAL)
        self.vAddType("e1Availability")


vAddClass("sADCS_SENSOR",sADCS_SENSOR)


class sADCS_OBSERVATION_POST(clsAdcsStructType):
    """Public class definition of type sADCS_OBSERVATION_POST
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_OBSERVATION_POST")
        self.u4TrackNumber = clsAdcsBaseType("U4", 0)
        self.vAddType("u4TrackNumber")
        self.u4PeTrackNumber = clsAdcsBaseType("U4", 0)
        self.vAddType("u4PeTrackNumber")
        self.sDescription = sADCS_STRING24()
        self.vAddType("sDescription")
        self.sKinematics = sADCS_POINT_KINEMATICS()
        self.vAddType("sKinematics")
        self.u4OpwlStartAzimuthRad = clsAdcsBaseType("U4", 0)
        self.vAddType("u4OpwlStartAzimuthRad")
        self.u4OpwlEndAzimuthRad = clsAdcsBaseType("U4", 0)
        self.vAddType("u4OpwlEndAzimuthRad")
        self.sClassification = sADCS_CLASSIFICATION()
        self.vAddType("sClassification")
        self.sPhysics = sADCS_PHYSICS()
        self.vAddType("sPhysics")
        self.f4Priority = clsAdcsBaseType("F4", 0)
        self.vAddType("f4Priority")
        self.e1Availability = E1_ADCS_AVAILABILITY_STATE(E1_ADCS_AVAILABILITY_STATE.AVAILABILITY_STATE_OPERATIONAL)
        self.vAddType("e1Availability")


vAddClass("sADCS_OBSERVATION_POST",sADCS_OBSERVATION_POST)


class sADCS_PHYSICAL_ELEMENT(clsAdcsStructType):
    """Public class definition of type sADCS_PHYSICAL_ELEMENT
    """
    def __init__(self, defaultValue=0):
        super().__init__("sADCS_PHYSICAL_ELEMENT")
        self.u4TrackNumber = clsAdcsBaseType("U4", 0)
        self.vAddType("u4TrackNumber")
        self.sDescription = sADCS_STRING24()
        self.vAddType("sDescription")
        self.sKinematics = sADCS_POINT_KINEMATICS()
        self.vAddType("sKinematics")
        self.u4Aor = clsAdcsBaseType("U4", 0)
        self.vAddType("u4Aor")
        self.sClassification = sADCS_CLASSIFICATION()
        self.vAddType("sClassification")
        self.sIdentification = sADCS_IDENTIFICATION()
        self.vAddType("sIdentification")
        self.sComposition = sADCS_COMPOSITION()
        self.vAddType("sComposition")
        self.sPhysics = sADCS_PHYSICS()
        self.vAddType("sPhysics")
        self.f4Priority = clsAdcsBaseType("F4", 0)
        self.vAddType("f4Priority")
        self.e1Availability = E1_ADCS_AVAILABILITY_STATE(E1_ADCS_AVAILABILITY_STATE.AVAILABILITY_STATE_OPERATIONAL)
        self.vAddType("e1Availability")


vAddClass("sADCS_PHYSICAL_ELEMENT",sADCS_PHYSICAL_ELEMENT)


# TYPEDEFS END







