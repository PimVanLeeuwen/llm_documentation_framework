#### getTrailingIntValue()


 int String::getTrailingIntValue ( ) const noexcept 
 

Parses a decimal number from the end of the string.This will look for a value at the end of the string. e.g. for "321 xyz654" it will return 654; for "2 3 4" it'll return 4.If the string ends with a hyphen followed by numeric characters, the return value will be negative.See alsogetIntValue