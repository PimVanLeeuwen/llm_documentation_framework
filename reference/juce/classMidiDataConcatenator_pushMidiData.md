#### pushMidiData()


template<typename UserDataType , typename CallbackType > 

 void MidiDataConcatenator::pushMidiData ( const void \* inputData, 
 
 int numBytes, 
 double time, 
 UserDataType \* input, 
 CallbackType & callback ) 

References MidiMessage::getMessageLengthFromFirstByte().