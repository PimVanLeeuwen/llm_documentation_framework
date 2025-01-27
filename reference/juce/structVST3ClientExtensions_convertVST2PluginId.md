#### convertVST2PluginId()


 static InterfaceId VST3ClientExtensions::convertVST2PluginId ( uint32\_t pluginCode, const String & pluginName, InterfaceType interfaceType = InterfaceType::component ) static 
 

Returns a 16byte array indicating the VST3 interface ID used for a given VST2 plugin.Internally JUCE will use this method to assign an ID for the component and controller interfaces when JUCE\_VST3\_CAN\_REPLACE\_VST2 is enabled.See alsoconvertJucePluginId, getCompatibleClasses, getCompatibleParameterIds