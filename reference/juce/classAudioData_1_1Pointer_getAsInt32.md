#### getAsInt32()


template<typename SampleFormat , typename Endianness , typename InterleavingType , typename Constness > 

 int32 AudioData::Pointer< SampleFormat, Endianness, InterleavingType, Constness >::getAsInt32 ( ) const noexcept 
 

Returns the value of the first sample as a 32bit integer.The value returned will be in the range 0x80000000 to 0x7fffffff, and shorter values will be shifted to fill this range (e.g. if you're reading from 24bit data, the values will be shifted up by 8 bits when returned here). If the source data is floating point, values beyond 1.0 to 1.0 will be clipped so that 1.0 maps onto 0x7fffffff and 1.0 maps to 0x7fffffff.Referenced by AudioData::Pointer< SampleFormat, Endianness, InterleavingType, Constness >::findMinAndMax().