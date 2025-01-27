#### setIComponentHandler()


 virtual void VST3ClientExtensions::setIComponentHandler ( Steinberg::FUnknown \* ) virtual 
 

This may be called by the VST3 wrapper when the host sets an IComponentHandler for the plugin to use.You should not make any assumptions about how and when this will be called this function may not be called at all!