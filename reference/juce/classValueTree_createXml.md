#### createXml()


 std::unique\_ptr< XmlElement > ValueTree::createXml ( ) const 
 

Creates an XmlElement that holds a complete image of this tree and all its children.If this tree is invalid, this may return nullptr. Otherwise, the XML that is produced can be used to recreate a similar tree by calling ValueTree::fromXml().See alsofromXml, toXmlString