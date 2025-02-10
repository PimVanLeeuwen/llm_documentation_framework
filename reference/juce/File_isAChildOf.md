#### isAChildOf()


 bool File::isAChildOf ( const File & potentialParentDirectory ) const 
 

Checks whether a file is somewhere inside a directory.Returns true if this file is somewhere inside a subdirectory of the directory that is passed in. Neither file actually has to exist, because the function just checks the paths for similarities.e.g. File ("/moose/fish/foo.txt").isAChildOf ("/moose") is true. File ("/moose/fish/foo.txt").isAChildOf ("/moose/fish") is also true.