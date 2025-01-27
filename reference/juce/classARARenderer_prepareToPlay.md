#### prepareToPlay()


 virtual void ARARenderer::prepareToPlay ( double sampleRate, int maximumSamplesPerBlock, int numChannels, AudioProcessor::ProcessingPrecision precision, AlwaysNonRealtime alwaysNonRealtime = AlwaysNonRealtime::no ) virtual 
 

Initialises the renderer for playback.Parameters

 sampleRate The sample rate that will be used for the data that is sent to the renderer 
 
 maximumSamplesPerBlock The maximum number of samples that will be in the blocks sent to process() method 
 numChannels The number of channels that the process() method will be expected to handle 
 precision This should be the same as the result of getProcessingPrecision() for the enclosing AudioProcessor 
 alwaysNonRealtime yes if this renderer is never used in realtime (e.g. if providing data for views only)