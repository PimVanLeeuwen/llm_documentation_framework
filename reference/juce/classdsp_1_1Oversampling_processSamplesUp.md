#### processSamplesUp()


template<typename SampleType > 

 AudioBlock< SampleType > dsp::Oversampling< SampleType >::processSamplesUp ( const AudioBlock< const SampleType > & inputBlock ) noexcept 
 

Must be called to perform the upsampling, prior to any oversampled processing.Returns an AudioBlock referencing the oversampled input signal, which must be used to perform the nonlinear processing which needs the higher sample rate. Don't forget to set the sample rate of that processing to N times the original sample rate.