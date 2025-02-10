#### getIndexOfFileName()


 int ZipFile::getIndexOfFileName ( const String & fileName, bool ignoreCase = false ) const noexcept 
 

Returns the index of the first entry with a given filename.This uses a casesensitive comparison to look for a filename in the list of entries. It might return 1 if no match is found.See alsoZipFile::ZipEntry