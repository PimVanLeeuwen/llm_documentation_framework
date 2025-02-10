#### writeCompressedInt()


 virtual bool OutputStream::writeCompressedInt ( int value ) virtual 
 

Writes a condensed binary encoding of a 32bit integer.If you're storing a lot of integers which are unlikely to have very large values, this can save a lot of space, because values under 0xff will only take up 2 bytes, under 0xffff only 3 bytes, etc.The format used is: number of significant bytes + up to 4 bytes in littleendian order.Returnsfalse if the write operation fails for some reason 
See alsoInputStream::readCompressedInt