#### addBlock()


 void AudioThumbnail::addBlock ( int64 sampleNumberInSource, const AudioBuffer< float > & newData, int startOffsetInBuffer, int numSamples ) overridevirtual 
 

Adds a block of level data to the thumbnail.Call reset() before using this, to tell the thumbnail about the data format.Implements AudioFormatWriter::ThreadedWriter::IncomingDataReceiver.