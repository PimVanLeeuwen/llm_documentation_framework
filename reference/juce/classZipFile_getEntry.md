#### getEntry() [2/2]


 const ZipEntry \* ZipFile::getEntry ( const String & fileName, bool ignoreCase = false ) const noexcept 
 

Returns a structure that describes one of the entries in the zip file.This uses a casesensitive comparison to look for a filename in the list of entries. It might return 0 if no match is found.See alsoZipFile::ZipEntry