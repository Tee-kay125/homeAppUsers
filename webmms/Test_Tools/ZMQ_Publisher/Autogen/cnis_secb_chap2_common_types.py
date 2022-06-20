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
class E1_LZA_MESSAGE_TYPE(clsAdcsEnumType):
    """Public class definition of type E1_LZA_MESSAGE_TYPE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    LZA_MESSAGE_TYPE_T10 = 0x0A
    LZA_MESSAGE_TYPE_T11 = 0x0B
    LZA_MESSAGE_TYPE_T12 = 0x0C
    LZA_MESSAGE_TYPE_T61 = 0x3D
    LZA_MESSAGE_TYPE_T63 = 0x3F
    LZA_MESSAGE_TYPE_T98 = 0x62
    LZA_MESSAGE_TYPE_T99 = 0x63
    LZA_MESSAGE_TYPE_C01 = 0x65
    LZA_MESSAGE_TYPE_C02 = 0x66
    LZA_MESSAGE_TYPE_C04 = 0x68
    LZA_MESSAGE_TYPE_L06 = 0x92
    LZA_MESSAGE_TYPE_Z01 = 0xB5
    LZA_MESSAGE_TYPE_Z02 = 0xB6
    LZA_MESSAGE_TYPE_Z03 = 0xB7
    LZA_MESSAGE_TYPE_Z04 = 0xB8


vAddEnum("E1_LZA_MESSAGE_TYPE", E1_LZA_MESSAGE_TYPE)


class E1_LZA_PRECEDENCE_LEVEL(clsAdcsEnumType):
    """Public class definition of type E1_LZA_PRECEDENCE_LEVEL
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    LZA_PRECEDENCE_LEVEL_FLASH_OVERRIDE = 0x00
    LZA_PRECEDENCE_LEVEL_FLASH = 0x01
    LZA_PRECEDENCE_LEVEL_IMMEDIATE = 0x02
    LZA_PRECEDENCE_LEVEL_PRIORITY = 0x03
    LZA_PRECEDENCE_LEVEL_ROUTINE = 0x04


vAddEnum("E1_LZA_PRECEDENCE_LEVEL", E1_LZA_PRECEDENCE_LEVEL)


class E1_LZA_FLAG(clsAdcsEnumType):
    """Public class definition of type E1_LZA_FLAG
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    LZA_FLAG_FALSE = 0x00
    LZA_FLAG_TRUE = 0x01


vAddEnum("E1_LZA_FLAG", E1_LZA_FLAG)


class E1_LZA_HOSTILITY(clsAdcsEnumType):
    """Public class definition of type E1_LZA_HOSTILITY
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    LZA_HOSTILITY_A = 0x00
    LZA_HOSTILITY_B = 0x01
    LZA_HOSTILITY_C = 0x02
    LZA_HOSTILITY_D = 0x03
    LZA_HOSTILITY_E = 0x04
    LZA_HOSTILITY_F = 0x05
    LZA_HOSTILITY_G = 0x07


vAddEnum("E1_LZA_HOSTILITY", E1_LZA_HOSTILITY)


class E1_LZA_SENSOR_ID(clsAdcsEnumType):
    """Public class definition of type E1_LZA_SENSOR_ID
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    LZA_SENSORID_RADAR = 0x00
    LZA_SENSORID_ESM = 0x01
    LZA_SENSORID_EOS = 0x02
    LZA_SENSORID_MARKER = 0x03
    LZA_SENSORID_TDP_TARGET = 0x04
    LZA_SENSORID_PREPLANNED_TARGET = 0x05
    LZA_SENSORID_BLANK = 0x07


vAddEnum("E1_LZA_SENSOR_ID", E1_LZA_SENSOR_ID)


class E1_LZA_PRESENT(clsAdcsEnumType):
    """Public class definition of type E1_LZA_PRESENT
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    LZA_INDICATOR_ABSENT = 0x00
    LZA_INDICATOR_PRESENT = 0x01


vAddEnum("E1_LZA_PRESENT", E1_LZA_PRESENT)


class E1_LZA_TRACK_QUALITY_FORMAT(clsAdcsEnumType):
    """Public class definition of type E1_LZA_TRACK_QUALITY_FORMAT
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    LZA_QUALITY_FORMAT_XYZ = 0x01


vAddEnum("E1_LZA_TRACK_QUALITY_FORMAT", E1_LZA_TRACK_QUALITY_FORMAT)


class E1_LZA_TRACK_POSITION_QUALITY(clsAdcsEnumType):
    """Public class definition of type E1_LZA_TRACK_POSITION_QUALITY
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    LZA_POSITION_QUALITY_LT001 = 0x00
    LZA_POSITION_QUALITY_LT003 = 0x01
    LZA_POSITION_QUALITY_LT010 = 0x02
    LZA_POSITION_QUALITY_LT030 = 0x03
    LZA_POSITION_QUALITY_LT100 = 0x04
    LZA_POSITION_QUALITY_LT300 = 0x05
    LZA_POSITION_QUALITY_GT300 = 0x06
    LZA_POSITION_QUALITY_UNKNOWN = 0x07


vAddEnum("E1_LZA_TRACK_POSITION_QUALITY", E1_LZA_TRACK_POSITION_QUALITY)


