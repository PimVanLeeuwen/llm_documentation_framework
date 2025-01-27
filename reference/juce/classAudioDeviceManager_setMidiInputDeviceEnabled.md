#### setMidiInputDeviceEnabled()


 void AudioDeviceManager::setMidiInputDeviceEnabled ( const String & deviceIdentifier, 
 
 bool enabled ) 

Enables or disables a midi input device.The list of devices can be obtained with the MidiInput::getAvailableDevices() method.Any incoming messages from enabled input devices will be forwarded on to all the listeners that have been registered with the addMidiInputDeviceCallback() method. They can either register for messages from a particular device, or from just the "default" midi input.Routing the midi input via an AudioDeviceManager means that when a listener registers for the default midi input, this default device can be changed by the manager without the listeners having to know about it or reregister.It also means that a listener can stay registered for a midi input that is disabled or not present, so that when the input is reenabled, the listener will start receiving messages again.See alsoaddMidiInputDeviceCallback, isMidiInputDeviceEnabled