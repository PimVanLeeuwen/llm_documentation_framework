#### hasTagNameIgnoringNamespace()


 bool XmlElement::hasTagNameIgnoringNamespace ( StringRef possibleTagName ) const 
 

Tests whether this element has a particular tag name, ignoring any XML namespace prefix.So a test for e.g. "xyz" will return true for "xyz" and also "foo:xyz", "bar::xyz", etc.See alsogetTagName