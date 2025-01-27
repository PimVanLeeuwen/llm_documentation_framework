#### convert()


 virtual Image ImageType::convert ( const Image & source ) const virtual 
 

Returns an image which is a copy of the source image, but using this type of storage mechanism.For example, to make sure that an image is stored inmemory, you could use:myImage = SoftwareImageType().convert (myImage); 
ImageType::convertvirtual Image convert(const Image &source) constReturns an image which is a copy of the source image, but using this type of storage mechanism.
SoftwareImageTypeAn image storage type which holds the pixels inmemory as a simple block of values.Definition juce\_Image.h:567