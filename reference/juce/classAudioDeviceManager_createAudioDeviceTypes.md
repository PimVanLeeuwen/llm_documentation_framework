#### createAudioDeviceTypes()


 virtual void AudioDeviceManager::createAudioDeviceTypes ( OwnedArray< AudioIODeviceType > & types ) virtual 
 

Creates a list of available types.This will add a set of new AudioIODeviceType objects to the specified list, to represent each available types of device.You can override this if your app needs to do something specific, like avoid using DirectSound devices, etc.