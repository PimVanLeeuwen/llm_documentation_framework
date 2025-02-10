#### setResamplingRatio()


 void ResamplingAudioSource::setResamplingRatio ( double samplesInPerOutputSample ) 
 

Changes the resampling ratio.(This value can be changed at any time, even while the source is running).Parameters

 samplesInPerOutputSample if set to 1.0, the input is passed through; higher values will speed it up; lower values will slow it down. The ratio must be greater than 0