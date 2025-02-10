#### scanMinAndMaxInterleaved()


template<typename SampleType , typename Endianness > 

 Range< float > MemoryMappedAudioFormatReader::scanMinAndMaxInterleaved ( int channel, int64 startSampleInFile, int64 numSamples ) const protectednoexcept 
 

Used by AudioFormatReader subclasses to scan for min/max ranges in interleaved data.References addBytesToPointer().

Member Data Documentation