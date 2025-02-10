#### setPlayConfigDetails()


 void AudioProcessor::setPlayConfigDetails ( int numIns, 
 
 int numOuts, 
 double sampleRate, 
 int blockSize ) 

This is called by the processor to specify its details before being played.Use this version of the function if you are not interested in any sidechain and/or aux buses and do not care about the layout of channels. Otherwise use setRateAndBufferSizeDetails.