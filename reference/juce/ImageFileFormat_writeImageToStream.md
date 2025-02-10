#### writeImageToStream()


 virtual bool ImageFileFormat::writeImageToStream ( const Image & sourceImage, OutputStream & destStream ) pure virtual 
 

Attempts to write an image to a stream.To specify extra information like encoding quality, there will be appropriate parameters in the subclasses of the specific file types.Returnstrue if it nothing went wrong. Implemented in GIFImageFormat, JPEGImageFormat, and PNGImageFormat.