#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
""" This module contains base classes which are inherited within Python autogen definitions.

Todo:

"""


from enum import Enum
import struct
import logging
from typing import Dict
from collections import OrderedDict

# In python __all__ is a list of public objects of that module, as interpreted by import *.
# It overrides the default of hiding everything that begins with an underscore.

__all__ = ['E_ADCS_MESSAGE_TYPE', 'E_ADCS_MESSAGE_STATUS', 'dctAdcsBaseTypesToStructPackUnpackSyntaxLookup',
           'clsAdcsBaseType', 'clsAdcsEnumType', 'clsAdcsEnumArrayType', 'clsAdcsStructType', 'clsAdcsStructArrayType',
           'clsAdcsHeaderStructType', 'clsAdcsMessageStructType', 'clsAdcsMessageType',
           'vAddClass', 'vAddEnum', 'vAddMessage']

G_bLoggingEnabled = bool(True)
G_dctStoreForAllClasses = OrderedDict()  # Dictionary to store classes
G_dctStoreForAllEnums = OrderedDict()  # Dictionary to store enums
G_dctStoreForAllMessages = OrderedDict()  # Dictionary to store messages


class E_ADCS_MESSAGE_TYPE(Enum):
    """ Enum class to enumerate the message types

    """
    MESSAGE_TYPE_CMD = 0x00
    MESSAGE_TYPE_CMD_RSP = 0x01
    MESSAGE_TYPE_REQ = 0x02
    MESSAGE_TYPE_REQ_RSP = 0x03
    MESSAGE_TYPE_UNSOL = 0x04


class E_ADCS_MESSAGE_STATUS(Enum):
    """ Enum class to enumerate the message status

    """

    ADCS_MESSAGE_STATUS_NORMAL = 0x00  # /* everything OK */
    ADCS_MESSAGE_STATUS_INVALID_FIELD = 0x01  # /* A payload field has an invalid value  */
    ADCS_MESSAGE_STATUS_FIELD_MISSING = 0x02  # /* A payload length is shorter than expected */
    ADCS_MESSAGE_STATUS_MODE_ERROR = 0x03  # /* Cannot process this msg in this mode */
    ADCS_MESSAGE_STATUS_HARDWARE_ERROR = 0x04  # /* Operation cannot be done due to hardware failure or missing */
    ADCS_MESSAGE_STATUS_UNDEF_MSG_ID = 0x05  # /* Unrecognised msg id */
    ADCS_MESSAGE_STATUS_UNDEF_SUB_DEST = 0x06  # /* Unrecognised sub-destination or module address */
    ADCS_MESSAGE_STATUS_NOT_READY = 0x07  # /* Hardware not ready to perform operation e.g. warming up */
    ADCS_MESSAGE_STATUS_TIMEOUT = 0x08  # /* No reply from sub-unit within waiting time */
    ADCS_MESSAGE_STATUS_SOFTWARE_ERROR = 0x09  # /* Internal software error detected e.g. malloc fail */
    ADCS_MESSAGE_STATUS_INVALID_MSG_TYPE = 0x0A  # /* Unrecognised or invalid msg type */
    ADCS_MESSAGE_STATUS_IN_PROGRESS = 0x0B  # /* Only one msg of this msg id can be processed at a time */
    ADCS_MESSAGE_STATUS_INVALID_MSG_FIELD = 0x0C  # /* Overall length of msg (including all headers) is invalid */


# Sizes of default types
dctAdcsBaseTypeToSizeLookup = {
    'F4': 4,  # typedef float    F4;
    'F8': 8,  # typedef double   F8;

    'U1': 1,  # typedef uint8_t  U1;
    'U2': 2,  # typedef uint16_t U2;
    'U4': 4,  # typedef uint32_t U4;
    'U8': 8,  # typedef uint64_t U8;

    'I1': 1,  # typedef int8_t   I1;
    'I2': 2,  # typedef int16_t  I2;
    'I4': 4,  # typedef int32_t  I4;
    'I8': 8,  # typedef int64_t  I8;

    'CH': 1,  # typedef char     CH;
}


# Notice formating here takes a %d count qualifier
dctAdcsBaseTypesToStructPackUnpackSyntaxLookup = {
    'F4': '<%df',  # typedef float    F4;
    'F8': '<%dd',  # typedef double   F8;

    'U1': '%dB',  # typedef uint8_t  U1;
    'U2': '<%dH',  # typedef uint16_t U2;
    'U4': '<%dL',  # typedef uint32_t U4;
    'U8': '<%dQ',  # typedef uint64_t U8;

    'I1': '%db',  # typedef int8_t   I1;
    'I2': '<%dh',  # typedef int16_t  I2;
    'I4': '<%dl',  # typedef int32_t  I4;
    'I8': '<%dq',  # typedef int64_t  I8;

    'CH': '%dB',  # typedef char     CH;
}


def _convertValueToCorrectBaseType(acTypePar: str, value):
    """This is a public function

    Args:
        acTypePar (str): The type as a string
        value (float/int/str):

    Returns:
        (float/int/str): The return value. Tuple with a type name and type count

    Raises:
        Raises no exception.
    """
    acType = str("")
    acReturn = str("")

    iColonIndex = acTypePar.find(':')
    if (iColonIndex != -1):
        acType = acTypePar[0:iColonIndex]
    else:
        acType = acTypePar

    if acType in dctAdcsBaseTypesToStructPackUnpackSyntaxLookup.keys():
        if acType[0:1] == 'F':
            return(float(value))
        if acType[0:1] in ['I', 'U']:
            return(int(value))
        if acType[0:1] in ['C', 'S']:
            acReturn = str(value)
            if acReturn == '0':
                acReturn = ''
            return(acReturn)
    else:
        if (G_bLoggingEnabled is True):
            logging.error("Could not find type %s in the base type list", acType)
        return(value)


