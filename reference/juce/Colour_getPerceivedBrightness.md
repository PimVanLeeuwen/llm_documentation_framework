#### getPerceivedBrightness()


 float Colour::getPerceivedBrightness ( ) const noexcept 
 

Returns a skewed brightness value, adjusted to better reflect the way the human eye responds to different colour channels.This makes it better than getBrightness() for comparing differences in brightness.