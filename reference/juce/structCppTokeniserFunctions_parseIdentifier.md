#### parseIdentifier()


template<typename Iterator > 

 static int CppTokeniserFunctions::parseIdentifier ( Iterator & source ) staticnoexcept 
 

References isIdentifierBody(), isReservedKeyword(), CPlusPlusCodeTokeniser::tokenType\_identifier, CPlusPlusCodeTokeniser::tokenType\_keyword, CharPointer\_UTF8::write(), and CharPointer\_UTF8::writeNull().Referenced by readNextToken().