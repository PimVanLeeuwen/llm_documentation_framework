#### setPlayHead()


 virtual void AudioProcessor::setPlayHead ( AudioPlayHead \* newPlayHead ) virtual 
 

Tells the processor to use this playhead object.The processor will not take ownership of the object, so the caller must delete it when it is no longer being used.Referenced by StandalonePluginHolder::startPlaying().