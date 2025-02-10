#### getSiblingFile()


 File File::getSiblingFile ( StringRef siblingFileName ) const 
 

Returns a file which is in the same directory as this one.This is equivalent to getParentDirectory().getChildFile (name).See alsogetChildFile, getParentDirectory