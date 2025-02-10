#### getHexValue32()


 int String::getHexValue32 ( ) const noexcept 
 

Parses the string as a hexadecimal number.Nonhexadecimal characters in the string are ignored.If the string contains too many characters, then the lowest significant digits are returned, e.g. "ffff12345678" would produce 0x12345678.Returnsa 32bit number which is the value of the string in hex.