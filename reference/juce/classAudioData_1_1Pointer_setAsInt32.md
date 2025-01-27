#### setAsInt32()


template<typename SampleFormat , typename Endianness , typename InterleavingType , typename Constness > 

 void AudioData::Pointer< SampleFormat, Endianness, InterleavingType, Constness >::setAsInt32 ( int32 newValue ) noexcept 
 

Sets the value of the first sample as a 32bit integer.This will be mapped to the range of the format that is being written see getAsInt32().