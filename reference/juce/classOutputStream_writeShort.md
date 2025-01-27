#### writeShort()


 virtual bool OutputStream::writeShort ( short value ) virtual 
 

Writes a 16bit integer to the stream in a littleendian byte order.This will write two bytes to the stream: (value & 0xff), then (value >> 8).Returnsfalse if the write operation fails for some reason 
See alsoInputStream::readShort