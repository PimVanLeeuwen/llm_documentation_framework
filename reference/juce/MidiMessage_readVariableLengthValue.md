#### readVariableLengthValue()


 static VariableLengthValue MidiMessage::readVariableLengthValue ( const uint8 \* data, int maxBytesToUse ) staticnoexcept 
 

Reads a midi variablelength integer, with protection against buffer overflow.Parameters

 data the data to read the number from 
 
 maxBytesToUse the number of bytes in the region following `data` 



Returnsa struct containing the parsed value, and the number of bytes that were read. If parsing fails, both the `value` and `bytesUsed` fields will be set to 0 and `isValid()` will return false