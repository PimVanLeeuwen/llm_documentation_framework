#### processSamplesDown()


template<typename SampleType > 

 void dsp::Oversampling< SampleType >::processSamplesDown ( AudioBlock< SampleType > & outputBlock ) noexcept 
 

Must be called to perform the downsampling, after the upsampling and the nonlinear processing.The output signal is probably delayed by the internal latency of the whole oversampling behaviour, so don't forget to take this into account.