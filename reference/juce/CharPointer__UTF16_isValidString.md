#### isValidString()


 static bool CharPointer\_UTF16::isValidString ( const CharType \* codeUnits, int maxBytesToRead ) static 
 

Returns true if this data contains a valid string in this encoding.References canRepresent(), CharacterFunctions::isHighSurrogate(), and CharacterFunctions::isLowSurrogate().