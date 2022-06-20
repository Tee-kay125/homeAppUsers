# Introduction

The details to follow will describe a set of test steps that can be used to test the functionality of the WebMM

# Tests

## OLHM related

### Test 1: OLHM single MIC

#### Test 1.1

* Start the OLHM
* Start the WebMM
* In the WebMM configure a pipe called "OLHM" using the OLHM MsgDef and OLHM MIC file
* Verify that the OlhmAdcsStatusUnsol and OlhmHmiAdcsStatusUnsol are being received and about the rate of once per second
* View the OlhmAdcsStatusUnsol message and verify that the MsgCount and the TimeStampMs fields are ticking over
* View the OlhmAdcsStatusUnsol message and verify that the payload looks correct. The OLHM must be in a READY state and all the other modules must be in a FAILED state

#### Test 1.2

* Start the WebMM
* In the WebMM configure a pipe called "OLHM" using the OLHM MsgDef and OLHM MIC file
* Start the OTT
* Start the OLHM
* Check the counters and verify that one OlhmActionStatusReportUnsol message was received.
* View the received OlhmActionStatusReportUnsol messages
* Check that there is a non-zero value in the TimeStampMs field
* Check that the OlhmActionStatusReport is showing READY_FOR_ACTION

#### Test 1.3

* Start the WebMM
* In the WebMM configure a pipe called "OLHM" using the OLHM MsgDef and OLHM MIC file
* Start the OTT
* Start the OLHM
* Send the OlhmAdcsShutdownCmd message
* Examine the OlhmAdcsStatusUnsol message payload. Verify that all the modules is showing a SHUTDOWN status



### Test 2: HMI single MIC

#### Test 2.1

* Start the OTT
* Start the WebMM
* In the WebMM configure a pipe called "HMI" using the HMI MsgDef and HMI MIC file
* Verify that the HmiStatusReportUnsol message is being received
* Examine 