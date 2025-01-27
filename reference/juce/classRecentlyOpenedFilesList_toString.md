#### toString()


 String RecentlyOpenedFilesList::toString ( ) const 
 

Returns a string that encapsulates all the files in the list.The string that is returned can later be passed into restoreFromString() in order to recreate the list. This is handy for persisting your list, e.g. in a PropertiesFile object.See alsorestoreFromString