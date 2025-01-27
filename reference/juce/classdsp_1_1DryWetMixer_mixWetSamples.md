#### mixWetSamples()


template<typename SampleType > 

 void dsp::DryWetMixer< SampleType >::mixWetSamples ( AudioBlock< SampleType > wetSamples ) 
 

Mixes the supplied wet samples with the latencycompensated dry samples from pushDrySamples.Parameters

 wetSamples Input: The AudioBlock references fully wet samples. Output: The AudioBlock references the wet samples mixed with the latency compensated dry samples. 
 



See alsopushDrySamples