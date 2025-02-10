#### setResonance()


template<typename SampleType > 

 void dsp::LadderFilter< SampleType >::setResonance ( SampleType newResonance ) noexcept 
 

Sets the resonance of the filter.Parameters

 newResonance a value between 0 and 1; higher values increase the resonance and can result in self oscillation!