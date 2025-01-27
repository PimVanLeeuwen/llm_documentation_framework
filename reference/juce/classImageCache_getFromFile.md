#### getFromFile()


 static Image ImageCache::getFromFile ( const File & file ) static 
 

Loads an image from a file, (or just returns the image if it's already cached).If the cache already contains an image that was loaded from this file, that image will be returned. Otherwise, this method will try to load the file, add it to the cache, and return it.Remember that the image returned is shared, so drawing into it might affect other things that are using it! If you want to draw on it, first call Image::duplicateIfShared()Parameters

 file the file to try to load 
 



Returnsthe image, or null if it there was an error loading it 
See alsogetFromMemory, getFromCache, ImageFileFormat::loadFrom