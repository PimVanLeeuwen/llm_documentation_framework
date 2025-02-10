#### writeShortBigEndian()


 virtual bool OutputStream::writeShortBigEndian ( short value ) virtual 
 

Writes a 16bit integer to the stream in a bigendian byte order.This will write two bytes to the stream: (value >> 8), then (value & 0xff).Returnsfalse if the write operation fails for some reason 
See alsoInputStream::readShortBigEndian