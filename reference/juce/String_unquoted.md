#### unquoted()


 String String::unquoted ( ) const 
 

Removes quotation marks from around the string, (if there are any).Returns a copy of this string with any quotes removed from its ends. Quotes that aren't at the ends of the string are not affected. If there aren't any quotes, the original string is returned.Note that this is a const method, and won't alter the string itself.See alsoisQuotedString, quoted