def _typeToFormat(acType: str):
    """This is a private which converts a type to a format

    Args:
        acType (str): A string describing the type which will be converted

    Returns:
        (acTypeName, iTypeCount): The return value. Tuple with a type name and type count

    Raises:
        Raises no exception.
    """
    iTypeCount = int(0)
    iColonIndex = int(-1)
    iTypeCountStrIndex = int(0)
    acTypeName = str("")

    # Make sure the input parameter is not None
    if (acType is None):
        return(None, 0)

    # The find function will return -1 if the character was not found
    iColonIndex = acType.find(':')  # Check if a type count was given
    if (iColonIndex != -1):
        iTypeCountStrIndex = iColonIndex + 1    # The count follows directly after the type like 'ST:10'
        iTypeCount = int(acType[iTypeCountStrIndex:])   # Convert the count string to an int
        acTypeName = acType[0:iColonIndex]  # Now get the type name as a string
    else:
        # A type string without a colon means the iTypeCount must be 1 like a U1 etc
        iTypeCount = 1
        acTypeName = acType
    if acTypeName in dctAdcsBaseTypesToStructPackUnpackSyntaxLookup.keys():
        return((dctAdcsBaseTypesToStructPackUnpackSyntaxLookup[acTypeName] % (iTypeCount,)), iTypeCount)
    else:
        return(None, 1)


def _tplTypeToSizeAndCount(acTypePar):
    """Global function which converts a type string into a size and count.

    Args:
        acTypePar (str): The first parameter. The type string. An example is "U4:16".

    Returns:
        (tuple): (int, int) -> (base type size, iCount)

    Raises:
        Raises no exceptions

    """
    iColonIndex = int(-1)
    iColonIndex = acTypePar.find(':')
    iCountStartIndex = int(0)
    acType = str("")
    iCount = int(0)

    if (iColonIndex != -1):
        iCountStartIndex = iColonIndex + 1
        iCount = int(acTypePar[iCountStartIndex:])
        acType = acTypePar[0:iColonIndex]
    else:
        iCount = 1
        acType = acTypePar

    if acType in dctAdcsBaseTypeToSizeLookup.keys():
        return((dctAdcsBaseTypeToSizeLookup[acType] * iCount), iCount)
    else:
        if (G_bLoggingEnabled):
            logging.error("Base type %s is invalid", acType)
        return((None, 1))

    return((None, 1))


def vAddClass(acClassNamePar: str, typeClassTypePar):
    """Global function to add class to a dictionary of classes.

    Args:
        acClassNamePar (str): The first parameter. The name of the class.
        typeClassTypePar (type): The second parameter. The type of class.

    Returns:

    Raises:
        Raises no exceptions

    """
    G_dctStoreForAllClasses[acClassNamePar] = typeClassTypePar
    return


def vAddEnum(acEnumNamePar: str, typeClassTypePar):
    """Global function to add enum class to a dictionary of enums classes.

    Args:
        acEnumNamePar (str): The first parameter. The name of the enum class.
        typeClassTypePar (type): The second parameter. The type of enum class.

    Returns:

    Raises:
        Raises no exceptions

    """
    G_dctStoreForAllEnums[acEnumNamePar] = typeClassTypePar
    return


def vAddMessage(typedefName, typeClassTypePar):
    """Global function to add message class to a dictionary of message classes.

    Args:
        typedefName (str): The first parameter. The name of the message class.
        typeClassTypePar (type): The second parameter. The type of message class.

    Returns:

    Raises:
        Raises no exceptions

    """
    G_dctStoreForAllMessages[typedefName] = typeClassTypePar
    return


def tplFindClassBasedOnName(className):
    """Global function which go through the the classes and enum dictionaries.

    The function will return the type and the count.

    This function is called in the constructor of the clsAdcsStructArrayType and clsAdcsEnumArrayType classes

    Args:
        className (str): The first parameter. The name of the class.

    Returns:
        (tuple): (type, count)

    Raises:
        Raises no exceptions

    """
    iColonIndex = className.find(':')
    iCountStartIndex = int(0)
    iCount = int(0)
    acClassName = str("")

    # Seperate the type from the count
    if (iColonIndex != -1):
        iCountStartIndex = iColonIndex + 1
        iCount = int(className[iCountStartIndex:])
        acClassName = className[0:iColonIndex]
    else:
        iCount = 1
        acClassName = className

    # At this stage we have acClassName which can be used as a key to deference the dictionary
    if acClassName in G_dctStoreForAllClasses.keys():
        return (G_dctStoreForAllClasses[acClassName], iCount)
    elif acClassName in G_dctStoreForAllEnums.keys():
        return (G_dctStoreForAllEnums[acClassName], iCount)
    else:
        if (G_bLoggingEnabled is True):
            logging.error("Could not find %s", str(acClassName))
        return (None, None)


