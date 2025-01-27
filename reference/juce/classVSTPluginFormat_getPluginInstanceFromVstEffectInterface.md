#### getPluginInstanceFromVstEffectInterface()


 static AudioPluginInstance \* VSTPluginFormat::getPluginInstanceFromVstEffectInterface ( void \* aEffect ) static 
 

Given a VstEffectInterface\* (aka vst::AEffect\*), this will return the juce AudioPluginInstance that is being used to wrap it.