#### getSubBlock() [2/2]


template<typename SampleType > 

 AudioBlock dsp::AudioBlock< SampleType >::getSubBlock ( size\_t newOffset ) const noexcept 
 

Return a new AudioBlock pointing to a subblock inside this block.This function does not copy the memory and you must ensure that the original memory pointed to by the receiver remains valid throughout the lifetime of the returned subblock.Parameters

 newOffset The index of an element inside the block which will will become the first element of the return value. The return value will include all subsequent elements of the receiver. 
 


References dsp::AudioBlock< SampleType >::getNumSamples(), and dsp::AudioBlock< SampleType >::getSubBlock().