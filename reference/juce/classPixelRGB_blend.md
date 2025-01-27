#### blend() [3/3]


template<class Pixel > 

 forcedinline void PixelRGB::blend ( const Pixel & src, uint32 extraAlpha ) noexcept 
 

Blends another pixel onto this one, applying an extra multiplier to its opacity.The opacity of the pixel being overlaid is scaled by the extraAlpha factor before being used, so this can blend semitransparently from a PixelRGB argument.References clampPixelComponents(), and maskPixelComponents().