#### restoreFromXml()


 bool KeyPressMappingSet::restoreFromXml ( const XmlElement & xmlVersion ) 
 

Tries to recreate the mappings from a previously stored state.The XML passed in must have been created by the createXml() method.If the stored state makes any reference to commands that aren't currently available, these will be ignored.If the set of mappings being loaded was a set of differences (using createXml (true)), then this will call resetToDefaultMappings() and then merge the saved mappings on top. If the saved set was created with createXml (false), then this method will first clear all existing mappings and load the saved ones as a complete set.Returnstrue if it manages to load the XML correctly 
See alsocreateXml