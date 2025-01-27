#### lastIndexOfChar()


 int String::lastIndexOfChar ( juce\_wchar character ) const noexcept 
 

Searches for a character inside this string (working backwards from the end of the string).Uses a casesensitive comparison.Returnsthe index of the last occurrence of the character in this string, or 1 if it's not found.