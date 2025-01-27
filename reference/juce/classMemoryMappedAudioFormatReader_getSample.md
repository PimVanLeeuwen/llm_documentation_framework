#### getSample()


 virtual void MemoryMappedAudioFormatReader::getSample ( int64 sampleIndex, float \* result ) const pure virtualnoexcept 
 

Returns the samples for all channels at a given sample position.The result array must be large enough to hold a value for each channel that this reader contains.