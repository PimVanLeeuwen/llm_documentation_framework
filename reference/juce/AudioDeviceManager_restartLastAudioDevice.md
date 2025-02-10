#### restartLastAudioDevice()


 void AudioDeviceManager::restartLastAudioDevice ( ) 
 

Tries to reload the last audio device that was running.Note that this only reloads the last device that was running before closeAudioDevice() was called it doesn't reload any kind of savedstate, and can only be called after a device has been opened with setAudioDeviceSetup().If a device is already open, this call will do nothing.