#### setFileFilter()


 void DirectoryContentsList::setFileFilter ( const FileFilter \* newFileFilter ) 
 

Replaces the current FileFilter.This can be nullptr to have no filter. The DirectoryContentList does not take ownership of this object it just keeps a pointer to it, so you must manage its lifetime. Note that this only replaces the filter, it doesn't refresh the list you'll probably want to call refresh() after calling this.