#### addAudioCallback()


 void AudioDeviceManager::addAudioCallback ( AudioIODeviceCallback \* newCallback ) 
 

Registers an audio callback to be used.The manager will redirect callbacks from whatever audio device is currently in use to all registered callback objects. If more than one callback is active, they will all be given the same input data, and their outputs will be summed.If necessary, this method will invoke audioDeviceAboutToStart() on the callback object before returning.To remove a callback, use removeAudioCallback().