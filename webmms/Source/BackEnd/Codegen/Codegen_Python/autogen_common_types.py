import xml.etree.ElementTree as ET
import sys, os, json
import logging

G_dctADCS_common_types = dict()
def vGetCommonTypes():
    """
        Autogen common types and get all enums
        
        Args:
            
        Returns:
            
        Raises:
            Raises no exceptions
    """
    acPathToSICD = os.path.join(os.path.dirname(__file__), "../../SICD/")
    lstFiles = os.listdir(acPathToSICD)

    for i in range(len(lstFiles)):
        if lstFiles[i][-10:] == "_Types.xml":
            try:
                acTree = ET.parse(os.path.join(os.path.dirname(__file__),"../../SICD/"+lstFiles[i]))
                objRoot = acTree.getroot()
                for objTypedef in objRoot:
                    if objTypedef.tag == 'Typedef':
                        if objTypedef.attrib['Name'][:1] != 's':
                            G_dctADCS_common_types[objTypedef.attrib['Name']] = dict()
                            for objRecord in objTypedef:
                                if objRecord.tag == 'Record':
                                    G_dctADCS_common_types[objTypedef.attrib['Name']][objRecord.attrib['Name']] = dict()
                                    for objEnum in objRecord:
                                        if objEnum.tag== 'Enumeration':
                                            G_dctADCS_common_types[objTypedef.attrib['Name']][objRecord.attrib['Name']].update({objEnum.attrib['Name']: objEnum.attrib['Value']})
            except Exception as E:
                logging.error("Error getting enums from Type xmls, error -> %s", E)