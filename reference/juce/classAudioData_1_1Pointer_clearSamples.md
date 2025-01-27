#### clearSamples()


template<typename SampleFormat , typename Endianness , typename InterleavingType , typename Constness > 

 void AudioData::Pointer< SampleFormat, Endianness, InterleavingType, Constness >::clearSamples ( int numSamples ) const noexcept 
 

Sets a number of samples to zero.Referenced by AudioFormatReader::ReadHelper< DestSampleType, SourceSampleType, SourceEndianness >::read(), and AudioFormatWriter::WriteHelper< DestSampleType, SourceSampleType, DestEndianness >::write().