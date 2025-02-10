#### addFile()


 void RecentlyOpenedFilesList::addFile ( const File & file ) 
 

Adds a file to the list.The file will be added at index 0. If this file is already in the list, it will be moved up to index 0, but a file can only appear once in the list.If the list already contains the maximum number of items that is permitted, the leastrecently added file will be dropped from the end.