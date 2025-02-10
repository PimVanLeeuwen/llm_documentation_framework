#### writeBool()


 virtual bool OutputStream::writeBool ( bool boolValue ) virtual 
 

Writes a boolean to the stream as a single byte.This is encoded as a binary byte (not as text) with a value of 1 or 0.Returnsfalse if the write operation fails for some reason 
See alsoInputStream::readBool