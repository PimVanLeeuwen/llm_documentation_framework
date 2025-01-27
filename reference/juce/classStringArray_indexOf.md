#### indexOf()


 int StringArray::indexOf ( StringRef stringToLookFor, 
 
 bool ignoreCase = false, 
 int startIndex = 0 ) const 

Searches for a string in the array.The comparison will be caseinsensitive if the ignoreCase parameter is true.Parameters

 stringToLookFor the string to try to find 
 
 ignoreCase whether the comparison should be caseinsensitive 
 startIndex the first index to start searching from 



Returnsthe index of the first occurrence of the string in this array, or 1 if it isn't found.