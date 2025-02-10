#### imageReceived()


 virtual void CameraDevice::Listener::imageReceived ( const Image & image ) pure virtual 
 

This method is called when a new image arrives.This may be called by any thread, so be careful about threadsafety, and make sure that you process the data as quickly as possible to avoid glitching!Simply add a listener to be continuously notified about new frames becoming available and remove the listener when you no longer need new frames.If you just need to take one picture, use takeStillPicture() instead.See alsoCameraDevice::takeStillPicture