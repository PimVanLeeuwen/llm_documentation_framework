#### openDevice()


 static std::unique\_ptr< MidiInput > MidiInput::openDevice ( const String & deviceIdentifier, MidiInputCallback \* callback ) static 
 

Tries to open one of the midi input devices.This will return a MidiInput object if it manages to open it, you can then call start() and stop() on this device.If the device can't be opened, this will return an empty object.Parameters

 deviceIdentifier the ID of the device to open use the getAvailableDevices() method to find the available devices that can be opened 
 
 callback the object that will receive the midi messages from this device 



See alsoMidiInputCallback, getDevices