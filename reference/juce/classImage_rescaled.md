#### rescaled()


 Image Image::rescaled ( int newWidth, 
 
 int newHeight, 
 Graphics::ResamplingQuality quality = Graphics::mediumResamplingQuality ) const 

Returns a rescaled version of this image.A new image is returned which is a copy of this one, rescaled to the given size.Note that if the new size is identical to the existing image, this will just return a reference to the original image, and won't actually create a duplicate.