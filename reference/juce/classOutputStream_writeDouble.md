#### writeDouble()


 virtual bool OutputStream::writeDouble ( double value ) virtual 
 

Writes a 64bit floating point value to the stream in a binary format.The eight raw bytes of the double value are written out as a littleendian 64bit int.Returnsfalse if the write operation fails for some reason 
See alsoInputStream::readDouble