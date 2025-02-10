#### isByteOrderMark()


 static bool CharPointer\_UTF8::isByteOrderMark ( const void \* possibleByteOrder ) staticnoexcept 
 

Returns true if the first three bytes in this pointer are the UTF8 byteorder mark (BOM).The pointer must not be null, and must point to at least 3 valid bytes.References byteOrderMark1, byteOrderMark2, byteOrderMark3, jassert, JUCE\_BEGIN\_IGNORE\_WARNINGS\_MSVC, and JUCE\_END\_IGNORE\_WARNINGS\_MSVC.