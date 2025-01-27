#### getFileName()


 String File::getFileName ( ) const 
 

Returns the last section of the pathname.Returns just the final part of the path e.g. if the whole path is "/moose/fish/foo.txt" this will return "foo.txt".For a directory, it returns the final part of the path e.g. for the directory "/moose/fish" it'll return "fish".If the filename begins with a dot, it'll return the whole filename, e.g. for "/moose/.fish", it'll return ".fish"See alsogetFullPathName, getFileNameWithoutExtension