#### createPluginInstance()


 virtual void AudioPluginFormat::createPluginInstance ( const PluginDescription & , double initialSampleRate, int initialBufferSize, PluginCreationCallback ) protectedpure virtual 
 

Implementors must override this function.This is guaranteed to be called on the message thread. You may call the callback on any thread.