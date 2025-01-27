#### compareAttribute()


 bool XmlElement::compareAttribute ( StringRef attributeName, StringRef stringToCompareAgainst, bool ignoreCase = false ) const noexcept 
 

Compares the value of a named attribute with a value passedin.Parameters

 attributeName the name of the attribute to look up 
 
 stringToCompareAgainst the value to compare it with 
 ignoreCase whether the comparison should be caseinsensitive 



Returnstrue if the value of the attribute is the same as the string passedin; false if it's different (or if no such attribute exists)