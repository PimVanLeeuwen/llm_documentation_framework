#### createInstanceFromDescription() [2/2]


 std::unique\_ptr< AudioPluginInstance > AudioPluginFormat::createInstanceFromDescription ( const PluginDescription & , 
 
 double initialSampleRate, 
 int initialBufferSize, 
 String & errorMessage ) 

Same as above but with the possibility of returning an error message.See alsoAudioPluginFormatManager::createInstance