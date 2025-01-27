#### getSample()


template<typename SampleType > 

 SampleType dsp::AudioBlock< SampleType >::getSample ( int channel, int sampleIndex ) const noexcept 
 

Returns a sample from the buffer.The channel and index are not checked they are expected to be inrange. If not, an assertion will be thrown, but in a release build, you're into 'undefined behaviour' territory.References isPositiveAndBelow(), and jassert.