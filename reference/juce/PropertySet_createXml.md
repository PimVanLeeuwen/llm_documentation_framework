#### createXml()


 std::unique\_ptr< XmlElement > PropertySet::createXml ( const String & nodeName ) const 
 

Returns an XML element which encapsulates all the items in this property set.The string parameter is the tag name that should be used for the node.See alsorestoreFromXml