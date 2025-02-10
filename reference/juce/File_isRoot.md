#### isRoot()


 bool File::isRoot ( ) const 
 

Checks whether the path of this file represents the root of a file system, irrespective of its existence.This will return true for "C:", "D:", etc on Windows and "/" on other platforms.