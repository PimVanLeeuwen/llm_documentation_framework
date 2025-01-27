#### setPointer()


 static std::optional< var > JSONUtils::setPointer ( const var & v, String pointer, const var & newValue ) static 
 

Given a JSON array/object 'v', a string representing a JSON pointer, and a new property value 'newValue', returns a copy of 'v' where the property or array index referenced by the pointer has been set to 'newValue'.If the pointer cannot be followed, due to referencing missing array indices or fields, then this returns nullopt.For more details, check the JSON Pointer RFC 6901: https://datatracker.ietf.org/doc/html/rfc6901