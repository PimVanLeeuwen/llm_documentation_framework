#### addSample()


template<typename SampleType > 

 void dsp::AudioBlock< SampleType >::addSample ( int destChannel, int destSample, SampleType valueToAdd ) const noexcept 
 

Adds a value to a sample in the buffer.The channel and index are not checked they are expected to be inrange. If not, an assertion will be thrown, but in a release build, you're into 'undefined behaviour' territory.References isPositiveAndBelow(), and jassert.