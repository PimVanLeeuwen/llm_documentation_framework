#### getRawData()


 const uint8 \* Uuid::getRawData ( ) const noexcept 
 

Returns a pointer to the internal binary representation of the ID.This is an array of 16 bytes. To reconstruct a Uuid from its data, use the constructor or operator= method that takes an array of uint8s.