#### createXml()


 std::unique\_ptr< XmlElement > KeyPressMappingSet::createXml ( bool saveDifferencesFromDefaultSet ) const 
 

Creates an XML representation of the current mappings.This will produce a lump of XML that can be later reloaded using restoreFromXml() to recreate the current mapping state.Parameters

 saveDifferencesFromDefaultSet if this is false, then all keypresses will be saved into the XML. If it's true, then the XML will only store the differences between the current mappings and the default mappings you'd get from calling resetToDefaultMappings(). The advantage of saving a set of differences from the default is that if you change the default mappings (in a new version of your app, for example), then these will be merged into a user's saved preferences. 
 



See alsorestoreFromXml