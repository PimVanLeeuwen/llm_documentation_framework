#### reset()


 void AudioThumbnail::reset ( int numChannels, double sampleRate, int64 totalSamplesInSource = 0 ) overridevirtual 
 

Resets the thumbnail, ready for adding data with the specified format.If you're going to generate a thumbnail yourself, call this before using addBlock() to add the data.Implements AudioFormatWriter::ThreadedWriter::IncomingDataReceiver.