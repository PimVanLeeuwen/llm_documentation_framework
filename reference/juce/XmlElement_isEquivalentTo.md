#### isEquivalentTo()


 bool XmlElement::isEquivalentTo ( const XmlElement \* other, bool ignoreOrderOfAttributes ) const noexcept 
 

Compares two XmlElements to see if they contain the same text and attributes.The elements are only considered equivalent if they contain the same attributes with the same values, and have the same subnodes.Parameters

 other the other element to compare to 
 
 ignoreOrderOfAttributes if true, this means that two elements with the same attributes in a different order will be considered the same; if false, the attributes must be in the same order as well