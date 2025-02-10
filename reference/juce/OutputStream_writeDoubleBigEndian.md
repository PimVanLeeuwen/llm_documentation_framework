#### writeDoubleBigEndian()


 virtual bool OutputStream::writeDoubleBigEndian ( double value ) virtual 
 

Writes a 64bit floating point value to the stream in a binary format.The eight raw bytes of the double value are written out as a bigendian 64bit int.See alsoInputStream::readDoubleBigEndian 
Returnsfalse if the write operation fails for some reason