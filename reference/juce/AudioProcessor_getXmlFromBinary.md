#### getXmlFromBinary()


 static std::unique\_ptr< XmlElement > AudioProcessor::getXmlFromBinary ( const void \* data, int sizeInBytes ) static 
 

Retrieves an XML element that was stored as binary with the copyXmlToBinary() method.This might return nullptr if the data's unsuitable or corrupted.