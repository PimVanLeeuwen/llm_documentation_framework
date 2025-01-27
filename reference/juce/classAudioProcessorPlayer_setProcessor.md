#### setProcessor()


 void AudioProcessorPlayer::setProcessor ( AudioProcessor \* processorToPlay ) 
 

Sets the processor that should be played.The processor that is passed in will not be deleted or owned by this object. To stop anything playing, pass a nullptr to this method.Referenced by StandalonePluginHolder::startPlaying(), and StandalonePluginHolder::stopPlaying().