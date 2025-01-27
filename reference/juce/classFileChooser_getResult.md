#### getResult()


 File FileChooser::getResult ( ) const 
 

Returns the last file that was chosen by one of the browseFor methods.After calling the appropriate browseFor... method, this method lets you find out what file or directory they chose.Note that the file returned is only valid if the browse method returned true (i.e. if the user pressed 'ok' rather than cancelling).On mobile platforms, the file browser may return a URL instead of a local file. Therefore, on mobile platforms, you should call getURLResult() instead.If you're using a multiplefile select, then use the getResults() method instead, to obtain the list of all files chosen.See alsogetURLResult, getResults Referenced by StandalonePluginHolder::askUserToLoadState(), StandalonePluginHolder::askUserToSaveState(), and StandalonePluginHolder::setLastFile().