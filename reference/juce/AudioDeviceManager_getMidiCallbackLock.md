#### getMidiCallbackLock()


 CriticalSection & AudioDeviceManager::getMidiCallbackLock ( ) noexcept 
 

Returns the a lock that can be used to synchronise access to the midi callback.Obviously while this is locked, you're blocking the midi system from running, so it must only be used for very brief periods when absolutely necessary.