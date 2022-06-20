# //-----------------------------------------------------------------------------
# // $Id: CCS_Types.h,v 1.1 2010/09/28 13:00:38 tferet Exp $
# //-----------------------------------------------------------------------------
# // SUMMARY: External interface - Data Processor/CCS type definitions
# //
# //-----------------------------------------------------------------------------
# //************************* Enumerated type definitions ***************************************
from enum import Enum
import struct
import copy
import logging
from typing import Dict

__all__ = ['eCCSMSGTYPE', 'eCCSMSGSTATUS', 'dRRSBASETYPES',
           'CCS_Base', 'CCS_Enum', 'CCS_EnumArray', 'CCS_Struct', 'CCS_StructArray', 'CCS_Typedef',
           'CCS_HdrStruct', 'CCS_MsgStruct', 'CCS_Message',
           'CCS_Add_Class', 'CCS_Add_Enum', 'CCS_Add_Typedef', 'CCS_Add_Message']

G_bCcsTypesLoggingEnabled = bool(True)

def xrange(x):
    return iter(range(x))


class eCCSMSGTYPE(Enum):
    MtCmd = 0x00
    MtCmdRsp = 0x01
    MtReq = 0x02
    MtReqRsp = 0x03
    MtUnsol = 0x04


class eCCSMSGSTATUS(Enum):
    MsNormal = 0x00  # /* everything OK */
    MsInvalidField = 0x01  # /* A payload field has an invalid value  */
    MsFieldMissing = 0x02  # /* A payload length is shorter than expected */
    MsModeError = 0x03  # /* Cannot process this msg in this mode */
    MsHardwareError = 0x04  # /* Operation cannot be done due to hardware failure or missing */
    MsUndefMsgId = 0x05  # /* Unrecognised msg id */
    MsUndefSubDest = 0x06  # /* Unrecognised sub-destination or module address */
    MsNotReady = 0x07  # /* Hardware not ready to perform operation e.g. warming up */
    MsTimeout = 0x08  # /* No reply from sub-unit within waiting time */
    MsSoftwareError = 0x09  # /* Internal software error detected e.g. malloc fail */
    MsInvalidMsgType = 0x0A  # /* Unrecognised or invalid msg type */
    MsInProgress = 0x0B  # /* Only one msg of this msg id can be processed at a time */
    MsInvalidMsgLength = 0x0C  # /* Overall length of msg (including all headers) is invalid */


# Sizes of default types
dRRSBASETYPESIZES = {
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
    'ST': 1,  # typedef char     ST;
}


# Notice formating here takes a %d count qualifier
dRRSBASETYPES = {
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
    'ST': '%dB',  # typedef char     ST;
}


def _typeForseValue(ldType, value):
    cntBracket = ldType.find(':')
    if (cntBracket != -1):
        tpName = ldType[0:cntBracket]
    else:
        tpName = ldType
    if tpName in dRRSBASETYPES.keys():
        if tpName[0:1] == 'F':
            return float(value)
        if tpName[0:1] in ['I', 'U']:
            return int(value)
        if tpName[0:1] in ['C', 'S']:
            ret = str(value)
            if ret == '0':
                ret = ''
            return ret
    else:
        return value


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
        return None, 0
    
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
    if acTypeName in dRRSBASETYPES.keys():
        return (dRRSBASETYPES[acTypeName] % (iTypeCount,)), iTypeCount
    else:
        return None, 1


def _typeToSize(ldType):
    cntBracket = ldType.find(':')
    if (cntBracket != -1):
        beg = cntBracket + 1
        count = int(ldType[beg:])
        tpName = ldType[0:cntBracket]
    else:
        count = 1
        tpName = ldType
    if tpName in dRRSBASETYPESIZES.keys():
        return (dRRSBASETYPESIZES[tpName] * count), count
    else:
        return None, 1


_CCS_Classes = dict()
_CCS_Enums = dict()
_CCS_Typedef = dict()
_CCS_Messages = dict()


def CCS_Add_Class(className, class_type):
    _CCS_Classes[className] = class_type


def CCS_Add_Enum(enumName, class_type):
    _CCS_Enums[enumName] = class_type


