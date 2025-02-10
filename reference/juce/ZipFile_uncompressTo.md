#### uncompressTo()


 Result ZipFile::uncompressTo ( const File & targetDirectory, 
 
 bool shouldOverwriteFiles = true ) 

Uncompresses all of the files in the zip file.This will expand all the entries into a target directory. The relative paths of the entries are used.Parameters

 targetDirectory the root folder to uncompress to 
 
 shouldOverwriteFiles whether to overwrite existing files with similarlynamed ones 



Returnssuccess if the file is successfully unzipped