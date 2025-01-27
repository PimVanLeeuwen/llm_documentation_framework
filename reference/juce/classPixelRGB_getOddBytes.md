#### getOddBytes()


 forcedinline uint32 PixelRGB::getOddBytes ( ) const noexcept 
 

Return channels with an odd index and insert zero bytes between them.This is useful for blending operations. The exact channels which are returned is platform dependent but compatible with the return value of getOddBytes of the PixelARGB class.See alsoPixelARGB::getOddBytes