#### getHexDigitValue()


 static int CharacterFunctions::getHexDigitValue ( juce\_wchar digit ) staticnoexcept 
 

Returns 0 to 16 for '0' to 'F", or 1 for characters that aren't a legal hex digit.Referenced by CharacterFunctions::HexParser< ResultType >::parse(), and CppTokeniserFunctions::writeEscapeChars().