def CCS_Add_Typedef(typedefName, class_type):
    _CCS_Typedef[typedefName] = class_type


def CCS_Add_Message(typedefName, class_type):
    _CCS_Messages[typedefName] = class_type


# Not Sure what to do with enums yet
def CCS_Find_Class(className):
    cntBracket = className.find(':')
    if (cntBracket != -1):
        beg = cntBracket + 1
        count = int(className[beg:])
        tpName = className[0:cntBracket]
    else:
        count = 1
        tpName = className
    if tpName in _CCS_Classes.keys():
        return (_CCS_Classes[tpName], count)
    elif tpName in _CCS_Typedef.keys():
        return (_CCS_Typedef[tpName], count)
    elif tpName in _CCS_Enums.keys():
        return (_CCS_Enums[tpName], count)
    else:
        return (None, None)


class CCS_Base:
    def __init__(self, typeFormat, defaultValue=0):
        self._typeFormat = typeFormat
        sz, count = _typeToSize(self._typeFormat)
        self._count = count
        self._size = sz
        self._default = _typeForseValue(self._typeFormat, defaultValue)
        self._Min = None
        self._Max = None
        if count > 1:
            if self._typeFormat[0:2] == 'ST' or self._typeFormat[0:2] == 'CH':
                if (isinstance(self._default, str) is True):
                    self._Value = self._default
                else:
                    self._Value = ""
            else:
                self._Value = list()
        else:
            self._Value = self._default

    def SetMin(self, value):
        self._Min = value

    def SetMax(self, value):
        self._Max = value

    def _calc_size(self):
        return self._size

    def size(self):
        return self._size

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, value):  # lint:ok
        self._Value = value

    def LoadFromStream(self, btaBufferStream: bytes):
        """This is a public method which takes a bytes stream and unpacks it into class

        Args:
            btaBufferStream: A bytes type containing the data which needs to be unpacked

        Returns:
            iBufferIndex: The return value. If the last buffer index used.
            self: The self reference 

        Raises:
            Raises no exception.
        """

        UnpackFormat, count = _typeToFormat(self._typeFormat)
        tmpbuffer = btaBufferStream[0:self._size]
        val = struct.unpack_from(UnpackFormat, tmpbuffer)
        if count > 1:
            if self._typeFormat[0:2] == 'ST' or self._typeFormat[0:2] == 'CH':
                val = (''.join(chr(e) for e in val)).strip(chr(0))
            else:
                val = val
        else:
            val = val[0]
        self._Value = val
        return self._size, self

    def StoreToStream(self):
        UnpackFormat, count = _typeToFormat(self._typeFormat)
        if count > 1:
            if self._typeFormat[0:2] == 'ST' or self._typeFormat[0:2] == 'CH':
                storearray = list(str.encode(self._Value, "utf-8"))  # String to list
            else:
                storearray = self._Value
            while len(storearray) < count:
                if self._typeFormat[0:2] == 'ST' or self._typeFormat[0:2] == 'CH':
                    storearray.append(0)
                else:
                    storearray.append(self._default)
            outval = struct.pack(UnpackFormat, *storearray[0: count])
        else:
            outval = struct.pack(UnpackFormat, self._Value)
        return outval

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
            if (G_bCcsTypesLoggingEnabled):
                logging.error("CCS_Base() field validation failed - value %s - min %s - max %s", self._Value, self._Min, self._Max)

        return(bReturnValue)


