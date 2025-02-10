#### setLatencySamples()


 void AudioProcessor::setLatencySamples ( int newLatency ) 
 

Your processor subclass should call this to set the number of samples delay that it introduces.The processor should call this as soon as it can during initialisation, and can call it later if the value changes.