#### createNewChildElement()


 XmlElement \* XmlElement::createNewChildElement ( StringRef tagName ) 
 

Creates a new element with the given name and returns it, after adding it as a child element.This is a handy method that means that instead of writing this:XmlElement\* newElement = new XmlElement ("foobar");
myParentElement>addChildElement (newElement);
..you could just write this:XmlElement\* newElement = myParentElement>createNewChildElement ("foobar");
XmlElement::createNewChildElementXmlElement \* createNewChildElement(StringRef tagName)Creates a new element with the given name and returns it, after adding it as a child element.