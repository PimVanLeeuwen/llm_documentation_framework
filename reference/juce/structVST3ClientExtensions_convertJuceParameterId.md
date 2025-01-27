#### convertJuceParameterId()


 static uint32\_t VST3ClientExtensions::convertJuceParameterId ( const String & parameterId, bool studioOneCompatible = true ) static 
 

Returns the VST3 compatible parameter ID reported for a given JUCE parameter.Internally JUCE will use this method to determine the Vst::ParamID for a HostedAudioProcessorParameter, unless JUCE\_FORCE\_LEGACY\_PARAM\_IDS is enabled, in which case it will use the parameter index.See alsogetCompatibleParameterIds