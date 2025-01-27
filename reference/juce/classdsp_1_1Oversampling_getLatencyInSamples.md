#### getLatencyInSamples()


template<typename SampleType > 

 SampleType dsp::Oversampling< SampleType >::getLatencyInSamples ( ) const noexcept 
 

Returns the latency in samples of the overall processing.You can use this information in your main processor to compensate the additional latency involved with the oversampling, for example with a dry / wet mixer, and to report the latency to the DAW.Note: If you have not opted to use an integer latency then the latency may not be integer, so you might need to round its value or to compensate it properly in your processing code since plugins can only report integer latency values in samples to the DAW.