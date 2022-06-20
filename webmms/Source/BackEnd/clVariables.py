from Codegen.Codegen_Python import generate_Json
from collections import OrderedDict


G_mainJsonFile = dict()
G_dctReceivedMessages = dict()

class CLVARIABLES:
    # G_mainJsonFile = dict()
    # G_dctReceivedMessages = dict()
    def __init__(self):
        pass

    def _getJsonFile():
        global G_mainJsonFile
        # G_mainJsonFile = generate_Json.getJsonFiles()
        G_mainJsonFile = {'xmls':[]}
    def _getReceivedMsgs():
        global G_dctReceivedMessages
        G_dctReceivedMessages = generate_Json.getReceivedMsgs()
        print(G_dctReceivedMessages)