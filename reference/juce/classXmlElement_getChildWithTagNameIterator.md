#### getChildWithTagNameIterator()


 Iterator< GetNextElementWithTagName > XmlElement::getChildWithTagNameIterator ( StringRef name ) const 
 

Allows iterating children of an XmlElement with a specific tag using rangefor syntax.void doSomethingWithXmlChildren (const XmlElement& myParentXml)
{
 for (auto\* element : myParentXml.getChildWithTagNameIterator ("MYTAG"))
 doSomethingWithXmlElement (element);
}
XmlElement::getChildWithTagNameIteratorIterator< GetNextElementWithTagName > getChildWithTagNameIterator(StringRef name) constAllows iterating children of an XmlElement with a specific tag using rangefor syntax.Definition juce\_XmlElement.h:745
References name.