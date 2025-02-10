#### audioDeviceError()


 void SoundPlayer::audioDeviceError ( const String & errorMessage ) overridevirtual 
 

This can be overridden to be told if the device generates an error while operating.Be aware that this could be called by any thread! And not all devices perform this callback.Reimplemented from AudioIODeviceCallback.