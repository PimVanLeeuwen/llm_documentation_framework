#### isFileInPath()


 bool FileSearchPath::isFileInPath ( const File & fileToCheck, 
 
 bool checkRecursively ) const 

Finds out whether a file is inside one of the path's directories.This will return true if the specified file is a child of one of the directories specified by this path. Note that this doesn't actually do any searching or check that the files exist it just looks at the pathnames to work out whether the file would be inside a directory.Parameters

 fileToCheck the file to look for 
 
 checkRecursively if true, then this will return true if the file is inside a subfolder of one of the path's directories (at any depth). If false it will only return true if the file is actually a direct child of one of the directories. 



See alsoFile::isAChildOf