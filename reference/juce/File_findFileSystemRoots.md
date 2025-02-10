#### findFileSystemRoots()


 static void File::findFileSystemRoots ( Array< File > & results ) static 
 

Creates a set of files to represent each file root.e.g. on Windows this will create files for "c:\", "d:" etc according to which ones are available. On the Mac/Linux, this will probably just add a single entry for "/".