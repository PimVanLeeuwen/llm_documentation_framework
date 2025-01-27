#### getTypeForIdentifierString()


 std::unique\_ptr< PluginDescription > KnownPluginList::getTypeForIdentifierString ( const String & identifierString ) const 
 

Looks for a type in the list which matches a plugin type ID.The identifierString parameter must have been created by PluginDescription::createIdentifierString().