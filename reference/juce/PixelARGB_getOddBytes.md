#### getOddBytes()


 forcedinline uint32 PixelARGB::getOddBytes ( ) const noexcept 
 

Return channels with an odd index and insert zero bytes between them.This is useful for blending operations. The exact channels which are returned is platform dependent.