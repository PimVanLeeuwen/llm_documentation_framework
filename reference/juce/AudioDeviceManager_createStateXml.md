#### createStateXml()


 std::unique\_ptr< XmlElement > AudioDeviceManager::createStateXml ( ) const 
 

Returns some XML representing the current state of the manager.This stores the current device, its samplerate, block size, etc, and can be restored later with initialise().Note that this can return a null pointer if no settings have been explicitly changed (i.e. if the device manager has just been left in its default state).Referenced by StandalonePluginHolder::saveAudioDeviceState().