class CCS_Enum:
    def __init__(self, typeFormat=None, defaultValue=0):
        if typeFormat is None:
            self._typeFormat = 'U1'
        else:
            self._typeFormat = typeFormat
        sz, count = _typeToSize(self._typeFormat)
        self._count = count
        self._size = sz
        if isinstance(defaultValue, str):
            self._default = int(defaultValue, 10)
        else:
            self._default = defaultValue
        if count > 1:
            self._Value = list()
        else:
            self._Value = self._default
        pass

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, value):  # lint:ok
        self._Value = value

    def _calc_size(self):
        return self._size

    def size(self):
        return self._size

    def LoadFromStream(self, bufferStream):
        UnpackFormat, count = _typeToFormat(self._typeFormat)
        tmpbuffer = bufferStream[0:self._size]
        if count > 1:
            val = struct.unpack_from(UnpackFormat, tmpbuffer)
            self._Value = val
        else:
            val = struct.unpack_from(UnpackFormat, tmpbuffer)
            self._Value = val[0]
        return self._size, self

    def StoreToStream(self):
        # UnpackFormat = self._typeToFormat('U1')
        UnpackFormat, count = _typeToFormat(self._typeFormat)
        if count > 1:
            value = copy.deepcopy(self._Value)
            while len(value) < count:
                value.append(self._default)
            outval = struct.pack(UnpackFormat, value[0:count])
        else:
            outval = struct.pack(UnpackFormat, self._Value)
        return outval

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

    def enumStr(self, tst_value):
        for key, value in self.items():
            if value == tst_value:
                return key
        return 'Oops:' + str(tst_value)

    def __iter__(self):
        result = []
        for key in iter(self.keys()):
            result.append((key, self[key]),)
        return iter(result)

    def __len__(self):
        MyClass = self.__class__
        members = [attr for attr in dir(MyClass) if not callable(getattr(MyClass, attr)) and not attr.startswith("_") and not attr.startswith("Value")]
        return len(members)

    def __getitem__(self, key):
        MyClass = self.__class__
        return getattr(MyClass, key)

    def keys(self):
        MyClass = self.__class__
        members = [attr for attr in dir(MyClass) if not callable(getattr(MyClass, attr)) and not attr.startswith("_") and not attr.startswith("Value")]
        return members

    def values(self):
        return [self.__getitem__(attr) for attr in self.keys()]

    def items(self):
        return [(attr, self.__getitem__(attr)) for attr in self.keys()]

    def bValidate(self) -> bool:
        """ This method is used to validate a CCS_Enum object.

        Args:

        Returns:
            bool: The return value. If the validation passed.

        Raises:
            Raises no exception.
        """
        bReturnValue = bool(False)
        lstValues = self.values()

        if (lstValues is None):
            if (G_bCcsTypesLoggingEnabled):
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
            if (G_bCcsTypesLoggingEnabled):
                if (not lstValues):
                    logging.error("CCS_Enum() validation failed for class %s - current value %s", self.__class__.__name__, str(self._Value))
                else:
                    logging.error("CCS_Enum() validation failed for class %s - current value %s - enum values %s", self.__class__.__name__, str(self._Value), str(lstValues))

        return(bReturnValue)


