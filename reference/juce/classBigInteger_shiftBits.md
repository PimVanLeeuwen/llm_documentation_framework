#### shiftBits()


 BigInteger & BigInteger::shiftBits ( int howManyBitsLeft, 
 
 int startBit ) 

Shifts a section of bits left or right.Parameters

 howManyBitsLeft how far to move the bits (+ve numbers shift it left, ve numbers shift it right). 
 
 startBit the first bit to affect if this is > 0, only bits above that index will be affected.