#### setAudioPreprocessingEnabled()


 virtual bool AudioIODevice::setAudioPreprocessingEnabled ( bool shouldBeEnabled ) virtual 
 

On devices which support it, this allows automatic gain control or other mic processing to be disabled.If the device doesn't support this operation, it'll return false.