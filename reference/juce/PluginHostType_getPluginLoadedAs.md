#### getPluginLoadedAs()


 static AudioProcessor::WrapperType PluginHostType::getPluginLoadedAs ( ) staticnoexcept 
 

Returns the plugin format via which the plugin file was loaded.This value is identical to AudioProcessor::wrapperType of the main audio processor of this plugin. This function is useful for code that does not have access to the plugin's main audio processor.See alsoAudioProcessor::wrapperType