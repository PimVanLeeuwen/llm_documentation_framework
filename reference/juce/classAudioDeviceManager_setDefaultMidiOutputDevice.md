#### setDefaultMidiOutputDevice()


 void AudioDeviceManager::setDefaultMidiOutputDevice ( const String & deviceIdentifier ) 
 

Sets a midi output device to use as the default.The list of devices can be obtained with the MidiOutput::getAvailableDevices() method.The specified device will be opened automatically and can be retrieved with the getDefaultMidiOutput() method.Pass in an empty string to deselect all devices. For the default device, you can use MidiOutput::getDefaultDevice().See alsogetDefaultMidiOutput, getDefaultMidiOutputIdentifier