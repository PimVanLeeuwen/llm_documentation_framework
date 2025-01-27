#### convertSamples() [2/2]


template<typename SampleFormat , typename Endianness , typename InterleavingType , typename Constness > 
template<class OtherPointerType > 

 void AudioData::Pointer< SampleFormat, Endianness, InterleavingType, Constness >::convertSamples ( OtherPointerType source, int numSamples ) const noexcept 
 

Writes a stream of samples into this pointer from another pointer.This will copy the specified number of samples, converting between formats appropriately.