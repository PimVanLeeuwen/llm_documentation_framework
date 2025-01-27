#### setIHostApplication()


 virtual void VST3ClientExtensions::setIHostApplication ( Steinberg::FUnknown \* ) virtual 
 

This may be called shortly after the AudioProcessor is constructed with the current IHostApplication.You should not make any assumptions about how and when this will be called this function may not be called at all!