#### getChildIterator()


 Iterator< GetNextElement > XmlElement::getChildIterator ( ) const 
 

Allows iterating the children of an XmlElement using rangefor syntax.void doSomethingWithXmlChildren (const XmlElement& myParentXml)
{
 for (auto\* element : myParentXml.getChildIterator())
 doSomethingWithXmlElement (element);
}
XmlElement::getChildIteratorIterator< GetNextElement > getChildIterator() constAllows iterating the children of an XmlElement using rangefor syntax.Definition juce\_XmlElement.h:730