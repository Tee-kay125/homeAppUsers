
# General

Key = MsgId + ModAddr + MsgType


# For the Python codegen

* Only the "CH" and "ST" will have an count.
* Structs and enums whith a count > 1 will be in a for loop in the Python code.


# For the JSON files

dctFieldVal.json:  NB: Maybe not needed

favourites.json: Keeps all the favourite messages as the key

jsonFiles.json: 
* Contains all messages for sending and receiving and will be updated when messages are received and when one changes the values on the WebMM GUI.
* If CH type then the count will indicate how many characters.
* For structs and enums if the count is greater than 1 then the field will be repeated by how many counts there are.
* When new messages are received only the values are updated not the things like the keys, structures or layout.
* If a message has no payload then the "Payload" field will be an empty list.

messagesToRecord.json:
* Will include keys


Pipes.json
* All the that have been defined

receivedMsgs.json:
* Contains the keys of received messages and number of messages (as in the number of messages since WebMM started).

recordedMessages.json:
* Contains recorded messages (only selected ones) as keys and values. Will not just be the latest but all the messages recorded over time which is different jsonFiles.json which only keeps the latest message.
* This file can become very large in size. There is no code to manage the size right now. 