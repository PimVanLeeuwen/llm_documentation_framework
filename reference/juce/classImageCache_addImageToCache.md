#### addImageToCache()


 static void ImageCache::addImageToCache ( const Image & image, int64 hashCode ) static 
 

Adds an image to the cache with a userdefined hashcode.The image passedin will be referenced (not copied) by the cache, so it's probably a good idea not to draw into it after adding it, otherwise this will affect all instances of it that may be in use.Parameters

 image the image to add 
 
 hashCode the hashcode to associate with it 



See alsogetFromHashCode