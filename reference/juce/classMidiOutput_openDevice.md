#### openDevice()


 static std::unique\_ptr< MidiOutput > MidiOutput::openDevice ( const String & deviceIdentifier ) static 
 

Tries to open one of the midi output devices.This will return a MidiOutput object if it manages to open it, you can then send messages to this device.If the device can't be opened, this will return an empty object.Parameters

 deviceIdentifier the ID of the device to open use the getAvailableDevices() method to find the available devices that can be opened 
 



See alsogetDevices