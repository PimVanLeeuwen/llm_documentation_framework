#### createPluginInstanceAsync()


 void AudioPluginFormatManager::createPluginInstanceAsync ( const PluginDescription & description, 
 
 double initialSampleRate, 
 int initialBufferSize, 
 AudioPluginFormat::PluginCreationCallback callback ) 

Tries to asynchronously load the type for this description, by trying all the formats that this manager knows about.The caller must supply a callback object which will be called when the instantiation has completed.If it can't load the plugin then the callback function will be called passing a nullptr as the instance argument along with an error message.The callback function will be called on the message thread so the caller must not block the message thread.The callback object will be deleted automatically after it has been invoked.The caller is responsible for deleting the instance that is passed to the callback function.If you intend to instantiate a AudioUnit v3 plugin then you must use this nonblocking asynchronous version or call the synchronous method from an auxiliary thread.