class E1_LZA_TRACK_VELOCITY_QUALITY(clsAdcsEnumType):
    """Public class definition of type E1_LZA_TRACK_VELOCITY_QUALITY
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    LZA_VELOCITY_QUALITY_LT010 = 0x00
    LZA_VELOCITY_QUALITY_LT030 = 0x01
    LZA_VELOCITY_QUALITY_GT030 = 0x02
    LZA_VELOCITY_QUALITY_UNKNOWN = 0x03


vAddEnum("E1_LZA_TRACK_VELOCITY_QUALITY", E1_LZA_TRACK_VELOCITY_QUALITY)


class E1_LZA_BEARING_ERROR(clsAdcsEnumType):
    """Public class definition of type E1_LZA_BEARING_ERROR
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    E1_LZA_BEARING_ERROR_LT_009 = 0x00
    E1_LZA_BEARING_ERROR_LT_018 = 0x01
    E1_LZA_BEARING_ERROR_LT_035 = 0x02
    E1_LZA_BEARING_ERROR_LT_090 = 0x03
    E1_LZA_BEARING_ERROR_GT_090 = 0x04
    E1_LZA_BEARING_ERROR_UNKNOWN = 0x07


vAddEnum("E1_LZA_BEARING_ERROR", E1_LZA_BEARING_ERROR)


class E1_LZA_BEARING_ELEVATION_ERROR(clsAdcsEnumType):
    """Public class definition of type E1_LZA_BEARING_ELEVATION_ERROR
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    E1_LZA_BEARING_ELEVATION_ERROR_LT_005 = 0x00
    E1_LZA_BEARING_ELEVATION_ERROR_LT_010 = 0x01
    E1_LZA_BEARING_ELEVATION_ERROR_LT_020 = 0x02
    E1_LZA_BEARING_ELEVATION_ERROR_LT_050 = 0x03
    E1_LZA_BEARING_ELEVATION_ERROR_GT_050 = 0x04
    E1_LZA_BEARING_ELEVATION_ERROR_UNKNOWN = 0x07


vAddEnum("E1_LZA_BEARING_ELEVATION_ERROR", E1_LZA_BEARING_ELEVATION_ERROR)


class E1_LZA_BEARING_TRACK_PINNACLE(clsAdcsEnumType):
    """Public class definition of type E1_LZA_BEARING_TRACK_PINNACLE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    E1_LZA_BEARING_TRACK_PINNACLE_AIR = 0x00
    E1_LZA_BEARING_TRACK_PINNACLE_SURFACE = 0x01
    E1_ZA_BEARING_TRACK_PINNACLE_LAND = 0x02
    E1_LZA_BEARING_TRACK_PINNACLE_UNKNOWN = 0x07


vAddEnum("E1_LZA_BEARING_TRACK_PINNACLE", E1_LZA_BEARING_TRACK_PINNACLE)


class E1_LZA_TRACK_PRIORITY(clsAdcsEnumType):
    """Public class definition of type E1_LZA_TRACK_PRIORITY
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    LZA_TRACK_PRIORITY_HIGH = 0x00
    LZA_TRACK_PRIORITY_MEDIUM = 0x01
    LZA_TRACK_PRIORITYY_LOW = 0x02
    LZA_TRACK_PRIORITY_BLANK = 0x03


vAddEnum("E1_LZA_TRACK_PRIORITY", E1_LZA_TRACK_PRIORITY)


class E1_LZA_TRACK_TIMESTAMP_FORMAT(clsAdcsEnumType):
    """Public class definition of type E1_LZA_TRACK_TIMESTAMP_FORMAT
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    LZA_TRACK_TIMESTAMP_FORMAT_REAL_TIME = 0x01


vAddEnum("E1_LZA_TRACK_TIMESTAMP_FORMAT", E1_LZA_TRACK_TIMESTAMP_FORMAT)


class E1_LZA_TRACK_DELETE(clsAdcsEnumType):
    """Public class definition of type E1_LZA_TRACK_DELETE
    """
    def __init__(self, defaultValue=0):
        super().__init__("U1", defaultValue)
    LZA_TRACK_DO_NOT_DELETE = 0x00
    LZA_TRACK_DELETE = 0x01


vAddEnum("E1_LZA_TRACK_DELETE", E1_LZA_TRACK_DELETE)


class sLZA_HEADER_DESTINATION(clsAdcsStructType):
    """Public class definition of type sLZA_HEADER_DESTINATION
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_HEADER_DESTINATION")
        self.u2PhysicalAddress = clsAdcsBaseType("U2", 0)
        self.u2PhysicalAddress.vSetMin(0)
        self.u2PhysicalAddress.vSetMax(8191)
        self.vAddType("u2PhysicalAddress")
        self.u1HostID = clsAdcsBaseType("U1", 0)
        self.u1HostID.vSetMin(0)
        self.u1HostID.vSetMax(14)
        self.vAddType("u1HostID")
        self.u1ApplicationTerminal = clsAdcsBaseType("U1", 0)
        self.u1ApplicationTerminal.vSetMin(0)
        self.u1ApplicationTerminal.vSetMax(14)
        self.vAddType("u1ApplicationTerminal")
        self.e1AcknowledgeRequired = E1_LZA_FLAG(E1_LZA_FLAG.LZA_FLAG_TRUE)
        self.vAddType("e1AcknowledgeRequired")


vAddClass("sLZA_HEADER_DESTINATION",sLZA_HEADER_DESTINATION)


class sLZA_HEADER_ORIGIN(clsAdcsStructType):
    """Public class definition of type sLZA_HEADER_ORIGIN
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_HEADER_ORIGIN")
        self.u2PhysicalAddress = clsAdcsBaseType("U2", 0)
        self.u2PhysicalAddress.vSetMin(0)
        self.u2PhysicalAddress.vSetMax(8191)
        self.vAddType("u2PhysicalAddress")
        self.u1HostID = clsAdcsBaseType("U1", 0)
        self.u1HostID.vSetMin(0)
        self.u1HostID.vSetMax(14)
        self.vAddType("u1HostID")
        self.u1ApplicationTerminal = clsAdcsBaseType("U1", 0)
        self.u1ApplicationTerminal.vSetMin(0)
        self.u1ApplicationTerminal.vSetMax(14)
        self.vAddType("u1ApplicationTerminal")


