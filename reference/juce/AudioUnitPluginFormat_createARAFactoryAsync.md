#### createARAFactoryAsync()


 void AudioUnitPluginFormat::createARAFactoryAsync ( const PluginDescription & , ARAFactoryCreationCallback callback ) overridevirtual 
 

Tries to create an ARAFactoryWrapper for this description.The result of the operation will be wrapped into an ARAFactoryResult, which will be passed to a callback object supplied by the caller.See alsoAudioPluginFormatManager::createARAFactoryAsync Reimplemented from AudioPluginFormat.