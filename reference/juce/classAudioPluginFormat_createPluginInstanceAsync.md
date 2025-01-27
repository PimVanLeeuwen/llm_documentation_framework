#### createPluginInstanceAsync()


 void AudioPluginFormat::createPluginInstanceAsync ( const PluginDescription & description, 
 
 double initialSampleRate, 
 int initialBufferSize, 
 PluginCreationCallback ) 

Tries to recreate a type from a previously generated PluginDescription.When the plugin has been created, it will be passed to the caller via an asynchronous call to the PluginCreationCallback lambda that was provided.See alsoAudioPluginFormatManager::createPluginInstanceAsync