vAddClass("sLZA_HEADER_ORIGIN",sLZA_HEADER_ORIGIN)


class sLZA_HEADER_TIME(clsAdcsStructType):
    """Public class definition of type sLZA_HEADER_TIME
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_HEADER_TIME")
        self.u1Second = clsAdcsBaseType("U1", 0)
        self.u1Second.vSetMin(0)
        self.u1Second.vSetMax(59)
        self.vAddType("u1Second")
        self.u1Minute = clsAdcsBaseType("U1", 0)
        self.u1Minute.vSetMin(0)
        self.u1Minute.vSetMax(59)
        self.vAddType("u1Minute")
        self.u1Hour = clsAdcsBaseType("U1", 0)
        self.u1Hour.vSetMin(0)
        self.u1Hour.vSetMax(23)
        self.vAddType("u1Hour")


vAddClass("sLZA_HEADER_TIME",sLZA_HEADER_TIME)


class sLZA_HEADER(clsAdcsStructType):
    """Public class definition of type sLZA_HEADER
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_HEADER")
        self.e1MessageTypeNumber = E1_LZA_MESSAGE_TYPE(E1_LZA_MESSAGE_TYPE.LZA_MESSAGE_TYPE_T10)
        self.vAddType("e1MessageTypeNumber")
        self.sOrigin = sLZA_HEADER_ORIGIN()
        self.vAddType("sOrigin")
        self.u1NetIdentifier = clsAdcsBaseType("U1", 255)
        self.u1NetIdentifier.vSetMin(255)
        self.u1NetIdentifier.vSetMax(255)
        self.vAddType("u1NetIdentifier")
        self.e1PrecedenceLevel = E1_LZA_PRECEDENCE_LEVEL(E1_LZA_PRECEDENCE_LEVEL.LZA_PRECEDENCE_LEVEL_ROUTINE)
        self.vAddType("e1PrecedenceLevel")
        self.u1ExpiryTimeLza15Second = clsAdcsBaseType("U1", 0)
        self.u1ExpiryTimeLza15Second.vSetMin(0)
        self.u1ExpiryTimeLza15Second.vSetMax(255)
        self.vAddType("u1ExpiryTimeLza15Second")
        self.u2Date = clsAdcsBaseType("U2", 0)
        self.u2Date.vSetMin(1)
        self.u2Date.vSetMax(366)
        self.vAddType("u2Date")
        self.sTransmissionTime = sLZA_HEADER_TIME()
        self.vAddType("sTransmissionTime")
        self.u2SerialNumber = clsAdcsBaseType("U2", 0)
        self.u2SerialNumber.vSetMin(1)
        self.u2SerialNumber.vSetMax(65535)
        self.vAddType("u2SerialNumber")
        self.u1NumberOfDestinations = clsAdcsBaseType("U1", 0)
        self.u1NumberOfDestinations.vSetMin(0)
        self.u1NumberOfDestinations.vSetMax(8)
        self.vAddType("u1NumberOfDestinations")
        self.asDestinations = clsAdcsStructArrayType("sLZA_HEADER_DESTINATION:8")
        self.vAddType("asDestinations")


vAddClass("sLZA_HEADER",sLZA_HEADER)


class sLZA_TRACK_QUALITY(clsAdcsStructType):
    """Public class definition of type sLZA_TRACK_QUALITY
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_TRACK_QUALITY")
        self.e1QualityFormat = E1_LZA_TRACK_QUALITY_FORMAT(E1_LZA_TRACK_QUALITY_FORMAT.LZA_QUALITY_FORMAT_XYZ)
        self.vAddType("e1QualityFormat")
        self.e1VelocityZ = E1_LZA_TRACK_VELOCITY_QUALITY(E1_LZA_TRACK_VELOCITY_QUALITY.LZA_VELOCITY_QUALITY_UNKNOWN)
        self.vAddType("e1VelocityZ")
        self.e1VelocityY = E1_LZA_TRACK_VELOCITY_QUALITY(E1_LZA_TRACK_VELOCITY_QUALITY.LZA_VELOCITY_QUALITY_UNKNOWN)
        self.vAddType("e1VelocityY")
        self.e1VelocityX = E1_LZA_TRACK_VELOCITY_QUALITY(E1_LZA_TRACK_VELOCITY_QUALITY.LZA_VELOCITY_QUALITY_UNKNOWN)
        self.vAddType("e1VelocityX")
        self.e1PositionZ = E1_LZA_TRACK_POSITION_QUALITY(E1_LZA_TRACK_POSITION_QUALITY.LZA_POSITION_QUALITY_UNKNOWN)
        self.vAddType("e1PositionZ")
        self.e1PositionY = E1_LZA_TRACK_POSITION_QUALITY(E1_LZA_TRACK_POSITION_QUALITY.LZA_POSITION_QUALITY_UNKNOWN)
        self.vAddType("e1PositionY")
        self.e1PositionX = E1_LZA_TRACK_POSITION_QUALITY(E1_LZA_TRACK_POSITION_QUALITY.LZA_POSITION_QUALITY_UNKNOWN)
        self.vAddType("e1PositionX")


vAddClass("sLZA_TRACK_QUALITY",sLZA_TRACK_QUALITY)


class sLZA_TRACK_POSITION_LLA(clsAdcsStructType):
    """Public class definition of type sLZA_TRACK_POSITION_LLA
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_TRACK_POSITION_LLA")
        self.i4LatitudeLzaArcSecond = clsAdcsBaseType("I4", 0x7FFFFF)
        self.i4LatitudeLzaArcSecond.vSetMin(-3240000)
        self.i4LatitudeLzaArcSecond.vSetMax(3240000)
        self.vAddType("i4LatitudeLzaArcSecond")
        self.i4LongitudeLzaArcSecond = clsAdcsBaseType("I4", 0xFFFFFF)
        self.i4LongitudeLzaArcSecond.vSetMin(-6480000)
        self.i4LongitudeLzaArcSecond.vSetMax(6480000)
        self.vAddType("i4LongitudeLzaArcSecond")
        self.i4AltitudeLzaMAWGS84 = clsAdcsBaseType("I4", 0x7FFFF)
        self.i4AltitudeLzaMAWGS84.vSetMin(-262140)
        self.i4AltitudeLzaMAWGS84.vSetMax(262140)
        self.vAddType("i4AltitudeLzaMAWGS84")


