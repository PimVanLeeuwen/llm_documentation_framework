#### initialise()


 String AudioDeviceManager::initialise ( int numInputChannelsNeeded, 
 
 int numOutputChannelsNeeded, 
 const XmlElement \* savedState, 
 bool selectDefaultDeviceOnFailure, 
 const String & preferredDefaultDeviceName = String(), 
 const AudioDeviceSetup \* preferredSetupOptions = nullptr ) 

Opens a set of audio devices ready for use.This will attempt to open either a default audio device, or one that was previously saved as XML.Parameters

 numInputChannelsNeeded the maximum number of input channels your app would like to use (the actual number of channels opened may be less than the number requested) 
 
 numOutputChannelsNeeded the maximum number of output channels your app would like to use (the actual number of channels opened may be less than the number requested) 
 savedState either a previouslysaved state that was produced by createStateXml(), or nullptr if you want the manager to choose the best device to open. 
 selectDefaultDeviceOnFailure if true, then if the device specified in the XML fails to open, then a default device will be used instead. If false, then on failure, no device is opened. 
 preferredDefaultDeviceName if this is not empty, and there's a device with this name, then that will be used as the default device (assuming that there wasn't one specified in the XML). The string can actually be a simple wildcard, containing "\*" and "?" characters 
 preferredSetupOptions if this is nonnull, the structure will be used as the set of preferred settings when opening the device. If you use this parameter, the preferredDefaultDeviceName field will be ignored. If you set the outputDeviceName or inputDeviceName data members of the AudioDeviceSetup to empty strings, then a default device will be used. 



Returnsan error message if anything went wrong, or an empty string if it worked ok. Referenced by StandalonePluginHolder::reloadAudioDeviceState().