class CCS_EnumArray:
    def __init__(self, typeFormat=None, defaultValue=0):
        super(CCS_EnumArray, self).__init__()
        self._typeFormat = typeFormat
        clsname, count = CCS_Find_Class(self._typeFormat)
        self._BaseClass = clsname
        self._Base = clsname(defaultValue)
        self._count = count
        self._size = 0
        self._Value = [None] * self._count  # Make a list with the correct count but all Nones

        for iIndex, _ in enumerate(self._Value):
            self._Value[iIndex] = self._BaseClass(defaultValue)

    def iGetCount(self) -> int:
        """ This is a public method which returns the number of items in the list

        Args:

        Returns:
            (int): The number of items in the list

        Raises:
            Raises no exceptions
        """
        return(self._count)

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, value):  # lint:ok
        self._Value = value

    def _calc_size(self):
        if self._size == 0:
            obj = self._BaseClass()
            self._size = obj.size() * self._count
        return self._size

    def size(self):
        return self._calc_size()

    def LoadFromStream(self, bufferStream):
        BufferIndex = 0
        self._Value.clear()
        for cnt in range(self._count):
            tmpObj = self._BaseClass()
            sz = tmpObj.size()
            tmpbuffer = bufferStream[BufferIndex: BufferIndex + sz]
            if len(tmpbuffer) != sz:
                print("BufferIndex: BufferIndex + sz", sz, tmpbuffer)
                raise Exception("Ooops")
            tmpObj.LoadFromStream(tmpbuffer)
            self._Value.append(tmpObj)
            BufferIndex += sz
        return BufferIndex, self

    def StoreToStream(self):
        value = copy.deepcopy(self._Value)
        while len(value) < self._count:
            value.append(self._BaseClass())
        outBuffer = bytearray()
        for cnt in range(self._count):
            outval = value[cnt].StoreToStream()
            outBuffer = outBuffer + outval
        return outBuffer

    def dctToDict(self) -> Dict:
        """This is a public method which creates a nested (recursive) dictionary based on the attributes of the derived class.

        Args:

        Returns:
            (dict): A dictionary containing the attributes of the derived class

        Raises:
            Raises no exception.
        """

        dctReturn = {}
        dctReturn["Attr"] = []    # The attributes from the EnumArray will also be stored in a list
        acSelfType = str(type(self)).split('\'')[1]

        lstValue = self._Value
        for iIndex, objCCSEnum in enumerate(lstValue):
            dctReturn["Attr"] += [{}]
            # Because we are iterating through a EnumArray every element will be an Enum, therefore add the Value as well
            dctReturn["Attr"][iIndex] = {"Name": acSelfType + str(iIndex), "Type": str(type(objCCSEnum)).split('\'')[1], "Value": objCCSEnum.Value}

        return(dctReturn)

    def bValidate(self) -> bool:
        bReturnValue = bool(False)
        bReturnItem = bool(True)
        lstValue = copy.deepcopy(self._Value)

        if (lstValue is None):
            if (G_bCcsTypesLoggingEnabled):
                logging.error("lstValue cannot be None")
            return(bReturnValue)

        if (isinstance(lstValue, list) is False):
            if (G_bCcsTypesLoggingEnabled):
                logging.error("lstValue must be a list")
            return(bReturnValue)

        # Return True if the list is empty
        if (not lstValue):
            return(True)

        bReturnValue = bool(True)  # Set to True for bitwise and
        for _, objItem in enumerate(lstValue):
            bReturnItem = objItem.bValidate()
            if (bReturnItem is False):
                if (G_bCcsTypesLoggingEnabled):
                    logging.error("CCS_EnumArray() validation failed for %s ", self.__class__.__name__)

            bReturnValue &= bReturnItem

        return(bReturnValue)


class CCS_Typedef:
    def __init__(self, typeFormat=None, defaultValue=0):
        self.typeFormat = typeFormat
        sz, count = _typeToSize(self.typeFormat)
        if sz is None:
            clsname, count = CCS_Find_Class(self.typeFormat)
            self.BaseClass = clsname
            self.Base = clsname(self.typeFormat, defaultValue)
        else:
            self.BaseClass = CCS_Base  # (self.typeFormat, defaultValue)
            self.Base = CCS_Base(self.typeFormat, defaultValue)
        pass

    @property
    def count(self):
        return self.Base.count()

    @property
    def default(self):
        return self.Base.default()

    @property
    def Value(self):
        return self.Base.Value

    @Value.setter
    def Value(self, value):  # lint:ok
        self.Base.Value = value

    def _calc_size(self):
        return self.Base.size()

    def size(self):
        return self.Base.size()

    def LoadFromStream(self, Buffer):
        return self.Base.LoadFromStream(Buffer)

    # Special Calse Need to be passed the default possibly
    def StoreToStream(self):
        return self.Base.StoreToStream()


