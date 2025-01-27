#### setAsFloat()


template<typename SampleFormat , typename Endianness , typename InterleavingType , typename Constness > 

 void AudioData::Pointer< SampleFormat, Endianness, InterleavingType, Constness >::setAsFloat ( float newValue ) noexcept 
 

Sets the value of the first sample as a floating point value.(This method can only be used if the AudioData::NonConst option was used). The value should be in the range 1.0 to 1.0 for integer formats, values outside that range will be clipped. For floating point formats, any value passed in here will be written directly, although 1 to 1 is the standard range.