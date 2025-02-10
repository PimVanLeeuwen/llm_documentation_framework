#### toInt64()


 int64 BigInteger::toInt64 ( ) const noexcept 
 

Attempts to get the lowest 64 bits of the value as an integer.If the value is bigger than the integer limits, this will return only the lower bits.