#### stop()


 virtual void AudioIODevice::stop ( ) pure virtual 
 

Stops the device playing.Once a device has been started, this will stop it. Any pending calls to the callback class will be flushed before this method returns.