class CCS_StructArray:
    def __init__(self, typeFormat, defaultValue=None):
        self._typeFormat = typeFormat
        class_type, count = CCS_Find_Class(self._typeFormat)
        self._BaseClass = class_type
        self._Base = self._BaseClass()
        self._BaseObjSize = 0  # Will later be the size of one item
        self._BaseTotalSize = 0  # Will later be the total size
        self._count = count  # How many items in the array/list
        self._Value = [None] * self._count  # Make a list with the correct count but all Nones

        for iIndex, _ in enumerate(self._Value):
            self._Value[iIndex] = self._BaseClass()

    def typeGetBaseClassType(self):
        """ This is a public method which gets the type of the base class

        Args:

        Returns:
            (type): The type of the base class

        Raises:
            Raises no exception.
        """
        return(self._BaseClass)

    def iGetCount(self):
        """ This is a public method which gets the number of elements in the StructArray

        Args:

        Returns:
            (int): The number of elements in the array

        Raises:
            Raises no exception.
        """
        return(self._count)

    def acGetTypeFormat(self):
        """ This is a public method which gets typeformat of the object as passed in during construction

        Args:

        Returns:
            (str): The typeformat as a string "[CLASS]:[NUM]"

        Raises:
            Raises no exception.
        """
        return(self._typeFormat)

    def _calc_size(self):
        # The total size only needs to be calculated once
        if self._BaseTotalSize == 0:
            tmpObj = self._BaseClass()
            self._BaseObjSize = tmpObj.size()
            self._BaseTotalSize = self._BaseObjSize * self._count
        return self._BaseTotalSize

    def size(self):
        return self._calc_size()

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, value):  # lint:ok
        if (value is None):
            if (G_bCcsTypesLoggingEnabled):
                logging.error("value is None")
            return

        if (isinstance(value, list) is False):
            if (G_bCcsTypesLoggingEnabled):
                logging.error("value is not a list")
            return

        if (len(value) != self._count):
            if (G_bCcsTypesLoggingEnabled):
                logging.error("value should be a list of length %d and it is not", self._count)
            return

        self._Value = value

    def LoadFromStream(self, Buffer):
        self._Value.clear()
        BufferIndex = 0
        for cnt in range(self._count):
            tmpObj = self._BaseClass()
            sz = tmpObj.size()
            tmpbuffer = Buffer[BufferIndex: BufferIndex + sz]
            tmpObj.LoadFromStream(tmpbuffer)
            self._Value.append(tmpObj)
            BufferIndex += sz
        return BufferIndex, self

    # Special Calse Need to be passed the default possibly
    def StoreToStream(self):
        outputbuffer = bytearray()
        ValToWrite = copy.deepcopy(self._Value)
        validCnt = min(self._count, len(ValToWrite))
        toAdd = self._count - validCnt
        if toAdd > 0:
            for ctr in range(toAdd):
                tmpObj = self._BaseClass()
                ValToWrite.append(tmpObj)
        for ctr in range(self._count):
            tmpObj = ValToWrite[ctr]
            output = tmpObj.StoreToStream()
            outputbuffer.extend(output)
        return outputbuffer

    def dctToDict(self) -> Dict:
        """This is a public method which creates a nested (recursive) dictionary based on the attributes of the derived class.

        Args:

        Returns:
            (dict): A dictionary containing the attributes of the derived class

        Raises:
            Raises no exception.
        """

        dctReturn = {}
        dctReturn["Attr"] = []  # The Value list items will also be stored in a list
        lstValues = self._Value
        acSelfType = str(type(self)).split('\'')[1]

        # Iterate through the list - all items will be a CCS_Struct()
        for iIndex, objCCSStruct in enumerate(lstValues):
            dctReturn["Attr"] += [{}]
            # Each nested attribute must have a "Name", "Type" and "Attr"
            dctReturn["Attr"][iIndex] = {"Name": acSelfType + str(iIndex), "Type": str(type(objCCSStruct)).split('\'')[1], "Attr": None}
            dctReturn["Attr"][iIndex]["Attr"] = [objCCSStruct.dctToDict()]

        return(dctReturn)

    def bValidate(self):
        """This is a public method which validates the CCS_StructArray object.

        This is a public method which validates the CCS_StructArray object.

        Args:

        Returns:
            bool: The return value. If the validation passed.

        Raises:
            Raises no exception.
        """
        bValidationResult = bool(False)  # Start the result as true
        bValidationItem = bool(False)

        # First make a deep copy
        lstValToValidate = copy.deepcopy(self._Value)

        if (lstValToValidate is None):
            if (G_bCcsTypesLoggingEnabled):
                logging.error("lstValToValidate cannot be None")
            return(bValidationResult)

        # Then list of structs are empty
        if (not lstValToValidate):
            if (G_bCcsTypesLoggingEnabled):
                logging.error("List of structs cannot be empty")
            return(bValidationResult)

        # Make sure it is a List
        if (isinstance(lstValToValidate, list) is False):
            if (G_bCcsTypesLoggingEnabled):
                logging.error("lstValToValidate must be a list")
            return(bValidationResult)

        bValidationResult = bool(True) 

        for iIndex, objItem in enumerate(lstValToValidate):
            if (isinstance(objItem, CCS_Struct) is True):
                bValidationItem = objItem.bValidate()

                if (bValidationItem is False):
                    if (G_bCcsTypesLoggingEnabled):
                        logging.error("CCS_StructArray() item validation failed for index %d", iIndex)

                bValidationResult &= bValidationItem

        return(bValidationResult)


