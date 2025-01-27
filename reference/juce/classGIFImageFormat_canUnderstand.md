#### canUnderstand()


 bool GIFImageFormat::canUnderstand ( InputStream & input ) overridevirtual 
 

Returns true if the given stream seems to contain data that this format understands.The format class should only read the first few bytes of the stream and sniff for header bytes that it understands.Note that this will advance the stream and leave it in a new position, so if you're planning on reusing it, you may want to rewind it after calling this method.See alsodecodeImage Implements ImageFileFormat.