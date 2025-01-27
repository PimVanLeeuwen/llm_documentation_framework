#### createPluginInstance()


 std::unique\_ptr< AudioPluginInstance > AudioPluginFormatManager::createPluginInstance ( const PluginDescription & description, 
 
 double initialSampleRate, 
 int initialBufferSize, 
 String & errorMessage ) const 

Tries to load the type for this description, by trying all the formats that this manager knows about.If it can't load the plugin, it returns nullptr and leaves a message in the errorMessage string.If you intend to instantiate a AudioUnit v3 plugin then you must either use the nonblocking asynchronous version below or call this method from a thread other than the message thread and without blocking the message thread.