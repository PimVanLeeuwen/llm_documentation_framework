#### aboutToScanVSTShellPlugin()


 virtual void VSTPluginFormat::aboutToScanVSTShellPlugin ( const PluginDescription & ) virtual 
 

Can be overridden to receive a callback when each member of a shell plugin is about to be tested during a call to findAllTypesForFile().Only the name and uid members of the PluginDescription are guaranteed to be valid when this is called.