#### toInteger()


 int BigInteger::toInteger ( ) const noexcept 
 

Attempts to get the lowest 32 bits of the value as an integer.If the value is bigger than the integer limits, this will return only the lower bits.