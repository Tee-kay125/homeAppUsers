import json, codecs, struct, time, re, os, glob, argparse, sys
from datetime import datetime
from itertools import islice

def getHeader(lstHeaders ,data, name):
    for key, value in data.items():
        if key == "name":
            name = name+"_"+value
        if isinstance(value, dict):
            name = name+"_"+key
        elif isinstance(value, list):
            for lstVal in value:
                getHeader(lstHeaders, lstVal, name)
        else:
            if key == "value":
                lstHeaders.append(name[1:])
                name = ""

def getPayload(lstPayload, data, name):
    for key, value in data.items():
        if key == "name":
            name = name+"_"+value
        if isinstance(value, dict):
            name = name+"_"+key
        elif isinstance(value, list):
            for lstVal in value:
                getPayload(lstPayload, lstVal, name)
        else:
            if key == "value":
                lstPayload.append(str(value))
                name = ""

def getName(data):
    return data['Name']

def main(path, outputPath):
    try:
        fh = open(path, "r")
        fh.close()
        # Store configuration file values
    except FileNotFoundError:
        print("file not found")
        sys.exit(0)

    jsonFileName = open(path, "r")
    jsonData = jsonFileName.read()
    dctData = json.loads(jsonData)
    messgaeName = getName(dctData)

    try:
        os.makedirs(outputPath)
    except FileExistsError:
        # directory already exists
        pass

    dctKey = list(dctData["Messages"].keys())[0]
    lstHeaders = []
    for index, column in enumerate(dctData["Messages"][dctKey]):
        getHeader(lstHeaders, dctData["Messages"][dctKey][index], "")

    f = open(outputPath+"/"+messgaeName+".csv","w+")

    f.write("Timestamp_Epoch_UTC")
    f.write(",")
    for index, val in enumerate(lstHeaders):
        if index+1 != len(lstHeaders):
            f.write(val)
            f.write(",")
        else:
            f.write(val)
    f.write("\n")

    dctKeys = list(dctData["Messages"].keys())

    lstPayload = []

    print("writing load to file...")
    for key, value in dctData["Messages"].items():
        getPayload(lstPayload, {key:value}, "")

        f.write(key)
        f.write(",")
        for index, val in enumerate(lstPayload):
            if index+1 != len(lstHeaders):
                f.write(val)
                f.write(",")
            else:
                f.write(val)
        f.write("\n")
        lstPayload = []
    print("done")

    f.close()