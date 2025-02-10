#### processSample() [2/2]


template<typename SampleType > 

 void dsp::LinkwitzRileyFilter< SampleType >::processSample ( int channel, 
 
 SampleType inputValue, 
 SampleType & outputLow, 
 SampleType & outputHigh ) 

Performs the filter operation on a single sample at a time, and returns both the lowpass and the highpass outputs of the TPT structure.