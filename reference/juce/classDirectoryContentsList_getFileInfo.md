#### getFileInfo()


 bool DirectoryContentsList::getFileInfo ( int index, 
 
 FileInfo & resultInfo ) const 

Returns the cached information about one of the files in the list.If the index is inrange, this will return true and will copy the file's details to the structure that is passedin.If it returns false, then the index wasn't in range, and the structure won't be affected.See alsogetNumFiles, getFile