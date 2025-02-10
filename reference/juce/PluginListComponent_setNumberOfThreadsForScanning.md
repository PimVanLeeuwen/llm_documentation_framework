#### setNumberOfThreadsForScanning()


 void PluginListComponent::setNumberOfThreadsForScanning ( int numThreads ) 
 

Sets how many threads to simultaneously scan for plugins.If this is 0, then all scanning happens on the message thread (this is the default when allowPluginsWhichRequireAsynchronousInstantiation is false). If allowPluginsWhichRequireAsynchronousInstantiation is true then numThreads must not be zero (it is one by default).