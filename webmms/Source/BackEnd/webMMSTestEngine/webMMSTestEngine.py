import threading, sys, os, struct, json, time, signal
import mqttHandler
G_lstFileInfo = []
G_lstTopicValues = []
G_lstMessageTypes = []
G_lstMessageValues = []
G_TypeDict = {
            'ST': 's',
            'CH': 's',
            'I1': 'b',
            'I2': 'h',
            'I4': 'i',
            'I8': 'q',
            'U1': 'B',
            'U2': 'H',
            'U4': 'I',
            'U8': 'Q',
            'F4': 'f',
            'F8': 'd'
        }

G_dctMain = {}

def readJsonFile():
    global G_lstFileInfo
    with open(os.path.join(os.path.dirname(__file__),"../Structure/jsonFiles.json"), 'r') as f:
        tmp_G_lstFileInfo= dict(json.load(f))
        G_lstFileInfo.append(tmp_G_lstFileInfo['xmls'])
        f.close()

def generateLstInfo():
    global G_lstFileInfo
    global G_lstTopicValues
    global G_lstMessageTypes
    global G_lstMessageValues
    global G_dctMain
    xmlSchema = str("")

    for xml in G_lstFileInfo[0]:
        for conMsg, msgInfo in xml.items():
            if conMsg == "Connection":
                xmlSchema = msgInfo["xmlSchema"]
            if conMsg == "Messages":
                for key, dctValues in msgInfo.items():
                    G_lstMessageTypes = []
                    G_lstMessageValues = []

                    recursive_getPayloadType(dctValues["Payload"])
                    getHeaderValues(dctValues["Header"])
                    recursive_getPayloadValues(dctValues["Payload"])

                    if xmlSchema == "BR12":
                        G_lstMessageTypes.insert(0,"5H")
                    else:
                        G_lstMessageTypes.insert(0,"6HQH")

                    # print(dctValues['Msg_Topic'])
                    # print(G_lstMessageTypes)
                    # print(G_lstMessageValues)

                    if len(G_lstMessageTypes) > 0:
                        packFormat = "="+''.join(G_lstMessageTypes)
                    else:
                        packFormat = str("")
                    G_dctMain[dctValues['Msg_Topic']] = [packFormat,G_lstMessageValues]


def recursive_getPayloadType(Msgs):
    if type(Msgs) == list: 
        for field in Msgs:
            if "type" in field and "value" in field:
                if len(G_lstMessageTypes) > 0:
                    if field['type'] == 'CH':
                        G_lstMessageTypes.append(str(field['count']) + G_TypeDict[field['type']])
                    elif field['type'] != 'CH':
                        if len(G_lstMessageTypes[-1]) == 1:
                            if G_lstMessageTypes[-1] == G_TypeDict[field['type']]:
                                G_lstMessageTypes[-1] = str(2) + G_TypeDict[field['type']]
                            elif G_lstMessageTypes[-1] != G_TypeDict[field['type']]:
                                G_lstMessageTypes.append(G_TypeDict[field['type']])
                        elif len(G_lstMessageTypes[-1]) > 1:
                            numAndType = G_lstMessageTypes[-1]
                            num = numAndType[:-1]
                            typ = numAndType[-1]
                            newNum = int(num) + 1
                            newVar = str(newNum)+typ
                            if typ == G_TypeDict[field['type']]:
                                G_lstMessageTypes[-1] = newVar
                            elif G_lstMessageTypes[-1] != G_TypeDict[field['type']]:
                                G_lstMessageTypes.append(G_TypeDict[field['type']])
                elif len(G_lstMessageTypes) == 0:
                    try:
                        G_lstMessageTypes.append(str(field['count'])+G_TypeDict[field['type']])
                    except:
                        G_lstMessageTypes.append(G_TypeDict[field['type']])
            if 'members' in field:
                recursive_getPayloadType(field["members"])

def getHeaderValues(Msgs):
    for key, val in Msgs.items():
        G_lstMessageValues.append(int(val))
    
def recursive_getPayloadValues(Msgs):
    if type(Msgs) == list:
        for field in Msgs:
            if 'enumType' not in field and 'value' not in field:
                recursive_getPayloadValues((field['members']))
            elif 'enumType' not in field and 'value' in field:
                if field['type'] == "CH":
                    G_lstMessageValues.append(field['value'].encode("utf-8"))
                # elif field['type'] == "F8":
                #     G_lstMessageValues.append(field['value'])
                else:
                    G_lstMessageValues.append(int(str(field['value']),16))
            elif 'enumType' in field:
                if field['type'] == "CH":
                    G_lstMessageValues.append(field['value'].encode("utf-8"))
                # elif field['type'] == "F8":
                #     G_lstMessageValues.append(field['value'])
                else:
                    G_lstMessageValues.append(int(str(field['value']),16))

def main():
    readJsonFile()
    generateLstInfo()
    mqttHandler.mqttFunctions(G_dctMain)

    while True:
        readJsonFile()
        generateLstInfo()
        mqttHandler.getGlobalDict(G_dctMain)
        time.sleep(2)
    

if __name__=="__main__":
    main()