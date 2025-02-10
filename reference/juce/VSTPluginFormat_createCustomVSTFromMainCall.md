#### createCustomVSTFromMainCall()


 static AudioPluginInstance \* VSTPluginFormat::createCustomVSTFromMainCall ( void \* entryPointFunction, double initialSampleRate, int initialBufferSize ) static 
 

Given a suitable function pointer to a VSTPluginMain function, this will attempt to instantiate and return a plugin for it.