vAddClass("sLZA_TRACK_POSITION_LLA",sLZA_TRACK_POSITION_LLA)


class sLZA_POSITION_LL(clsAdcsStructType):
    """Public class definition of type sLZA_POSITION_LL
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_POSITION_LL")
        self.i4LatitudeLzaArcSecond = clsAdcsBaseType("I4", 0x7FFFFF)
        self.i4LatitudeLzaArcSecond.vSetMin(-3240000)
        self.i4LatitudeLzaArcSecond.vSetMax(3240000)
        self.vAddType("i4LatitudeLzaArcSecond")
        self.i4LongitudeLzaArcSecond = clsAdcsBaseType("I4", 0xFFFFFF)
        self.i4LongitudeLzaArcSecond.vSetMin(-6480000)
        self.i4LongitudeLzaArcSecond.vSetMax(6480000)
        self.vAddType("i4LongitudeLzaArcSecond")


vAddClass("sLZA_POSITION_LL",sLZA_POSITION_LL)


class sLZA_TRACK_POSITION_LLA_SURFACE(clsAdcsStructType):
    """Public class definition of type sLZA_TRACK_POSITION_LLA_SURFACE
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_TRACK_POSITION_LLA_SURFACE")
        self.i4LatitudeLzaArcSecond = clsAdcsBaseType("I4", 0x7FFFFF)
        self.i4LatitudeLzaArcSecond.vSetMin(-3240000)
        self.i4LatitudeLzaArcSecond.vSetMax(3240000)
        self.vAddType("i4LatitudeLzaArcSecond")
        self.i4LongitudeLzaArcSecond = clsAdcsBaseType("I4", 0xFFFFFF)
        self.i4LongitudeLzaArcSecond.vSetMin(-6480000)
        self.i4LongitudeLzaArcSecond.vSetMax(6480000)
        self.vAddType("i4LongitudeLzaArcSecond")
        self.i4AltitudeLzaMAWGS84 = clsAdcsBaseType("I4", 0x3FFFF)
        self.i4AltitudeLzaMAWGS84.vSetMin(0)
        self.i4AltitudeLzaMAWGS84.vSetMax(131071)
        self.vAddType("i4AltitudeLzaMAWGS84")


vAddClass("sLZA_TRACK_POSITION_LLA_SURFACE",sLZA_TRACK_POSITION_LLA_SURFACE)


class sLZA_TRACK_VELOCITY_XYZ(clsAdcsStructType):
    """Public class definition of type sLZA_TRACK_VELOCITY_XYZ
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_TRACK_VELOCITY_XYZ")
        self.i2VelocityXLzaMpS = clsAdcsBaseType("I2", 0)
        self.i2VelocityXLzaMpS.vSetMin(-32766)
        self.i2VelocityXLzaMpS.vSetMax(32766)
        self.vAddType("i2VelocityXLzaMpS")
        self.i2VelocityYLzaMpS = clsAdcsBaseType("I2", 0)
        self.i2VelocityYLzaMpS.vSetMin(-32766)
        self.i2VelocityYLzaMpS.vSetMax(32766)
        self.vAddType("i2VelocityYLzaMpS")
        self.i2VelocityZLzaMpS = clsAdcsBaseType("I2", 0)
        self.i2VelocityZLzaMpS.vSetMin(-32766)
        self.i2VelocityZLzaMpS.vSetMax(32766)
        self.vAddType("i2VelocityZLzaMpS")


vAddClass("sLZA_TRACK_VELOCITY_XYZ",sLZA_TRACK_VELOCITY_XYZ)


class sLZA_TRACK_VELOCITY_XYZ_SURFACE(clsAdcsStructType):
    """Public class definition of type sLZA_TRACK_VELOCITY_XYZ_SURFACE
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_TRACK_VELOCITY_XYZ_SURFACE")
        self.i2VelocityXLzaMpS = clsAdcsBaseType("I2", 0)
        self.i2VelocityXLzaMpS.vSetMin(-1022)
        self.i2VelocityXLzaMpS.vSetMax(1022)
        self.vAddType("i2VelocityXLzaMpS")
        self.i2VelocityYLzaMpS = clsAdcsBaseType("I2", 0)
        self.i2VelocityYLzaMpS.vSetMin(-1022)
        self.i2VelocityYLzaMpS.vSetMax(1022)
        self.vAddType("i2VelocityYLzaMpS")
        self.i2VelocityZLzaMpS = clsAdcsBaseType("I2", 0)
        self.i2VelocityZLzaMpS.vSetMin(-1022)
        self.i2VelocityZLzaMpS.vSetMax(1022)
        self.vAddType("i2VelocityZLzaMpS")


vAddClass("sLZA_TRACK_VELOCITY_XYZ_SURFACE",sLZA_TRACK_VELOCITY_XYZ_SURFACE)


