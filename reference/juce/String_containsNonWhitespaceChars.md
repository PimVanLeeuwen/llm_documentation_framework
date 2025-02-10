#### containsNonWhitespaceChars()


 bool String::containsNonWhitespaceChars ( ) const noexcept 
 

Returns true if this string contains any nonwhitespace characters.This will return false if the string contains only whitespace characters, or if it's empty.It is equivalent to calling "myString.trim().isNotEmpty()".