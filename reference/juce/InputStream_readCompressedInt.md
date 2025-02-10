#### readCompressedInt()


 virtual int InputStream::readCompressedInt ( ) virtual 
 

Reads an encoded 32bit number from the stream using a spacesaving compressed format.For small values, this is more spaceefficient than using readInt() and OutputStream::writeInt() The format used is: number of significant bytes + up to 4 bytes in littleendian order.See alsoOutputStream::writeCompressedInt()