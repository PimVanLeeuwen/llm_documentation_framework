#### getVST3ClientExtensions()


 virtual VST3ClientExtensions \* AudioProcessor::getVST3ClientExtensions ( ) virtual 
 

Returns a nonowning pointer to an object that implements VST3 specific information regarding this AudioProcessor.By default, for backwards compatibility, this will attempt to dynamiccast this AudioProcessor to VST3ClientExtensions. It is recommended to override this function to return a pointer directly to an object of the correct type in order to avoid this dynamic cast.