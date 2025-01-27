#### matchesIdentifierString()


 bool PluginDescription::matchesIdentifierString ( const String & identifierString ) const 
 

Return true if this description is equivalent to another one which created the given identifier string.Note that this isn't quite as simple as them just calling createIdentifierString() and comparing the strings, because the identifiers can differ (thanks to shell plugins).