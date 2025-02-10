#### getAudioCallbackLock()


 CriticalSection & AudioDeviceManager::getAudioCallbackLock ( ) noexcept 
 

Returns the a lock that can be used to synchronise access to the audio callback.Obviously while this is locked, you're blocking the audio thread from running, so it must only be used for very brief periods when absolutely necessary.