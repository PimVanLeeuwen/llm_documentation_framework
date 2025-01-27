#### setAudioDeviceSetup()


 String AudioDeviceManager::setAudioDeviceSetup ( const AudioDeviceSetup & newSetup, 
 
 bool treatAsChosenDevice ) 

Changes the current device or its settings.If you want to change a device property, like the current sample rate or block size, you can call getAudioDeviceSetup() to retrieve the current settings, then tweak the appropriate fields in the AudioDeviceSetup structure, and pass it back into this method to apply the new settings.Parameters

 newSetup the settings that you'd like to use. If you don't need an input or output device, set the inputDeviceName or outputDeviceName data members respectively to empty strings. Note that this behaviour differs from the behaviour of initialise(). 
 
 treatAsChosenDevice if this is true and if the device opens correctly, these new settings will be taken as having been explicitly chosen by the user, and the next time createStateXml() is called, these settings will be returned. If it's false, then the device is treated as a temporary or default device, and a call to createStateXml() will return either the last settings that were made with treatAsChosenDevice as true, or the last XML settings that were passed into initialise(). 



Returnsan error message if anything went wrong, or an empty string if it worked ok.
See alsogetAudioDeviceSetup