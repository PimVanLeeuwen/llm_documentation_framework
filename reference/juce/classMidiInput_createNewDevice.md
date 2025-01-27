#### createNewDevice()


 static std::unique\_ptr< MidiInput > MidiInput::createNewDevice ( const String & deviceName, MidiInputCallback \* callback ) static 
 

This will try to create a new midi input device (only available on Linux, macOS and iOS).This will attempt to create a new midi input device with the specified name for other apps to connect to.NB if you are calling this method on iOS you must have enabled the "Audio Background Capability" setting in the iOS exporter otherwise this method will fail.Returns an empty object if a device can't be created.Parameters

 deviceName the name of the device to create 
 
 callback the object that will receive the midi messages from this device