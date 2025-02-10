#### set()


template<class Pixel > 

 forcedinline void PixelRGB::set ( const Pixel & src ) noexcept 
 

Copies another pixel colour over this one.This doesn't blend it this colour is simply replaced by the other one. Because PixelRGB has no alpha channel, any alpha value in the source pixel is thrown away.