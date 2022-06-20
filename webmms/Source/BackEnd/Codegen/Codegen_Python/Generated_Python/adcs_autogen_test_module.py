#!/bin/bash/env python3.6

"""
    This module tests the autogen code of the WebMM by making an ADCS EIU_Msg.xml pipe.
    Instance of all messages are created to see of there are any exceptions generated.

    Usage:
        python3.6 adcs_autogen_test_module.py


"""
from MW_Common_Types_TypeDef import *
from ADCS_Common_Types_TypeDef import *
from EIU_Msg_MsgDef import *


def vMainMethod():
    """ This public function creates an instance of every EIU message to check for errors.
    Exceptions will be generated if the autogen was not bug free.

    Parameters:

    Returns:

    Raises:
        Raises no exceptions

    """


    objsEiuSensorBearingTrackUnsolMsgCls = sEiuSensorBearingTrackUnsolMsgCls()
    objsEiuSensorPointTrackUnsolMsgCls = sEiuSensorPointTrackUnsolMsgCls()
    objsEiuShutdownCmdRspMsgCls = sEiuShutdownCmdRspMsgCls()
    objsEiuShutdownCmdMsgCls = sEiuShutdownCmdMsgCls()
    objsEiuEndOfReadyCmdRspMsgCls = sEiuEndOfReadyCmdRspMsgCls()
    objsEiuEndOfReadyCmdMsgCls = sEiuEndOfReadyCmdMsgCls()
    objsEiuEndOfSetupCmdRspMsgCls = sEiuEndOfSetupCmdRspMsgCls()
    objsEiuEndOfSetupCmdMsgCls = sEiuEndOfSetupCmdMsgCls()
    objsEiuStatusReportUnsolMsgCls = sEiuStatusReportUnsolMsgCls()



if __name__ == "__main__":
    vMainMethod()