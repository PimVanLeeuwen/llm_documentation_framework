#### create()


 Result File::create ( ) const 
 

Creates an empty file if it doesn't already exist.If the file that this object refers to doesn't exist, this will create a file of zero size.If it already exists or is a directory, this method will do nothing.If the parent directories of the File do not exist then this method will recursively create the parent directories.Returnsa result to indicate whether the file was created successfully, or an error message if it failed. 
See alsocreateDirectory