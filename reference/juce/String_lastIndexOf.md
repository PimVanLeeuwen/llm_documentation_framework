#### lastIndexOf()


 int String::lastIndexOf ( StringRef textToLookFor ) const noexcept 
 

Searches for a substring inside this string (working backwards from the end of the string).Uses a casesensitive comparison.Returnsthe index of the start of the last occurrence of the substring within this string, or 1 if it's not found. If textToLookFor is an empty string, this will always return 1.