#### getSubsetChannelBlock()


template<typename SampleType > 

 AudioBlock dsp::AudioBlock< SampleType >::getSubsetChannelBlock ( size\_t channelStart, size\_t numChannelsToUse ) const noexcept 
 

Returns a subset of contiguous channels.Parameters

 channelStart First channel of the subset 
 
 numChannelsToUse Count of channels in the subset 


References dsp::AudioBlock< SampleType >::AudioBlock, and jassert.