#### getHexValue64()


 int64 String::getHexValue64 ( ) const noexcept 
 

Parses the string as a hexadecimal number.Nonhexadecimal characters in the string are ignored.If the string contains too many characters, then the lowest significant digits are returned, e.g. "ffff1234567812345678" would produce 0x1234567812345678.Returnsa 64bit number which is the value of the string in hex.