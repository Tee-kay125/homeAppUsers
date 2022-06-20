#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""This module is the WebMM ZMQ publisher process

Example:
    To run this file do the following:

        $ python3.6 zmq_publisher.py -i config.toml

Todo:

"""
# ===========================================
# Imports
# ===========================================

import asyncio
import zmq
import argparse
import toml

from Autogen.eiu_msg import sEIU_SENSOR_POINT_TRACK_UNSOL
from Autogen.tm_msg import sTM_SYSTEM_POINT_TRACK_UNSOL
from Autogen.mgb_msg import sLZA_C01_AIR_TRACK_REPORT_UNSOL
from Autogen.mgb_msg import sLZA_C04_BEARING_TRACK_REPORT_UNSOL
from Autogen.mgb_msg import sLZA_C02_SURFACE_TRACK_REPORT_UNSOL
from Autogen.mgb_msg import sLZA_L06_OWN_POSITION_REPORT_UNSOL
from Autogen.mgb_msg import sLZA_T61_G_AIR_DEFENCE_READINESS_STATE_UNSOL
from Autogen.mgb_msg import sLZA_T61_H_LOCAL_WARNING_ORDER_UNSOL
from Autogen.mgb_msg import sLZA_T61_I_ENGAGEMENT_ORDER_UNSOL
from Autogen.mgb_msg import sLZA_T61_J_WEAPON_CONTROL_ORDER_UNSOL
from Autogen.mgb_msg import sLZA_T63_A_ENGAGEMENT_COMPLIANCE_REPORT_UNSOL
from Autogen.mgb_msg import sLZA_T63_B_ENGAGEMENT_CONTROL_STATE_REPORT_UNSOL
from Autogen.mgb_msg import sLZA_T63_C_ENGAGEMENT_ACTION_STATUS_REPORT_UNSOL
from Autogen.mgb_msg import sLZA_T63_D_ENGAGEMENT_OUTCOME_REPORT_UNSOL
from Autogen.mgb_msg import sLZA_T63_L_WEAPON_SYSTEM_STATUS_UNSOL
from Autogen.mgb_msg import sLZA_T63_H_ACTION_STATUS_REPORT_UNSOL
from Autogen.mgb_msg import sLZA_C01_AIR_TRACK_REPORT_UNSOL
from Autogen.mgb_msg import sLZA_T10_Q_AIR_RAID_WARNING_STATE_UNSOL


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
    objZmqSocket = context.socket(zmq.PUB)
    objZmqSocket.bind("tcp://*:%s" % (objParsedTomlContent["acBindPort"]))
    lstAllMessages = []

    # ===

    sEiuSensorPointTrackUnsol = sEIU_SENSOR_POINT_TRACK_UNSOL()
    btaData = sEiuSensorPointTrackUnsol.btaSerialise()
    btaTopic = b"ADCS/EIU/EiuSensorPointTrackUnsol"

    lstDataPartsPar = [btaTopic, btaData]
    lstAllMessages.append(lstDataPartsPar)

    # ===

    sTmSystemPointTrackUnsol = sTM_SYSTEM_POINT_TRACK_UNSOL()
    btaData = sTmSystemPointTrackUnsol.btaSerialise()
    btaTopic = b"ADCS/TM/TmSystemPointTrackUnsol"

    lstDataPartsPar = [btaTopic, btaData]
    lstAllMessages.append(lstDataPartsPar)

    # ===

    sLzaC01AirTrackReportUnsol = sLZA_C01_AIR_TRACK_REPORT_UNSOL()
    btaData = sLzaC01AirTrackReportUnsol.btaSerialise()
    btaTopic = b"ELM/MGB/LzaC01AirTrackReportUnsol"

    lstDataPartsPar = [btaTopic, btaData]
    lstAllMessages.append(lstDataPartsPar)

    # ===

    sLzaC02SurfaceTrackReportUnsol = sLZA_C02_SURFACE_TRACK_REPORT_UNSOL()
    btaData = sLzaC02SurfaceTrackReportUnsol.btaSerialise()
    btaTopic = b"ELM/MGB/LzaC02SurfaceTrackReportUnsol"

    lstDataPartsPar = [btaTopic, btaData]
    lstAllMessages.append(lstDataPartsPar)

    # ===

    sLzaC04BearingTrackReportUnsol = sLZA_C04_BEARING_TRACK_REPORT_UNSOL()
    btaData = sLzaC04BearingTrackReportUnsol.btaSerialise()
    btaTopic = b"ELM/MGB/LzaC04BearingTrackReportUnsol"

    lstDataPartsPar = [btaTopic, btaData]
    lstAllMessages.append(lstDataPartsPar)

    # ===

    sLzaL06OwnPositionReportUnsol = sLZA_L06_OWN_POSITION_REPORT_UNSOL()
    btaData = sLzaL06OwnPositionReportUnsol.btaSerialise()
    btaTopic = b"ELM/MGB/LzaL06OwnPositionReportUnsol"

    lstDataPartsPar = [btaTopic, btaData]
    lstAllMessages.append(lstDataPartsPar)

    # ===

    sLzaT61GAirDefenceReadinessStateUnsol = sLZA_T61_G_AIR_DEFENCE_READINESS_STATE_UNSOL()
    btaData = sLzaT61GAirDefenceReadinessStateUnsol.btaSerialise()
    btaTopic = b"ELM/MGB/LzaT61GAirDefenceReadinessStateUnsol"

    lstDataPartsPar = [btaTopic, btaData]
    lstAllMessages.append(lstDataPartsPar)

    # ===

    sLzaT61HLocalWarningOrderUnsol = sLZA_T61_H_LOCAL_WARNING_ORDER_UNSOL()
    btaData = sLzaT61HLocalWarningOrderUnsol.btaSerialise()
    btaTopic = b"ELM/MGB/LzaT61HLocalWarningOrderUnsol"

    lstDataPartsPar = [btaTopic, btaData]
    lstAllMessages.append(lstDataPartsPar)

    # ===

    sLzaT61IEngagementOrderUnsol = sLZA_T61_I_ENGAGEMENT_ORDER_UNSOL()
    btaData = sLzaT61IEngagementOrderUnsol.btaSerialise()
    btaTopic = b"ELM/MGB/LzaT61IEngagementOrderUnsol"

    lstDataPartsPar = [btaTopic, btaData]
    lstAllMessages.append(lstDataPartsPar)

    # ===

    sLzaT61JWeaponControlOrderUnsol = sLZA_T61_J_WEAPON_CONTROL_ORDER_UNSOL()
    btaData = sLzaT61JWeaponControlOrderUnsol.btaSerialise()
    btaTopic = b"ELM/MGB/LzaT61JWeaponControlOrderUnsol"

    lstDataPartsPar = [btaTopic, btaData]
    lstAllMessages.append(lstDataPartsPar)

    # ===

    sLzaT63AEngagementComplianceReportUnsol = sLZA_T63_A_ENGAGEMENT_COMPLIANCE_REPORT_UNSOL()
    btaData = sLzaT63AEngagementComplianceReportUnsol.btaSerialise()
    btaTopic = b"ELM/MGB/LzaT63AEngagementComplianceReportUnsol"

    lstDataPartsPar = [btaTopic, btaData]
    lstAllMessages.append(lstDataPartsPar)

    # ===

    sLzaT63BEngagementControlStateReportUnsol = sLZA_T63_B_ENGAGEMENT_CONTROL_STATE_REPORT_UNSOL()
    btaData = sLzaT63BEngagementControlStateReportUnsol.btaSerialise()
    btaTopic = b"ELM/MGB/LzaT63BEngagementControlStateReportUnsol"

    lstDataPartsPar = [btaTopic, btaData]
    lstAllMessages.append(lstDataPartsPar)

    # ===

    sLzaT63CEngagementActionStatusReportUnsol = sLZA_T63_C_ENGAGEMENT_ACTION_STATUS_REPORT_UNSOL()
    btaData = sLzaT63CEngagementActionStatusReportUnsol.btaSerialise()
    btaTopic = b"ELM/MGB/LzaT63CEngagementActionStatusReportUnsol"

    lstDataPartsPar = [btaTopic, btaData]
    lstAllMessages.append(lstDataPartsPar)

    # ===

    sLzaT63DEngagementOutcomeReportUnsol = sLZA_T63_D_ENGAGEMENT_OUTCOME_REPORT_UNSOL()
    btaData = sLzaT63DEngagementOutcomeReportUnsol.btaSerialise()
    btaTopic = b"ELM/MGB/LzaT63DEngagementOutcomeReportUnsol"

    lstDataPartsPar = [btaTopic, btaData]
    lstAllMessages.append(lstDataPartsPar)

    # ===

    sLzaT63HActionStatusReportUnsol = sLZA_T63_H_ACTION_STATUS_REPORT_UNSOL()
    btaData = sLzaT63HActionStatusReportUnsol.btaSerialise()
    btaTopic = b"ELM/MGB/LzaT63HActionStatusReportUnsol"

    lstDataPartsPar = [btaTopic, btaData]
    lstAllMessages.append(lstDataPartsPar)

    # ===

    sLzaT63LWeaponSystemStatusUnsol = sLZA_T63_L_WEAPON_SYSTEM_STATUS_UNSOL()
    btaData = sLzaT63LWeaponSystemStatusUnsol.btaSerialise()
    btaTopic = b"ELM/MGB/LzaT63LWeaponSystemStatusUnsol"

    lstDataPartsPar = [btaTopic, btaData]
    lstAllMessages.append(lstDataPartsPar)

    # ===

    sLzaT10QAirRaidWarningStateUnsol = sLZA_T10_Q_AIR_RAID_WARNING_STATE_UNSOL()
    btaData = sLzaT10QAirRaidWarningStateUnsol.btaSerialise()
    btaTopic = b"ELM/MGB/LzaT10QAirRaidWarningStateUnsol"

    lstDataPartsPar = [btaTopic, btaData]
    lstAllMessages.append(lstDataPartsPar)

    while True:  # main loop

        for lstDataPartsPar in lstAllMessages:

            print(lstDataPartsPar[0])

            try:
                objZmqSocket.send_multipart(lstDataPartsPar, flags=zmq.NOBLOCK, copy=True, track=False, routing_id=None, group=None)
            except Exception:
                print("Send error")

        await asyncio.sleep(1)

# ===========================================
# Global functions
# ===========================================


def vModuleMain():
    """ This is a public function which is called when the global name is __main__. The entire Python module is kicked off using this
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
