#### open()


 virtual String AudioIODevice::open ( const BigInteger & inputChannels, const BigInteger & outputChannels, double sampleRate, int bufferSizeSamples ) pure virtual 
 

Tries to open the device ready to play.Parameters

 inputChannels a BigInteger in which a set bit indicates that the corresponding input channel should be enabled 
 
 outputChannels a BigInteger in which a set bit indicates that the corresponding output channel should be enabled 
 sampleRate the sample rate to try to use to find out which rates are available, see getAvailableSampleRates() 
 bufferSizeSamples the size of i/o buffer to use to find out the available buffer sizes, see getAvailableBufferSizes() 



Returnsan error description if there's a problem, or an empty string if it succeeds in opening the device 
See alsoclose