#### getFormattedAddress()


 static String IPAddress::getFormattedAddress ( const String & unformattedAddress ) static 
 

Returns a formatted version of the provided IPv6 address conforming to RFC 5952 with leading zeros suppressed, lower case characters, and doublecolon notation used to represent contiguous 16bit fields of zeros.Parameters

 unformattedAddress the IPv6 address to be formatted