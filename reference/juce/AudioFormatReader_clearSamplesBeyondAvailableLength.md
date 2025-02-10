#### clearSamplesBeyondAvailableLength()


 static void AudioFormatReader::clearSamplesBeyondAvailableLength ( int \*const \* destChannels, int numDestChannels, int startOffsetInDestBuffer, int64 startSampleInFile, int & numSamples, int64 fileLengthInSamples ) staticprotected 
 

Used by AudioFormatReader subclasses to clear any parts of the data blocks that lie beyond the end of their available length.References jassertfalse, and zeromem().

Member Data Documentation