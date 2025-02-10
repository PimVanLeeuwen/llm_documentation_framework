#### findImageFormatForStream()


 static ImageFileFormat \* ImageFileFormat::findImageFormatForStream ( InputStream & input ) static 
 

Tries the builtin formats to see if it can find one to read this stream.There are currently builtin decoders for PNG, JPEG and GIF formats. The object that is returned should not be deleted by the caller.See alsocanUnderstand, decodeImage, loadFrom