class sLZA_TRACK_VELOCITY_XYZ_PU(clsAdcsStructType):
    """Public class definition of type sLZA_TRACK_VELOCITY_XYZ_PU
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_TRACK_VELOCITY_XYZ_PU")
        self.i2VelocityXLzaMpS = clsAdcsBaseType("I2", 0)
        self.i2VelocityXLzaMpS.vSetMin(-8190)
        self.i2VelocityXLzaMpS.vSetMax(8190)
        self.vAddType("i2VelocityXLzaMpS")
        self.i2VelocityYLzaMpS = clsAdcsBaseType("I2", 0)
        self.i2VelocityYLzaMpS.vSetMin(-8190)
        self.i2VelocityYLzaMpS.vSetMax(8190)
        self.vAddType("i2VelocityYLzaMpS")
        self.i2VelocityZLzaMpS = clsAdcsBaseType("I2", 0)
        self.i2VelocityZLzaMpS.vSetMin(-8190)
        self.i2VelocityZLzaMpS.vSetMax(8190)
        self.vAddType("i2VelocityZLzaMpS")


vAddClass("sLZA_TRACK_VELOCITY_XYZ_PU",sLZA_TRACK_VELOCITY_XYZ_PU)


class sLZA_ACCELERATION_XYZ(clsAdcsStructType):
    """Public class definition of type sLZA_ACCELERATION_XYZ
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_ACCELERATION_XYZ")
        self.i2AccelerationXLzaMpS2 = clsAdcsBaseType("I2", 0)
        self.i2AccelerationXLzaMpS2.vSetMin(-510)
        self.i2AccelerationXLzaMpS2.vSetMax(510)
        self.vAddType("i2AccelerationXLzaMpS2")
        self.i2AccelerationYLzaMpS2 = clsAdcsBaseType("I2", 0)
        self.i2AccelerationYLzaMpS2.vSetMin(-510)
        self.i2AccelerationYLzaMpS2.vSetMax(510)
        self.vAddType("i2AccelerationYLzaMpS2")
        self.i2AccelerationZLzaMpS2 = clsAdcsBaseType("I2", 0)
        self.i2AccelerationZLzaMpS2.vSetMin(-510)
        self.i2AccelerationZLzaMpS2.vSetMax(510)
        self.vAddType("i2AccelerationZLzaMpS2")


vAddClass("sLZA_ACCELERATION_XYZ",sLZA_ACCELERATION_XYZ)


class sLZA_ACCELERATION_XYZ_SURFACE(clsAdcsStructType):
    """Public class definition of type sLZA_ACCELERATION_XYZ_SURFACE
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_ACCELERATION_XYZ_SURFACE")
        self.i2AccelerationXLzaMpS2 = clsAdcsBaseType("I2", 0)
        self.i2AccelerationXLzaMpS2.vSetMin(-126)
        self.i2AccelerationXLzaMpS2.vSetMax(126)
        self.vAddType("i2AccelerationXLzaMpS2")
        self.i2AccelerationYLzaMpS2 = clsAdcsBaseType("I2", 0)
        self.i2AccelerationYLzaMpS2.vSetMin(-126)
        self.i2AccelerationYLzaMpS2.vSetMax(126)
        self.vAddType("i2AccelerationYLzaMpS2")
        self.i2AccelerationZLzaMpS2 = clsAdcsBaseType("I2", 0)
        self.i2AccelerationZLzaMpS2.vSetMin(-126)
        self.i2AccelerationZLzaMpS2.vSetMax(126)
        self.vAddType("i2AccelerationZLzaMpS2")


vAddClass("sLZA_ACCELERATION_XYZ_SURFACE",sLZA_ACCELERATION_XYZ_SURFACE)


class sLZA_TIMESTAMP(clsAdcsStructType):
    """Public class definition of type sLZA_TIMESTAMP
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_TIMESTAMP")
        self.e1TimeStampFormat = E1_LZA_TRACK_TIMESTAMP_FORMAT(E1_LZA_TRACK_TIMESTAMP_FORMAT.LZA_TRACK_TIMESTAMP_FORMAT_REAL_TIME)
        self.vAddType("e1TimeStampFormat")
        self.u4TimeStampRealLzaSeconds = clsAdcsBaseType("U4", 0)
        self.u4TimeStampRealLzaSeconds.vSetMin(0)
        self.u4TimeStampRealLzaSeconds.vSetMax(359999)
        self.vAddType("u4TimeStampRealLzaSeconds")


vAddClass("sLZA_TIMESTAMP",sLZA_TIMESTAMP)


class sLZA_C04_BEARING(clsAdcsStructType):
    """Public class definition of type sLZA_C04_BEARING
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_C04_BEARING")
        self.u2BearingMils = clsAdcsBaseType("U2", 0x1FFF)
        self.u2BearingMils.vSetMin(1)
        self.u2BearingMils.vSetMax(6400)
        self.vAddType("u2BearingMils")
        self.e1BearingError = E1_LZA_BEARING_ERROR(E1_LZA_BEARING_ERROR.E1_LZA_BEARING_ERROR_UNKNOWN)
        self.vAddType("e1BearingError")


vAddClass("sLZA_C04_BEARING",sLZA_C04_BEARING)


class sLZA_C04_BEARING_ELEVATION(clsAdcsStructType):
    """Public class definition of type sLZA_C04_BEARING_ELEVATION
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_C04_BEARING_ELEVATION")
        self.i2BearingElevationDeg = clsAdcsBaseType("I2", 0)
        self.i2BearingElevationDeg.vSetMin(-900)
        self.i2BearingElevationDeg.vSetMax(900)
        self.vAddType("i2BearingElevationDeg")
        self.e1BearingError = E1_LZA_BEARING_ELEVATION_ERROR(E1_LZA_BEARING_ELEVATION_ERROR.E1_LZA_BEARING_ELEVATION_ERROR_UNKNOWN)
        self.vAddType("e1BearingError")


vAddClass("sLZA_C04_BEARING_ELEVATION",sLZA_C04_BEARING_ELEVATION)


