#### getParentDirectory()


 File File::getParentDirectory ( ) const 
 

Returns the directory that contains this file or directory.e.g. for "/moose/fish/foo.txt" this will return "/moose/fish".If you are already at the root directory ("/" or "C:") then this method will return the root directory.