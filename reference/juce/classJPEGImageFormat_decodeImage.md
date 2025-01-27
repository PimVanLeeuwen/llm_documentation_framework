#### decodeImage()


 Image JPEGImageFormat::decodeImage ( InputStream & input ) overridevirtual 
 

Tries to decode and return an image from the given stream.This will be called for an image format after calling its canUnderStand() method to see if it can handle the stream.Parameters

 input the stream to read the data from. The stream will be positioned at the start of the image data (but this may not necessarily be position 0) 
 



Returnsthe image that was decoded, or an invalid image if it fails. 
See alsoloadFrom Implements ImageFileFormat.