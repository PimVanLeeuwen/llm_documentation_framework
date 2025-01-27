#### getClippedImage()


 Image Image::getClippedImage ( const Rectangle< int > & area ) const 
 

Returns an image which refers to a subsection of this image.This will not make a copy of the original the new image will keep a reference to it, so that if the original image is changed, the contents of the subsection will also change. Likewise if you draw into the subimage, you'll also be drawing onto that area of the original image. Note that if you use operator= to make the original Image object refer to something else, the subsection image won't pick up this change, it'll remain pointing at the original.The area passedin will be clipped to the bounds of this image, so this may return a smaller image than the area you asked for, or even a null image if the area was outofbounds.