#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""This module is the WebMM ZMQ test subscriber process

Example:
    To run this file do the following:

        $ python3.6 zmq_generic_subscriber.py -i config.toml

Todo:

"""
# ===========================================
# Imports
# ===========================================

import asyncio
import zmq
import argparse  # Needed to help manage command line arguments
import toml  # Needed to parse the TOML file


async def main(objAsyncioLoopPar, dctGlobalInterfaceDictionaryPar: dict) -> None:
    """ This is a public method which is called in the main thread as part of the asyncio loop.

    This is a public method which is called in the main thread as part of the asyncio loop. The main focus of this function is to always be
    servicing the queue and process the messages received. The processing of a message must always be done with a asyncio create_task() call.

    Args:
        objAsyncioLoopPar (obj): The asyncio event loop.
        dctGlobalInterfaceDictionaryPar (dict): The global interface dictionary.

    Returns:

    Raises:
        Raises no exceptions
    """

    # Make an instance of a argeparse to help us manage command line arguments
    objArgParser = argparse.ArgumentParser()
    objArgParser.add_argument("-i", required=True, help="The INI file path")  # We must supply a INI file path
    args = objArgParser.parse_args()  # Parse the args and make sure we have everything we need

    # Open and parse the TOML file
    objTomlFile = open(args.i, "r")
    acTomlContent = objTomlFile.read()
    objTomlFile.close()

    # Parse the TOML content
    objParsedTomlContent = toml.loads(acTomlContent)

    # Socket to talk to server
    context = zmq.Context()
    objZmqSocket = context.socket(zmq.SUB)  # Create a SUB socket
    objZmqSocket.connect("tcp://%s:%s" % (objParsedTomlContent["acPublisherIp"], objParsedTomlContent["acPublisherBindPort"]))

    for acTopic in objParsedTomlContent["lstSubscribeTopics"]:
        objZmqSocket.setsockopt(zmq.SUBSCRIBE, acTopic.encode("ascii"))

    while True:  # main loop

        lstRxMessage = None

        try:
            # Reference information -> recv_multipart(flags=0, copy=True, track=False)
            # Reference information -> With flags=NOBLOCK, this raises ZMQError if no messages have arrived; otherwise, this waits until a message arrives.
            lstRxMessage = objZmqSocket.recv_multipart(flags=zmq.NOBLOCK, copy=True, track=False)
        except Exception:
            pass

        if (lstRxMessage):
            print("Topic: %s" % (lstRxMessage[0]))
            print("Message data in hex: %s" % (lstRxMessage[1].hex()))
            print("Message length (bytes): %s" % (len(lstRxMessage[1])))
            print("")
        await asyncio.sleep(0.05)

# ===========================================
# Global functions
# ===========================================



def vModuleMain():
    """ This is a public function which is called when the global name is __main__. The entire Pythom module is kicked off using this
    method.

    Args:

    Returns:

    Raises:
        Raises no exceptions
    """
    dctGlobalInterfaceDictionary = {}

    try:
        # Get the asyncio event loop instance
        objAsyncioLoop = asyncio.get_event_loop()
    except Exception as E:
        objAsyncioLoop = None

    if (objAsyncioLoop is not None):
        objAsyncioLoop.run_until_complete(main(objAsyncioLoop, dctGlobalInterfaceDictionary))

    return

# ===========================================
# Module "__main__" function
# ===========================================


if __name__ == "__main__":
    vModuleMain()