class clsAdcsBaseType:
    """ This is a class which represents a base type field.

    In this base type the value can be a singular value or an array of values. It will
    be an array of values if the Count field in the XML is greater than 1. If the type
    is "CH" then the value stored will a str.

    Args:
        acTypeFormatPar (str): The first parameter. The type of base type we are trying to make.
        defaultValue (int/float/str): The second parameter. The default value of this base type.

    """

    def __init__(self, acTypeFormatPar: str, defaultValue=0):
        self._typeFormat = acTypeFormatPar
        iBaseTypeSizeBytes, iBaseTypeCount = _tplTypeToSizeAndCount(self._typeFormat)
        self._iBaseTypeCount = iBaseTypeCount
        self._iSizeBytes = iBaseTypeSizeBytes
        self._default = _convertValueToCorrectBaseType(self._typeFormat, defaultValue)
        self._Min = None  # This can be an int or a float
        self._Max = None  # This can be an int or a float
        if iBaseTypeCount > 1:
            if self._typeFormat[0:2] == 'CH':
                if (isinstance(self._default, str) is True):
                    self._Value = self._default
                else:
                    self._Value = ""
            else:
                # Previously  the code was self._Value = list()
                # That was a bug because then the list is empty of values
                if (isinstance(self._default, (int, float)) is True):
                    self._Value = [self._default] * iBaseTypeCount
                else:
                    self._Value = [None] * iBaseTypeCount
        else:
            self._Value = self._default

        return

    def vSetMin(self, value):
        """ This method sets the min value for the base type.

        Args:
            value (int/float): The first parameter. The min value.

        Returns:

        Raises:
            Raises no exceptions
        """

        self._Min = value
        return

    def vSetMax(self, value):
        """ This method sets the max value for the base type.

        Args:
            value (int/float): The first parameter. The max value.

        Returns:

        Raises:
            Raises no exceptions
        """
        self._Max = value
        return

    def iCalcSize(self):
        """ This method calculates the size of a base type.

        Args:

        Returns:
            (int): The size of the base type in bytes.

        Raises:
            Raises no exceptions
        """
        return(self._iSizeBytes)

    def iSizeBytes(self):
        """ This method returns the size of the base type.

        Args:

        Returns:
            (int): The size of the base type in bytes.

        Raises:
            Raises no exceptions
        """
        return self._iSizeBytes

    @property
    def Value(self):
        """ This method returns the value.

        Args:

        Returns:
            (): The value.

        Raises:
            Raises no exceptions
        """
        return self._Value

    @Value.setter
    def Value(self, value):  # lint:ok
        """ This method sets the value.

        Args:
            value (): The first parameter. The value to set.

        Returns:
            (): The value.

        Raises:
            Raises no exceptions
        """
        self._Value = value
        return

    def vDeserialise(self, btaBufferStream: bytes):
        """ This method deserialize a bytes into the base type value

        Args:
            btaBufferStream (bytes): The first parameters. A bytes containing the data which needs to be deserialized.

        Returns:

        Raises:
            Raises no exception.
        """
        acUnpackFormat = str("")

        acUnpackFormat, iBaseTypeCount = _typeToFormat(self._typeFormat)
        btaBaseTypeBuffer = btaBufferStream[0:self._iSizeBytes]
        val = struct.unpack_from(acUnpackFormat, btaBaseTypeBuffer)

        if iBaseTypeCount > 1:
            if self._typeFormat[0:2] == 'CH':
                val = (''.join(chr(e) for e in val)).strip(chr(0))
            else:
                # We have to convert the tuple to a list so that the Value is mutable
                if (isinstance(val, tuple) is True):
                    val = list(val)
                else:
                    val = val
        else:
            val = val[0]

        self._Value = val
        return

    def btaSerialise(self):
        """ This method serializes the value of the base type to a bytes.

        Args:

        Returns:
            (bytes): A bytes is returned.

        Raises:
            Raises no exceptions
        """
        lstBaseTypeValues = list()
        btaBaseTypeSerialiseBuffer = bytearray()
        acUnpackFormat = str("")

        acUnpackFormat, iBaseTypeCount = _typeToFormat(self._typeFormat)
        if iBaseTypeCount > 1:
            if self._typeFormat[0:2] == 'CH':
                lstBaseTypeValues = list(str.encode(self._Value, "utf-8"))  # String to list
            else:
                lstBaseTypeValues = self._Value
            while len(lstBaseTypeValues) < iBaseTypeCount:
                if self._typeFormat[0:2] == 'CH':
                    lstBaseTypeValues.append(0)
                else:
                    lstBaseTypeValues.append(self._default)
            btaBaseTypeSerialiseBuffer = struct.pack(acUnpackFormat, *lstBaseTypeValues[0: iBaseTypeCount])
        else:
            btaBaseTypeSerialiseBuffer = struct.pack(acUnpackFormat, self._Value)

        return(btaBaseTypeSerialiseBuffer)

    def dctToDict(self) -> Dict:
        """This is a public method which creates a nested (recursive) dictionary. This method must alwauys return None
        because it's a tree leaf.

        Args:

        Returns:
            (dict): A dictionary containing the attributes of the derived class

        Raises:
            Raises no exception.
        """
        return(None)

    def bValidate(self):
        """This is a public method which validates the value

        This is a public method which validates the value

        Args:

        Returns:
            bool: The return value. If the validation passed.

        Raises:
            Raises no exception.
        """
        bReturnValue = bool(False)  # Make it False for now

        # If the _Value of this clsAdcsBaseType is a list then don't do validation checking
        # The reason is because a clsAdcsBaseType of count > 1 might have a _Min and _Max then
        # the code below will throw an exception
        if (isinstance(self._Value, list) is True):
            bReturnValue = True
            return(bReturnValue)

        if ((self._Min is not None) and (self._Max is not None)):
            bReturnValue = (self._Value >= self._Min) and (self._Value <= self._Max)
        elif (self._Min is not None):
            bReturnValue = self._Value >= self._Min
        elif (self._Max is not None):
            bReturnValue = self._Value <= self._Max
        else:
            # There isn't a min or max defined in the XML
            bReturnValue = True

        if (bReturnValue is False):
            if (G_bLoggingEnabled):
                logging.error("clsAdcsBaseType() field validation failed - value %s - min %s - max %s", self._Value, self._Min, self._Max)

        return(bReturnValue)


