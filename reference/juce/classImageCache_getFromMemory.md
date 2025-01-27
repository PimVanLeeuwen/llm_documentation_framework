#### getFromMemory()


 static Image ImageCache::getFromMemory ( const void \* imageData, int dataSize ) static 
 

Loads an image from an inmemory image file, (or just returns the image if it's already cached).If the cache already contains an image that was loaded from this block of memory, that image will be returned. Otherwise, this method will try to load the file, add it to the cache, and return it.Remember that the image returned is shared, so drawing into it might affect other things that are using it! If you want to draw on it, first call Image::duplicateIfShared()Parameters

 imageData the block of memory containing the image data 
 
 dataSize the data size in bytes 



Returnsthe image, or an invalid image if it there was an error loading it 
See alsogetFromMemory, getFromCache, ImageFileFormat::loadFrom