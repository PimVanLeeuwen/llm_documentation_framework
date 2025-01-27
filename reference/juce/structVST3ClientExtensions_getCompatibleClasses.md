#### getCompatibleClasses()


 virtual std::vector< InterfaceId > VST3ClientExtensions::getCompatibleClasses ( ) const virtual 
 

This function should return the UIDs of any compatible VST2 or VST3 plugins.This information will be used to implement the IPluginCompatibility interface. Hosts can use this interface to determine whether this VST3 is capable of replacing a given VST2.Each compatible class is a 16byte array that corresponds to the VST3 interface ID for the class implementing the IComponent interface. For VST2 or JUCE plugins these IDs can be determined in the following ways:Use convertVST2PluginId() for VST2 plugins or JUCE VST3 plugins with JUCE\_VST3\_CAN\_REPLACE\_VST3 enabledUse convertJucePluginId() for any other JUCE VST3 pluginsIf JUCE\_VST3\_CAN\_REPLACE\_VST2 is enabled the VST3 plugin will have the same identifier as the VST2 plugin and therefore there will be no need to implement this function.If the parameter IDs between compatible versions differ getCompatibleParameterIds() should also be overridden. However, unlike getCompatibleParameterIds() this function should remain constant and always return the same IDs.See alsogetCompatibleParameterIds()