class clsAdcsEnumType:
    """ This is a class which represents an enum type.

    Note that an array of enums is not represented here. For that we use the CCS_Enum_Array.

    Args:
        typeFormat (str): The first parameter. The type of enum we are trying to make.
        defaultValue (): The second parameter. The default value of this enum.

    """

    def __init__(self, typeFormat=None, defaultValue=0):
        if typeFormat is None:
            if (G_bLoggingEnabled is True):
                logging.error("typeFormat cannot be None")
            self._typeFormat = 'U1'
        else:
            self._typeFormat = typeFormat

        iEnumSizeBytes, iEnumCount = _tplTypeToSizeAndCount(self._typeFormat)

        self._iEnumTypeCount = iEnumCount
        self._iSizeBytes = iEnumSizeBytes
        if (isinstance(defaultValue, str) is True):
            self._default = int(defaultValue, 10)
        else:
            self._default = defaultValue

        self._Value = self._default

        return

    @property
    def Value(self):
        """ This method returns the value.

        Args:

        Returns:
            (): The value.

        Raises:
            Raises no exceptions
        """
        return(self._Value)

    @Value.setter
    def Value(self, value):  # lint:ok
        """ This method sets the value.

        Args:
            value (): The first parameter. The value to set.

        Returns:

        Raises:
            Raises no exceptions
        """
        self._Value = value
        return

    def iCalcSize(self):
        """ This method calculates the size of the enum.

        Args:

        Returns:
            (int): The size of the enum in bytes.

        Raises:
            Raises no exceptions
        """
        # This _iSizeBytes attribute was set in the constructor.
        return(self._iSizeBytes)

    def iSizeBytes(self):
        """ This method returns the size of the enum.

        Args:

        Returns:
            (int): The size of the enum in bytes.

        Raises:
            Raises no exceptions
        """
        # This _iSizeBytes attribute was set in the constructor.
        return(self._iSizeBytes)

    def vDeserialise(self, btaBytesDataPar):
        """ This method deserialize a bytes into an enum value

        Args:
            btaBytesDataPar (bytes): The first parameters. A bytes containing the data which needs to be deserialized.

        Returns:

        Raises:
            Raises no exception.
        """
        acUnpackFormat = str("")

        acUnpackFormat, iEnumCount = _typeToFormat(self._typeFormat)
        btaEnumTypeBuffer = btaBytesDataPar[0:self._iSizeBytes]

        if iEnumCount > 1:
            val = struct.unpack_from(acUnpackFormat, btaEnumTypeBuffer)
            self._Value = val
        else:
            val = struct.unpack_from(acUnpackFormat, btaEnumTypeBuffer)
            self._Value = val[0]

        return

    def btaSerialise(self):
        """ This method serializes the value of the enum to a bytes.

        Args:

        Returns:
            (bytes): A bytes is returned.

        Raises:
            Raises no exceptions
        """
        btaEnumTypeSerialiseBuffer = bytearray()
        acUnpackFormat = str("")

        acUnpackFormat, iEnumCount = _typeToFormat(self._typeFormat)
        if iEnumCount > 1:
            value = (self._Value)
            while len(value) < iEnumCount:
                value.append(self._default)
            btaEnumTypeSerialiseBuffer = struct.pack(acUnpackFormat, value[0:iEnumCount])
        else:
            btaEnumTypeSerialiseBuffer = struct.pack(acUnpackFormat, self._Value)

        return(btaEnumTypeSerialiseBuffer)

    def dctToDict(self) -> Dict:
        """This is a public method which creates a nested (recursive) dictionary. This method must alwauys return None
        because it's a tree leaf.

        Args:

        Returns:
            (dict): A dictionary containing the attributes of the derived class

        Raises:
            Raises no exception.
        """

        return(None)

    def __iter__(self):
        """ This method overrides the default iterator

        Args:

        Returns:
            (iterator): An iterator for this class.

        Raises:
            Raises no exception.
        """

        lstReturn = []

        for acKey in iter(self.keys()):
            lstReturn.append((acKey, self[acKey]),)

        return(iter(lstReturn))

    def __len__(self):
        """ This method overrides the default len method

        Args:

        Returns:
            (int): The length of the class.

        Raises:
            Raises no exception.
        """
        MyClass = self.__class__
        lstMembers = [attr for attr in dir(MyClass) if not callable(getattr(MyClass, attr)) and not attr.startswith("_") and not attr.startswith("Value")]
        return(len(lstMembers))

    def __getitem__(self, acKeyPar: str):
        """ This method overrides the default getitem method

        Args:
            acKeyPar (str): The first parameter. The key of item we want to get.

        Returns:
            (object): The item we requested.

        Raises:
            Raises no exception.
        """
        MyClass = self.__class__
        return(getattr(MyClass, acKeyPar))

    def keys(self):
        """ This gets the keys of the class.

        Args:

        Returns:
            (list): The keys in a list.

        Raises:
            Raises no exception.
        """
        MyClass = self.__class__
        lstMembers = [attr for attr in dir(MyClass) if not callable(getattr(MyClass, attr)) and not attr.startswith("_") and not attr.startswith("Value")]
        return(lstMembers)

    def lstEnumValues(self):
        """ This method gets the values

        Args:

        Returns:
            (list): A list of values.

        Raises:
            Raises no exception.
        """
        return([self.__getitem__(attr) for attr in self.keys()])

    def items(self):
        """ This method gets the items

        Args:

        Returns:
            (list): A list of items.

        Raises:
            Raises no exception.
        """
        return([(attr, self.__getitem__(attr)) for attr in self.keys()])

    def bValidate(self) -> bool:
        """ This method is used to validate a clsAdcsEnumType object.

        Args:

        Returns:
            bool: The return value. If the validation passed.

        Raises:
            Raises no exception.
        """
        bReturnValue = bool(False)
        lstValues = self.lstEnumValues()

        if (lstValues is None):
            if (G_bLoggingEnabled):
                logging.error("lstValues cannot be None")
            return(False)

        # When calling this method it is possible to be have callen it from a base class only or from a derived class. When there is no derived class
        # then there will be no enum values to do the validation with which means it will always fail. We therefore say if there are no values to compare
        # with then return the validation as True
        if (len(lstValues) <= 0):
            bReturnValue = True
        else:
            bReturnValue = (self._Value in lstValues)

        if (bReturnValue is False):
            if (G_bLoggingEnabled):
                if (not lstValues):
                    logging.error("clsAdcsEnumType() validation failed for class %s - current value %s", self.__class__.__name__, str(self._Value))
                else:
                    logging.error("clsAdcsEnumType() validation failed for class %s - current value %s - enum values %s", self.__class__.__name__, str(self._Value), str(lstValues))

        return(bReturnValue)


