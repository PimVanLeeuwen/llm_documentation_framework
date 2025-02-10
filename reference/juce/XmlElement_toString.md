#### toString()


 String XmlElement::toString ( const TextFormat & format = {} ) const 
 

Returns a text version of this XML element.If your intention is to write the XML to a file or stream, it's probably more efficient to use writeTo() instead of creating an intermediate string.See alsowriteTo