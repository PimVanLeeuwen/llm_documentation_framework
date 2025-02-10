#### getChannelPointer()


template<typename SampleType > 

 SampleType \* dsp::AudioBlock< SampleType >::getChannelPointer ( size\_t channel ) const noexcept 
 

Returns a raw pointer into one of the channels in this block.References jassert.Referenced by dsp::AudioBlock< SampleType >::process().