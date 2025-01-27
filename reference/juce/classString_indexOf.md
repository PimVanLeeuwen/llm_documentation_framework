#### indexOf() [2/2]


 int String::indexOf ( int startIndex, StringRef textToLookFor ) const noexcept 
 

Searches for a substring within this string.Uses a casesensitive comparison.Parameters

 startIndex the index from which the search should proceed 
 
 textToLookFor the string to search for 



Returnsthe index of the first occurrence of this substring, or 1 if it's not found. If textToLookFor is an empty string, this will always return 1.