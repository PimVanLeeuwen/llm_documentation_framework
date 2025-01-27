#### setWetLatency()


template<typename SampleType > 

 void dsp::DryWetMixer< SampleType >::setWetLatency ( SampleType wetLatencyInSamples ) 
 

Sets the relative latency of the wet signal path compared to the dry signal path, and thus the amount of latency compensation that will be added to the dry samples in this processor.