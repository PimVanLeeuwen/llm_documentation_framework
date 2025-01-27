#### findChildFiles() [2/2]


 int FileSearchPath::findChildFiles ( Array< File > & results, 
 
 int whatToLookFor, 
 bool searchRecursively, 
 const String & wildCardPattern = "\*" ) const 

Searches the path for a wildcard.Note that there's a newer, better version of this method which returns the results array, and in almost all cases, you should use that one instead! This one is kept around mainly for legacy code to use.