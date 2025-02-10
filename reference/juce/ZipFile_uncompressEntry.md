#### uncompressEntry() [2/2]


 Result ZipFile::uncompressEntry ( int index, 
 
 const File & targetDirectory, 
 OverwriteFiles overwriteFiles, 
 FollowSymlinks followSymlinks ) 

Uncompresses one of the entries from the zip file.This will expand the entry and write it in a target directory. The entry's path is used to determine which subfolder of the target should contain the new file.Parameters

 index the index of the entry to uncompress this must be a valid index between 0 and (getNumEntries() 1). 
 
 targetDirectory the root folder to uncompress into 
 overwriteFiles whether to overwrite existing files with similarlynamed ones 
 followSymlinks whether to follow symlinks inside the target directory 



Returnssuccess if all the files are successfully unzipped