#### overwriteTargetFileWithTemporary()


 bool TemporaryFile::overwriteTargetFileWithTemporary ( ) const 
 

Tries to move the temporary file to overwrite the target file that was specified in the constructor.If you used the constructor that specified a target file, this will attempt to replace that file with the temporary one.Before calling this, make sure:that you've actually written to the temporary filethat you've closed any open streams that you were using to write to itand that you don't have any streams open to the target file, which would prevent it being overwrittenIf the file move succeeds, this returns true, and the temporary file will have disappeared. If it fails, the temporary file will probably still exist, but will be deleted when this object is destroyed.