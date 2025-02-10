#### reloadAudioDeviceState()


 void StandalonePluginHolder::reloadAudioDeviceState ( bool enableAudioInput, 
 
 const String & preferredDefaultDeviceName, 
 const AudioDeviceManager::AudioDeviceSetup \* preferredSetupOptions ) 

References deviceManager, PropertySet::getBoolValue(), getNumInputChannels(), getNumOutputChannels(), PropertySet::getXmlValue(), AudioDeviceManager::initialise(), AudioProcessor::isMidiEffect(), processor, settings, Value::setValue(), and shouldMuteInput.