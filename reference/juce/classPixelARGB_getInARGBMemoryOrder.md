#### getInARGBMemoryOrder()


 uint32 PixelARGB::getInARGBMemoryOrder ( ) const noexcept 
 

Returns a uint32 which when written to memory, will be in the order a, r, g, b.In other words, if the returnvalue is read as a uint8 array then the elements will be in the order of a, r, g, b