#### isPlaying()


 virtual bool AudioIODevice::isPlaying ( ) pure virtual 
 

Returns true if the device is still calling back.The device might mysteriously stop, so this checks whether it's still playing.