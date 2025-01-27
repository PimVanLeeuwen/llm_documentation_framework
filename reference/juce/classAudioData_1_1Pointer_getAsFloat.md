#### getAsFloat()


template<typename SampleFormat , typename Endianness , typename InterleavingType , typename Constness > 

 float AudioData::Pointer< SampleFormat, Endianness, InterleavingType, Constness >::getAsFloat ( ) const noexcept 
 

Returns the value of the first sample as a floating point value.The value will be in the range 1.0 to 1.0 for integer formats. For floating point formats, the value could be outside that range, although 1 to 1 is the standard range.Referenced by AudioData::Pointer< SampleFormat, Endianness, InterleavingType, Constness >::findMinAndMax().