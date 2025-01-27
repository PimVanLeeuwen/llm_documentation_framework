#### indexOfChar() [2/2]


 int String::indexOfChar ( int startIndex, juce\_wchar characterToLookFor ) const noexcept 
 

Searches for a character inside this string.Uses a casesensitive comparison.Parameters

 startIndex the index from which the search should proceed 
 
 characterToLookFor the character to look for 



Returnsthe index of the first occurrence of the character in this string, or 1 if it's not found.