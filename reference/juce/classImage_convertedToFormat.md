#### convertedToFormat()


 Image Image::convertedToFormat ( PixelFormat newFormat ) const 
 

Returns a version of this image with a different image format.A new image is returned which has been converted to the specified format.Note that if the new format is no different to the current one, this will just return a reference to the original image, and won't actually create a copy.