#### renderNextSubBlock() [2/2]


 void MPESynthesiser::renderNextSubBlock ( AudioBuffer< double > & outputAudio, int startSample, int numSamples ) overrideprotectedvirtual 
 

This will simply call renderNextBlock for each currently active voice and fill the buffer with the sum.(doubleprecision version) Override this method if you need to do more work to render your audio.Reimplemented from MPESynthesiserBase.