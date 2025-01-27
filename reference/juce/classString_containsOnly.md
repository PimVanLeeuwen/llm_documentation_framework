#### containsOnly()


 bool String::containsOnly ( StringRef charactersItMightContain ) const noexcept 
 

Looks for a set of characters in the string.Uses a casesensitive comparison.ReturnsReturns false if any of the characters in this string do not occur in the parameter string. If this string is empty, the return value will always be true.