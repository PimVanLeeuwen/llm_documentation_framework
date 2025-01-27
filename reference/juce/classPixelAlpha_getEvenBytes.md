#### getEvenBytes()


 forcedinline uint32 PixelAlpha::getEvenBytes ( ) const noexcept 
 

Return channels with an even index and insert zero bytes between them.This is useful for blending operations. The exact channels which are returned is platform dependent but compatible with the return value of getEvenBytes of the PixelARGB class.See alsoPixelARGB::getEvenBytes