class clsAdcsEnumArrayType:
    """ This is a class which represents an enum array type.

    Args:
        typeFormat (str): The first parameter. The type of enum we are trying to make.
        defaultValue (): The second parameter. The default value of this enum.

    """

    def __init__(self, typeFormat=None, defaultValue=0):
        super(clsAdcsEnumArrayType, self).__init__()
        self._typeFormat = typeFormat
        typeClass, iEnumArrayCount = tplFindClassBasedOnName(self._typeFormat)
        self._typeBaseClass = typeClass  # This typeClass is a type which means we can make an instance of it
        self._iEnumArrayCount = iEnumArrayCount  # This is the number of enums in the array
        self._iSizeBytes = 0
        self._Value = [None] * self._iEnumArrayCount  # Make a list with the correct count but all Nones

        for iIndex, _ in enumerate(self._Value):
            self._Value[iIndex] = self._typeBaseClass(defaultValue)

        return

    def iGetCount(self) -> int:
        """ This is a public method which returns the number of items in the list

        Args:

        Returns:
            (int): The number of items in the list

        Raises:
            Raises no exceptions
        """
        return(self._iEnumArrayCount)

    @property
    def Value(self):
        """ This method returns the value.

        Args:

        Returns:
            (): The value.

        Raises:
            Raises no exceptions
        """
        return(self._Value)

    @Value.setter
    def Value(self, value):  # lint:ok
        """ This method sets the value.

        Args:
            value (list): The first parameter. The value to set. A list of clsAdcsEnumType()

        Returns:

        Raises:
            Raises no exceptions
        """
        self._Value = value
        return

    def iCalcSize(self):
        """ This method calculates the size of the enum array and returns the value

        Args:

        Returns:
            (int): The size of the enum array in bytes.

        Raises:
            Raises no exceptions
        """
        # If the size has not been calculated yet then do it
        if self._iSizeBytes == 0:
            obj = self._typeBaseClass()  # This _typeBaseClass is a type with which we can make an instance of
            self._iSizeBytes = obj.iSizeBytes() * self._iEnumArrayCount  # Calculate the size as the size of the base class times the number in the array

        return(self._iSizeBytes)

    def iSizeBytes(self):
        """ This method returns the size of the enum array.

        Args:

        Returns:
            (int): The size of the enum array in bytes.

        Raises:
            Raises no exceptions
        """
        # The method which will be called will take the size of the base class and multiply it
        # with the size of the base class
        return(self.iCalcSize())

    def vDeserialise(self, btaBytesDataPar):
        """ This method deserialize a bytes into an enum array

        Args:
            btaBytesDataPar (bytes): The first parameters. A bytes containing the data which needs to be deserialized.

        Returns:

        Raises:
            Raises no exception.
        """
        iEnumArrayBufferIndexBytes = 0  # This variable counts in bytes
        objEnumArrayBaseClass = self._typeBaseClass()  # Make an instance of the base class
        iEnumArrayBaseClassSizeBytes = int(0)  # The size of the base class
        btaEnumArrayTypeBuffer = bytearray()

        # Verify that we have enough data in the byte stream to dereference without an exception
        if (len(btaBytesDataPar) < (objEnumArrayBaseClass.iSizeBytes() * self._iEnumArrayCount)):

            if (G_bLoggingEnabled):
                logging.error("Byte stream is not long enough to deserialize the enum array")

            return

        self._Value.clear()  # This self._Value is a list. First clear it before deserializing

        # This self._iEnumArrayCount stores the number of enums in the array
        for _ in range(self._iEnumArrayCount):
            objEnumArrayBaseClass = self._typeBaseClass()  # Make an instance of the base class
            iEnumArrayBaseClassSizeBytes = objEnumArrayBaseClass.iSizeBytes()  # Get the size in bytes of the base class

            # For every iteration in the loop take a little bit of binary data the size of the base class
            btaEnumArrayTypeBuffer = btaBytesDataPar[iEnumArrayBufferIndexBytes: iEnumArrayBufferIndexBytes + iEnumArrayBaseClassSizeBytes]

            if len(btaEnumArrayTypeBuffer) != iEnumArrayBaseClassSizeBytes:

                if (G_bLoggingEnabled):
                    logging.error("length of btaEnumArrayTypeBuffer is different to iEnumArrayBaseClassSizeBytes")

                break

            objEnumArrayBaseClass.vDeserialise(btaEnumArrayTypeBuffer)
            self._Value.append(objEnumArrayBaseClass)  # Add the newly created clsAdcsEnumType() to the value array
            iEnumArrayBufferIndexBytes += iEnumArrayBaseClassSizeBytes

        return

    def btaSerialise(self):
        """ This method serializes the value of the enum array to a bytes.

        Args:

        Returns:
            (bytes): A bytes is returned.

        Raises:
            Raises no exceptions
        """
        btaEnumArrayReturnBuffer = bytearray()
        btaEnumSerialiseBuffer = bytearray()

        value = (self._Value)  # Keep a local reference of the value array

        while len(value) < self._iEnumArrayCount:
            value.append(self._typeBaseClass())

        for iEnumArrayIndex in range(self._iEnumArrayCount):
            btaEnumSerialiseBuffer = value[iEnumArrayIndex].btaSerialise()
            btaEnumArrayReturnBuffer = btaEnumArrayReturnBuffer + btaEnumSerialiseBuffer

        return(btaEnumArrayReturnBuffer)

    def dctToDict(self) -> Dict:
        """This is a public method which creates a nested (recursive) dictionary based on the attributes of the derived class.

        Args:

        Returns:
            (dict): A dictionary containing the attributes of the derived class

        Raises:
            Raises no exception.
        """

        dctReturn = OrderedDict()
        dctReturn["Attr"] = []    # The attributes from the EnumArray will also be stored in a list
        acSelfType = str(type(self)).split('\'')[1]
        objAdcsEnum = None

        lstValue = self._Value
        for iIndex, objAdcsEnum in enumerate(lstValue):
            dctReturn["Attr"] += [OrderedDict()]
            # Because we are iterating through a EnumArray every element will be an Enum, therefore add the Value as well
            dctReturn["Attr"][iIndex] = {"Name": acSelfType + str(iIndex), "Type": str(type(objAdcsEnum)).split('\'')[1], "Value": objAdcsEnum.Value}

        return(dctReturn)

    def bValidate(self) -> bool:
        """This is a public method which validates the enum array.

        Args:

        Returns:
            (bool): A flag to indicate if the validation passed.

        Raises:
            Raises no exception.
        """
        bReturnValue = bool(False)
        bReturnItem = bool(True)
        lstValue = (self._Value)

        if (lstValue is None):
            if (G_bLoggingEnabled):
                logging.error("lstValue cannot be None")
            return(bReturnValue)

        if (isinstance(lstValue, list) is False):
            if (G_bLoggingEnabled):
                logging.error("lstValue must be a list")
            return(bReturnValue)

        # Return True if the list is empty
        if (not lstValue):
            return(True)

        bReturnValue = bool(True)  # Set to True for bitwise and
        for _, objItem in enumerate(lstValue):
            bReturnItem = objItem.bValidate()
            if (bReturnItem is False):
                if (G_bLoggingEnabled):
                    logging.error("clsAdcsEnumArrayType() validation failed for %s ", self.__class__.__name__)

            bReturnValue &= bReturnItem

        return(bReturnValue)


