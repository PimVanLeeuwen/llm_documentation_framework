#### getCompatibleParameterIds()


 virtual std::map< uint32\_t, String > VST3ClientExtensions::getCompatibleParameterIds ( const InterfaceId & compatibleClass ) const virtual 
 

This function should return a map of VST3 parameter IDs and the JUCE parameters they map to.This information is used to implement the IRemapParameter interface. Hosts can use this to preserve automation data when a session was saved using a compatible plugin that has different parameter IDs.Not all hosts will take this information into account. Therefore, parameter IDs should be maintained between plugin versions. For JUCE plugins migrating from VST2 to VST3 the best method for achieving this is enabling JUCE\_FORCE\_LEGACY\_PARAM\_IDS. However, if a plugin has already been released without enabling this flag, this method offers an alternative approach that won't cause any further compatibility issues.The key in the map is a VST3 parameter identifier or Vst::ParamID. For VST2 or JUCE plugins these IDs can be determined in the following waysUse the parameter index forVST2 pluginsJUCE VST3 plugins with JUCE\_FORCE\_LEGACY\_PARAM\_IDS enabledAny parameter that doesn't inherit from HostedAudioProcessorParameterUse convertJuceParameterId() for JUCE VST3 plugins where JUCE\_FORCE\_LEGACY\_PARAM\_IDS is disabledThe value in the map is the JUCE parameter ID for the parameter to map to, or an empty string to indicate that there is no parameter to map to. If a parameter doesn't inherit from HostedAudioProcessorParameter its ID will be the parameter index as a string, for example "1". Otherwise always use the actual parameter ID (even if JUCE\_FORCE\_LEGACY\_PARAM\_IDS is enabled).In the unlikely event that two plugins share the same plugin ID, and both have a different parameters that share the same parameter ID, it may be possible to determine which version of the plugin is being loaded during setStateInformation(). This method will always be called after setStateInformation(), so that the map with the correct mapping can be provided when queried.Below is an example of how you might implement this function for a JUCE VST3 plugin where JUCE\_VST3\_CAN\_REPLACE\_VST2 is enabled, but JUCE\_FORCE\_LEGACY\_PARAM\_IDS is disabled.std::map<uint32\_t, String> getCompatibleParameterIds (const String&) const override
{
 return { { 0, "Frequency" },
 { 1, "CutOff" },
 { 2, "Gain" },
 { 3, "Bypass" } };
}
StringThe JUCE String class!Definition juce\_String.h:68
VST3ClientExtensions::getCompatibleParameterIdsvirtual std::map< uint32\_t, String > getCompatibleParameterIds(const InterfaceId &compatibleClass) constThis function should return a map of VST3 parameter IDs and the JUCE parameters they map to.
Parameters

 compatibleClass A plugin identifier, either for the current plugin or one listed in getCompatibleClasses(). This parameter allows the implementation to return a different parameter map for each compatible class. Use convertJucePluginId() and convertVST2PluginId() to determine the class IDs used by JUCE plugins. 
 



ReturnsA map where each key is a VST3 parameter ID in the compatible plugin, and the value is the unique JUCE parameter ID in the current plugin that it should be mapped to.
See alsogetCompatibleClasses, convertJucePluginId, convertVST2PluginId, convertJuceParameterId