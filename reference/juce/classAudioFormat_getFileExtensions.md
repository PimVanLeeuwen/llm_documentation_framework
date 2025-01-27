#### getFileExtensions()


 virtual StringArray AudioFormat::getFileExtensions ( ) const virtual 
 

Returns all the file extensions that might apply to a file of this format.The first item will be the one that's preferred when creating a new file. So for a wav file this might just return ".wav"; for an AIFF file it might return two items, ".aif" and ".aiff"