class sLZA_AIR_TRACK(clsAdcsStructType):
    """Public class definition of type sLZA_AIR_TRACK
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_AIR_TRACK")
        self.u2Number = clsAdcsBaseType("U2", 0)
        self.u2Number.vSetMin(1)
        self.u2Number.vSetMax(16382)
        self.vAddType("u2Number")
        self.u1SymbolCode = clsAdcsBaseType("U1", 127)
        self.u1SymbolCode.vSetMin(0)
        self.u1SymbolCode.vSetMax(127)
        self.vAddType("u1SymbolCode")
        self.u1Classification = clsAdcsBaseType("U1", 0)
        self.u1Classification.vSetMin(0)
        self.u1Classification.vSetMax(255)
        self.vAddType("u1Classification")
        self.e1Hostility = E1_LZA_HOSTILITY(E1_LZA_HOSTILITY.LZA_HOSTILITY_G)
        self.vAddType("e1Hostility")
        self.u1Owner = clsAdcsBaseType("U1", 7)
        self.u1Owner.vSetMin(0)
        self.u1Owner.vSetMax(7)
        self.vAddType("u1Owner")
        self.e1SensorID = E1_LZA_SENSOR_ID(E1_LZA_SENSOR_ID.LZA_SENSORID_BLANK)
        self.vAddType("e1SensorID")
        self.e1QualityPresent = E1_LZA_PRESENT(E1_LZA_PRESENT.LZA_INDICATOR_PRESENT)
        self.vAddType("e1QualityPresent")
        self.sQuality = sLZA_TRACK_QUALITY()
        self.vAddType("sQuality")
        self.e1Priority = E1_LZA_TRACK_PRIORITY(E1_LZA_TRACK_PRIORITY.LZA_TRACK_PRIORITY_BLANK)
        self.vAddType("e1Priority")
        self.sPositionLLA = sLZA_TRACK_POSITION_LLA()
        self.vAddType("sPositionLLA")
        self.e1VelocityPresent = E1_LZA_PRESENT(E1_LZA_PRESENT.LZA_INDICATOR_PRESENT)
        self.vAddType("e1VelocityPresent")
        self.sVelocity = sLZA_TRACK_VELOCITY_XYZ()
        self.vAddType("sVelocity")
        self.e1AccelerationPresent = E1_LZA_PRESENT(E1_LZA_PRESENT.LZA_INDICATOR_ABSENT)
        self.vAddType("e1AccelerationPresent")
        self.sAcceleration = sLZA_ACCELERATION_XYZ()
        self.vAddType("sAcceleration")
        self.e1TimeStampPresent = E1_LZA_PRESENT(E1_LZA_PRESENT.LZA_INDICATOR_PRESENT)
        self.vAddType("e1TimeStampPresent")
        self.sTimeStamp = sLZA_TIMESTAMP()
        self.vAddType("sTimeStamp")
        self.e1TrackDelete = E1_LZA_TRACK_DELETE(E1_LZA_TRACK_DELETE.LZA_TRACK_DO_NOT_DELETE)
        self.vAddType("e1TrackDelete")


vAddClass("sLZA_AIR_TRACK",sLZA_AIR_TRACK)


class sLZA_SURFACE_TRACK(clsAdcsStructType):
    """Public class definition of type sLZA_SURFACE_TRACK
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_SURFACE_TRACK")
        self.u2Number = clsAdcsBaseType("U2", 0)
        self.u2Number.vSetMin(1)
        self.u2Number.vSetMax(16382)
        self.vAddType("u2Number")
        self.u1SymbolCode = clsAdcsBaseType("U1", 127)
        self.u1SymbolCode.vSetMin(0)
        self.u1SymbolCode.vSetMax(127)
        self.vAddType("u1SymbolCode")
        self.u2Classification = clsAdcsBaseType("U2", 0)
        self.u2Classification.vSetMin(0)
        self.u2Classification.vSetMax(8191)
        self.vAddType("u2Classification")
        self.e1Hostility = E1_LZA_HOSTILITY(E1_LZA_HOSTILITY.LZA_HOSTILITY_G)
        self.vAddType("e1Hostility")
        self.u1Owner = clsAdcsBaseType("U1", 7)
        self.u1Owner.vSetMin(0)
        self.u1Owner.vSetMax(7)
        self.vAddType("u1Owner")
        self.e1SensorID = E1_LZA_SENSOR_ID(E1_LZA_SENSOR_ID.LZA_SENSORID_BLANK)
        self.vAddType("e1SensorID")
        self.e1QualityPresent = E1_LZA_PRESENT(E1_LZA_PRESENT.LZA_INDICATOR_PRESENT)
        self.vAddType("e1QualityPresent")
        self.sQuality = sLZA_TRACK_QUALITY()
        self.vAddType("sQuality")
        self.e1Priority = E1_LZA_TRACK_PRIORITY(E1_LZA_TRACK_PRIORITY.LZA_TRACK_PRIORITY_BLANK)
        self.vAddType("e1Priority")
        self.sPositionLLA = sLZA_TRACK_POSITION_LLA_SURFACE()
        self.vAddType("sPositionLLA")
        self.e1VelocityPresent = E1_LZA_PRESENT(E1_LZA_PRESENT.LZA_INDICATOR_PRESENT)
        self.vAddType("e1VelocityPresent")
        self.sVelocity = sLZA_TRACK_VELOCITY_XYZ_SURFACE()
        self.vAddType("sVelocity")
        self.e1AccelerationPresent = E1_LZA_PRESENT(E1_LZA_PRESENT.LZA_INDICATOR_ABSENT)
        self.vAddType("e1AccelerationPresent")
        self.sAcceleration = sLZA_ACCELERATION_XYZ_SURFACE()
        self.vAddType("sAcceleration")
        self.e1TimeStampPresent = E1_LZA_PRESENT(E1_LZA_PRESENT.LZA_INDICATOR_PRESENT)
        self.vAddType("e1TimeStampPresent")
        self.sTimeStamp = sLZA_TIMESTAMP()
        self.vAddType("sTimeStamp")
        self.e1TrackDelete = E1_LZA_TRACK_DELETE(E1_LZA_TRACK_DELETE.LZA_TRACK_DO_NOT_DELETE)
        self.vAddType("e1TrackDelete")


