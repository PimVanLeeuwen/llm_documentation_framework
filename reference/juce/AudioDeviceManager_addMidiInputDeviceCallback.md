#### addMidiInputDeviceCallback()


 void AudioDeviceManager::addMidiInputDeviceCallback ( const String & deviceIdentifier, 
 
 MidiInputCallback \* callback ) 

Registers a listener for callbacks when midi events arrive from a midi input.The device identifier can be empty to indicate that it wants to receive all incoming events from all the enabled MIDI inputs. Or it can be the identifier of one of the MIDI input devices if it just wants the events from that device. (see MidiInput::getAvailableDevices() for the list of devices).Only devices which are enabled (see the setMidiInputDeviceEnabled() method) will have their events forwarded on to listeners.