#### getChildFile()


 File File::getChildFile ( StringRef relativeOrAbsolutePath ) const 
 

Returns a file that represents a relative (or absolute) subpath of the current one.This will find a child file or directory of the current object.e.g. File ("/moose/fish").getChildFile ("foo.txt") will produce "/moose/fish/foo.txt". File ("/moose/fish").getChildFile ("haddock/foo.txt") will produce "/moose/fish/haddock/foo.txt". File ("/moose/fish").getChildFile ("../foo.txt") will produce "/moose/foo.txt".If the string is actually an absolute path, it will be treated as such, e.g. File ("/moose/fish").getChildFile ("/foo.txt") will produce "/foo.txt"See alsogetSiblingFile, getParentDirectory, getRelativePathFrom, isAChildOf