vAddClass("sLZA_SURFACE_TRACK",sLZA_SURFACE_TRACK)


class sLZA_BEARING_TRACK(clsAdcsStructType):
    """Public class definition of type sLZA_BEARING_TRACK
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_BEARING_TRACK")
        self.u2Number = clsAdcsBaseType("U2", 0)
        self.u2Number.vSetMin(1)
        self.u2Number.vSetMax(16382)
        self.vAddType("u2Number")
        self.u1SymbolCode = clsAdcsBaseType("U1", 127)
        self.u1SymbolCode.vSetMin(0)
        self.u1SymbolCode.vSetMax(127)
        self.vAddType("u1SymbolCode")
        self.u1Classification = clsAdcsBaseType("U1", 0)
        self.u1Classification.vSetMin(0)
        self.u1Classification.vSetMax(255)
        self.vAddType("u1Classification")
        self.e1Hostility = E1_LZA_HOSTILITY(E1_LZA_HOSTILITY.LZA_HOSTILITY_G)
        self.vAddType("e1Hostility")
        self.u1Owner = clsAdcsBaseType("U1", 7)
        self.u1Owner.vSetMin(0)
        self.u1Owner.vSetMax(7)
        self.vAddType("u1Owner")
        self.e1SensorID = E1_LZA_SENSOR_ID(E1_LZA_SENSOR_ID.LZA_SENSORID_BLANK)
        self.vAddType("e1SensorID")
        self.e1Priority = E1_LZA_TRACK_PRIORITY(E1_LZA_TRACK_PRIORITY.LZA_TRACK_PRIORITY_BLANK)
        self.vAddType("e1Priority")
        self.sBearing = sLZA_C04_BEARING()
        self.vAddType("sBearing")
        self.e1ElevationAnglePresent = E1_LZA_PRESENT(E1_LZA_PRESENT.LZA_INDICATOR_PRESENT)
        self.vAddType("e1ElevationAnglePresent")
        self.sBearingElevation = sLZA_C04_BEARING_ELEVATION()
        self.vAddType("sBearingElevation")
        self.u2InterceptorId = clsAdcsBaseType("U2", 0)
        self.u2InterceptorId.vSetMin(1)
        self.u2InterceptorId.vSetMax(16382)
        self.vAddType("u2InterceptorId")
        self.sInterceptorPositionLL = sLZA_POSITION_LL()
        self.vAddType("sInterceptorPositionLL")
        self.e1PinnacleofBearingTrack = E1_LZA_BEARING_TRACK_PINNACLE(E1_LZA_BEARING_TRACK_PINNACLE.E1_LZA_BEARING_TRACK_PINNACLE_UNKNOWN)
        self.vAddType("e1PinnacleofBearingTrack")
        self.e1InterceptorAltitudePresent = E1_LZA_PRESENT(E1_LZA_PRESENT.LZA_INDICATOR_ABSENT)
        self.vAddType("e1InterceptorAltitudePresent")
        self.i4InterceptorAltitudeLzaMAWGS84 = clsAdcsBaseType("I4", 0)
        self.i4InterceptorAltitudeLzaMAWGS84.vSetMin(-262140)
        self.i4InterceptorAltitudeLzaMAWGS84.vSetMax(262140)
        self.vAddType("i4InterceptorAltitudeLzaMAWGS84")
        self.e1TimeStampPresent = E1_LZA_PRESENT(E1_LZA_PRESENT.LZA_INDICATOR_PRESENT)
        self.vAddType("e1TimeStampPresent")
        self.sTimeStamp = sLZA_TIMESTAMP()
        self.vAddType("sTimeStamp")
        self.e1TrackDelete = E1_LZA_TRACK_DELETE(E1_LZA_TRACK_DELETE.LZA_TRACK_DO_NOT_DELETE)
        self.vAddType("e1TrackDelete")


vAddClass("sLZA_BEARING_TRACK",sLZA_BEARING_TRACK)


class sLZA_OWN_POSITION_TRACK(clsAdcsStructType):
    """Public class definition of type sLZA_OWN_POSITION_TRACK
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_OWN_POSITION_TRACK")
        self.u2Number = clsAdcsBaseType("U2", 0)
        self.u2Number.vSetMin(1)
        self.u2Number.vSetMax(16382)
        self.vAddType("u2Number")
        self.u1SymbolCode = clsAdcsBaseType("U1", 127)
        self.u1SymbolCode.vSetMin(0)
        self.u1SymbolCode.vSetMax(127)
        self.vAddType("u1SymbolCode")
        self.u2Classification = clsAdcsBaseType("U2", 0)
        self.u2Classification.vSetMin(0)
        self.u2Classification.vSetMax(8191)
        self.vAddType("u2Classification")
        self.u1Owner = clsAdcsBaseType("U1", 7)
        self.u1Owner.vSetMin(0)
        self.u1Owner.vSetMax(7)
        self.vAddType("u1Owner")
        self.e1QualityPresent = E1_LZA_PRESENT(E1_LZA_PRESENT.LZA_INDICATOR_PRESENT)
        self.vAddType("e1QualityPresent")
        self.sQuality = sLZA_TRACK_QUALITY()
        self.vAddType("sQuality")
        self.sPositionLLA = sLZA_TRACK_POSITION_LLA()
        self.vAddType("sPositionLLA")
        self.e1VelocityPresent = E1_LZA_PRESENT(E1_LZA_PRESENT.LZA_INDICATOR_PRESENT)
        self.vAddType("e1VelocityPresent")
        self.sVelocity = sLZA_TRACK_VELOCITY_XYZ_PU()
        self.vAddType("sVelocity")
        self.e1MachNumberPresent = E1_LZA_PRESENT(E1_LZA_PRESENT.LZA_INDICATOR_PRESENT)
        self.vAddType("e1MachNumberPresent")
        self.u1MachNumber = clsAdcsBaseType("U1", 0)
        self.u1MachNumber.vSetMin(0)
        self.u1MachNumber.vSetMax(255)
        self.vAddType("u1MachNumber")
        self.e1AccelerationPresent = E1_LZA_PRESENT(E1_LZA_PRESENT.LZA_INDICATOR_ABSENT)
        self.vAddType("e1AccelerationPresent")
        self.sAcceleration = sLZA_ACCELERATION_XYZ()
        self.vAddType("sAcceleration")
        self.e1TimeStampPresent = E1_LZA_PRESENT(E1_LZA_PRESENT.LZA_INDICATOR_PRESENT)
        self.vAddType("e1TimeStampPresent")
        self.u4TimeStamp = clsAdcsBaseType("U4", 0)
        self.u4TimeStamp.vSetMin(0)
        self.u4TimeStamp.vSetMax(359999)
        self.vAddType("u4TimeStamp")


