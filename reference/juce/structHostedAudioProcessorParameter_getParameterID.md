#### getParameterID()


 virtual String HostedAudioProcessorParameter::getParameterID ( ) const pure virtual 
 

Returns an ID that is unique to this parameter.Parameter indices are unstable across plugin versions, which means that the parameter found at a particular index in one version of a plugin might move to a different index in the subsequent version.Unlike the parameter index, the ID returned by this function should be somewhat stable (depending on the format of the plugin), so it is more suitable for storing/recalling automation data.Implemented in AudioProcessorParameterWithID.