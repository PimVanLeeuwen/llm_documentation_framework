#### setMaxNumberOfItems()


 void RecentlyOpenedFilesList::setMaxNumberOfItems ( int newMaxNumber ) 
 

Sets a limit for the number of files that will be stored in the list.When addFile() is called, then if there is no more space in the list, the leastrecently added file will be dropped.See alsogetMaxNumberOfItems