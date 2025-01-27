#### findMinAndMax() [2/2]


template<typename SampleFormat , typename Endianness , typename InterleavingType , typename Constness > 

 void AudioData::Pointer< SampleFormat, Endianness, InterleavingType, Constness >::findMinAndMax ( size\_t numSamples, float & minValue, float & maxValue ) const noexcept 
 

Scans a block of data, returning the lowest and highest levels as floats.References findMinAndMax(), Range< ValueType >::getEnd(), and Range< ValueType >::getStart().