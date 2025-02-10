#### getDefaultMidiOutput()


 MidiOutput \* AudioDeviceManager::getDefaultMidiOutput ( ) const noexcept 
 

Returns the current default midi output device.If no device has been selected, or the device can't be opened, this will return nullptr.See alsogetDefaultMidiOutputIdentifier