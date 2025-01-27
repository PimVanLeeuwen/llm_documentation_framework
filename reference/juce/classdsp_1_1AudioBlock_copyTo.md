#### copyTo()


template<typename SampleType > 

 void dsp::AudioBlock< SampleType >::copyTo ( AudioBuffer< std::remove\_const\_t< NumericType > > & dst, 
 
 size\_t srcPos = 0, 
 size\_t dstPos = 0, 
 size\_t numElements = std::numeric\_limits<size\_t>::max() ) const 

Copies the values from this block to an AudioBuffer.All indices and sizes are in this AudioBlock's units, i.e. if SampleType is a SIMDRegister then incrementing dstPos by one will increase the sample position in the AudioBuffer's units by a factor of SIMDRegister<SampleType>::SIMDNumElements.References jmin().