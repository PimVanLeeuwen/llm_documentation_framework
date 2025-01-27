#### fromBase64Encoding()


 bool MemoryBlock::fromBase64Encoding ( StringRef encodedString ) 
 

Takes a string created by MemoryBlock::toBase64Encoding() and extracts the original data.The string passed in must have been created by to64BitEncoding(), and this block will be resized to recreate the original data block.Note that these methods use a JUCEspecific (i.e. not standard!) 64bit encoding system. You may prefer to use the Base64::convertFromBase64() method if you want to use the standard base64 encoding.See alsotoBase64Encoding, Base64::convertFromBase64 Referenced by StandalonePluginHolder::reloadPluginState().