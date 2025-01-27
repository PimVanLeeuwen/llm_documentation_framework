#### convertJucePluginId()


 static InterfaceId VST3ClientExtensions::convertJucePluginId ( uint32\_t manufacturerCode, uint32\_t pluginCode, InterfaceType interfaceType = InterfaceType::component ) static 
 

Returns a 16byte array indicating the VST3 interface ID used for a given JUCE VST3 plugin.Internally this is what JUCE will use to assign an ID to each VST3 interface, unless JUCE\_VST3\_CAN\_REPLACE\_VST2 is enabled.See alsoconvertVST2PluginId, getCompatibleClasses, getCompatibleParameterIds