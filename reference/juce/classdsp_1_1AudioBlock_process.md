#### process()


template<typename SampleType > 
template<typename Src1SampleType , typename Src2SampleType , typename FunctionType > 

 static void dsp::AudioBlock< SampleType >::process ( AudioBlock< Src1SampleType > inBlock, AudioBlock< Src2SampleType > outBlock, FunctionType && function ) static 
 

Applies a function to each value in an input block, putting the result into an output block.The function supplied must take a SampleType as its parameter, and return a SampleType. The two blocks must have the same number of channels and samples.References dsp::AudioBlock< SampleType >::getChannelPointer(), dsp::AudioBlock< SampleType >::getNumChannels(), dsp::AudioBlock< SampleType >::getNumSamples(), and jassert.Referenced by dsp::WaveShaper< FloatType, Function >::process().