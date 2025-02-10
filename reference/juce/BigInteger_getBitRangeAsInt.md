#### getBitRangeAsInt()


 uint32 BigInteger::getBitRangeAsInt ( int startBit, int numBits ) const noexcept 
 

Returns a range of bits as an integer value.e.g. getBitRangeAsInt (0, 32) would return the lowest 32 bits.Asking for more than 32 bits isn't allowed (obviously) for that, use getBitRange().