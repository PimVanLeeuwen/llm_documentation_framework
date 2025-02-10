#### getFromHashCode()


 static Image ImageCache::getFromHashCode ( int64 hashCode ) static 
 

Checks the cache for an image with a particular hashcode.If there's an image in the cache with this hashcode, it will be returned, otherwise it will return an invalid image.Parameters

 hashCode the hash code that was associated with the image by addImageToCache() 
 



See alsoaddImageToCache