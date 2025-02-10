#### getLatencySamples()


 int AudioProcessor::getLatencySamples ( ) const noexcept 
 

This returns the number of samples delay that the processor imposes on the audio passing through it.The host will call this to find the latency the processor itself should set this value by calling setLatencySamples() as soon as it can during its initialisation.