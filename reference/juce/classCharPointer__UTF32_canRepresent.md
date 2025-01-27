#### canRepresent()


 static bool CharPointer\_UTF32::canRepresent ( juce\_wchar character ) staticnoexcept 
 

Returns true if the given unicode character can be represented in this encoding.References CharacterFunctions::isNonSurrogateCodePoint().Referenced by isValidString().