#### findNextSetBit()


 int BigInteger::findNextSetBit ( int startIndex ) const noexcept 
 

Looks for the index of the next set bit after a given starting point.This searches from startIndex (inclusive) upwards for the first set bit, and returns its index. If no set bits are found, it returns 1.