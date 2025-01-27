#### getExtensions()


 virtual void AudioPluginInstance::getExtensions ( ExtensionsVisitor & ) const virtual 
 

Allows retrieval of information related to the inner workings of a particular plugin format, such as the AEffect\* of a VST, or the handle of an AudioUnit.To use this, create a new class derived from ExtensionsVisitor, and override each of the visit member functions. If this AudioPluginInstance wraps a VST3 plugin the visitVST3() member will be called, while if the AudioPluginInstance wraps an unknown format the visitUnknown() member will be called. The argument of the visit function can be queried to extract information related to the AudioPluginInstance's implementation.