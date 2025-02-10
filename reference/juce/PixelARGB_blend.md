#### blend() [2/2]


template<class Pixel > 

 forcedinline void PixelARGB::blend ( const Pixel & src, uint32 extraAlpha ) noexcept 
 

Blends another pixel onto this one, applying an extra multiplier to its opacity.The opacity of the pixel being overlaid is scaled by the extraAlpha factor before being used, so this can blend semitransparently from a PixelRGB argument.References clampPixelComponents(), and maskPixelComponents().