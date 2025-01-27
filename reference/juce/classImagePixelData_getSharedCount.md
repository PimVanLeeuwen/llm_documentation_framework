#### getSharedCount()


 virtual int ImagePixelData::getSharedCount ( ) const virtualnoexcept 
 

Returns the number of Image objects which are currently referring to the same internal shared image data.This is different to the reference count as an instance of ImagePixelData can internally depend on another ImagePixelData via it's member variables.