#### getEvenBytes()


 forcedinline uint32 PixelARGB::getEvenBytes ( ) const noexcept 
 

Return channels with an even index and insert zero bytes between them.This is useful for blending operations. The exact channels which are returned is platform dependent.