class CCS_Struct:
    def __init__(self, typeFormat=None, defaultValue=None):
        self._typeFormat = typeFormat
        self._loaddefault = dict()
        self._loadorder = list()
        self._loadmins = dict()
        self._loadmax = dict()
        self._size = 0

    def _calc_size(self):
        if self._size == 0:
            calced_size = 0
            members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("_")]
            for LdName in members:
                tmpObj = self.objGetItem(LdName)
                if not (tmpObj is None):
                    sz = tmpObj._calc_size()
                    calced_size += sz
            self._size = calced_size
        return self._size

    def size(self):
        return self._calc_size()

    def objGetItem(self, key):
        if not key.startswith("_"):
            obj = getattr(self, key)
            return obj
        return None

    def AddType(self, ldName):
        self._loadorder.append(ldName)

    def AddMin(self, ldName, ldValue):
        self._loadmins[ldName] = ldValue

    def AddMax(self, ldName, ldValue):
        self._loadmax[ldName] = ldValue

    def LoadFromStream(self, btaBuffer: bytes):
        """This is a public method which takes a bytes stream and unpacks it into class

        Args:
            btaBufferStream: A bytes type containing the data which needs to be unpacked

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
            return iBufferIndex, self

        # The bytes buffer must at least have some length
        if (len(btaBuffer) <= 0):
            return iBufferIndex, self

        for acLoadName in self._loadorder:
            objLoadOrderItem = self.objGetItem(acLoadName)
            if not (objLoadOrderItem is None):
                iSizeBytes = objLoadOrderItem.size()
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
                if (len(btaTempBuffer) > 0):
                    objLoadOrderItem.LoadFromStream(btaTempBuffer)
                iBufferIndex += iSizeBytes
        return iBufferIndex, self

    def StoreToStream(self):
        outBuffer = bytearray()
        for ldName in self._loadorder:
            tmpObj = self.objGetItem(ldName)
            if not (tmpObj is None):
                resout = tmpObj.StoreToStream()
                outBuffer.extend(resout)
        return outBuffer

    def dctToDict(self) -> Dict:
        """This is a public method which creates a nested (recursive) dictionary based on the attributes of the derived class.

        Args:

        Returns:
            (dict): A dictionary containing the attributes of the derived class

        Raises:
            Raises no exception.
        """

        dctReturn = {}
        dctReturn["Attr"] = []  # The attributes will be stored in a list

        # Get a list of all the attributes in the derived class
        lstAttributes = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("_")]
        # Iterate through the attributes
        for iIndex, acAttribute in enumerate(lstAttributes):
            dctReturn["Attr"] += [{}]
            objAttribute = getattr(self, acAttribute)
            # Each nested attribute must have a "Name", "Type" and "Attr"
            dctReturn["Attr"][iIndex] = {"Name": acAttribute, "Type": str(type(objAttribute)).split('\'')[1], "Attr": None}
            dctReturn["Attr"][iIndex]["Attr"] = objAttribute.dctToDict()

            # If the attribute is a tree leaf then stop and get the value
            if (isinstance(objAttribute, (CCS_Base, CCS_Enum)) is True):
                dctReturn["Attr"][iIndex]["Value"] = objAttribute.Value

        return(dctReturn)

    def bValidate(self):
        """This is a public method which validates the CCS_Base objects in the items list

        This is a public method which validates the CCS_Base objects in the items list

        Args:

        Returns:
            bool: The return value. If the validation passed.

        Raises:
            Raises no exception.
        """
        bValidationResult = bool(True)  # Start the result as true
        bValidationPetItem = bool(False)

        # Iterate through the loader list
        for acLoadName in self._loadorder:
            # Get the object based on a string
            objItemFromLoadOrder = self.objGetItem(acLoadName)
            if objItemFromLoadOrder is not None:
                bValidationPetItem = objItemFromLoadOrder.bValidate()
                if (bValidationPetItem is False):
                    if (G_bCcsTypesLoggingEnabled):
                        logging.error("CCS_Struct() field %s validation failed!!!", str(acLoadName))
                # Bitwise and the results
                bValidationResult = bValidationResult & bValidationPetItem

        return(bValidationResult)


class CCS_HdrStruct(CCS_Struct):

    def __init__(self, formatType=None):
        super(CCS_HdrStruct, self).__init__(formatType)


class CCS_MsgStruct(CCS_Struct):

    def __init__(self, formatType=None):
        super(CCS_MsgStruct, self).__init__(formatType)


class CCS_Message():

    def __init__(self, formatType=None):  # formatType is Ignored
        self._size = 0
        pass

    def _calc_size(self):
        # Need to Get The Structures Here and then Calculate the sizes, and then set the header Length Field
        members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("_")]
        if self._size == 0:
            calced_size = 0
            for member in members:
                obj = self.objGetItem(member)
                if type(obj) != list:
                    sz = obj._calc_size()
                    calced_size += sz
                elif type(obj) == list:
                    sz = len(obj)
                    calced_size += sz
            self._size = calced_size
        return self._size

    def size(self):
        return self._calc_size()

    def objGetItem(self, key):
        if not key.startswith("_"):
            obj = getattr(self, key)
            if not callable(obj):
                return obj
        return None

    def StoreToStream(self):
        outBuffer = bytearray()
        members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("_")]
        for member in members:
            val = getattr(self, member)
            outBuffer.extend(val.StoreToStream())
        return outBuffer

    def dctToDict(self) -> Dict:
        """This is a public method which creates a nested (recursive) dictionary based on the attributes of the derived class.

        Args:

        Returns:
            (dict): A dictionary containing the attributes of the derived class

        Raises:
            Raises no exception.
        """
        dctReturn = {}
        dctReturn["Attr"] = []  # The attributes will be stored in a list

        # Get a list of all the attributes in the derived class
        lstAttributes = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("_")]
        # Iterate through the attributes
        for iIndex, acAttribute in enumerate(lstAttributes):
            dctReturn["Attr"] += [{}]
            objAttribute = getattr(self, acAttribute)
            # Each nested attribute must have a "Name", "Type" and "Attr"
            dctReturn["Attr"][iIndex] = {"Name": acAttribute, "Type": str(type(objAttribute)).split('\'')[1], "Attr": None}
            dctReturn["Attr"][iIndex]["Attr"] = objAttribute.dctToDict()

        return(dctReturn)

    def LoadFromStream(self, btaBufferStream: bytes):
        """This is a public method which takes a bytes stream and unpacks it into class

        Args:
            btaBufferStream: A bytes type containing the data which needs to be unpacked

        Returns:
            iBufferIndex: The return value. If the last buffer index used.
            self: The self reference

        Raises:
            Raises no exception.
        """

        iBufferIndex = int(0)
        btaTempBuffer = bytes([])
        iSizeBytes = int(0)

        # Do some sanity checks - the buffer cannot be None
        if (btaBufferStream is None):
            return iBufferIndex, self

        # The bytes buffer must at least have some length
        if (len(btaBufferStream) <= 0):
            return iBufferIndex, self

        # Iterate through the members of the class - put them in a list
        lstMembers = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("_")]
        for acMember in lstMembers:
            objItem = getattr(self, acMember)
            if not (objItem is None):
                iSizeBytes = objItem.size()
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
                if (len(btaTempBuffer) > 0):
                    objItem.LoadFromStream(btaTempBuffer)
                iBufferIndex += iSizeBytes
        return iBufferIndex, self
    
    def bValidate(self):
        """This is a public method which validates the CCS_Base objects in the items list

        This is a public method which validates the CCS_Base objects in the items list

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
                if (G_bCcsTypesLoggingEnabled):
                    logging.error("CCS_Message() field %s validation failed!!!", str(acMember))
            bValidationResult = bValidationResult & bValidationItem

        return(bValidationResult)
