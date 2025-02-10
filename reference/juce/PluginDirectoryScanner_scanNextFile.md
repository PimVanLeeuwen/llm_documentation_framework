#### scanNextFile()


 bool PluginDirectoryScanner::scanNextFile ( bool dontRescanIfAlreadyInList, 
 
 String & nameOfPluginBeingScanned ) 

Tries the next likelylooking file.If dontRescanIfAlreadyInList is true, then the file will only be loaded and retested if it's not already in the list, or if the file's modification time has changed since the list was created. If dontRescanIfAlreadyInList is false, the file will always be reloaded and tested. The nameOfPluginBeingScanned will be updated to the name of the plugin being scanned before the scan starts.Returns false when there are no more files to try.