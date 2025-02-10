#### fromUTF32()


 static MD5 MD5::fromUTF32 ( StringRef ) static 
 

Creates an MD5 from a littleendian UTF32 encoded string.Note that this method is provided for backwardscompatibility with the old version of this class, which had a constructor that took a string and performed this operation on it. In new code, you shouldn't use this, and are recommended to use the constructor that takes a CharPointer\_UTF8 instead.