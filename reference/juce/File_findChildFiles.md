#### findChildFiles() [2/2]


 int File::findChildFiles ( Array< File > & results, 
 
 int whatToLookFor, 
 bool searchRecursively, 
 const String & wildCardPattern = "\*", 
 FollowSymlinks followSymlinks = FollowSymlinks::yes ) const 

Searches inside a directory for files matching a wildcard pattern.Note that there's a newer, better version of this method which returns the results array, and in almost all cases, you should use that one instead! This one is kept around mainly for legacy code to use.