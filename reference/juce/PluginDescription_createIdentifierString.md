#### createIdentifierString()


 String PluginDescription::createIdentifierString ( ) const 
 

Returns a string that can be saved and used to uniquely identify the plugin again.This contains less info than the XML encoding, and is independent of the plugin's file location, so can be used to store a plugin ID for use across different machines.