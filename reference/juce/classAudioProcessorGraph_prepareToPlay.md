#### prepareToPlay()


 void AudioProcessorGraph::prepareToPlay ( double sampleRate, int maximumExpectedSamplesPerBlock ) overridevirtual 
 

Called before playback starts, to let the processor prepare itself.The sample rate is the target sample rate, and will remain constant until playback stops.You can call getTotalNumInputChannels and getTotalNumOutputChannels or query the busLayout member variable to find out the number of channels your processBlock callback must process.The maximumExpectedSamplesPerBlock value is a strong hint about the maximum number of samples that will be provided in each block. You may want to use this value to resize internal buffers. You should program defensively in case a buggy host exceeds this value. The actual block sizes that the host uses may be different each time the callback happens: completely variable block sizes can be expected from some hosts.See alsobusLayout, getTotalNumInputChannels, getTotalNumOutputChannels Implements AudioProcessor.