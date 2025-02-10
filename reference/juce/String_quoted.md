#### quoted()


 String String::quoted ( juce\_wchar quoteCharacter = '"' ) const 
 

Adds quotation marks around a string.This will return a copy of the string with a quote at the start and end, (but won't add the quote if there's already one there, so it's safe to call this on strings that may already have quotes around them).Note that this is a const method, and won't alter the string itself.Parameters

 quoteCharacter the character to add at the start and end 
 



See alsoisQuotedString, unquoted