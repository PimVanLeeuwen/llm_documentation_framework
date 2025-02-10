#### getRelativePathFrom()


 String File::getRelativePathFrom ( const File & directoryToBeRelativeTo ) const 
 

Creates a relative path that refers to a file relatively to a given directory.e.g. File ("/moose/foo.txt").getRelativePathFrom (File ("/moose/fish/haddock")) would return "../../foo.txt".If it's not possible to navigate from one file to the other, an absolute path is returned. If the paths are invalid, an empty string may also be returned.Parameters

 directoryToBeRelativeTo the directory which the resultant string will be relative to. If this is actually a file rather than a directory, its parent directory will be used instead. If it doesn't exist, it's assumed to be a directory. 
 



See alsogetChildFile, isAbsolutePath