#### createReaderFor()


 AudioFormatReader \* MP3AudioFormat::createReaderFor ( InputStream \* sourceStream, bool deleteStreamIfOpeningFails ) overridevirtual 
 

Tries to create an object that can read from a stream containing audio data in this format.The reader object that is returned can be used to read from the stream, and should then be deleted by the caller.Parameters

 sourceStream the stream to read from the AudioFormatReader object that is returned will delete this stream when it no longer needs it. 
 
 deleteStreamIfOpeningFails if no reader can be created, this determines whether this method should delete the stream object that was passedin. (If a valid reader is returned, it will always be in charge of deleting the stream, so this parameter is ignored) 



See alsoAudioFormatReader Implements AudioFormat.