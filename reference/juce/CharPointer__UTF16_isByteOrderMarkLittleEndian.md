#### isByteOrderMarkLittleEndian()


 static bool CharPointer\_UTF16::isByteOrderMarkLittleEndian ( const void \* possibleByteOrder ) staticnoexcept 
 

Returns true if the first pair of bytes in this pointer are the UTF16 byteorder mark (little endian).The pointer must not be null, and must contain at least two valid bytes.References byteOrderMarkLE1, byteOrderMarkLE2, jassert, JUCE\_BEGIN\_IGNORE\_WARNINGS\_MSVC, and JUCE\_END\_IGNORE\_WARNINGS\_MSVC.