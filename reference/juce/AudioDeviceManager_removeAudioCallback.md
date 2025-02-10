#### removeAudioCallback()


 void AudioDeviceManager::removeAudioCallback ( AudioIODeviceCallback \* callback ) 
 

Deregisters a previously added callback.If necessary, this method will invoke audioDeviceStopped() on the callback object before returning.See alsoaddAudioCallback