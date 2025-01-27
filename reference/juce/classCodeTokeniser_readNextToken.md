#### readNextToken()


 virtual int CodeTokeniser::readNextToken ( CodeDocument::Iterator & source ) pure virtual 
 

Reads the next token from the source and returns its token type.This must leave the source pointing to the first character in the next token.Implemented in CPlusPlusCodeTokeniser, LuaTokeniser, and XmlTokeniser.