class clsAdcsStructArrayType:
    """ This is a class which represents a struct array type.

    Args:
        typeFormat (str): The first parameter. The type of enum we are trying to make.

    """
    def __init__(self, typeFormat):
        self._typeFormat = typeFormat
        typeStructArrayType, iStructArrayCount = tplFindClassBasedOnName(self._typeFormat)
        self._typeBaseClass = typeStructArrayType
        self._iBaseStructSizeBytes = 0  # Will later be the size of one item
        self._iStructArrayTotalSizeBytes = int(0)  # Will later be the total size
        self._iStructArrayCount = iStructArrayCount  # How many items in the array/list
        self._Value = [None] * self._iStructArrayCount  # Make a list with the correct count but all Nones

        for iIndex, _ in enumerate(self._Value):
            self._Value[iIndex] = self._typeBaseClass()

    def typeGetBaseClassType(self):
        """ This is a public method which gets the type of the base class

        Args:

        Returns:
            (type): The type of the base class

        Raises:
            Raises no exception.
        """
        return(self._typeBaseClass)

    def iGetCount(self):
        """ This is a public method which gets the number of elements in the StructArray

        Args:

        Returns:
            (int): The number of elements in the array

        Raises:
            Raises no exception.
        """
        return(self._iStructArrayCount)

    def acGetTypeFormat(self):
        """ This is a public method which gets typeformat of the object as passed in during construction

        Args:

        Returns:
            (str): The typeformat as a string "[CLASS]:[NUM]"

        Raises:
            Raises no exception.
        """
        return(self._typeFormat)

    def iCalcSize(self):
        """ This is a public method which calculates the size

        Args:

        Returns:
            (int): The size in bytes

        Raises:
            Raises no exception.
        """

        # The total size only needs to be calculated once
        if (self._iStructArrayTotalSizeBytes == 0):
            objStructArrayBaseClass = self._typeBaseClass()
            self._iBaseStructSizeBytes = objStructArrayBaseClass.iSizeBytes()
            self._iStructArrayTotalSizeBytes = self._iBaseStructSizeBytes * self._iStructArrayCount

        return(self._iStructArrayTotalSizeBytes)

    def iSizeBytes(self):
        """ This method returns the size of the struct array.

        Args:

        Returns:
            (int): The size of the struct array in bytes.

        Raises:
            Raises no exceptions
        """
        return(self.iCalcSize())

    @property
    def Value(self):
        """ This method returns the value.

        Args:

        Returns:
            (): The value.

        Raises:
            Raises no exceptions
        """
        return(self._Value)

    @Value.setter
    def Value(self, value):  # lint:ok
        """ This method sets the value.

        Args:
            value (list): The first parameter. The value to set. A list of clsAdcsStructType()

        Returns:

        Raises:
            Raises no exceptions
        """
        if (value is None):
            if (G_bLoggingEnabled):
                logging.error("value is None")
            return

        if (isinstance(value, list) is False):
            if (G_bLoggingEnabled):
                logging.error("value is not a list")
            return

        if (len(value) != self._iStructArrayCount):
            if (G_bLoggingEnabled):
                logging.error("value should be a list of length %d and it is not", self._iStructArrayCount)
            return

        self._Value = value
        return

    def vDeserialise(self, btaBytesDataPar):
        """ This method deserialize a bytes into a struct array

        Args:
            btaBytesDataPar (bytes): The first parameters. A bytes containing the data which needs to be deserialized.

        Returns:

        Raises:
            Raises no exception.
        """
        iBufferIndex = 0  # This stores the index in bytes
        objTempBaseClass = self._typeBaseClass()
        iSizeOfBaseClassBytes = int(0)  # The size of the base class in bytes
        btaStructArrayBuffer = bytearray()

        # Check if the byte stream provided is long enough for the length of this struct array
        if (len(btaBytesDataPar) < (objTempBaseClass.iSizeBytes() * self._iStructArrayCount)):

            if (G_bLoggingEnabled):
                logging.error("Buffer not long enough to deserialize")

            return

        self._Value.clear()  # First clear the list of value

        for _ in range(self._iStructArrayCount):
            objTempBaseClass = self._typeBaseClass()
            iSizeOfBaseClassBytes = objTempBaseClass.iSizeBytes()
            btaStructArrayBuffer = btaBytesDataPar[iBufferIndex: iBufferIndex + iSizeOfBaseClassBytes]
            objTempBaseClass.vDeserialise(btaStructArrayBuffer)
            self._Value.append(objTempBaseClass)
            iBufferIndex += iSizeOfBaseClassBytes

        return

    def btaSerialise(self):
        """ This method serializes the value of the struct array to a bytes.

        Args:

        Returns:
            (bytes): A bytes is returned.

        Raises:
            Raises no exceptions
        """
        btaStructArrayReturnBuffer = bytearray()
        lstValuesToSerialise = (self._Value)
        iValidStructArrayCount = min(self._iStructArrayCount, len(lstValuesToSerialise))
        iToSerialiseCount = self._iStructArrayCount - iValidStructArrayCount
        objStructArrayBaseClass = None
        iToSerialiseIndex = int(0)

        if iToSerialiseCount > 0:
            for iToSerialiseIndex in range(iToSerialiseCount):
                objStructArrayBaseClass = self._typeBaseClass()
                lstValuesToSerialise.append(objStructArrayBaseClass)

        for iToSerialiseIndex in range(self._iStructArrayCount):
            objStructArrayBaseClass = lstValuesToSerialise[iToSerialiseIndex]
            output = objStructArrayBaseClass.btaSerialise()
            btaStructArrayReturnBuffer.extend(output)

        return(btaStructArrayReturnBuffer)

    def dctToDict(self) -> Dict:
        """This is a public method which creates a nested (recursive) dictionary based on the attributes of the derived class.

        Args:

        Returns:
            (dict): A dictionary containing the attributes of the derived class

        Raises:
            Raises no exception.
        """

        dctReturn = OrderedDict()
        dctReturn["Attr"] = []  # The Value list items will also be stored in a list
        lstValues = self._Value
        acSelfType = str(type(self)).split('\'')[1]

        # Iterate through the list - all items will be a clsAdcsStructType()
        for iIndex, objCCSStruct in enumerate(lstValues):
            dctReturn["Attr"] += [OrderedDict()]
            # Each nested attribute must have a "Name", "Type" and "Attr"
            dctReturn["Attr"][iIndex] = {"Name": acSelfType + str(iIndex), "Type": str(type(objCCSStruct)).split('\'')[1], "Attr": None}
            dctReturn["Attr"][iIndex]["Attr"] = [objCCSStruct.dctToDict()]

        return(dctReturn)

    def bValidate(self):
        """This is a public method which validates the clsAdcsStructArrayType object.

        This is a public method which validates the clsAdcsStructArrayType object.

        Args:

        Returns:
            bool: The return value. If the validation passed.

        Raises:
            Raises no exception.
        """
        bValidationResult = bool(False)  # Start the result as true
        bValidationItem = bool(False)

        # First make a deep copy
        lstValToValidate = (self._Value)

        if (lstValToValidate is None):
            if (G_bLoggingEnabled):
                logging.error("lstValToValidate cannot be None")
            return(bValidationResult)

        # Then list of structs are empty
        if (not lstValToValidate):
            if (G_bLoggingEnabled):
                logging.error("List of structs cannot be empty")
            return(bValidationResult)

        # Make sure it is a List
        if (isinstance(lstValToValidate, list) is False):
            if (G_bLoggingEnabled):
                logging.error("lstValToValidate must be a list")
            return(bValidationResult)

        bValidationResult = bool(True)

        for iIndex, objItem in enumerate(lstValToValidate):
            if (isinstance(objItem, clsAdcsStructType) is True):
                bValidationItem = objItem.bValidate()

                if (bValidationItem is False):
                    if (G_bLoggingEnabled):
                        logging.error("clsAdcsStructArrayType() item validation failed for index %d", iIndex)

                bValidationResult &= bValidationItem

        return(bValidationResult)


