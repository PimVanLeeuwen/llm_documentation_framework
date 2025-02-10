#### quarterFrame()


 static MidiMessage MidiMessage::quarterFrame ( int sequenceNumber, int value ) staticnoexcept 
 

Creates a quarterframe MTC message.Parameters

 sequenceNumber a value 0 to 7 for the upper nybble of the message's data byte 
 
 value a value 0 to 15 for the lower nybble of the message's data byte