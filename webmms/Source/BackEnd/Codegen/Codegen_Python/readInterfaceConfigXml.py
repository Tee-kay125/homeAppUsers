import xml.etree.ElementTree as ET
import os
import sys
import logging
import json
from collections import OrderedDict

# G_dctInterfaceMessages = dict()


# acPathToGenFolder = os.path.join(os.path.dirname(__file__), "../../SICD/")
# lstFiles = os.listdir(acPathToGenFolder)

# for i in range(len(lstFiles)):
#     if lstFiles[i].startswith('Module_Interface_Config_'):
#         try:
#             tree = ET.parse(os.path.join(os.path.dirname(__file__),"../../SICD/"+lstFiles[i]))
#             root = tree.getroot()
#             for pubSub in root:
#                 if pubSub.tag == "Subscribe":
#                     print(pubSub.tag)
#                     for Topic in pubSub:
#                         for msg in Topic:
#                             acSystem    = Topic.attrib['System']
#                             acModule    = Topic.attrib['Name']
#                             acMsgName      = msg.attrib['Name']
#                             acProtocol  = msg.attrib['Protocol']
#                             G_dctInterfaceMessages.update({acMsgName:[acSystem, acModule, acProtocol, pubSub.tag]})
#         except Exception as E:
#             logging.error("unable to open the config file, Error -> %s",E)
#             sys.exit()

# # print("\n")
# # print(G_dctInterfaceMessages)

# stringName = 'OlhmAdcsHmiStatusUnsol'
# if stringName in G_dctInterfaceMessages:
#     print(G_dctInterfaceMessages[stringName])


def main ():
    removeXmlWithModAddress = str(0)
    dctLoadedData = {}
    with open(os.path.join(os.path.dirname(__file__),"../../Structure/jsonFiles.json"), 'r') as f:
        dctLoadedData = OrderedDict(json.load(f))
        f.close()

    for xmlNum, xml in enumerate(dctLoadedData["xmls"]):
        for conMessage, conMessageVal in xml.items():
            if conMessage == "Messages":
                for key, vals in conMessageVal.items():
                    keyMod = key.split("_")[1]
                    if keyMod == removeXmlWithModAddress:
                        del dctLoadedData["xmls"][xmlNum]
                        print("xml Deleted")
                        break
    with open(os.path.join(os.path.dirname(__file__),"../../Structure/jsonFiles.json"), 'w') as f:
        f.write(json.dumps(dctLoadedData))
        f.close()
main()
# if __name__ == "__main__":
#     main()