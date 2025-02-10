#### createSymbolicLink() [2/2]


 static bool File::createSymbolicLink ( const File & linkFileToCreate, const String & nativePathOfTarget, bool overwriteExisting ) static 
 

Create a symbolic link to a native path and return a boolean to indicate success.Use this method if you want to create a link to a relative path or a special native file path (such as a device file on Windows).