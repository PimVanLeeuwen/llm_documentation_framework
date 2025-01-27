#### loadFromHexString()


 void MemoryBlock::loadFromHexString ( StringRef sourceHexString ) 
 

Parses a string of hexadecimal numbers and writes this data into the memory block.The block will be resized to the number of valid bytes read from the string. Nonhex characters in the string will be ignored.See alsoString::toHexString()