class clsAdcsStructType:
    """ This is a class which represents a struct type.

    Args:
        typeFormat (str): The first parameter. The type.
        defaultValue (): The second parameter. The default value.

    """
    def __init__(self, typeFormat=None):
        self._typeFormat = typeFormat
        self._lstStructLoadOrder = list()
        self._iSizeBytes = 0

        return

    def iCalcSize(self):
        """ This private method calculates the size.

        Args:

        Returns:
            (int): The size in bytes.

        Raises:
            Raises no exceptions
        """
        objStructBaseClass = None
        iStructBaseClassSizeBytes = int(0)
        iAccumulatedSizeBytes = int(0)

        # Check if we calculated the size before
        if self._iSizeBytes == 0:
            iAccumulatedSizeBytes = 0

            # Make a list of all the members of this class
            lstMembers = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("_")]
            for acStructMemberName in lstMembers:
                objStructBaseClass = self.objGetItem(acStructMemberName)
                if not (objStructBaseClass is None):
                    iStructBaseClassSizeBytes = objStructBaseClass.iCalcSize()
                    iAccumulatedSizeBytes += iStructBaseClassSizeBytes
            self._iSizeBytes = iAccumulatedSizeBytes
        return(self._iSizeBytes)

    def iSizeBytes(self):
        """ This method returns the size

        Args:

        Returns:
            (int): The size in bytes.

        Raises:
            Raises no exceptions
        """
        return(self.iCalcSize())

    def objGetItem(self, acKeyPar):
        """ This method returns a member from the class

        Args:
            acKeyPar (str). The first parameter. The key of the member.

        Returns:
            (object): The return object.

        Raises:
            Raises no exceptions
        """

        if not acKeyPar.startswith("_"):
            obj = getattr(self, acKeyPar)
            return obj

        return(None)

    def vAddType(self, acRecordNamePar: str):
        """ This method adds the record name to a load order list.

        Args:
            acRecordNamePar (str). The first parameter. The name of the record.

        Returns:
            (object): The return object.

        Raises:
            Raises no exceptions
        """
        self._lstStructLoadOrder.append(acRecordNamePar)
        return

    def vDeserialise(self, btaBuffer: bytes):
        """This is a public method which takes a bytes stream and unpacks it into class

        Args:
            btaBuffer: A bytes type containing the data which needs to be unpacked

        Returns:
            iBufferIndex: The return value. If the last buffer index used.
            self: The self reference

        Raises:
            Raises no exception.
        """

        iBufferIndex = int(0)
        btaTempBuffer = bytes([])

        # Do some sanity checks - the buffer cannot be None
        if (btaBuffer is None):
            return

        # The bytes buffer must at least have some length
        if (len(btaBuffer) <= 0):
            return

        for acLoadName in self._lstStructLoadOrder:
            objLoadOrderItem = self.objGetItem(acLoadName)
            if not (objLoadOrderItem is None):
                iSizeBytes = objLoadOrderItem.iSizeBytes()
                if (iSizeBytes == 0):
                    continue

                # Take care to not go out of bounds
                if (iBufferIndex >= len(btaBuffer)):
                    break

                # Take care to not go out of bounds
                if (((iBufferIndex + iSizeBytes) > len(btaBuffer))):
                    break

                btaTempBuffer = btaBuffer[iBufferIndex: iBufferIndex + iSizeBytes]

                # We must at least have something in the temp buffer
                if (btaTempBuffer):
                    objLoadOrderItem.vDeserialise(btaTempBuffer)
                iBufferIndex += iSizeBytes

        return

    def btaSerialise(self):
        """ This method serializes the value of the struct to bytes.

        Args:

        Returns:
            (bytes): A bytes is returned.

        Raises:
            Raises no exceptions
        """
        btaStructReturnBuffer = bytearray()

        # Iterate through the loadorder list and get all the members
        for ldName in self._lstStructLoadOrder:
            objStructBaseClass = self.objGetItem(ldName)
            if not (objStructBaseClass is None):
                resout = objStructBaseClass.btaSerialise()
                btaStructReturnBuffer.extend(resout)

        return(btaStructReturnBuffer)

    def dctToDict(self) -> Dict:
        """This is a public method which creates a nested (recursive) dictionary based on the attributes of the derived class.

        Args:

        Returns:
            (dict): A dictionary containing the attributes of the derived class

        Raises:
            Raises no exception.
        """

        dctReturn = OrderedDict()
        dctReturn["Attr"] = []  # The attributes will be stored in a list

        # Get a list of all the attributes in the derived class
        lstAttributes = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("_")]
        # Iterate through the attributes
        for iIndex, acAttribute in enumerate(lstAttributes):
            dctReturn["Attr"] += [OrderedDict()]
            objAttribute = getattr(self, acAttribute)
            # Each nested attribute must have a "Name", "Type" and "Attr"
            dctReturn["Attr"][iIndex] = {"Name": acAttribute, "Type": str(type(objAttribute)).split('\'')[1], "Attr": None}
            dctReturn["Attr"][iIndex]["Attr"] = objAttribute.dctToDict()

            # If the attribute is a tree leaf then stop and get the value
            if (isinstance(objAttribute, (clsAdcsBaseType, clsAdcsEnumType)) is True):
                dctReturn["Attr"][iIndex]["Value"] = objAttribute.Value

        return(dctReturn)

    def bValidate(self):
        """This is a public method which validates the clsAdcsBaseType objects in the items list

        This is a public method which validates the clsAdcsBaseType objects in the items list

        Args:

        Returns:
            bool: The return value. If the validation passed.

        Raises:
            Raises no exception.
        """
        bValidationResult = bool(True)  # Start the result as true
        bValidationPetItem = bool(False)

        # Iterate through the loader list
        for acLoadName in self._lstStructLoadOrder:
            # Get the object based on a string
            objItemFromLoadOrder = self.objGetItem(acLoadName)
            if objItemFromLoadOrder is not None:
                bValidationPetItem = objItemFromLoadOrder.bValidate()
                if (bValidationPetItem is False):
                    if (G_bLoggingEnabled):
                        logging.error("clsAdcsStructType() field %s validation failed!!!", str(acLoadName))
                # Bitwise and the results
                bValidationResult = bValidationResult & bValidationPetItem

        if ((G_bLoggingEnabled is True) and (bValidationResult is False)):
            logging.error("Struct %s validation failed!!!", str(self))

        return(bValidationResult)


