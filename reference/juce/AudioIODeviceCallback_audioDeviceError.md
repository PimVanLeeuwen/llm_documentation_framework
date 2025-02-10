#### audioDeviceError()


 virtual void AudioIODeviceCallback::audioDeviceError ( const String & errorMessage ) virtual 
 

This can be overridden to be told if the device generates an error while operating.Be aware that this could be called by any thread! And not all devices perform this callback.Reimplemented in SoundPlayer.