#### getXmlValue()


 std::unique\_ptr< XmlElement > PropertySet::getXmlValue ( StringRef keyName ) const 
 

Returns one of the properties as an XML element.The result will a new XMLElement object. It may return nullptr if the key isn't found, or if the entry contains an string that isn't valid XML.If the value isn't found in this set, then this will look for it in a fallback property set (if you've specified one with the setFallbackPropertySet() method), and if it can't find one there, it'll return the default value passedin.Parameters

 keyName the name of the property to retrieve 
 


Referenced by StandalonePluginHolder::reloadAudioDeviceState().