#### setRateAndBufferSizeDetails()


 void AudioProcessor::setRateAndBufferSizeDetails ( double sampleRate, int blockSize ) noexcept 
 

This is called by the processor to specify its details before being played.You should call this function after having informed the processor about the channel and bus layouts via setBusesLayout.See alsosetBusesLayout