vAddClass("sLZA_OWN_POSITION_TRACK",sLZA_OWN_POSITION_TRACK)


class sLZA_C01(clsAdcsStructType):
    """Public class definition of type sLZA_C01
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_C01")
        self.sLzaHeader = sLZA_HEADER()
        self.vAddType("sLzaHeader")
        self.u1NumberOfTracks = clsAdcsBaseType("U1", 1)
        self.u1NumberOfTracks.vSetMin(1)
        self.u1NumberOfTracks.vSetMax(16)
        self.vAddType("u1NumberOfTracks")
        self.asAirTrack = clsAdcsStructArrayType("sLZA_AIR_TRACK:16")
        self.vAddType("asAirTrack")


vAddClass("sLZA_C01",sLZA_C01)


class sLZA_C02(clsAdcsStructType):
    """Public class definition of type sLZA_C02
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_C02")
        self.sLzaHeader = sLZA_HEADER()
        self.vAddType("sLzaHeader")
        self.u1NumberOfTracks = clsAdcsBaseType("U1", 1)
        self.u1NumberOfTracks.vSetMin(1)
        self.u1NumberOfTracks.vSetMax(16)
        self.vAddType("u1NumberOfTracks")
        self.asSurfaceTrack = clsAdcsStructArrayType("sLZA_SURFACE_TRACK:16")
        self.vAddType("asSurfaceTrack")


vAddClass("sLZA_C02",sLZA_C02)


class sLZA_C04(clsAdcsStructType):
    """Public class definition of type sLZA_C04
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_C04")
        self.sLzaHeader = sLZA_HEADER()
        self.vAddType("sLzaHeader")
        self.u1NumberOfTracks = clsAdcsBaseType("U1", 1)
        self.u1NumberOfTracks.vSetMin(1)
        self.u1NumberOfTracks.vSetMax(16)
        self.vAddType("u1NumberOfTracks")
        self.asBearingTrack = clsAdcsStructArrayType("sLZA_BEARING_TRACK:16")
        self.vAddType("asBearingTrack")


vAddClass("sLZA_C04",sLZA_C04)


class sLZA_L06(clsAdcsStructType):
    """Public class definition of type sLZA_L06
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_L06")
        self.sLzaHeader = sLZA_HEADER()
        self.vAddType("sLzaHeader")
        self.sOwnPositionTrack = sLZA_OWN_POSITION_TRACK()
        self.vAddType("sOwnPositionTrack")


vAddClass("sLZA_L06",sLZA_L06)


class sLZA_C01_UNSOL_MSG(clsAdcsStructType):
    """Public class definition of type sLZA_C01_UNSOL_MSG
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_C01_UNSOL_MSG")
        self.sMsgHeader = sLZA_HEADER()
        self.vAddType("sMsgHeader")
        self.sLzaC01 = sLZA_C01()
        self.vAddType("sLzaC01")


vAddClass("sLZA_C01_UNSOL_MSG",sLZA_C01_UNSOL_MSG)


class sLZA_C02_UNSOL_MSG(clsAdcsStructType):
    """Public class definition of type sLZA_C02_UNSOL_MSG
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_C02_UNSOL_MSG")
        self.sMsgHeader = sLZA_HEADER()
        self.vAddType("sMsgHeader")
        self.sLzaC02 = sLZA_C02()
        self.vAddType("sLzaC02")


vAddClass("sLZA_C02_UNSOL_MSG",sLZA_C02_UNSOL_MSG)


class sLZA_C04_UNSOL_MSG(clsAdcsStructType):
    """Public class definition of type sLZA_C04_UNSOL_MSG
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_C04_UNSOL_MSG")
        self.sMsgHeader = sLZA_HEADER()
        self.vAddType("sMsgHeader")
        self.sLzaC04 = sLZA_C04()
        self.vAddType("sLzaC04")


vAddClass("sLZA_C04_UNSOL_MSG",sLZA_C04_UNSOL_MSG)


class sLZA_L06_UNSOL_MSG(clsAdcsStructType):
    """Public class definition of type sLZA_L06_UNSOL_MSG
    """
    def __init__(self, defaultValue=0):
        super().__init__("sLZA_L06_UNSOL_MSG")
        self.sMsgHeader = sLZA_HEADER()
        self.vAddType("sMsgHeader")
        self.sLzaL06 = sLZA_L06()
        self.vAddType("sLzaL06")


vAddClass("sLZA_L06_UNSOL_MSG",sLZA_L06_UNSOL_MSG)


# TYPEDEFS END







