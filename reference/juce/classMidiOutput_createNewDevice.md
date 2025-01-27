#### createNewDevice()


 static std::unique\_ptr< MidiOutput > MidiOutput::createNewDevice ( const String & deviceName ) static 
 

This will try to create a new midi output device (only available on Linux, macOS and iOS).This will attempt to create a new midi output device with the specified name that other apps can connect to and use as their midi input.NB if you are calling this method on iOS you must have enabled the "Audio Background Capability" setting in the iOS exporter otherwise this method will fail.Returns an empty object if a device can't be created.Parameters

 deviceName the name of the device to create