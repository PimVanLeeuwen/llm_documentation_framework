#### getNextElement()


 XmlElement \* XmlElement::getNextElement ( ) const noexcept 
 

Returns the next of this element's siblings.This can be used for iterating an element's subelements, e.g.XmlElement\* child = myXmlDocument>getFirstChildElement();
 
while (child != nullptr)
{
 ...do stuff with this child..
 
 child = child>getNextElement();
}
XmlElement::getFirstChildElementXmlElement \* getFirstChildElement() const noexceptReturns the first of this element's subelements.Definition juce\_XmlElement.h:366
XmlElement::getNextElementXmlElement \* getNextElement() const noexceptReturns the next of this element's siblings.Definition juce\_XmlElement.h:394
Note that when iterating the child elements, some of them might be text elements as well as XML tags use isTextElement() to work this out.Also, it's much easier and neater to use this method indirectly via the getChildIterator() method.Returnsthe sibling element that follows this one, or a nullptr if this is the last element in its parent
See alsogetNextElement, isTextElement, getChildIterator Referenced by isValidXmlName().