#### createARAFactoryAsync()


 void AudioPluginFormatManager::createARAFactoryAsync ( const PluginDescription & description, 
 
 AudioPluginFormat::ARAFactoryCreationCallback callback ) const 

Tries to create an ARAFactoryWrapper for this description.The result of the operation will be wrapped into an ARAFactoryResult, which will be passed to a callback object supplied by the caller.The operation may fail, in which case the callback will be called with with a result object where ARAFactoryResult::araFactory.get() will return a nullptr.In case of success the returned ARAFactoryWrapper will ensure that modules required for the correct functioning of the ARAFactory will remain loaded for the lifetime of the object.