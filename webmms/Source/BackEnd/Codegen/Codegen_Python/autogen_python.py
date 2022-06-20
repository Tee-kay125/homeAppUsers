#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""This module autogens RRS XML into python source for the use with the WebMM

Example:
    To run this file do the following:

        $ python3.6 autogen_python.py PATH_TO_INI_FILE

Todo:
    * Add more logging and comments
    * Clean up the code

Originally created on Thu Feb 25 10:35:28 2016 @author: riyaadh
Modified by erossouw
"""
import logging
import time
import sys
import os
import json
import xml.etree.ElementTree as ET
import configparser as ConfigParser
from shutil import copyfile
from enum import Enum
from lxml import etree
from jinja2 import Environment, FileSystemLoader
from jinja2 import __version__ as JinjaVersion


# =====================================
# Global variables
# =====================================


G_dctEnumTypes = {}  # We keep this dictionary to store the enumerations
G_lstXmlFileContextDictionaries = []    # A list of all the context dictionaries of all the XML files parsed
G_objConfigParser = ConfigParser.ConfigParser()    # We make the config parser a global so that all functions have access to it

G_dctPreparseTypedefStructs = {}
G_dctPreparseTypedefEnums = {}

# Set the base types
G_dctXmlSchemaBaseTypes = {'F4': '0.0',
                           'F8': '0.0',
                           'U1': '0',
                           'U2': '0',
                           'U4': '0',
                           'U8': '0',
                           'I1': '0',
                           'I2': '0',
                           'I4': '0',
                           'I8': '0',
                           'CH': '0',
                           'ST': ''}

G_lstXmlSchemaIntegerBaseTypes = ["U1", "U2", "U4", "U8", "I1", "I2", "I4", "I8"]

G_dctXmlSchemaBaseTypeToPrefixLookup = {}
G_dctXmlSchemaBaseTypeToPrefixLookup["F4"] = "f4"
G_dctXmlSchemaBaseTypeToPrefixLookup["F8"] = "f8"
G_dctXmlSchemaBaseTypeToPrefixLookup["I1"] = "i1"
G_dctXmlSchemaBaseTypeToPrefixLookup["I2"] = "i2"
G_dctXmlSchemaBaseTypeToPrefixLookup["I4"] = "i4"
G_dctXmlSchemaBaseTypeToPrefixLookup["I8"] = "i8"
G_dctXmlSchemaBaseTypeToPrefixLookup["U1"] = "u1"
G_dctXmlSchemaBaseTypeToPrefixLookup["U2"] = "u2"
G_dctXmlSchemaBaseTypeToPrefixLookup["U4"] = "u4"
G_dctXmlSchemaBaseTypeToPrefixLookup["U8"] = "u8"
G_dctXmlSchemaBaseTypeToPrefixLookup["CH"] = "ach"
G_dctXmlSchemaBaseTypeToPrefixLookup["ST"] = "ach"

G_dctXmlSchemaBaseTypesToDefaultValueLookup = {}
G_dctXmlSchemaBaseTypesToDefaultValueLookup["F4"] = "0.0"
G_dctXmlSchemaBaseTypesToDefaultValueLookup["F8"] = "0.0"
G_dctXmlSchemaBaseTypesToDefaultValueLookup["I1"] = "0"
G_dctXmlSchemaBaseTypesToDefaultValueLookup["I2"] = "0"
G_dctXmlSchemaBaseTypesToDefaultValueLookup["I4"] = "0"
G_dctXmlSchemaBaseTypesToDefaultValueLookup["I8"] = "0"
G_dctXmlSchemaBaseTypesToDefaultValueLookup["U1"] = "0"
G_dctXmlSchemaBaseTypesToDefaultValueLookup["U2"] = "0"
G_dctXmlSchemaBaseTypesToDefaultValueLookup["U4"] = "0"
G_dctXmlSchemaBaseTypesToDefaultValueLookup["U8"] = "0"
G_dctXmlSchemaBaseTypesToDefaultValueLookup["CH"] = "\"\""
G_dctXmlSchemaBaseTypesToDefaultValueLookup["ST"] = "\"\""

# =====================================
# Global enums
# =====================================


class E_XML_FILE_TYPE(Enum):
    """ This is enum which denotes all the kinds of XML file namely main or common include

    """
    XML_FILE_TYPE_MAIN_DEFINITION = 1
    XML_FILE_TYPE_TYPE_INCLUDE = 2


class E_XML_FILE_SCHEMA_FORMAT_TYPE(Enum):
    """ This is enum which denotes all the different kind of supported XML schemas

    """
    XML_FILE_SCHEMA_FORMAT_BR12 = 1
    XML_FILE_SCHEMA_FORMAT_ADCS = 2


class E_XML_FIELD_TYPE(Enum):
    """ This is enum which denotes all the XML field types

    """
    XML_FIELD_TYPE_ENUM = 1
    XML_FIELD_TYPE_STRUCT = 2
    XML_FIELD_TYPE_BASE = 3


class E_NUMERIC_VALUE_TYPE(Enum):
    """ This is enum which denotes all the types of numeric values of a string

    """
    NUMERIC_VALUE_TYPE_INVALID = 1  # Indicates value is invalid - not a value
    NUMERIC_VALUE_TYPE_INTEGER = 2  # Indicates value is an integer (not hex)
    NUMERIC_VALUE_TYPE_FLOAT = 3  # Indicates value is a float
    NUMERIC_VALUE_TYPE_HEX_INTEGER = 4  # Indicates value in hex


# =====================================
# Global functions
# =====================================


# =====================================
# Global declarations
# =====================================


# =====================================
# Class definitions
# =====================================

class clsETreeXmlParser:
    """ Class for parsing XML file into Elementree root

    Args:
        acXmlFilePathPar (str): The path to the XML file.
        acOutputGenerationPathPar (str): The path to the generation output directory.
        eXmlSchemaFormatPar (E_XML_FILE_SCHEMA_FORMAT_TYPE): Enum which says if it's ADCS or BR12 type XML schema files.
        bFindXmlIncludesPar (bool): Bool flag which indicates if we should search and find other included common include XML files.

    """

    def __init__(self, acXmlFilePathPar, acOutputGenerationPathPar, eXmlSchemaFormatPar: E_XML_FILE_SCHEMA_FORMAT_TYPE, bFindXmlIncludesPar: bool):
        """
        Create a class object that parses the xml file specified in
        'acXmlFilePathPar' using an element tree structure (ElementTree objects). 
        It also creates the autogen output directory specified in 'acOutputGenerationPathPar' if the
        path does not exist already.

        Furthermore, inside this constructor the ElementTree object will be created and then parse the
        XML file. If the parse was successful we will save the root ElementTree Element object. The root
        element will then be used to search for ./Section/Message tags in the XML file. That means after
        this class object (of type clsETreeXmlParser) is constructed we will have a list of Messages in
        the XML as a list of ElementTree elements.

        Args:
            acXmlFilePathPar (str): Path to the xml file to be parsed.
            acOutputGenerationPathPar (str): Path to where the output files will be generated to.
            eXmlSchemaFormatPar (E_XML_FILE_SCHEMA_FORMAT_TYPE): The schema format BR12 or ADCS.
            bFindXmlIncludesPar (bool): Flag to say if we should parse and look for common XML includes.

        Returns:

        Raises:
            Raises no exception.

        """

        # Declare the local variables
        self.bFindXmlIncludes = bFindXmlIncludesPar  # Keep a local indicating if this object looked for included XML files
        self.acXmlFilePath = str("")
        self.acXmlFileBaseDirectory = str("")  # This will store the path of the XML file path but without the filename
        self.acXmlFileNameOnly = str("")
        self.acXmlFileWithoutExtension = str("")
        self.lstIncludedXmlFiles = []  # This is a list of all the included XML files we find
        self.lstIncludedXmlFilesAsPythonModules = []  # This is a list of all the included XML files we find but as autogened modules
        self.objElementTreeTree = None  # This will store the ElementTree object later
        self.objRootElement = None  # This will store the ElementTree root Element later
        self.acHeaderStructName = "sMESSAGE_HEADER"  # We will need this later
        self.eXmlFileType = E_XML_FILE_TYPE(E_XML_FILE_TYPE.XML_FILE_TYPE_MAIN_DEFINITION)  # Set to main for now will change later
        self.eXmlFileSchemaType = eXmlSchemaFormatPar
        self.acOutputGenerationPath = acOutputGenerationPathPar

        self.lstMessageElements = []  # Make this list empty for now
        self.lstTypedefElements = []  # Make this list empty for now

        if (bFindXmlIncludesPar is True):
            self.eXmlFileType = E_XML_FILE_TYPE(E_XML_FILE_TYPE.XML_FILE_TYPE_MAIN_DEFINITION)
        else:
            self.eXmlFileType = E_XML_FILE_TYPE(E_XML_FILE_TYPE.XML_FILE_TYPE_TYPE_INCLUDE)

        # This is for Windows file paths I guess. For Linux however this is not needed but we will keep it in
        acXmlFilePathPar = acXmlFilePathPar.replace("\\", "/")

        self.acXmlFilePath = acXmlFilePathPar
        self.acXmlFileBaseDirectory = os.path.dirname(acXmlFilePathPar)
        self.acXmlFileNameOnly = os.path.basename(acXmlFilePathPar)
        # Remove '.xml' from xml filename and add _
        self.acXmlFilePrename = self.acXmlFileNameOnly[:-4] + "_"

        # We only allow one level of common includes
        if (bFindXmlIncludesPar is True):
            self.vFindXmlIncludes(acXmlFilePathPar)

            for acFilename in self.lstIncludedXmlFiles:
                acFilename, _ = os.path.splitext(acFilename)
                acFilename += "_TypeDef"
                self.lstIncludedXmlFilesAsPythonModules.append(acFilename)

        # Try to parse the xml path
        try:
            self.objElementTreeTree = ET.parse(acXmlFilePathPar)
        except ET.ParseError as E:
            logging.error("Could not do ElementTree parse - Exception %s", str(E))
            return
        except Exception as ex:
            logging.error("Could not do ElementTree parse - Exception %s", str(ex))
            return

        try:
            self.objRootElement = self.objElementTreeTree.getroot()
        except Exception as E:
            logging.error("Could not get tree root element - Exception %s", str(E))
            return

        # Because the WebMM cannot interpret hex values
        # we need to convert hex values in Enumeration, Field and Record
        # elements into decimal integer. This is only if the type of
        # Field or Record is of type integer
        self.vConvertAllEnumerationAndRecordAndFieldHexValuesIntoDecimalInt(self.objRootElement)

        # In ElementTree find syntax say for example ".//egg" to find all the egg tags
        # in the entire tree. See URL https://docs.python.org/2/library/xml.etree.elementtree.html
        # for more details

        # Typefiles do not have messages - do not even look for some
        if (self.eXmlFileType == E_XML_FILE_TYPE.XML_FILE_TYPE_MAIN_DEFINITION):

            # Find all the Typedef tags
            self.lstTypedefElements = self.objRootElement.findall(".//Section/Typedef")

            # Find all the Messages tags in the Section tags

            self.lstMessageElements = self.objRootElement.findall("./Section/Message")

        else:
            # This means it is a typedef file
            self.lstTypedefElements = self.objRootElement.findall(".//Typedef")

        # Now sort Enumerations and Structs
        dctOut = self.dctFindEnumsAndStructsFromTypedefElements(self.lstTypedefElements)

        # Try to make output directory if it does not exist yet
        if (os.path.isdir(self.acOutputGenerationPath) is False):
            logging.warning("Generating output directory %s does not exist but we will try to create it")

            try:
                os.makedirs(self.acOutputGenerationPath)
            except Exception as E:
                logging.error("Could not create dir %s", str(self.acOutputGenerationPath))

        return

    def vFindXmlIncludes(self, acXmlPathPar):
        """ This public method checks whether or not there are other XML files to include with the current one. It fills in a list of XML
        files to be included.

        Args:
            acXmlPathPar (str): Path to the current xml file to be parsed.

        Returns:

        Raises:
            Raises no exceptions
        """

        bXmlFileExists = bool(False)  # Flag used to keep track of Xml file exists
        objOpenXmlFileRef = None  # Will be used to open a file
        acLineOfText = str("")  # Will be used later to store lines from the file
        bExitEarly = bool(True)  # Will be used later for some safety checks
        bDocTypeSectionEmpty = bool(False)
        iLineReadForIncludesTimeout = int(50)
        iLinesReadCounter = int(0)
        acFilename = str("")

        if (acXmlPathPar is None):
            logging.error("acXmlPathPar cannot be None")
            return

        if (isinstance(acXmlPathPar, str) is False):
            logging.error("acXmlPathPar must be str")
            return

        # Clear the class properties just to sure
        self.lstIncludedXmlFiles = []

        # Now check that the binary file actually exists
        try:
            bXmlFileExists = os.path.isfile(acXmlPathPar)
        except Exception as E:
            logging.error("XML file does not exist - Exception %s", str(E))
            return

        if (bXmlFileExists is False):
            logging.error("XML file does not exist - Exception %s", str(E))
            return

        # Open the XML file by using the provided path
        try:
            objOpenXmlFileRef = open(acXmlPathPar, "r")
        except Exception as E:
            logging.error("Could not open file %s - Exception %s", acXmlPathPar, str(E))
            return

        bExitEarly = bool(True)

        # Parse the file one line at a time. A newline means it is a line
        try:
            acLineOfText = objOpenXmlFileRef.readline()
        except Exception as E:
            logging.error("Could not call readline - Exception %s", str(E))

            try:
                objOpenXmlFileRef.close()
            except Exception as E:
                logging.error("Could not close file - Exception %s", str(E))

            return

        while acLineOfText:

            # We need to check where the <!DOCTYPE starts
            if "<!DOCTYPE" in acLineOfText:
                # If we also have a "greater-than" character in this line then the DOCTYPE section is empty

                if (acLineOfText.count(">") > 0):
                    bDocTypeSectionEmpty = bool(True)

                # We have found the DOCTYPE line so we can stop reading lines for now
                bExitEarly = bool(False)
                break
            else:
                # Otherwise if "<!DOCTYPE" was not found then keep reading lines

                try:
                    acLineOfText = objOpenXmlFileRef.readline()
                except Exception as E:
                    logging.error("Could not call readline - Exception %s", str(E))

        if (bExitEarly is True):
            logging.error("Error occurred")

            try:
                objOpenXmlFileRef.close()
            except Exception as E:
                logging.error("Could not close file - Exception %s", str(E))

            return

        # If the DOCTYPE section is empty then exit
        if (bDocTypeSectionEmpty is True):

            try:
                objOpenXmlFileRef.close()
            except Exception as E:
                logging.error("Could not close file - Exception %s", str(E))

            return

        # At this stage we have found the DOCTYPE section/lines and need to get all the XML filenames

        # Reset the lines read counter
        iLinesReadCounter = int(0)

        while acLineOfText:

            # We are only going to read a reasonable amount of lines and then give up for safety reasons
            if (iLinesReadCounter > iLineReadForIncludesTimeout):
                break

            # Look for lines with .xml in them
            # There must be:
            #  * Be a string
            #  * Be at least 4 chars long
            #  * Have 2 x " character
            #  * Contain the string ".xml\""
            if ((isinstance(acLineOfText, str) is True) and (len(acLineOfText) > 4) and (acLineOfText.count("\"") == 2) and (".xml\"" in acLineOfText)):

                # Note the Python call find will find the fist character
                acFilename = acLineOfText[acLineOfText.find('"') + 1:acLineOfText.rfind('"')]

                self.lstIncludedXmlFiles.append(acFilename)

            # When we reach the end of the DOCTYPE part we stop
            if "]>" in acLineOfText:
                break

            # Read the next line and start again

            try:
                acLineOfText = objOpenXmlFileRef.readline()
            except Exception as E:
                logging.error("Could not call readline - Exception %s", str(E))
                break

            # We want to count how many lines we have read since DOCTYPE section started
            iLinesReadCounter += 1

        try:
            objOpenXmlFileRef.close()
        except Exception as E:
            logging.error("Could not close file - Exception %s", str(E))

        return

    def dctFindEnumsAndStructsFromTypedefElements(self, lstTypedefElementsPar: list):
        """ This public method iterates over all Typedef ElementTree elements
            and seperate them into Enumerations or Structs.

        Args:
            lstTypedefElementsPar (list): List of ElementTree elements.

        Returns:
            (dict):

        Raises:
            Raises no exceptions
        """
        dctReturn = {}
        dctReturn["Enums"] = []
        dctReturn["Structs"] = []

        dctElementItem = {}
        dctElementItem["acTypedefName"] = str("")
        dctElementItem["eXmlFieldType"] = E_XML_FIELD_TYPE(E_XML_FIELD_TYPE.XML_FIELD_TYPE_BASE)  # Make base for now
        dctElementItem["acFile"] = str("")
        dctElementItem["acType"] = str("")
        dctElementItem["iSizeInBytes"] = int(0)
        dctElementItem["objElement"] = None
        dctElementItem["acFieldPrefix"] = str("")

        acTypedefName = str("")

        lstEnumerationElements = []
        lstRecordElements = []

        if (not lstTypedefElementsPar):
            return(dctReturn)

        for objTypedefElement in lstTypedefElementsPar:

            if (objTypedefElement.tag != "Typedef"):
                logging.error("objTypedefElement is not a Typedef tag")
                continue

            if ("Name" not in objTypedefElement.attrib):
                logging.error("Name not in objTypedefElement.attrib")
                continue

            lstRecordElements = objTypedefElement.findall("./Record")

            if (not lstRecordElements):
                logging.error("objTypedefElement does not contain any Record tags")
                continue

            dctElementItem = {}
            dctElementItem["acFile"] = self.acXmlFilePath
            dctElementItem["objTypedefElement"] = objTypedefElement
            acTypedefName = objTypedefElement.attrib["Name"]
            dctElementItem["acTypedefName"] = acTypedefName
            dctElementItem["acType"] = str("")
            dctElementItem["iSizeInBytes"] = int(0)
            dctElementItem["acFieldPrefix"] = str("")

            lstEnumerationElements = objTypedefElement.findall("./Record/Enumeration")

            # Here we need to decide if the Typedef is an Enum or a Struct
            # Thre rule is if the are any "Enumeration" XML tag children then it's
            # an Enum, otherwise a struct.
            if (lstEnumerationElements):
                # Then this must be an Enumeration
                dctElementItem["eXmlFieldType"] = E_XML_FIELD_TYPE(E_XML_FIELD_TYPE.XML_FIELD_TYPE_ENUM)
                G_dctPreparseTypedefEnums[acTypedefName] = dctElementItem
                dctElementItem["acType"] = lstRecordElements[0].attrib["Type"]

                if (dctElementItem["acType"] not in G_dctXmlSchemaBaseTypes):
                    logging.error("Type %s unknown", dctElementItem["acType"])
                    continue
                else:
                    dctElementItem["iSizeInBytes"] = int(dctElementItem["acType"][1])
                    dctElementItem["acFieldPrefix"] = "e" + dctElementItem["acType"][1]


                dctReturn["Enums"].append(dctElementItem)

            else:
                # Then this must be a Struct
                dctElementItem["eXmlFieldType"] = E_XML_FIELD_TYPE(E_XML_FIELD_TYPE.XML_FIELD_TYPE_STRUCT)
                G_dctPreparseTypedefStructs[acTypedefName] = dctElementItem

                dctReturn["Structs"].append(dctElementItem)

        return(dctReturn)

    def vConvertAllEnumerationAndRecordAndFieldHexValuesIntoDecimalInt(self, objElement: ET.Element):
        """ This public method which converts the Value of any 
        Enumeration, Record (of base type) or Field (of base type) form
        a hex int into a decimal int. The rest of the WebMM code does not
        like hex values so that's why we do it.

        Args:
            objElement (ET.Element): An Element (ET.Element)

        Returns:

        Raises:
            Raises no exceptions
        """
        acStringValue = str("")
        eStringNumericType = E_NUMERIC_VALUE_TYPE(E_NUMERIC_VALUE_TYPE.NUMERIC_VALUE_TYPE_INVALID)  # Just make invalid for now
        lstEnumerationElements = []  # Will store a list of Enumeration Elements
        lstRecordElements = []  # Will store a list of Record Elements
        lstFieldElements = []  # Will store a list of Field Elements
        lstFieldAndRecordElements = []  # Will store a list of Field and Record Elements
        lstOfFieldRecordAttributesToModify = ["Default", "Min", "Max"]

        if (objElement is None):
            logging.error("objElement cannot be None")
            return

        if (isinstance(objElement, ET.Element) is False):
            logging.error("objElement is not an ET.Element")
            return

        # First do all the Enumeration tags
        lstEnumerationElements = objElement.findall(".//Enumeration")
        for objEnumeration in lstEnumerationElements:
            if ("Value" in objEnumeration.attrib):
                acStringValue = objEnumeration.attrib["Value"]
                # See if the is a hex string value
                eStringNumericType = self.eClassifyStringAsNumericType(acStringValue)

                if eStringNumericType is E_NUMERIC_VALUE_TYPE(E_NUMERIC_VALUE_TYPE.NUMERIC_VALUE_TYPE_HEX_INTEGER):
                    try:
                        # Convert the hex string into a decimal int string
                        objEnumeration.attrib["Value"] = str(int(acStringValue, 16))
                    except Exception as E:
                        logging.error("Could not convert hex string value to decimal string value")
            else:
                logging.error("Enumeration does not have a Value attribute")
                continue

        lstRecordElements = objElement.findall(".//Record")  # Now do all the Record Elements
        lstFieldElements = objElement.findall(".//Field")  # Now do all the Field Elements

        lstFieldAndRecordElements += lstRecordElements
        lstFieldAndRecordElements += lstFieldElements

        for objRecordOrField in lstFieldAndRecordElements:
            for acAttribute in lstOfFieldRecordAttributesToModify:
                if (acAttribute in objRecordOrField.attrib):
                    if (objRecordOrField.attrib["Type"] in G_lstXmlSchemaIntegerBaseTypes):
                        if (acAttribute in objRecordOrField.attrib):
                            acStringValue = objRecordOrField.attrib[acAttribute]
                            # See if the is a hex string value
                            eStringNumericType = self.eClassifyStringAsNumericType(acStringValue)

                            if eStringNumericType is E_NUMERIC_VALUE_TYPE(E_NUMERIC_VALUE_TYPE.NUMERIC_VALUE_TYPE_HEX_INTEGER):
                                try:
                                    # Convert the hex string into a decimal int string
                                    objRecordOrField.attrib[acAttribute] = str(int(acStringValue, 16))
                                except Exception as E:
                                    logging.error("Could not convert hex string %s to decimal string value", acAttribute)

        return

    def eClassifyStringAsNumericType(self, acStringPar: str):
        """ This is a public static method which determines if a string represents a numeric value

        Args:
            acStringPar (str): The string value

        Returns:
            (E_NUMERIC_VALUE_TYPE): Enum which indicates the type

        Raises:
            Raises no exception.
        """
        eReturn = E_NUMERIC_VALUE_TYPE(E_NUMERIC_VALUE_TYPE.NUMERIC_VALUE_TYPE_INVALID)
        bIsValidInt = bool(False)
        bIsValidFloat = bool(False)
        bIsValidHexInt = bool(False)

        if (not acStringPar):
            logging.error("acStringPar is invalid")
            return(eReturn)

        if (isinstance(acStringPar, str) is False):
            logging.error("acStringPar is invalid")
            return(eReturn)

        # Check if this is a float
        try:
            float(acStringPar)
            bIsValidFloat = bool(True)
        except Exception as E:
            bIsValidFloat = bool(False)

        # Check if this is a base 10 int
        try:
            int(acStringPar, 10)
            bIsValidInt = bool(True)
        except Exception as E:
            bIsValidInt = bool(False)

        # Check if this is a base 16 int
        try:
            int(acStringPar, 16)
            bIsValidHexInt = bool(True)
        except Exception as E:
            bIsValidHexInt = bool(False)

        if ((bIsValidInt is True) and (bIsValidFloat is True)):
            eReturn = E_NUMERIC_VALUE_TYPE(E_NUMERIC_VALUE_TYPE.NUMERIC_VALUE_TYPE_INTEGER)
            return(eReturn)
        elif ((bIsValidInt is False) and (bIsValidFloat is True)):
            eReturn = E_NUMERIC_VALUE_TYPE(E_NUMERIC_VALUE_TYPE.NUMERIC_VALUE_TYPE_FLOAT)
            return(eReturn)
        elif ((bIsValidInt is False) and (bIsValidFloat is False) and (bIsValidHexInt is True)):
            eReturn = E_NUMERIC_VALUE_TYPE(E_NUMERIC_VALUE_TYPE.NUMERIC_VALUE_TYPE_HEX_INTEGER)
            return(eReturn)

        return(eReturn)



# =====================================
# Global functions
# =====================================


def template_writer(context, out_file, template_path):
    '''
    This function uses jinja2 to write the autogen file from a given template.

    Parameters
    ----------
    context : dict
        Dictionary that holds all the variables to be filled into the
        template file.
    out_file : string
        String contaning the path to where the outfile will be written.
        If a file with this name exists already, the file will be overwritten.
    template_path : string
        Path to the template file. This is a relative path to where the
        script is running from.
    '''

    context.update({"PyVersion": sys.version.split("\n")[0], "JinjaVersion": JinjaVersion})
    template_env = Environment(loader=FileSystemLoader(os.path.dirname(os.path.realpath(template_path))), trim_blocks=False)
    if os.path.isfile(template_path):
        with open(out_file, "w") as f:
            file_data = template_env.get_template(os.path.basename(template_path)).render(context)
            f.write(file_data)
            f.close()


def autogen_typedef_py(objClsETreeXmlParserPar, acJinjaDefinitionTemplatePathPar, acCcsTypesPythonFilePathPar, dctXmlConfigIniParamsPar, iRecursionLevel: int):
    """
    This function extracts all parameters needed from 'objClsETreeXmlParserPar' for the Jinja template

    Args:
        objClsETreeXmlParserPar (clsETreeXmlParser): The element tree xml objClsETreeXmlParserPar object created with "xml_path".
        acJinjaDefinitionTemplatePathPar (str): Path to the template file. This is a relative path to where the script is running from.
        acCcsTypesPythonFilePathPar (str): Path to RRS base types .py file. This path is relative to autogen_output_path.
        dctXmlConfigIniParamsPar: Dictionary
            acPath (str): Path to the XML file being processed

    Returns:

    Exceptions:
        Raises no exception.

    """

    # Declare required variables
    acPathToFindElements = str("")  # This variable is used later to build a path for searching for elements in the root

    # Do some sanity checks
    if (isinstance(dctXmlConfigIniParamsPar, dict) is False):
        logging.error("dctXmlConfigIniParamsPar must be a dict")
        return

    if ("acPath" not in dctXmlConfigIniParamsPar):
        logging.error("acPath not in dctXmlConfigIniParamsPar")
        return

    # First isolate just the name of the module (no extension) - We will need this later to know
    # what the name of the module is to include the separate classes. We are trying to avoid * imports

    # The postfix will be different depending if this is an included XML or the main one
    if (objClsETreeXmlParserPar.bFindXmlIncludes is True):
        acOutModuleName = str(objClsETreeXmlParserPar.acXmlFilePrename + "MsgDef")
    else:
        acOutModuleName = str(objClsETreeXmlParserPar.acXmlFilePrename + "TypeDef")

    outFilename = str(acOutModuleName + ".py")
    #logging.info("Output Filename:" + str(outFilename))
    XmlIncludes = objClsETreeXmlParserPar.lstIncludedXmlFilesAsPythonModules

    if (XmlIncludes):
        # Method autogen_typedef_h is called recursively for every included XML file there might be
        for index in range(len(objClsETreeXmlParserPar.lstIncludedXmlFiles)):
            inc_file_path = os.path.join(objClsETreeXmlParserPar.acXmlFileBaseDirectory, objClsETreeXmlParserPar.lstIncludedXmlFiles[index])
            objClsIncludeXmlETreeXmlParser = clsETreeXmlParser(inc_file_path, objClsETreeXmlParserPar.acOutputGenerationPath, objClsETreeXmlParserPar.eXmlFileSchemaType, False)
            if objClsIncludeXmlETreeXmlParser.lstIncludedXmlFiles:
                autogen_typedef_py(objClsIncludeXmlETreeXmlParser, acJinjaDefinitionTemplatePathPar, acCcsTypesPythonFilePathPar, dctXmlConfigIniParamsPar, iRecursionLevel + 1)
            else:
                autogen_typedef_py(objClsIncludeXmlETreeXmlParser, acJinjaDefinitionTemplatePathPar, acCcsTypesPythonFilePathPar, dctXmlConfigIniParamsPar, iRecursionLevel + 1)

    # Extract typedef element tree elements from the objClsETreeXmlParserPar and append them
    # to a list which will be used to render the typedef enums and structures
    # section of the template.

    # Gen Typedef typedef's and struct's start
    # Gen Typedef typedef's and struct's start
    # Gen Typedef typedef's and struct's start

    # Here '//' means select all subelements, on all levels beneath the current element which is the root
    lstTypedefsAll = objClsETreeXmlParserPar.objRootElement.findall(".//Typedef")  # A list of all the Typedef elements found in the root
    lstTypedefDictItemList = []   # This variable is later packed into the context dictionary for the writer to use
    acTypedefTypeStructOrEnum = str("enum")  # This string is only allowed to be "enum" or "struct" for the Jinja template

    # Here we need to iterate through all the Typedef (not Message Payload!!!) fields and prepare and process them for the jinja template
    # Iterate through all the Typedefs in Elementree root
    for typedef in lstTypedefsAll:
        lstOfEnumOrRecordElementObjects = []

        # Set to enum for now
        acTypedefTypeStructOrEnum = str("enum")  # This string is only allowed to be "enum" or "struct" for the Jinja template

        # Find all Enumeration in the current Typedef element
        # If we find even one Enumerations XML tag in the Typedef then it is considered and Enumeration and not a Struct

        if (typedef.findall("./Record/Enumeration")):
            # Then this Typedef is an Enum

            acTypedefTypeStructOrEnum = str("enum")  # This string is only allowed to be "enum" or "struct" for the Jinja template

            lstOfEnumOrRecordElementObjects.append(typedef.findall("./Record/Enumeration"))
            enum_type = typedef.findall("./Record")[0].get("Type")
            if not enum_type:
                logging.error("Error: No type given for enum " + str(typedef.get("Name")))
                return
            else:
                G_dctEnumTypes.update({typedef.get("Name"): enum_type})

        else:
            # Then this Typedef is a Struct

            acTypedefTypeStructOrEnum = str("struct")  # This string is only allowed to be "enum" or "struct" for the Jinja template

            # Find all the Record tag Elements
            lstOfEnumOrRecordElementObjects.append(typedef.findall("./Record"))  # Will be packed into the context dictionary for the writer

            # Iterate through all the Records in the Typedef
            for objCurrentRecordElement in typedef.findall("./Record"):

                # If a Record has a Count greater than 1 then we set CountBool to True, otherwise False
                # We want to set the "CountBool" attrib even if the Record does not define it
                if "Count" in objCurrentRecordElement.attrib:
                    if int(objCurrentRecordElement.get("Count")) > 1:
                        objCurrentRecordElement.attrib.update({"CountBool": True})
                    else:
                        objCurrentRecordElement.attrib.update({"CountBool": False})
                else:
                    objCurrentRecordElement.attrib.update({"CountBool": False})

                # See if this Record is an enum, struct or base type
                if (objCurrentRecordElement.attrib["Type"] in G_dctPreparseTypedefEnums):
                    objCurrentRecordElement.attrib.update({"bDefaultIsEnum": True})
                elif (objCurrentRecordElement.attrib["Type"] in G_dctPreparseTypedefStructs):
                    objCurrentRecordElement.attrib.update({"bDefaultIsEnum": False})
                elif (objCurrentRecordElement.attrib["Type"] in G_dctXmlSchemaBaseTypes):

                    objCurrentRecordElement.attrib.update({"bDefaultIsEnum": False})

                    if ("Default" in objCurrentRecordElement.attrib):

                        if (objCurrentRecordElement.get("Type") in ["CH", "ST"]):
                            objCurrentRecordElement.attrib.update({"CountBool": True})
                            objCurrentRecordElement.attrib.update({"Default": "\"" + str(objCurrentRecordElement.attrib["Default"]) + "\""})
                    else:
                        if (objCurrentRecordElement.get("Type") in ["CH", "ST"]):
                            objCurrentRecordElement.attrib.update({"CountBool": True})
                            objCurrentRecordElement.attrib.update({"Default": "\"" + "\""})

        param_dict = {"FunctionType": acTypedefTypeStructOrEnum, "FunctionVariables": lstOfEnumOrRecordElementObjects, "TypedefTest": typedef}
        lstTypedefDictItemList.append(param_dict)

    # Gen Typedef typedef's and struct's end
    # Gen Typedef typedef's and struct's end
    # Gen Typedef typedef's and struct's end

    # Gen Message struct's start
    # Gen Message struct's start
    # Gen Message struct's start

    # Extract header element tree element and append it to message structures list.
    # Message structure list will be used to render the message structures section of the template.

    # The XML file might not have any messages so at least define these empty variables for now
    lstPayloadTagElements = []  # Should be an empty list if there are no messages
    lstHeaderElements = []  # Should be an empty list if there are no headers
    objElementHeaderTag = None  # For the jinja template this variable must be None if there are no messages

    # Only process messages if there are any messages - check if the list is empty
    if (objClsETreeXmlParserPar.lstMessageElements):

        # General hints!!! :
        # The attributes of a message can be retrieved with message.get("Name") for instance
        # To modify or create a attribute one can say for instance message.attrib.update({"Example": "Yes"})
        # If one tries to get an attribute which does not exist the return value will be None

        # Extract the payload element from the element tree objClsETreeXmlParserPar and append
        # it to message structure list.
        for objMessageElement in objClsETreeXmlParserPar.lstMessageElements:
            acMessageName = objMessageElement.get("Name")  # Get the name of the Message tag
            acRoles= objMessageElement.get("Roles")  # Get the list of roles
            # Add Headers To A List
            objElementHeaderTag = objMessageElement.findall("./Header")[0]  # Get the Header tag of the Message tag Element
            objElementHeaderTag.attrib.update({"Name": acMessageName})  # Put the name of the Message in the Header
            objElementHeaderTag.attrib.update({"Roles": acRoles})
            lstHeaderElements.append(objElementHeaderTag)  # Add this Header Element to a list of Header Elements

            # Add Payload To A List
            objCurrentPayloadElement = objMessageElement.findall("./Payload")[0]  # Get the Payload tag Element from the message
            lstPayloadElements = []
            # Note!!! because we only keep the payload and not the message itself we need to add certain attributes we actually comes from the message and not the payload
            objCurrentPayloadElement.attrib.update({"Name": acMessageName})  # Add the name of the Message to the Payload Element attrib dict
            objCurrentPayloadElement.attrib.update({"Roles": acRoles})

            # Create empty structure for a message with empty payload.
            # If a Payload Element contains no Field elements then it's empty
            if (not objCurrentPayloadElement.findall("./Field")):
                lstPayloadElements.append("/* NO PAYLOAD */")
                objCurrentPayloadElement.attrib.update({"PayloadBool": True})

            # Extract payload element for all messages with payloads.
            else:
                # If we are here then it means the Payload does have Field tag elements
                for objCurrentFieldElement in objCurrentPayloadElement.findall("./Field"):

                    if "Count" in objCurrentFieldElement.attrib:
                        if int(objCurrentFieldElement.get("Count")) > 1:
                            objCurrentFieldElement.attrib.update({"CountBool": True})
                        else:
                            objCurrentFieldElement.attrib.update({"CountBool": False})

                    else:
                        objCurrentFieldElement.attrib.update({"CountBool": False})

                    # First by default set the "bDefaultIsEnum" to False
                    objCurrentFieldElement.attrib.update({"bDefaultIsEnum": False})

                    # Check if the Type is in the global Struct list
                    if (objCurrentFieldElement.attrib["Type"] in G_dctPreparseTypedefStructs):
                        # Then it's a struct field
                        objCurrentFieldElement.attrib.update({"bDefaultIsEnum": False})
                    # Check if the Type is in the global Enum list
                    elif (objCurrentFieldElement.attrib["Type"] in G_dctPreparseTypedefEnums):
                        # Then it's an enum field
                        objCurrentFieldElement.attrib.update({"bDefaultIsEnum": True})
                    else:
                        # Then it must be a base type

                        objCurrentFieldElement.attrib.update({"bDefaultIsEnum": False})

                        if (objCurrentFieldElement.attrib["Type"] in ["CH", "ST"]):
                            objCurrentFieldElement.attrib.update({"bDefaultIsEnum": True})

                            if ("Default" in objCurrentFieldElement.attrib):
                                objCurrentFieldElement.attrib.update({"Default": "\"" + str(objCurrentFieldElement.attrib["Default"]) + "\""})
                            else:
                                objCurrentFieldElement.attrib.update({"Default": "\"" + "\""})

            lstPayloadElements.append(objCurrentPayloadElement)

            lstPayloadTagElements.append(objCurrentPayloadElement)
    # Gen Message struct's end
    # Gen Message struct's end
    # Gen Message struct's end

    # New code ADCS: Prepare the header for Jinja

    lstHeaderFields = lstPrepareMsgHeaderJinjaTemplateInfo(objElementHeaderTag)
    lstMessagePopulateFields = lstPrepareMessagePopulateJinjaTemplateInfo(lstHeaderFields, lstHeaderElements)

    # Build up a dictionary with information for the Jinja writers to use to fill in the template
    dctJinjaWriterInfo = {}
    dctJinjaWriterInfo["date"] = time.strftime("%A, %d %B %Y %Z %H:%M")  # We need this for python.message.define.j2
    dctJinjaWriterInfo["name"] = outFilename
    dctJinjaWriterInfo["acXmlSchemaFormat"] = str(objClsETreeXmlParserPar.eXmlFileSchemaType)
    dctJinjaWriterInfo["TypeDefElements"] = lstTypedefDictItemList  # A list of Dict Typedef items which can either be a 'enum' or a 'struct'
    dctJinjaWriterInfo["MessageStructs"] = lstPayloadTagElements  # a list of Element of 'Payload' tag type
    dctJinjaWriterInfo["MessageDictItems"] = lstMessagePopulateFields  # a list of Message dictionary items
    dctJinjaWriterInfo["Header"] = lstHeaderFields  # List of dictionary items - one dict for each field in the header
    dctJinjaWriterInfo["EnumTypes"] = G_dctEnumTypes
    dctJinjaWriterInfo["PyCCSTypes"] = acCcsTypesPythonFilePathPar
    dctJinjaWriterInfo["XmlIncludes"] = XmlIncludes
    dctJinjaWriterInfo["CoreTypes"] = G_dctXmlSchemaBaseTypes

    G_lstXmlFileContextDictionaries.append(dctJinjaWriterInfo)
    #logging.info("Output Directory: %s", str(objClsETreeXmlParserPar.acOutputGenerationPath))
    #logging.info("Calling the template writer for %s", objClsETreeXmlParserPar.acXmlFileNameOnly)
    template_writer(dctJinjaWriterInfo, os.path.join(objClsETreeXmlParserPar.acOutputGenerationPath, outFilename), acJinjaDefinitionTemplatePathPar)
    copyfile(acCcsTypesPythonFilePathPar, os.path.join(objClsETreeXmlParserPar.acOutputGenerationPath, os.path.basename(acCcsTypesPythonFilePathPar)))


def lstPrepareMsgHeaderJinjaTemplateInfo(objElementHeaderTagPar: object):
    """
    This is the public function to parse the Header ElementTree element for the jinja template

    Args:
        objElementHeaderTagPar (object): A ElementTree Element object of the "Header" tag

    Returns:
        (list): A list of strings for each field in the header.

    Raises:
        Raises no exception.

    """
    lstReturn = []
    acFieldName = ""
    acFieldBaseTypePrefix = ""
    acFieldType = ""
    acFieldDefault = ""
    acOneFieldFullDefSource = ""  # An example of what thus line become is -> self.u2MsgLength = CCS_Base('U2', 0)
    acOneFieldFullAddTypeSource = ""  # An example of what thus line become is -> self.AddType('u2MsgLength')
    lstAdcsHeaderFields = None
    dctEnumTypedef = {}

    # This dictionary with these keys will be added to the return list
    dctHeaderField = {}
    dctHeaderField["objElement"] = None
    dctHeaderField["acHeaderFullDefLine"] = str("")  # Used in the Header define Jinja section
    dctHeaderField["acHeaderAddTypeLine"] = str("")  # Used in the Header define Jinja section
    dctHeaderField["acHeaderFieldNamePrefix"] = str("")
    dctHeaderField["acHeaderFieldFullName"] = str("")
    dctHeaderField["acDefaultValue"] = str("")
    dctHeaderField["acHeaderFieldType"] = str("")

    if (objElementHeaderTagPar is None):
        return(lstReturn)

    lstAdcsHeaderFields = objElementHeaderTagPar.findall("./Field")

    if (not lstAdcsHeaderFields):
        return(lstReturn)

    for objElementField in lstAdcsHeaderFields:
        if ("Name" not in objElementField.attrib):
            logging.error("Name attribute missing from Element")
            continue

        acFieldName = objElementField.attrib["Name"]

        if ("Type" not in objElementField.attrib):
            logging.error("Type attribute missing from Element")
            continue

        acFieldType = objElementField.attrib["Type"]

        if (not acFieldType):
            logging.error("Field type cannot be empty")
            continue

        # Make a new dictionary item
        dctHeaderField = {}
        dctHeaderField["objElement"] = objElementField
        dctHeaderField["acHeaderFullDefLine"] = str("")
        dctHeaderField["acHeaderAddTypeLine"] = str("")
        dctHeaderField["acHeaderFieldNamePrefix"] = str("")
        dctHeaderField["acHeaderFieldFullName"] = str("")
        dctHeaderField["acDefaultValue"] = str("")
        dctHeaderField["acHeaderFieldType"] = str("")

        if (acFieldType in G_dctPreparseTypedefEnums):
            # Then this must be an approved enumeration
            dctEnumTypedef = G_dctPreparseTypedefEnums[acFieldType]

            dctHeaderField["acHeaderFieldFullName"] = dctEnumTypedef["acFieldPrefix"] + acFieldName

            acOneFieldFullDefSource = str("self.") + dctHeaderField["acHeaderFieldFullName"]
            acOneFieldFullDefSource += " = " + acFieldType

            # Get the default
            if ("Default" in objElementField.attrib):
                acFieldDefault = objElementField.attrib["Default"]

            if (acFieldDefault != ""):
                acOneFieldFullDefSource += "(" + acFieldType + "." + acFieldDefault + ")"
            else:
                acOneFieldFullDefSource += "(0)"

            # Build up the AddType source line
            acOneFieldFullAddTypeSource = "self.AddType('" + dctHeaderField["acHeaderFieldFullName"] +"')"

            dctHeaderField["acHeaderFullDefLine"] = acOneFieldFullDefSource
            dctHeaderField["acHeaderAddTypeLine"] = acOneFieldFullAddTypeSource
            dctHeaderField["acHeaderFieldNamePrefix"] = dctEnumTypedef["acFieldPrefix"]
            dctHeaderField["acDefaultValue"] = acFieldType + "." + acFieldDefault
            dctHeaderField["acHeaderFieldType"] = acFieldType

        elif (acFieldType in G_dctXmlSchemaBaseTypes):
            # This section is for base types (F4, F8, I1 etc.

            if (acFieldType not in G_dctXmlSchemaBaseTypeToPrefixLookup):
                logging.error("Field type %s unknown", acFieldType)
                continue

            # Get the default if there is one
            if ("Default" in objElementField.attrib):
                acFieldDefault = objElementField.attrib["Default"]
            else:
                # If there is no default attribute then we use the base type default
                acFieldDefault = G_dctXmlSchemaBaseTypesToDefaultValueLookup[acFieldType]

            acFieldBaseTypePrefix = G_dctXmlSchemaBaseTypeToPrefixLookup[acFieldType]

            dctHeaderField["acHeaderFieldFullName"] = acFieldBaseTypePrefix + acFieldName

            acOneFieldFullDefSource = str("self.") + dctHeaderField["acHeaderFieldFullName"]
            acOneFieldFullDefSource += " = " + "CCS_Base('" + acFieldType + "', " + acFieldDefault + ")"

            # Build up the AddType source line
            acOneFieldFullAddTypeSource = "self.AddType('" + dctHeaderField["acHeaderFieldFullName"] + "')"

            dctHeaderField["acHeaderFullDefLine"] = acOneFieldFullDefSource
            dctHeaderField["acHeaderAddTypeLine"] = acOneFieldFullAddTypeSource
            dctHeaderField["acHeaderFieldNamePrefix"] = acFieldBaseTypePrefix
            dctHeaderField["acDefaultValue"] = acFieldDefault
            dctHeaderField["acHeaderFieldType"] = acFieldType

        # Finally add the dictionary item to the list
        lstReturn.append(dctHeaderField)

    return(lstReturn)

def lstPrepareMessagePopulateJinjaTemplateInfo(lstOfHeaderFieldDictionariesPar: list, lstMessageTagElementsPar: list):
    """
    This is the public function to parse the ElementTree elements for all the Message tags in an XML file

    Args:
        lstOfHeaderFieldDictionariesPar (list): A list of header field dictionary items
        lstMessageTagElementsPar (list): A list of Message tag elements

    Returns:
        (list): Return value

    Raises:
        Raises no exception.

    """
    lstReturn = []  # This is a list of Messages as dictionary items
    lstAdcsHeaderFields = []
    acFieldName = str("")

    # Variables for Field tag processing
    dctEnumTypedef = {}
    acFieldType = str("")

    # New dictionary for a Message tag item
    dctMessage = {}
    dctMessage['lstFields'] = []
    dctMessage['acMsgName'] = str("")
    dctMessage['acMsgNameInPythonSource'] = str("")
    dctMessage['acRolesInPythonSource'] = str("")
    dctMessage['acMsgPayloadConstructSourceLine'] = str("")

    # Make a new dictionary for a Field tag item
    dctHeaderField = {}
    dctHeaderField["objElement"] = None
    dctHeaderField["acHeaderFieldNamePrefix"] = str("")
    dctHeaderField["acHeaderFieldFullName"] = str("")
    dctHeaderField["acDefaultValue"] = str("")
    dctHeaderField["acHeaderFieldType"] = str("")
    dctHeaderField["acMsgPopulateSourceLine"] = str("")

    if (not lstOfHeaderFieldDictionariesPar):
        return(lstReturn)

    if (not lstMessageTagElementsPar):
        return(lstReturn)

    for objMessageTagElement in lstMessageTagElementsPar:

        # We must make a new dictionary to indicate a new Message
        dctMessage = {}
        dctMessage['lstFields'] = []
        dctMessage['acMsgName'] = objMessageTagElement.attrib["Name"]
        dctMessage['acMsgNameInPythonSource'] = str("s") + objMessageTagElement.attrib["Name"] + "MsgCls"
        dctMessage['acRolesInPythonSource'] = objMessageTagElement.attrib["Roles"]
        dctMessage['acMsgPayloadConstructSourceLine'] = str("self.sPayload = s") + objMessageTagElement.attrib["Name"] + "_PL().lstRecords"

        lstAdcsHeaderFields = objMessageTagElement.findall("./Field")

        if (not lstAdcsHeaderFields):
            # Then it means there are now Fields in this header
            continue

        for objElementField in lstAdcsHeaderFields:

            # Make a new dictionary item
            dctHeaderField = {}
            dctHeaderField["objElement"] = objElementField
            dctHeaderField["acHeaderFieldNamePrefix"] = str("")
            dctHeaderField["acHeaderFieldFullName"] = str("")
            dctHeaderField["acDefaultValue"] = str("")
            dctHeaderField["acHeaderFieldType"] = str("")
            dctHeaderField["acMsgPopulateSourceLine"] = str("")

            if ("Name" not in objElementField.attrib):
                logging.error("Name attribute missing from Element")
                continue

            acFieldName = objElementField.attrib["Name"]

            if ("Type" not in objElementField.attrib):
                logging.error("Type attribute missing from Element")
                continue

            acFieldType = objElementField.attrib["Type"]

            if (not acFieldType):
                logging.error("Field type cannot be empty")
                continue

            if (acFieldType in G_dctPreparseTypedefEnums):
                # Then this must be an approved enumeration
                dctEnumTypedef = G_dctPreparseTypedefEnums[acFieldType]

                dctHeaderField["acHeaderFieldFullName"] = dctEnumTypedef["acFieldPrefix"] + acFieldName

                # Get the default
                if ("Default" in objElementField.attrib):
                    acFieldDefault = objElementField.attrib["Default"]

                dctHeaderField["acHeaderFieldNamePrefix"] = dctEnumTypedef["acFieldPrefix"]
                dctHeaderField["acDefaultValue"] = acFieldType + "." + acFieldDefault
                dctHeaderField["acHeaderFieldType"] = acFieldType

            elif (acFieldType in G_dctXmlSchemaBaseTypes):
                # This section is for base types (F4, F8, I1 etc.

                if (acFieldType not in G_dctXmlSchemaBaseTypeToPrefixLookup):
                    logging.error("Field type %s unknown", acFieldType)
                    continue

                # Get the default if there is one
                if ("Default" in objElementField.attrib):
                    acFieldDefault = objElementField.attrib["Default"]
                else:
                    # If there is no default attribute then we use the base type default
                    acFieldDefault = G_dctXmlSchemaBaseTypesToDefaultValueLookup[acFieldType]

                acFieldBaseTypePrefix = G_dctXmlSchemaBaseTypeToPrefixLookup[acFieldType]

                dctHeaderField["acHeaderFieldFullName"] = acFieldBaseTypePrefix + acFieldName

                dctHeaderField["acHeaderFieldNamePrefix"] = acFieldBaseTypePrefix
                dctHeaderField["acDefaultValue"] = acFieldDefault
                dctHeaderField["acHeaderFieldType"] = acFieldType

            # We need to build up the string which will be used to initialise the header fields
            dctHeaderField["acMsgPopulateSourceLine"] = "self.sMsgHeader." + dctHeaderField["acHeaderFieldFullName"] + ".Value = "
            dctHeaderField["acMsgPopulateSourceLine"] += dctHeaderField["acDefaultValue"]

            # Add the Field to the list of Fields in the Message
            dctMessage['lstFields'].append(dctHeaderField)

        lstReturn.append(dctMessage)

    return(lstReturn)



# =====================================
# Module main function
# =====================================


def main(acConfigFilePar="autogen_python_config.ini", acWorkDirPathPar=None):
    """
    This is the Main method. It is called after some basic argument and ini file checks were done and passed

    Args:
        acConfigFilePar (str): Path to config file. The default path is "./Autogen_FileTypedefs_Config.ini" which contains default config values. For message ID's the config file needs a "Paths" section which contains "xml_path", "autogen_output_path" and "template_path".
        acWorkDirPathPar (str): The second parameter, the current working directory

    Returns:

    Raises:
        Raises no exception.

    """

    # Function variables
    lstXmlPaths = []    # Stores the paths of the XML files which will read
    lstXmlPathsPlusPrimaryInfo = []  # Stores a list of dictionaries containing the XML paths plus if they are primary
    acAutogenPath = str("")  # The path where the generated code will saved to
    acTemplatePath = str("")  # The path of the jinja template for the message definition generation
    acCcsTypesPath = str("")  # The path of where the CCS base class is located
    acSystemId = str("")  # We store a string which represents the system e.g. BR12
    bIniParsedSuccess = bool(False)  # A flag which indicates if the INI file was read correctly
    eXmlFileSchemaFormat = E_XML_FILE_SCHEMA_FORMAT_TYPE(E_XML_FILE_SCHEMA_FORMAT_TYPE.XML_FILE_SCHEMA_FORMAT_ADCS)  # Just make ADCS for now

    #logging.info("Attempting to read INI file with absolute path " + os.path.join(acWorkDirPathPar, acConfigFilePar))

    try:
        with open(os.path.join(acWorkDirPathPar, acConfigFilePar), 'r') as cfp:
            G_objConfigParser.read_file(cfp)
        cfp.close()
        #logging.info("INI file read successfully")
    except Exception as E:
        logging.error(str(E))

    try:
        # Test if the [System] section is there
        if(G_objConfigParser.has_section("System") is True):
            #logging.info("INI file section [System] is present")
            pass
        else:
            logging.error("INI file section [System] is missing")
            sys.exit()

        if (G_objConfigParser.has_option("System", "system") is True):
            #logging.info("INI file option system in section [System] is present")
            pass
        else:
            logging.error("INI file option system in section [System] is missing")
            sys.exit()

        if (G_objConfigParser.has_option("System", "schema_format") is True):
            #logging.info("INI file option schema_format in section [System] is present")
            pass
        else:
            logging.error("INI file option schema_format in section [System] is missing")
            sys.exit()

        # Now check if the schema_format is valid

        if (G_objConfigParser.get("System", "schema_format") not in ["BR12", "ADCS"]):
            logging.error("INI file option schema_format in section [System] must be BR12 or ADCS")
            sys.exit()

        if (G_objConfigParser.get("System", "schema_format") == "ADCS"):
            eXmlFileSchemaFormat = E_XML_FILE_SCHEMA_FORMAT_TYPE(E_XML_FILE_SCHEMA_FORMAT_TYPE.XML_FILE_SCHEMA_FORMAT_ADCS)
        else:
            eXmlFileSchemaFormat = E_XML_FILE_SCHEMA_FORMAT_TYPE(E_XML_FILE_SCHEMA_FORMAT_TYPE.XML_FILE_SCHEMA_FORMAT_BR12)

        if(G_objConfigParser.has_section("Paths") is True):
            #logging.info("INI file section [Paths] is present")
            pass
        else:
            logging.error("INI file section [Paths] is missing")
            sys.exit()

        if (G_objConfigParser.has_option("Paths", "xml_path") is True):
            #logging.info("INI file option xml_path in section [Paths] is present")
            pass
        else:
            logging.error("INI file option xml_path in section [Paths] is missing")
            sys.exit()

        if (G_objConfigParser.has_option("Paths", "autogen_output_path") is True):
            #logging.info("INI file option autogen_output_path in section [Paths] is present")
            pass
        else:
            logging.error("INI file option autogen_output_path in section [Paths] is missing")
            sys.exit()

        # Message definition (CCS_Types based) jinja path
        if (G_objConfigParser.has_option("Paths", "template_message_define_path") is True):
            pass
            #logging.info("INI file option template_message_define_path in section [Paths] is present")
        else:
            logging.error("INI file option template_message_define_path in section [Paths] is missing")
            sys.exit()

        # OPTIONAL!!! Database template jinja path - OPTIONAL!!! do not exit if not present
        if (G_objConfigParser.has_option("Paths", "template_message_processing_database_path") is True):
            pass
            #logging.info("INI file option template_message_processing_database_path in section [Paths] is present")
        else:
            pass
            # logging.error("INI file option template_message_processing_database_path in section [Paths] is missing")

        # The CCS_Types.py file path
        if (G_objConfigParser.has_option("Paths", "py_types_path") is True):
            pass
            #logging.info("INI file option py_types_path in section [Paths] is present")
        else:
            logging.error("INI file option py_types_path in section [Paths] is missing")
            sys.exit()

    except Exception as E:
        logging.error(str(E))

    # MANDATORY FIELDS!!!
    #logging.info("[System].system                                    -> %s", G_objConfigParser.get("System", "system"))
    #logging.info("[System].schema_format                             -> %s", G_objConfigParser.get("System", "schema_format"))
    #logging.info("[Paths].xml_path                                   -> %s", G_objConfigParser.get("Paths", "xml_path"))
    #logging.info("[Paths].autogen_output_path                        -> %s", G_objConfigParser.get("Paths", "autogen_output_path"))
    #logging.info("[Paths].template_message_define_path               -> %s", G_objConfigParser.get("Paths", "template_message_define_path"))
    #logging.info("[Paths].py_types_path                              -> %s", G_objConfigParser.get("Paths", "py_types_path"))

    # OPTIONAL FIELDS!!!
    if (G_objConfigParser.has_option("Paths", "template_message_processing_database_path") is True):
        #logging.info("[Paths].template_message_processing_database_path  -> %s", G_objConfigParser.get("Paths", "template_message_processing_database_path"))
        pass
    try:
        lstXmlPathsPlusPrimaryInfo = json.loads(G_objConfigParser.get("Paths", "xml_path"))
    except Exception as E:
        logging.error("Could not parse JSON string used for [Paths]->xml_path - " + str(E))
        sys.exit()

    # Iterate through the JSON source dictionary and verify that all the fields required are there
    for dctItem in lstXmlPathsPlusPrimaryInfo:
        if ("acPath" not in dctItem):
            logging.error("One of the xml_path JSON items is missing the \"acPath\" field")
            sys.exit()

    try:
        with open(os.path.join(acWorkDirPathPar, acConfigFilePar), 'r') as cfp:
            # G_objConfigParser.read_file(cfp)

            lstXmlPaths = []
            # Join the relative path with the working directory path
            for xml_file in [x["acPath"] for x in lstXmlPathsPlusPrimaryInfo]:
                lstXmlPaths.append(os.path.abspath(os.path.join(acWorkDirPathPar, xml_file)))

            # MANDATORY FILE PATH JOIN
            acAutogenPath = os.path.abspath(os.path.join(acWorkDirPathPar, G_objConfigParser.get("Paths", "autogen_output_path")))
            acTemplatePath = os.path.abspath(os.path.join(acWorkDirPathPar, G_objConfigParser.get("Paths", "template_message_define_path")))
            acCcsTypesPath = os.path.abspath(os.path.join(acWorkDirPathPar, G_objConfigParser.get("Paths", "py_types_path")))
            acSystemId = G_objConfigParser.get("System", "system")

            bIniParsedSuccess = True

    except ConfigParser.NoOptionError as E:
        logging.error("Config file error, make sure all Config variables are correctly named.\n\tDir:" + os.path.curdir() + "\n\tErr:" + str(E.message))
    except FileNotFoundError as E:
        logging.error("Config file error, file not found.\n\tDir:" + os.getcwd() + "\n\tErr:" + str(E))
    except Exception as E:
        logging.error(str(E))

    if (os.path.exists(acAutogenPath) is False):
        logging.error("The file " + acAutogenPath + " does not exist")
        sys.exit()
    else:
        #logging.info("Found " + acAutogenPath)
        pass
    if (os.path.exists(acCcsTypesPath) is False):
        logging.error("The file " + acCcsTypesPath + " does not exist")
        sys.exit()
    else:
        pass
        #logging.info("Found " + acCcsTypesPath)

    if (os.path.exists(acTemplatePath) is False):
        logging.error("The file " + acTemplatePath + " does not exist")
        sys.exit()
    else:
        pass
        #logging.info("Found " + acTemplatePath)

    if (bIniParsedSuccess is False):
        logging.error("The INI file could not be parsed correctly")
        sys.exit()

    if (len(acSystemId) <= 0):
        logging.error("The system id cannot be undefined")
        sys.exit()

    for acXmlPath in lstXmlPaths:
        if (os.path.isfile(acXmlPath.strip()) is False):
            logging.error("File " + acXmlPath.strip() + " does not exist")
            sys.exit()
        else:
            pass
            #logging.info("Found XML file " + acXmlPath.strip())

    for acXmlPath in lstXmlPaths:
        try:
            # From the lxml library use etree to validate the XML files for syntax errors
            etree.parse(acXmlPath)  # pylint: disable=E1101
            #logging.info("etree validation passed for " + acXmlPath)
        except Exception as E:
            logging.error("XML parse error -> " + str(E))
            sys.exit()

    # We will use this counter to derefence the JSON dictionary which came from the INI to get the parameters of each XML file
    iFilePathListCounter = 0

    for acXmlPath in lstXmlPaths:
        dctXmlJsonDictionary = lstXmlPathsPlusPrimaryInfo[iFilePathListCounter]

        if os.path.isfile(acXmlPath.strip()):
            #logging.info("Now Element tree parsing file %s", acXmlPath.strip())
            objClsETreeXmlParser = clsETreeXmlParser(acXmlPath.strip(), acAutogenPath, eXmlFileSchemaFormat, True)

            # In the future if one wants to process included XMLs, one can see if list "objClsETreeXmlParser.lstIncludedXmlFiles"
            if objClsETreeXmlParser.lstIncludedXmlFiles:
                # The last argument being passed in here is the recursion level. This is the main method so it's always 0 here.
                autogen_typedef_py(objClsETreeXmlParser, acTemplatePath, acCcsTypesPath, dctXmlJsonDictionary, 0)
            else:
                # The last argument being passed in here is the recursion level. This is the main method so it's always 0 here.
                autogen_typedef_py(objClsETreeXmlParser, acTemplatePath, acCcsTypesPath, dctXmlJsonDictionary, 0)
        else:
            logging.error("Error with path to xml file: " + acXmlPath)
            sys.exit()

        iFilePathListCounter += 1   # Increase the counter

    # This function generates the MQTT autogen template based on the Jinja file
    #logging.info("Now generating MQTT template and also message processing class")

    return


# =====================================
# Module main
# =====================================


if __name__ == "__main__":
    """
    This is the python module which autogens the XML into Python code

    Example:
        python autogen_python.py INI_FILE_WITH_RELATIVE_PATH

    Args:
        sys.argv[0] (str): The first parameter is the is the file path of the python file which was run
        sys.argv[1] (str): The second parameter. Must be the relative path of the autogen INI file
    """

    # Main variables
    acCurrentDirectory = str("")
    fPythonVersion = float(0.0)

    objRootLogger = logging.getLogger()  # Get the logger instance
    acLoggingFormatStr = str("%(asctime)s,%(filename)s,%(lineno)d,%(levelname)s,%(message)s")
    objLogFormatter = logging.Formatter(acLoggingFormatStr)

    # Immediately start the logger
    # We log datetime, filename, line number and message
    # Open the file in append mode so that we don't lose the hostory
    logging.basicConfig(format=acLoggingFormatStr,
                        datefmt='%Y/%m/%d %H:%M:%S',
                        filename='logging.log',
                        filemode='a',
                        level=logging.DEBUG)

    # Configure the logger to also log to stdout
    objConsoleHandler = logging.StreamHandler()
    objConsoleHandler.setFormatter(objLogFormatter)
    objRootLogger.addHandler(objConsoleHandler)

    # Indicate that the logging has started
    #logging.info("======================================================")
    #logging.info("= AUTOGEN                                            =")
    #logging.info("======================================================")

    #logging.info("Python version is [major] %d ", sys.version_info[0])
    #logging.info("Python version is [minor] %d ", sys.version_info[1])

    # Build up a python version number as a float
    fPythonVersion = float(sys.version_info[0]) + (float(sys.version_info[1])/10.0)

    if (fPythonVersion < 3.6):
        logging.error("Python version must be 3.6 or higher")
        sys.exit()

    #logging.info("Autogen started")
    #logging.info("sys.argv is " + str(sys.argv))
    # Get the current directory
    acCurrentDirectory = os.getcwd()
    #logging.info("The current directory is " + str(acCurrentDirectory))

    # Verify that the correct number of CLI args were passed
    if (len(sys.argv) != 2):
        logging.error("The number of command line arguments passed are invalid")
        logging.error("example -> python autogen_python INI_FILE_RELATIVE_PATH")
        sys.exit()

    # Verify that the ini file exists
    if (os.path.exists(sys.argv[1]) is False):
        logging.error("Autogen INI file does not exist.")
        sys.exit()
    else:
        #logging.info("The Autogen INI was found")
        pass
    # Now execute the main function - this is how the WebMM needs the path to be
    main(acWorkDirPathPar=acCurrentDirectory+"/Codegen/Codegen_Python/")

    # To debug the autogen alone uncomment the code below and comment out the line above so that the path is as is
    # main(acConfigFilePar=sys.argv[1], acWorkDirPathPar=acCurrentDirectory)

    #logging.info("Autogen complete")
