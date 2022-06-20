import xml.etree.ElementTree as ET
import os
import json
import logging


class clsGetIsDatabaseMessages:
    """
        This class declares all functions that will be used for auto Scripting
        Args:

    """
    def __init__(self):
        self.G_dctADCS_common_types = dict()
        self.G_dctDatabaseMessages = dict()
        self.G_lstTypeDict = ['ST', 'CH', 'I1', 'I2', 'I4', 'I8', 'U1', 'U2', 'U4', 'U8', 'F4', 'F8']
        self.G_dctTypeDict = {'ST': "ac", 'CH': "ac", 'I1': "i1", 'I2': "i2", 'I4': "i4", 'I8': "i8", 'U1': "u1", 'U2': "u2", 'U4': "u4", 'U8': "u8", 'F4': "f4", 'F8': "f8", 'E1': "e1", 'E2': "e2"}
        self.G_dctTypeValues = {'ST': "", 'CH': "", 'I1': 0, 'I2': 0, 'I4': 0, 'I8': 0, 'U1': 0, 'U2': 0, 'U4': 0, 'U8': 0, 'F4': 0.0, 'F8': 0.0}
        self.G_dctEnumToBaseType = {'E1': "U1", 'E2': "U2"}
        self.G_dctTypeFileName = dict()
        self.G_lstIntegers = ['I1', 'I2', 'I4', 'I8', 'U1', 'U2', 'U4', 'U8']
        self.G_lstFloats = ['F4', 'F8']
        self.G_dctEnumValues = dict()

    def vGetCommonTypes(self):
        """
            get all common type files and pass to vGenerateCommonTypes
            Args:
                
            Returns:
                
            Raises:
                Raises no exceptions
        """
        acPathToSICD = os.path.join(os.path.dirname(__file__), "../SICD/")
        lstFiles = os.listdir(acPathToSICD)

        for i in range(len(lstFiles)):
            acFileName = str(lstFiles[i])
            if 'common_types'.lower() in acFileName.lower():
                try:
                    acTree = ET.parse(os.path.join(os.path.dirname(__file__), "../SICD/" + lstFiles[i]))
                    objRoot = acTree.getroot()
                    acFileName = "Autogen." + lstFiles[i][:-4].lower()
                    self.vGenerateCommonTypes(acFileName, objRoot)
                except Exception as E:
                    logging.error("Error getting enums from adcs_common_types.xml, error -> %s", E)

    def vGenerateCommonTypes(self, acFileNamePar, objRootPar):
        """
            Autogen common types, get all enums and and structures and store in to a global dictionary
            Args:
                
            Returns:
                
            Raises:
                Raises no exceptions
        """
        for objTypedef in objRootPar:
            if objTypedef.tag == 'Typedef':
                # check if the attribute is an Enum or Structure
                if objTypedef.attrib['Name'][:1] == 'E':
                    # Store the enum name with the file name for later reference to a global dictionary
                    self.G_dctTypeFileName.update({objTypedef.attrib['Name']: acFileNamePar})
                    for objRecord in objTypedef:
                        if objRecord.tag == 'Record':
                            # Add all enums to a dictionary, with the enum type, enum name and value
                            self.G_dctEnumValues.update({objTypedef.attrib['Name']: {}})
                            dctEnums = dict()
                            for objEnum in objRecord:
                                if objEnum.tag == "Enumeration":
                                    dctEnums.update({objEnum.attrib['Name']: objEnum.attrib["Value"]})
                            self.G_dctEnumValues[objTypedef.attrib['Name']].update({"enums": dctEnums, "Type": objRecord.attrib["Type"]})

                elif objTypedef.attrib['Name'][:1] == 's':
                    self.G_dctADCS_common_types[objTypedef.attrib['Name']] = dict({"Attr": {}})
                    self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"] = list()
                    self.G_dctTypeFileName.update({objTypedef.attrib['Name']: acFileNamePar})
                    objIndex = 0
                    # Loop through the object to get all records
                    for objRecord in objTypedef:
                        self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"].append(dict())
                        if objRecord.tag == 'Record':
                            # If the tag name of is 'Record', read its attribute "Name, Type, Default, count, value, min value, max value ..."
                            if "Name" in objRecord.attrib:
                                self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Name": objRecord.attrib["Name"]})
                            if "Type" in objRecord.attrib:
                                self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Type": acFileNamePar + "." + objRecord.attrib["Type"]})
                                # Check if "Type" if of base type, enum or structure
                                if objRecord.attrib["Type"] in self.G_lstTypeDict:
                                    self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Name": self.G_dctTypeDict[objRecord.attrib["Type"]] + objRecord.attrib["Name"]})
                                    self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Type": "Autogen.adcs_base_types.clsAdcsBaseType"})
                                    self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"acBaseType": objRecord.attrib["Type"]})
                                    if objRecord.attrib["Type"] == "CH" or objRecord.attrib["Type"] == "ST":
                                        self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"acBaseType": objRecord.attrib["Type"] + ":" + objRecord.attrib["Count"]})

                                    if "Default" in objRecord.attrib:
                                        self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Value": objRecord.attrib["Default"]})
                                        if objRecord.attrib["Type"] in self.G_lstIntegers:
                                            self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Value": int(str(objRecord.attrib["Default"]), 0)})
                                        elif objRecord.attrib["Type"] in self.G_lstFloats:
                                            self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Value": float(objRecord.attrib["Default"])})
                                    else:
                                        self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Value": self.G_dctTypeValues[objRecord.attrib["Type"]]})
                                        if objRecord.attrib["Type"] in self.G_lstIntegers:
                                            self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Value": int(str(self.G_dctTypeValues[objRecord.attrib["Type"]]), 0)})
                                        elif objRecord.attrib["Type"] in self.G_lstFloats:
                                            self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Value": float(self.G_dctTypeValues[objRecord.attrib["Type"]])})

                                elif objRecord.attrib["Type"][:1] == 'E':
                                    enumType = objRecord.attrib["Type"].split("_")[0]
                                    self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Name": self.G_dctTypeDict[enumType] + objRecord.attrib["Name"]})
                                    self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"acBaseType": self.G_dctEnumToBaseType[enumType]})

                                elif objRecord.attrib["Type"][:1] == 's':
                                    self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Name": "s" + objRecord.attrib["Name"]})
                                    self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Type": acFileNamePar + "." + objRecord.attrib["Type"]})
                                
                            if "Default" in objRecord.attrib:
                                self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Value": objRecord.attrib["Default"]})

                                if objRecord.attrib["Type"] in self.G_lstIntegers:
                                    self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Value": int(str(objRecord.attrib["Default"]), 0)})
                                elif objRecord.attrib["Type"] in self.G_lstFloats:
                                    self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Value": float(objRecord.attrib["Default"])})

                                if objRecord.attrib["Type"][:1] == 'E':
                                    if objRecord.attrib["Type"] in self.G_dctEnumValues:
                                        enumVal = int(str(self.G_dctEnumValues[objRecord.attrib["Type"]]["enums"][objRecord.attrib["Default"]]), 0)
                                        self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Value": enumVal})
                                    else:
                                        self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Value": 0})

                            if "Count" in objRecord.attrib:
                                if "UseStruct" not in objRecord.attrib:
                                    self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"iBaseTypeCount": int(str(objRecord.attrib["Count"]), 0)})

                            elif objRecord.attrib["Type"][:1] != 's':
                                self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"iBaseTypeCount": 1})

                            if "Min" in objRecord.attrib:
                                if "Default" not in objRecord.attrib and "Max" not in objRecord.attrib:
                                    if objRecord.attrib["Type"] in self.G_lstIntegers:
                                        self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Value": int(str(objRecord.attrib["Min"]), 0)})
                                    elif objRecord.attrib["Type"] in self.G_lstFloats:
                                        self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Value": float(objRecord.attrib["Min"])})
                            if "Max" in objRecord.attrib:
                                if "Default" not in objRecord.attrib:
                                    if objRecord.attrib["Type"] in self.G_lstIntegers:
                                        self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Value": int(str(objRecord.attrib["Max"]), 0)})
                                    elif objRecord.attrib["Type"] in self.G_lstFloats:
                                        self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Value": float(objRecord.attrib["Max"])})

                            # if the Record is of struct type, get the count if exist and repeat the structure 'Count' times else get the structure as it is.
                            if "UseStruct" in objRecord.attrib:
                                if objRecord.attrib["UseStruct"] == "True":
                                    if "Count" in objRecord.attrib and int(objRecord.attrib["Count"]) > 1:
                                        self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Name": "as" + objRecord.attrib["Name"]})
                                        self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Type": "Autogen.adcs_base_types.clsAdcsStructArrayType"})
                                        self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Attr": {"Attr": list()}})
                                        for structCount in range(int(objRecord.attrib["Count"])):
                                            if objRecord.attrib['Type'] in self.G_dctADCS_common_types:
                                                self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex]["Attr"]["Attr"].append({"Attr": list()})
                                                self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex]["Attr"]["Attr"][structCount]["Attr"].append(self.G_dctADCS_common_types[objRecord.attrib['Type']])

                                                self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex]["Attr"]["Attr"][structCount].update({"Name": "Autogen.adcs_base_types.clsAdcsStructArrayType" + str(structCount)})
                                                self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex]["Attr"]["Attr"][structCount].update({"Type": self.G_dctTypeFileName[objRecord.attrib["Type"]] + "." + objRecord.attrib["Type"]})

                                    else:
                                        if objRecord.attrib['Type'] in self.G_dctADCS_common_types:
                                            self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Attr": self.G_dctADCS_common_types[objRecord.attrib['Type']]})

                            else:
                                self.G_dctADCS_common_types[objTypedef.attrib['Name']]["Attr"][objIndex].update({"Attr": None})
  
                        objIndex += 1

    def vGetAllMessages(self, acDatabaseFileNamePar):
        """
            This function reads the message def files and get the message payload
            Args:

            Returns:

            Raises:
                Raises no exceptions
        """
        acPathToSICD = os.path.join(os.path.dirname(__file__), "../SICD/")
        lstFiles = os.listdir(acPathToSICD)
        for i in range(len(lstFiles)):
            if lstFiles[i][-10:] != "_Types.xml" and lstFiles[i] != ".gitignore" and lstFiles[i][-4:] == ".xml":
                try:
                    acTree = ET.parse(os.path.join(os.path.dirname(__file__), "../SICD/" + lstFiles[i]))
                    objRoot = acTree.getroot()
                    if objRoot.tag == "MessageFile":
                        for objMessageFile in objRoot:
                            if objMessageFile.tag == "Section":
                                if "struct" not in objMessageFile.attrib["Name"]:
                                    for objMessages in objMessageFile:
                                        # Only get isDatabase messages
                                        if objMessages.tag == "Message" and "IsDatabaseMsg" in objMessages.attrib:
                                            self.G_dctDatabaseMessages.update({objMessages.attrib["Name"]: {}})
                                            self.G_dctDatabaseMessages[objMessages.attrib["Name"]].update({"acMessageName": objMessages.attrib["Name"], "dctMessagePayload": {"Attr": []}})
                                            for objPayload in objMessages:
                                                if objPayload.tag == "Payload":
                                                    for objField in objPayload:
                                                        if objField.tag == "Field":
                                                            dctFieldAttr = dict()
                                                            if "Name" in objField.attrib:
                                                                dctFieldAttr["Name"] = objField.attrib["Name"]
                                                            if "Type" in objField.attrib:
                                                                dctFieldAttr["Type"] = objField.attrib["Type"]
                                                                if objField.attrib["Type"] in self.G_lstTypeDict:
                                                                    dctFieldAttr["Name"] = self.G_dctTypeDict[objField.attrib["Type"]] + objField.attrib["Name"]
                                                                    dctFieldAttr["Type"] = "Autogen.adcs_base_types.clsAdcsBaseType"
                                                                    dctFieldAttr["acBaseType"] = objField.attrib["Type"]
                                                                    if "Default" in objField.attrib:
                                                                        dctFieldAttr["Value"] = (objField.attrib["Default"])
                                                                        if objField.attrib["Type"] in self.G_lstIntegers:
                                                                            dctFieldAttr["Value"] = int(str(objField.attrib["Default"]), 0)
                                                                        elif objField.attrib["Type"] in self.G_lstFloats:
                                                                            dctFieldAttr["Value"] = float(objField.attrib["Default"])

                                                                    else:
                                                                        dctFieldAttr["Value"] = 0
                                                                        if objField.attrib["Type"] in self.G_lstIntegers:
                                                                            dctFieldAttr["Value"] = 0
                                                                        elif objField.attrib["Type"] in self.G_lstFloats:
                                                                            dctFieldAttr["Value"] = 0.0
                                                                else:
                                                                    dctFieldAttr["Name"] = "s" + objField.attrib["Name"]

                                                                    if objField.attrib["Type"] in self.G_dctTypeFileName:
                                                                        dctFieldAttr["Type"] = self.G_dctTypeFileName[objField.attrib["Type"]] + "." + objField.attrib["Type"]
                                                                    else:
                                                                        dctFieldAttr["Type"] = objField.attrib["Type"]

                                                                    if objField.attrib["Type"][:1] == "E":
                                                                        fieldType = objField.attrib["Type"].split("_")[0]
                                                                        if fieldType in self.G_dctEnumToBaseType:
                                                                            dctFieldAttr["Name"] = self.G_dctTypeDict[fieldType] + objField.attrib["Name"]
                                                                            baseType = "U" + fieldType[1:]
                                                                            dctFieldAttr["acBaseType"] = baseType
                                                            if "Default" in objField.attrib:
                                                                dctFieldAttr["Value"] = objField.attrib["Default"]
                                                                if objField.attrib["Type"] in self.G_lstIntegers:
                                                                    dctFieldAttr["Value"] = int(str(objField.attrib["Default"]), 0)
                                                                elif objField.attrib["Type"] in self.G_lstFloats:
                                                                    dctFieldAttr["Value"] = float(objField.attrib["Default"])

                                                                if objField.attrib["Type"][:1] == 'E':
                                                                    if objField.attrib["Type"] in self.G_dctEnumValues:
                                                                        iEnumVal = int(str(self.G_dctEnumValues[objField.attrib["Type"]]["enums"][objField.attrib["Default"]]), 0)
                                                                        dctFieldAttr["Value"] = iEnumVal

                                                            if "Count" in objField.attrib and "UseStruct" not in objField.attrib:
                                                                dctFieldAttr["iBaseTypeCount"] = int(str(objField.attrib["Count"]), 0)
                                                            else:
                                                                if objField.attrib["Type"] in self.G_lstTypeDict and "UseStruct" not in objField.attrib:
                                                                    dctFieldAttr["iBaseTypeCount"] = 1
                                                                elif objField.attrib["Type"][:1] == "E":
                                                                    fieldType = objField.attrib["Type"].split("_")[0]
                                                                    if fieldType in self.G_dctEnumToBaseType:
                                                                        dctFieldAttr["iBaseTypeCount"] = 1

                                                            if "Min" in objField.attrib:
                                                                if "Default" not in objField.attrib and "Max" not in objField.attrib:
                                                                    if objField.attrib["Type"] in self.G_lstIntegers:
                                                                        dctFieldAttr["Value"] = int(str(objField.attrib["Min"]), 0)
                                                                    elif objField.attrib["Type"] in self.G_lstFloats:
                                                                        dctFieldAttr["Value"] = float(objField.attrib["Min"])

                                                            if "Max" in objField.attrib:
                                                                if "Default" not in objField.attrib:
                                                                    if objField.attrib["Type"] in self.G_lstIntegers:
                                                                        dctFieldAttr["Value"] = int(str(objField.attrib["Max"]), 0)
                                                                    elif objField.attrib["Type"] in self.G_lstFloats:
                                                                        dctFieldAttr["Value"] = float(objField.attrib["Max"])
                                                            if "UseStruct" in objField.attrib:
                                                                if objField.attrib["UseStruct"] == "True":
                                                                    dctFieldAttr["Attr"] = dict()
                                                                    dctFieldAttr["Name"] = "s" + objField.attrib["Name"]
                                                                    dctFieldAttr["Type"] = self.G_dctTypeFileName[objField.attrib["Type"]] + "." + objField.attrib['Type']
                                                                    if "Count" in objField.attrib:
                                                                        dctFieldAttr["Attr"].update({"Attr": list()})
                                                                        dctFieldAttr["Name"] = "as" + objField.attrib["Name"]
                                                                        dctFieldAttr["Type"] = "Autogen.adcs_base_types.clsAdcsStructArrayType"
                                                                        for structCount in range(int(objField.attrib["Count"])):
                                                                            if objField.attrib['Type'] in self.G_dctADCS_common_types:
                                                                                dctFieldAttr["Attr"]["Attr"].append({"Attr": list()})
                                                                                dctFieldAttr["Attr"]["Attr"][structCount]["Attr"].append(self.G_dctADCS_common_types[objField.attrib['Type']])
                                                                                dctFieldAttr["Attr"]["Attr"][structCount].update({"Name": "Autogen.adcs_base_types.clsAdcsStructArrayType" + str(structCount)})
                                                                                dctFieldAttr["Attr"]["Attr"][structCount].update({"Type": self.G_dctTypeFileName[objField.attrib["Type"]] + "." + objField.attrib["Type"]})
                                                                    else:
                                                                        if objField.attrib['Type'] in self.G_dctADCS_common_types:
                                                                            dctFieldAttr["Attr"] = self.G_dctADCS_common_types[objField.attrib['Type']]
                                                                        else:
                                                                            dctFieldAttr.update({"Attr": None})
                                                            else:
                                                                dctFieldAttr.update({"Attr": None})

                                                            self.G_dctDatabaseMessages[objMessages.attrib["Name"]]["dctMessagePayload"]["Attr"].append(dctFieldAttr)

                                elif "enumerations" not in objMessageFile.attrib["Name"] and "Enum" not in objMessageFile.attrib["Name"] and "struct" in objMessageFile.attrib["Name"]:
                                    self.vGenerateCommonTypes("", objMessageFile)

                except Exception as E:
                    logging.error("error -> %s", E)

        with open(os.path.join(os.path.dirname(__file__), "../databaseFiles/" + acDatabaseFileNamePar + ".json"), 'w') as f:
            f.write(json.dumps({"factory": self.G_dctDatabaseMessages, "operational": {}}, indent=1, sort_keys=True))
            f.close()
