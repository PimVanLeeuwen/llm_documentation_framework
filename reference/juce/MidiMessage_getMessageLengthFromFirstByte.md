#### getMessageLengthFromFirstByte()


 static int MidiMessage::getMessageLengthFromFirstByte ( uint8 firstByte ) staticnoexcept 
 

Based on the first byte of a short midi message, this uses a lookup table to return the message length (either 1, 2, or 3 bytes).The value passed in must be 0x80 or higher.Referenced by MidiDataConcatenator::pushMidiData().