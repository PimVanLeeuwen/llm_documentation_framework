#### loadFromMemoryBlock()


 void BigInteger::loadFromMemoryBlock ( const MemoryBlock & data ) 
 

Converts a block of raw data into a number.The data is arranged as littleendian, so the first byte of data is the low 8 bits of the number, and so on.See alsotoMemoryBlock