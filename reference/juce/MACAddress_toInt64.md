#### toInt64()


 int64 MACAddress::toInt64 ( ) const noexcept 
 

Returns the address in the lower 6 bytes of an int64.This uses a littleendian arrangement, with the first byte of the address being stored in the leastsignificant byte of the result value.