#### readFromStream()


 bool AudioThumbnailCache::readFromStream ( InputStream & source ) 
 

Attempts to reload a saved cache of thumbnails from a stream.The cache data must have been written by the writeToStream() method. This will replace all currentlyloaded thumbnails with the new data.