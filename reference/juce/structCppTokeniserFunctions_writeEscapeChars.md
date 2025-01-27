#### writeEscapeChars()


 static void CppTokeniserFunctions::writeEscapeChars ( OutputStream & out, const char \* utf8, const int numBytesToRead, const int maxCharsOnLine, const bool breakAtNewLines, const bool replaceSingleQuotes, const bool allowStringBreaks ) static 
 

Takes a UTF8 string and writes it to a stream using standard C++ escape sequences for any nonascii bytes.Although not strictly a tokenising function, this is still a function that often comes in handy when working with C++ code!Note that addEscapeChars() is easier to use than this function if you're working with Strings.See alsoaddEscapeChars References CharacterFunctions::getHexDigitValue(), JUCE\_FALLTHROUGH, newLine, and String::toHexString().Referenced by addEscapeChars().