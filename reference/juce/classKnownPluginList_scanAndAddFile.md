#### scanAndAddFile()


 bool KnownPluginList::scanAndAddFile ( const String & possiblePluginFileOrIdentifier, 
 
 bool dontRescanIfAlreadyInList, 
 OwnedArray< PluginDescription > & typesFound, 
 AudioPluginFormat & formatToUse ) 

Looks for all types that can be loaded from a given file, and adds them to the list.If dontRescanIfAlreadyInList is true, then the file will only be loaded and retested if it's not already in the list, or if the file's modification time has changed since the list was created. If dontRescanIfAlreadyInList is false, the file will always be reloaded and tested.Returns true if any new types were added, and all the types found in this file (even if it was already known and hasn't been rescanned) get returned in the array.