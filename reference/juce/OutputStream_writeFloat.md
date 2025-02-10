#### writeFloat()


 virtual bool OutputStream::writeFloat ( float value ) virtual 
 

Writes a 32bit floating point value to the stream in a binary format.The binary 32bit encoding of the float is written as a littleendian int.Returnsfalse if the write operation fails for some reason 
See alsoInputStream::readFloat