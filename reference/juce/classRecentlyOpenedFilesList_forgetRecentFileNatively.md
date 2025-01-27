#### forgetRecentFileNatively()


 static void RecentlyOpenedFilesList::forgetRecentFileNatively ( const File & file ) static 
 

Tells the OS to remove a file from the OSmanaged list of recent documents for this app.Not all OSes maintain a list of recent files for an application, so this function will have no effect on some OSes. Currently it's just implemented for OSX.