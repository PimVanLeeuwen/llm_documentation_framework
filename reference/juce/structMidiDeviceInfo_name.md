#### name


 String MidiDeviceInfo::name 
 

The name of this device.This will be provided by the OS unless the device has been created with the createNewDevice() method.Note that the name is not guaranteed to be unique and two devices with the same name will be indistinguishable. If you want to address a specific device it is better to use the identifier.Referenced by tie().