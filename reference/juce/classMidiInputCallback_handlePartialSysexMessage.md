#### handlePartialSysexMessage()


 virtual void MidiInputCallback::handlePartialSysexMessage ( MidiInput \* source, const uint8 \* messageData, int numBytesSoFar, double timestamp ) virtual 
 

Notification sent each time a packet of a multipacket sysex message arrives.If a long sysex message is broken up into multiple packets, this callback is made for each packet that arrives until the message is finished, at which point the normal handleIncomingMidiMessage() callback will be made with the entire message.The message passed in will contain the start of a sysex, but won't be finished with the terminating 0xf7 byte.