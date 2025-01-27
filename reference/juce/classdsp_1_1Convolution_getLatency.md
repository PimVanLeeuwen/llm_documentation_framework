#### getLatency()


 int dsp::Convolution::getLatency ( ) const 
 

This function returns the current latency of the process in samples.Note: This is the latency of the convolution engine, not the latency associated with the current impulse response choice that has to be considered separately (linear phase filters, for example).