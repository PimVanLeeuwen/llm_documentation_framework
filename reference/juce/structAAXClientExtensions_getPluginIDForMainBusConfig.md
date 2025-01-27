#### getPluginIDForMainBusConfig()


 virtual int32 AAXClientExtensions::getPluginIDForMainBusConfig ( const AudioChannelSet & mainInputLayout, const AudioChannelSet & mainOutputLayout, bool idForAudioSuite ) const virtual 
 

AAX plugins need to report a unique "plugin id" for every audio layout configuration that your AudioProcessor supports on the main bus.Override this function if you want your AudioProcessor to use a custom "plugin id" (for example to stay backward compatible with older versions of JUCE).The default implementation will compute a unique integer from the input and output layout and add this value to the 4 character code 'jcaa' (for native AAX) or 'jyaa' (for AudioSuite plugins).