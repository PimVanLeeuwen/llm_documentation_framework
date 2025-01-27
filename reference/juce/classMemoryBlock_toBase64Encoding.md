#### toBase64Encoding()


 String MemoryBlock::toBase64Encoding ( ) const 
 

Returns a string of characters in a JUCEspecific text encoding that represents the binary contents of this block.This uses a JUCEspecific (i.e. not standard!) 64bit encoding system to convert binary data into a string of ASCII characters for purposes like storage in XML. Note that this proprietary format is mainly kept here for backwardscompatibility, and you may prefer to use the Base64::toBase64() method if you want to use the standard base64 encoding.See alsofromBase64Encoding, Base64::toBase64, Base64::convertToBase64 Referenced by StandalonePluginHolder::savePluginState().