#### loadFrom() [3/3]


 static Image ImageFileFormat::loadFrom ( const void \* rawData, size\_t numBytesOfData ) static 
 

Tries to load an image from a block of raw image data.This will use the findImageFormatForStream() method to locate a suitable codec, and use that to load the image.Returnsthe image that was decoded, or an invalid image if it fails.