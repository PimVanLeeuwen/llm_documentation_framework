#### createStreamForEntry() [2/2]


 InputStream \* ZipFile::createStreamForEntry ( const ZipEntry & entry ) 
 

Creates a stream that can read from one of the zip file's entries.The stream that is returned must be deleted by the caller (and a nullptr might be returned if a stream can't be opened for some reason).The stream must not be used after the ZipFile object that created has been deleted.Note that if the ZipFile was created with a usersupplied InputStream object, then all the streams which are created by this method will by trying to share the same source stream, so cannot be safely used on multiple threads! (But if you create the ZipFile from a File or InputSource, then it is safe to do this).