class clsAdcsHeaderStructType(clsAdcsStructType):
    """ This is a class which represents a header struct type.

    This class inherits clsAdcsStructType()

    Args:
        typeFormat (str): The first parameter. The type.

    """

    def __init__(self, formatType=None):
        super(clsAdcsHeaderStructType, self).__init__(formatType)


class clsAdcsMessageStructType(clsAdcsStructType):
    """ This is a class which represents a message struct type.

    This class inherits clsAdcsStructType()

    Args:
        typeFormat (str): The first parameter. The type.

    """

    def __init__(self, formatType=None):
        super(clsAdcsMessageStructType, self).__init__(formatType)


class clsAdcsMessageType():
    """ This is a class which represents a message.

    Args:
        typeFormat (str): The first parameter. The type.

    """

    def __init__(self):
        self._iSizeBytes = 0

        return

    def iCalcSize(self):
        """ This is method which calculates the size.

        Args:

        Returns:
            int: The return value. The size in bytes.

        Raises:
            Raises no exception.
        """
        iMessageSizeBytes = int(0)
        iAccumulatedSizeBytes = int(0)

        # Need to Get The Structures Here and then Calculate the sizes, and then set the header Length Field
        lstMembers = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("_")]

        # Check if we ever calculated the size
        if self._iSizeBytes == 0:
            iAccumulatedSizeBytes = 0
            for member in lstMembers:
                obj = self.objGetItem(member)
                iMessageSizeBytes = obj.iCalcSize()
                iAccumulatedSizeBytes += iMessageSizeBytes
            self._iSizeBytes = iAccumulatedSizeBytes

        return(self._iSizeBytes)

    def iSizeBytes(self):
        """ This is method returns the size.

        Args:

        Returns:
            int: The return value. The size in bytes.

        Raises:
            Raises no exception.
        """
        return(self.iCalcSize())

    def objGetItem(self, acKeyPar):
        """ This method returns a member from the message

        Args:
            acKeyPar (str). The first parameter. The key of the member.

        Returns:
            (object): The return object.

        Raises:
            Raises no exceptions
        """
        if not acKeyPar.startswith("_"):
            obj = getattr(self, acKeyPar)
            if not callable(obj):
                return(obj)

        return(None)

    def btaSerialise(self):
        """ This method serializes the message into a bytes.

        Args:

        Returns:
            (bytes): A bytes is returned.

        Raises:
            Raises no exceptions
        """
        btaMessageReturnBuffer = bytearray()  # Create a new byte array

        # Make a list of the all the members of this message
        lstMembers = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("_")]

        # Iterate through the members
        for member in lstMembers:
            val = getattr(self, member)
            btaMessageReturnBuffer.extend(val.btaSerialise())

        return(btaMessageReturnBuffer)

    def dctToDict(self) -> Dict:
        """This is a public method which creates a nested (recursive) dictionary based on the attributes of the derived class.

        Args:

        Returns:
            (dict): A dictionary containing the attributes of the derived class

        Raises:
            Raises no exception.
        """
        dctReturn = OrderedDict()
        dctReturn["Attr"] = []  # The attributes will be stored in a list

        # Get a list of all the attributes in the derived class
        lstAttributes = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("_")]
        # Iterate through the attributes
        for iIndex, acAttribute in enumerate(lstAttributes):
            dctReturn["Attr"] += [OrderedDict()]
            objAttribute = getattr(self, acAttribute)
            # Each nested attribute must have a "Name", "Type" and "Attr"
            dctReturn["Attr"][iIndex] = {"Name": acAttribute, "Type": str(type(objAttribute)).split('\'')[1], "Attr": None}
            dctReturn["Attr"][iIndex]["Attr"] = objAttribute.dctToDict()

        return(dctReturn)

    def vDeserialise(self, btaBufferStream: bytes):
        """This is a public method which takes a bytes stream and unpacks it into class

        Args:
            btaBufferStream: A bytes type containing the data which needs to be unpacked

        Returns:

        Raises:
            Raises no exception.
        """

        iBufferIndex = int(0)
        btaTempBuffer = bytes([])
        iSizeBytes = int(0)

        # Do some sanity checks - the buffer cannot be None
        if (btaBufferStream is None):
            return

        # The bytes buffer must at least have some length
        if (len(btaBufferStream) <= 0):
            return

        # Iterate through the members of the class - put them in a list
        lstMembers = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("_")]
        for acMember in lstMembers:
            objItem = getattr(self, acMember)
            if not (objItem is None):
                iSizeBytes = objItem.iSizeBytes()
                # We have nothing to do if the size is zero
                if (iSizeBytes == 0):
                    continue

                # Take care to not go out of bounds
                if (iBufferIndex >= len(btaBufferStream)):
                    break

                # Take care to not go out of bounds
                if (((iBufferIndex + iSizeBytes) > len(btaBufferStream))):
                    break

                btaTempBuffer = btaBufferStream[iBufferIndex: iBufferIndex + iSizeBytes]

                # We must at least have something in the temp buffer
                if (btaTempBuffer):
                    objItem.vDeserialise(btaTempBuffer)
                iBufferIndex += iSizeBytes

        return

    def bValidate(self):
        """This is a public method which validates the clsAdcsBaseType objects in the items list

        This is a public method which validates the clsAdcsBaseType objects in the items list

        Args:

        Returns:
            bool: The return value. If the validation passed.

        Raises:
            Raises no exception.
        """
        bValidationResult = bool(True)  # Start the result as true
        bValidationItem = bool(False)  # Start the result as false

        # Iterate through the loader list
        lstMembers = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("_")]
        for acMember in lstMembers:
            objMember = self.objGetItem(acMember)
            bValidationItem = objMember.bValidate()
            if (bValidationItem is False):
                if (G_bLoggingEnabled):
                    logging.error("clsAdcsMessageType() field %s validation failed!!!", str(acMember))
            bValidationResult = bValidationResult & bValidationItem

        if ((G_bLoggingEnabled is True) and (bValidationResult is False)):
            logging.error("Message %s validation failed!!!", str(self))

        return(bValidationResult)
